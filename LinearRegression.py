# LINEAR REGRESSION                                                                                      NGJ, 2020
# 
# Usage:
#
# 1. Create an Instance of the class Linear Regression and supply with two arrays of floats/ints.
#    data = LinearRegression([1,2,3,4,5],[10,20,30,40,50])
#
# 2. Check your DataFrame. 
#    print(data.df)
#
# 3. Predict data using .predict(x).
#    data.predict(6)
#    >> 60
#
# 4. Plot your data using .plot()
#
# 5. Export your data to .csv using .export(file_name)
#


import pandas as pd
import matplotlib.pyplot as plt


def get_mean(x: list):
    return sum(x) / len(x)


class Array:
    std_dev = 0
    lenght = 0
    array = []
    mean = 0

    def __init__(self, array):
        self.array = array
        self.mean = get_mean(self.array)
        self.lenght = len(array)
        self.std_dev = [i - get_mean(array) for i in array]


class LinearRegression:
    df = pd.DataFrame()

    def __init__(self, arr_x, arr_y):
        self.x = Array(arr_x)
        self.y = Array(arr_y)

        self.deviation_products = [self.x.std_dev[i] * self.y.std_dev[i] for i in range(self.x.lenght)]
        self.dev_x_squared = [self.x.std_dev[i] * self.x.std_dev[i] for i in range(self.x.lenght)]

        self.sum_of_deviation_products = sum(self.deviation_products)
        self.sum_of_x_dev_squared = sum(self.dev_x_squared)

        self.slope = self.sum_of_deviation_products / self.sum_of_x_dev_squared
        self.intercept = self.y.mean - (self.slope * self.x.mean)

        self.df['ind(x)'] = self.x.array
        self.df['dep(y)'] = self.y.array
        self.df['dev_x'] = self.x.std_dev
        self.df['dev_y'] = self.y.std_dev
        self.df['dev_products'] = self.deviation_products
        self.df['dev_x²'] = self.dev_x_squared

    def predict(self, x, digits=2):
        return f"Prediction of {x}: {round(self.slope * x - self.intercept, digits)}"

    def plot(self):
        plt.scatter(self.x.array, self.y.array, edgecolors='black', s=10)
        plt.colormaps()
        plt.ylabel = 'Y Axis'
        plt.xlabel = 'X Axis'
        plt.show()

    def export(self, name_csv):
        self.df.to_csv(name_csv + '.csv', encoding='utf-8')
        print(f"file saved as '{name_csv}.csv'")
