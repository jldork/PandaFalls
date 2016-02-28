class waterfall:
    def __init__(self, name, dataframe):
        self.dataframe = dataframe
        self.equation = [('=', name)]

    def plus(self, column):
        self.equation.append(('+', column))
        return self

    def minus(self, column):
        self.equation.append(('-', column))
        return self

    def to_c3(self):
        data = self.generate_data()
        data['type'] = 'bar'
        data['order'] = """
                        function(column1, column2){
                        if (column2.id == 'Calculated'){
                            return 1 } else {
                            return 0
                            }
                        }
                        """
        return {
            'data': data,
            'grid': '{ y: { lines: [{value:0}] }}'
        }

    def equation_index(self, variable):
        try:
            index = self.equation.index(('+', variable))
        except:
            index = self.equation.index(('-', variable))
        return index

    def calculate_net(self):
        net = 0
        for variable in self.equation:
            if variable[0] == '+':
                net += self.dataframe[variable[1]][0]
            if variable[0] == '-':
                net -= self.dataframe[variable[1]][0]
        return net

    def generate_data(self):
        data = dict(columns=[], groups=[])

        for variable in self.equation:
            column = variable[1]

            values = [0] * (len(self.equation) + 1)
            values[0] = column
            if variable[0] == '=':
                values[-1] = self.calculate_net()
            else:
                values[self.equation_index(column)] = self.dataframe[column][0]

            data['columns'].append(values)
            data['groups'].append(column)
        data['columns'].append(self.calculated_column())

        return data

    def calculated_column(self):
        calculated_column = [0] * (len(self.equation) + 1)
        calculated_column[0] = 'Calculated'
        for i in range(2,len(self.equation)):
            operation = self.equation[i][0]
            num_operation = -1 if operation == '-' else 1

            name = self.equation[i][1]
            value = self.dataframe[name][0]

            name_prev = self.equation[i-1][1]
            value_prev = self.dataframe[name_prev][0]

            calculated_column[i] = value_prev + num_operation*value

        return calculated_column

