import pandas as pd
import general as gen_module
import visual as vis_module

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
print('1) get data of specific row\n2) get data according to condition\n')
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

# Visualisation
print('1) Bar Plot\n2) histo graph\n3) Scatter Plot\n4) Box plot')
user_input = input('Enter choise: ')
vis = vis_module.Visual(data)
match user_input:
    case '1':
        vis.bar_plot(colName=input('Enter Column Name: '), title=input('Enter Title: '), color=input('Enter Color: '), xlable=input('Enter X-Lable: '), ylable=input('Enter Y-Lable: '))
    case '2':
        vis.hist_plot(colName=input('Enter Column Name: '), title=input('Enter Title: '), color=input('Enter Color: '), bins=int(input('Enter Bins: ')))
    case '3':
        vis.scatter_plot(xColName=input('Enter X-Column Name: '), yColName=input('Enter Y-Column Name: '), title=input('Enter Title: '), color=input('Enter Color: '))
    case '4':
        vis.box_plot(xCol=input('Enter X-Column Name: '), yCol=input('Enter Y-Cloumn Name: '), title=input('Enter Title: '), color=input('Enter Color: '))  
    case _:
        raise ValueError('Invalid Input')
