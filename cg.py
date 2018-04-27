import sys
import math
import functools

def dist4(x1, y1, x2, y2):
   # print(str(x1) + " " + str(y1) + " " + str(x2) + " "+ str(y2) +" " +str( math.sqrt((x1-x2)**2 + (y1-y2)**2)), file=sys.stderr)
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def dist(a, b):
    return dist4(a['x'], a['y'], b['x'], b['y'])


def find_nearest(q, places):
 #   assert (type(places) is dict)
    print("queen at " + str(q['x']) + " " + str(q['y']), file=sys.stderr)
    return min(places, key=lambda k: dist(q, places[k]))


num_sites = int(input())
#num_sites = 0
sites = {}
buildings = {}
objects = []
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites[site_id] = {'site_id': site_id, 'x': x, 'y': y, 'radius': radius}


class Strategy:
    def get_strategy(self, sites, objects, queenM, queenE):
        print("BUILD 1 BARRACKS-KNIGHT")
        print("TRAIN 1")
        return


class Angry(Strategy):
    def get_strategy(self, sites, objects, queenM, queenE):
        mine = [v for k, v in sites.items() if v['owner'] == 0]
        empty_sites = {k:v for k, v in sites.items() if v['owner'] != 0 and v['structure_type'] != 1}

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


class Suicide(Strategy):
    def get_strategy(self, sites, objects, queenM, queenE):
        mine = [v for k, v in sites.items() if v['owner'] == 0]
        empty_sites = {k:v for k, v in sites.items() if v['owner'] != 0 and v['structure_type'] != 1}

        #   mine_sort = sorted(mine, key=lambda k: dist(queenE, mine[k]))
        mine_sort = sorted(mine, key=lambda k: dist(queenE, k))

        barrack_count = functools.reduce(lambda a, x: a+1 if x['owner'] == 0 and x['structure_type'] == 2 else a,
                                         sites.items(),
                                         0)

        if barrack_count > 2:
            print("BUILD " + str(find_nearest(queenM, empty_sites)) + " TOWER")
        else:
            print("BUILD " + str(find_nearest(queenM, empty_sites)) + " BARRACKS-KNIGHT")

        if mine:
            print("TRAIN " + str(mine_sort[0]['site_id']))
        else:
            print("TRAIN 1")
        return

strat = Suicide()
# game loop
while True:
#while False:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        buildings[site_id] = {'site_id': site_id, 'structure_type': structure_type, 'owner':owner}
        sites[site_id]['structure_type'] = structure_type
        sites[site_id]['owner'] = owner
        sites[site_id]['left'] = param_1
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        objects.append({'x':x, 'y': y, 'owner': owner, 'unit_type': unit_type, 'health': health})
        print(str(objects), file=sys.stderr)
        if unit_type == -1 and owner== 0:
            queenM = {'x':x, 'y':y, 'health':health}
        if unit_type == -1 and owner== 1:
            queenE = {'x':x, 'y':y, 'health':health}

    print (str(sites), file=sys.stderr)
    print (str(objects), file=sys.stderr)

    strat.get_strategy(sites, objects, queenM, queenE)
