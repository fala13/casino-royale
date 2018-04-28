import unittest
from unittest.mock import patch

import cg

objectsD = [{'x': 252, 'y': 252, 'owner': 0, 'unit_type': -1, 'health': 60}, {'x': 1668, 'y': 748, 'owner': 1, 'unit_type': -1, 'health': 60}]
sitesD = [{'site_id': 0, 'x': 403, 'y': 827, 'radius': 83, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 1, 'x': 1517, 'y': 173, 'radius': 83, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}]

objectsX = [{'site_id': 0, 'x': 403, 'y': 827, 'radius': 83, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 1, 'x': 1517, 'y': 173, 'radius': 83, 'gold': -1, 'maxMineSize': -1, 'structure_type': 1, 'owner': 1, 'param_1': 344, 'param_2': 341}, {'site_id': 2, 'x': 1042, 'y': 598, 'radius': 60, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 3, 'x': 878, 'y': 402, 'radius': 60, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 4, 'x': 160, 'y': 725, 'radius': 70, 'gold': 242, 'maxMineSize': 1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 5, 'x': 1760, 'y': 275, 'radius': 70, 'gold': -1, 'maxMineSize': -1, 'structure_type': 1, 'owner': 1, 'param_1': 376, 'param_2': 352}, {'site_id': 6, 'x': 619, 'y': 439, 'radius': 82, 'gold': 251, 'maxMineSize': 4, 'structure_type': 2, 'owner': 0, 'param_1': 0, 'param_2': 0}, {'site_id': 7, 'x': 1301, 'y': 561, 'radius': 82, 'gold': -1, 'maxMineSize': -1, 'structure_type': 2, 'owner': 1, 'param_1': 0, 'param_2': 1}, {'site_id': 8, 'x': 175, 'y': 445, 'radius': 85, 'gold': 221, 'maxMineSize': 1, 'structure_type': 2, 'owner': 0, 'param_1': 0, 'param_2': 0}, {'site_id': 9, 'x': 1745, 'y': 555, 'radius': 85, 'gold': -1, 'maxMineSize': -1, 'structure_type': 0, 'owner': 1, 'param_1': -1, 'param_2': -1}, {'site_id': 10, 'x': 453, 'y': 204, 'radius': 90, 'gold': 98, 'maxMineSize': 3, 'structure_type': 0, 'owner': 0, 'param_1': 3, 'param_2': -1}, {'site_id': 11, 'x': 1467, 'y': 796, 'radius': 90, 'gold': -1, 'maxMineSize': -1, 'structure_type': 0, 'owner': 1, 'param_1': -1, 'param_2': -1}, {'site_id': 12, 'x': 172, 'y': 172, 'radius': 82, 'gold': 130, 'maxMineSize': 2, 'structure_type': 0, 'owner': 0, 'param_1': 2, 'param_2': -1}, {'site_id': 13, 'x': 1748, 'y': 828, 'radius': 82, 'gold': -1, 'maxMineSize': -1, 'structure_type': 2, 'owner': 1, 'param_1': 0, 'param_2': 0}, {'site_id': 14, 'x': 942, 'y': 836, 'radius': 74, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 15, 'x': 978, 'y': 164, 'radius': 74, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 16, 'x': 1187, 'y': 820, 'radius': 80, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 17, 'x': 733, 'y': 180, 'radius': 80, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 18, 'x': 1522, 'y': 439, 'radius': 75, 'gold': -1, 'maxMineSize': -1, 'structure_type': 0, 'owner': 1, 'param_1': -1, 'param_2': -1}, {'site_id': 19, 'x': 398, 'y': 561, 'radius': 75, 'gold': 195, 'maxMineSize': 3, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 20, 'x': 1249, 'y': 177, 'radius': 84, 'gold': -1, 'maxMineSize': -1, 'structure_type': 1, 'owner': 1, 'param_1': 324, 'param_2': 331}, {'site_id': 21, 'x': 671, 'y': 823, 'radius': 84, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 22, 'x': 781, 'y': 616, 'radius': 60, 'gold': -1, 'maxMineSize': -1, 'structure_type': -1, 'owner': -1, 'param_1': -1, 'param_2': -1}, {'site_id': 23, 'x': 1139, 'y': 384, 'radius': 60, 'gold': -1, 'maxMineSize': -1, 'structure_type': 1, 'owner': 1, 'param_1': 304, 'param_2': 316}]
sitesX = [{'x': 252, 'y': 252, 'owner': 0, 'unit_type': -1, 'health': 60}, {'x': 1668, 'y': 748, 'owner': 1, 'unit_type': -1, 'health': 60}, {'x': 252, 'y': 252, 'owner': 0, 'unit_type': -1, 'health': 60}, {'x': 1668, 'y': 748, 'owner': 1, 'unit_type': -1, 'health': 60}, {'x': 252, 'y': 252, 'owner': 0, 'unit_type': -1, 'health': 60}, {'x': 1610, 'y': 762, 'owner': 1, 'unit_type': -1, 'health': 60}, {'x': 310, 'y': 238, 'owner': 0, 'unit_type': -1, 'health': 60}, {'x': 1585, 'y': 768, 'owner': 1, 'unit_type': -1, 'health': 60}, {'x': 335, 'y': 232, 'owner': 0, 'unit_type': -1, 'health': 60}]


class TestStringMethods(unittest.TestCase):

    def test_dist(self):
        self.assertEqual(0, cg.dist4(1, 2, 1, 2))
        a = {'x': 1, 'y': 2}
        self.assertEqual(0, cg.dist(a, a))

    @patch('cg.print', create=True)
    def test_angry(self, print_):
        cg.Angry().get_strategy(sitesD, objectsD)
        self.assertEqual(print_.call_count, 2)

    @patch('cg.print', create=True)
    def test_suicide(self, print_):
        cg.Suicide().get_strategy(sitesD, objectsD)
        self.assertEqual(print_.call_count, 2)

    @patch('cg.print', create=True)
    def test_dts(self, print_):
        cg.DTS().get_strategy(sitesD, objectsD)
        self.assertEqual(print_.call_count, 2)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
