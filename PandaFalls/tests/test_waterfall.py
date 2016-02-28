import unittest
import pandas as pd
from PandaFalls.Waterfall import waterfall
from expects import equal, expect, be_true


class TestWaterfall(unittest.TestCase):
    def test_waterfall_can_add_column(self):
        df = pd.DataFrame({'Revenue': [500], 'Cost': [200]})
        profit = waterfall('Profit', df).plus('Revenue')

        expect(profit.equation).to(equal([('Revenue', 500)]))

    def test_waterfall_can_subtract_column(self):
        df = pd.DataFrame({'Revenue': [500], 'Cost': [200]})
        profit = waterfall('Profit', df).plus('Revenue').minus('Cost')

        expect(profit.equation).to(equal([('Revenue', 500), ('Cost', -200)]))

    def test_waterfall_can_output_c3_json(self):
        df = pd.DataFrame({'Revenue': [500], 'Cost': [200]})
        profit = waterfall('Profit', df).plus('Revenue').minus('Cost')

        c3_json = profit.to_c3()

        expect(self.checkEqual(c3_json['columns'], [
            ['Profit', 0, 0, 300],
            ['Revenue', 500, 0, 0],
            ['Cost', 0, 200, 0],
            ['Calculated', 0, 300, 0]
        ]))

        expect(self.checkEqual(
            c3_json['groups'],
            ['Revenue', 'Cost', 'Profit']
        )).to(be_true)

    def test_waterfall_to_c3_can_handle_more_calculations(self):
        df = pd.DataFrame({'Revenue': [500], 'Cost': [200], 'Interest': [50]})
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
