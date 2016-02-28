import pandas as pd

class waterfall:
    def __init__(self, name, dataframe):
        self.name = name
        self.dataframe = dataframe
        self.equation = []

    def plus(self, column):
        self.equation.append(('+', column))
        return self

    def minus(self, column):
        self.equation.append(('-', column))
        return self