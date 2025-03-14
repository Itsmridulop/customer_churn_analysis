import pandas as pd
import general as gen_module
import visual as vis_module
import regression as reg_module

# Load the data
data = pd.read_csv('customer_churn.csv')
print('head:\n',data.head(5))

# matadata of data
print('duplicates:\n', data.duplicated().sum())
print('null:\n', data.isnull().sum().sum())
print('Description:\n', data.describe())
print('Info:\n')
data.info()

while True:
    print('1)Data general analsis\n2)Visualisation\n3)Model\n')
    user_input=input('Enter choise: ')
    match user_input:
        case '1':
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
        case '2':
            # Visualisation
            print('1) Bar Plot\n2) histo graph\n3) Scatter Plot\n4) Box plot')
            user_input = input('Enter choise: ')
            vis = vis_module.Visual(data)
            match user_input:
                case '1':
                    vis.bar_plot(colName=input('Enter Column Name: '), title=input('Enter Title: '), xlable=input('Enter X-Lable: '), ylable=input('Enter Y-Lable: '))
                case '2':
                    vis.hist_plot(colName=input('Enter Column Name: '), title=input('Enter Title: '), bins=int(input('Enter Bins: ')))
                case '3':
                    vis.scatter_plot(xColName=input('Enter X-Column Name: '), yColName=input('Enter Y-Column Name: '), title=input('Enter Title: '))
                case '4':
                    vis.box_plot(xCol=input('Enter X-Column Name: '), yCol=input('Enter Y-Cloumn Name: '), title=input('Enter Title: '))  
                case _:
                    raise ValueError('Invalid Input')
        case '3':
            # Model
            print('1) Logistic Regression\n2) Decision Tree\n3) Random Forest\n4) Linear Regression')
            user_input = input('Enter choise: ')
            reg = reg_module.Model(data, targetCol=input('Enter target column: '), trainCol=input('Enter columns on which model has to train(sperated by space): '), testSize=float(input('Enter test size: ')))
            match user_input:
                case '1':
                    reg.logistic_regression()
                case '2':
                    reg.decision_tree()
                case '3':
                    reg.random_forest()
                case '4':
                    reg.linear_regression()
                case _:
                    raise ValueError('Invalid Input')
        case _:
            raise ValueError('Invalid Input')
    
    print('1)For more analysis\n2)For Exit')
    user_input = input('Enter choise: ')
    if user_input == '2': 
        break