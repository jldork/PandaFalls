import unittest
import pandas as pd
from PandaFalls.Waterfall import waterfall
from expects import equal, expect, be_true


class TestWaterfall(unittest.TestCase):
    def test_waterfall_can_add_column(self):
        df = pd.DataFrame({'Revenue': [200, 300], 'Cost': [100, 100]})
        profit = waterfall('Profit', df).plus('Revenue')

        expect(profit.equation).to(equal([('Revenue', 500)]))

    def test_waterfall_can_subtract_column(self):
        df = pd.DataFrame({'Revenue': [200, 300], 'Cost': [100, 100]})
        profit = waterfall('Profit', df).plus('Revenue').minus('Cost')

        expect(profit.equation).to(equal([('Revenue', 500), ('Cost', -200)]))

    def test_waterfall_makes_c3_output(self):
        df = pd.DataFrame({'Revenue': [200, 300], 'Cost': [100, 100], 'Interest': [10,40]})
        profit = waterfall('Profit', df).plus('Revenue').minus('Cost').minus('Interest')

        expect(profit.equation).to(equal(
            [('Revenue', 500), ('Cost', -200), ('Interest', -50)]
        ))

        c3_json = profit.to_c3()

        expect(self.checkEqual(c3_json['columns'], [
            ['Profit', 0, 0, 0, 250],
            ['Revenue', 500, 0, 0, 0],
            ['Cost', 0, 200, 0, 0],
            ['Interest', 0, 0, 50, 0],
            ['Calculated', 0, 300, 250, 0]
        ]))

        expect(self.checkEqual(
            c3_json['groups'],
            ['Revenue', 'Cost', 'Profit', 'Interest']
        )).to(be_true)

    def checkEqual(self, list1, list2):
        return len(list1) == len(list2) and sorted(list1) == sorted(list2)
