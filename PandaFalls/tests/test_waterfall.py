import unittest
import pandas as pd
from PandaFalls.Waterfall import waterfall
from expects import equal, expect


class TestWaterfall(unittest.TestCase):
    def test_waterfall_can_add_column(self):
        df = pd.DataFrame({'Revenue': [500], 'Cost': [200]})
        profit = waterfall('Profit', df).plus('Revenue')
        expect(profit.equation).to(equal([('+', 'Revenue')]))
        # c3_json = """{
        #     data: {
        #         columns:[
        #             ['Revenue', 500],
        #             ['Calculated', 0],
        #             ['Profit', 500]
        #         ],
        #         type:#'bar',
        #         order: function(column1, column2){
        #                 if (column2.id == 'Calculated'){
        #                     return 1 } else {
        #                     return 0
        #                     }
        #                 },
        #         'groups': [
        #             ['Revenue','Cost','Profit']
        #             ]
        #     },
        #
        #     'grid': { y: { lines: [{value:0}] }}
        # }"""
        # expect(profit.to_c3()).to(equal(c3_json))

    def test_waterfall_can_subtract_column(self):
        df = pd.DataFrame({'Revenue': [500], 'Cost': [200]})
        profit = waterfall('Profit', df).plus('Revenue').minus('Cost')
        expect(profit.equation).to(equal([('+', 'Revenue'), ('-', 'Cost')]))

        # def test_waterfall_can_subtract_column(self):
        #     df = pd.DataFrame({'Revenue': [500], 'Cost': [200]})
        #     profit = Waterfall('Profit', df).plus('Revenue').minus('Cost')
        #     c3_json = """{
        #         data: {
        #             columns:[
        #                 ['Revenue', 500, 0, 0],
        #                 ['Cost', 0, 300, 0],
        #                 ['Calculated', 0, 200, 0],
        #                 ['Profit', 0, 0, 300]
        #             ],
        #             type:#'bar',
        #             order: function(column1, column2){
        #                     if (column2.id == 'Calculated'){
        #                         return 1 } else {
        #                         return 0
        #                         }
        #                     },
        #             'groups': [
        #                 ['Revenue','Cost','Profit']
        #                 ]
        #         },
        #
        #         'grid': { y: { lines: [{value:0}] }}
        #     }"""
        #     expect(profit.to_c3()).to(equal(c3_json))
