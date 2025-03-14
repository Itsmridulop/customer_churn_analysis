import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import general as gen_module

# Load the data
data = pd.read_csv('customer_churn.csv')
print('head:\n',data.head(5))

# matadata of data
print('duplicates:\n', data.duplicated().sum())
print('null:\n', data.isnull().sum().sum())
print('Description:\n', data.describe())
print('Info: \n')
data.info()

# data extraction
print('1) get data of specific row\n 2) get data according to condition\n')
user_input = input('Enter choise: ')
gen = gen_module.General(data)
match user_input:
    case '1':
        colNumber = int(input('Enter Column Number: '))
        print('Data of this column:\n', gen.getSpecificCol(colNumber))
    case '2':
        condition = input('Enter Condition: ')
        print('Data according to this condition:\n', gen.getDataOnCondition(condition))
    case _:
        raise ValueError('Invalid Input')


