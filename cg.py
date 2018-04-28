import sys
import math
import functools

UT = True
UT = False


def dist4(x1, y1, x2, y2):
   # print(str(x1) + " " + str(y1) + " " + str(x2) + " "+ str(y2) +" " +str( math.sqrt((x1-x2)**2 + (y1-y2)**2)), file=sys.stderr)
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def dist(a, b):
    return dist4(a['x'], a['y'], b['x'], b['y'])


def find_nearest(q, places):
 #   assert (type(places) is dict)
 #   print("queen at " + str(q['x']) + " " + str(q['y']), file=sys.stderr)
    return min(places, key=lambda k: dist(q, k))

if not UT:
    num_sites = int(input())
else:
    num_sites = 0
sites = []
objects = []
touched_site = 0
gold_left = [-2] * num_sites
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites.insert(site_id, {'site_id': site_id, 'x': x, 'y': y, 'radius': radius})

def get_queens(objects):
    queenM = next(q for q in objects if q['unit_type'] == -1 and q['owner'] == 0)
    queenE = next(q for q in objects if q['unit_type'] == -1 and q['owner'] == 1)
    return queenM, queenE


class Strategy:
    def get_strategy(self, sites, objects):
        print("BUILD 1 BARRACKS-KNIGHT")
        print("TRAIN 1")
        return


class Angry(Strategy):
    def get_strategy(self, sites, objects):
        queenM, queenE = get_queens(objects)

        mine = [v for  v in sites if v['owner'] == 0]
        empty_sites = [v for v in sites if v['owner'] != 0 and v['structure_type'] != 1]

    #   mine_sort = sorted(mine, key=lambda k: dist(queenE, mine[k]))
        mine_sort = sorted(mine, key=lambda k: dist(queenE, k))

    # First line: A valid queen action
    # Second line: A set of training instructions
        print("BUILD " + str(find_nearest(queenM, empty_sites)) + " BARRACKS-KNIGHT")
        if mine:
            print("TRAIN " + str(mine_sort[0]['site_id']))
        else:
            print("TRAIN 1")
        return


class Situation():
    def __init__(self, sites, objects):
        self.sites = sites
        self.objects = objects


class CounterSituation(Situation):
    def __init__(self, sites, objects):
        self.sites = sites
        self.objects = objects
        queenM, queenE = get_queens(objects)

        owned_sites = filter(lambda x: x['owner'] == 0, sites)
        self.mbarracks = functools.reduce(lambda a, x: a+1 if x['structure_type'] == 2 else a,
                                         owned_sites,
                                         0)

        self.mine_rate = functools.reduce(lambda a, x: a+x['param_1'] if x['structure_type'] == 0 else a, sites, 0)
        #print(str(self.mine_rate),file=sys.stderr)

        #self.enemy_near = [] == next(True for q in objects if q['owner'] == 1 and (dist(queenM, q) < 300))
        #self.enemy_near = [] == next(True for q in objects if q['owner'] == 1 and dist(queenM, q) < 300)
        self.enemy_near = [] != [True for q in objects if q['owner'] == 1 and dist(queenM, q) < 100]
        print(str(self.enemy_near), file=sys.stderr)

def dt(cond, l, r):
    if cond:
        return l
    else:
        return r

class DTS(Strategy):
    def get_strategy(self, sites, objects):
        queenM, queenE = get_queens(objects)

        sit = CounterSituation(sites, objects)

        mine = [v for v in sites if v['owner'] == 0]
        mine_kbaracks = [v for v in sites if v['owner'] == 0 and v['structure_type'] == 2 and v['param_2'] == 0]
        empty_sites = [v for v in sites if v['owner'] != 0 and v['structure_type'] != 1]

        #print(str(empty_sites), file=sys.stderr)
        #   mine_sort = sorted(mine, key=lambda k: dist(queenE, mine[k]))
        mine_sort = sorted(mine_kbaracks, key=lambda k: dist(queenE, k))

        s_id, build = dt(sites[touched_site]['structure_type'] == 1 and sites[touched_site]['param_1'] < 700 and sites[touched_site]['owner'] == 0,
                         (touched_site, 1),
                         dt(not sit.enemy_near and sites[touched_site]['structure_type'] == 0 and sites[touched_site]['param_1'] < sites[touched_site]['maxMineSize'] and sites[touched_site]['gold'] > 5,
                            (touched_site, 0),
                            dt(not sit.enemy_near and sit.mine_rate < 3 and empty_sites,
                               (find_nearest(queenM, filter(lambda x: x['gold'] == -2 or x['gold'] > 5, empty_sites))['site_id'], 0),
                               dt(sit.mbarracks > 0,
                                  (find_nearest(queenM, empty_sites)['site_id'], 1),
                                  (find_nearest(queenM, empty_sites)['site_id'], 2)
                                  )
                               )
                            )
                         )

        building = "MINE"
        if build == 1:
            building = "TOWER"
        elif build == 2:
            building = "BARRACKS-KNIGHT"

        print("BUILD " + str(s_id) + " " + building)

        if mine_sort:
            print("TRAIN " + str(mine_sort[0]['site_id']))
        else:
            print("TRAIN 1")
        return


class Suicide(Strategy):
    def get_strategy(self, sites, objects):
        queenM, queenE = get_queens(objects)

        sit = CounterSituation(sites, objects)

        mine = [v for v in sites if v['owner'] == 0]
        mine_kbaracks = [v for v in sites if v['owner'] == 0 and v['structure_type'] == 2 and v['param_2'] == 0]
        empty_sites = [v for v in sites if v['owner'] != 0 and v['structure_type'] != 1]

        #   mine_sort = sorted(mine, key=lambda k: dist(queenE, mine[k]))
        mine_sort = sorted(mine_kbaracks, key=lambda k: dist(queenE, k))

        #if sites[touched_site]['structure_type'] == 0 and sites[touched_site]['maxMineSize'] < sites[touched_site]['maxMineSize']:
         #   print("BUILD " + str(touched_site) + " MINE")

  #      if sit.mine_rate < 5:
 #           print("BUILD " + str(find_nearest(queenM, empty_sites)['site_id']) + " MINE")

        if sit.mbarracks > 2:
            print("BUILD " + str(find_nearest(queenM, empty_sites)['site_id']) + " TOWER")
        else:
            print("BUILD " + str(find_nearest(queenM, empty_sites)['site_id']) + " BARRACKS-KNIGHT")

        if mine:
            print("TRAIN " + str(mine_sort[0]['site_id']))
        else:
            print("TRAIN 1")
        return


strat = DTS()
# game loop
while True and not UT:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        if ignore_1 == -1:
            sites[site_id]['gold'] = gold_left[site_id]
        else:
            sites[site_id]['gold'] = ignore_1
            gold_left[site_id] = ignore_1

        sites[site_id]['maxMineSize'] = ignore_2
        sites[site_id]['structure_type'] = structure_type
        sites[site_id]['owner'] = owner
        sites[site_id]['param_1'] = param_1
        sites[site_id]['param_2'] = param_2
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        objects.append({'x':x, 'y': y, 'owner': owner, 'unit_type': unit_type, 'health': health})
        #print(str(objects), file=sys.stderr)

    #print(str(sites).replace("}","}\n") + "\n", file=sys.stderr)
    #print(str(objects).replace("}","}\n") + "\n", file=sys.stderr)


    strat.get_strategy(sites, objects)
