import numpy as np

class waterfall:
    def __init__(self, name, dataframe):
        self.name = name
        self.dataframe = transpose(dataframe)
        self.equation = []

    def plus(self, column):
        self.equation.append((column, self.dataframe[column][0]))
        return self

    def minus(self, column):
        self.equation.append((column, self.dataframe[column][0]*-1))
        return self

    def to_c3(self):
        data = dict(columns=[], groups=[])

        for i in range(len(self.equation)):
            chart_row = [0] * (len(self.equation) + 2)

            column_name = self.equation[i][0]
            value = self.equation[i][1]

            chart_row[0] = column_name
            chart_row[i+1] = value

            data['columns'].append(chart_row)
            data['groups'].append(column_name)

        values = [variable[1] for variable in self.equation]
        values_shifted = values[1:] + [0]
        calculated_row = ['Calculated',0] + list(np.array(values) + np.array(values_shifted))[:-1] + [0]
        data['columns'].append(calculated_row)

        final_row = [0] * (len(self.equation) + 2)
        final_row[0] = self.name
        final_row[-1] = calculated_row[-2]
        data['columns'].append(final_row)
        data['groups'].append(self.name)

        return data

    def calculated_column(self):
        calculated_column = [0] * (len(self.equation) + 1)
        calculated_column[0] = 'Calculated'
        for i in range(2, len(self.equation)):
            operation = self.equation[i][0]
            num_operation = -1 if operation == '-' else 1

            name = self.equation[i][1]
            value = self.dataframe[name][0]

            name_prev = self.equation[i - 1][1]
            value_prev = self.dataframe[name_prev][0]

            calculated_column[i] = value_prev + num_operation * value

        return calculated_column

def transpose(dataframe):
    return dataframe.sum().to_frame().transpose()        

