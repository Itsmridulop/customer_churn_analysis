from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

class Model:
    def __init__(self, data, targetCol, trainCol, testSize):
        self.data = data
        if len(targetCol.split(' ')) != 1:
            raise ValueError('Invalid target column')
        self.targetCol = targetCol
        self.trainCol = trainCol.split(' ')
        self.testSize = testSize

    def linear_regression(self):
        # treatment of null and duplicates
        if self.data.isnull().sum().sum() > 0:
            if self.data.isnull().sum().sum() > 0.3 * len(self.data):
                self.data.fillna(self.data.mean(), inplace=True)
            else:
                self.data.dropna(inplace=True)

        if self.data.duplicated().sum() > 0:
            self.data.drop_duplicates(inplace=True)
        
        # treatment of outliers
        for col in self.trainCol:
            if col in self.data.columns and self.data[col].dtype != 'object':
                iqr = self.data[col].quantile(0.75) - self.data[col].quantile(0.25)
                lower_bound = self.data[col].quantile(0.25) - (iqr * 1.5)
                upper_bound = self.data[col].quantile(0.75) + (iqr * 1.5)
                self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]
            else:
                raise KeyError('Invalid Column Name')
        
        # label encoding
        le = LabelEncoder()
        for col in self.trainCol:
            if col in self.data.columns:
                if self.data[col].dtype == 'object':
                    self.data[col] = le.fit_transform(self.data[col])
            else:
                raise KeyError('Invalid Column Name')
        
        if self.targetCol in self.data.columns:
            if self.data[self.targetCol].dtype == 'object':
                self.data[self.targetCol] = le.fit_transform(self.data[self.trainCol])
        else:
            raise KeyError('Invalid Column Name')

        # split the data
        x = self.data[self.trainCol]
        y = self.data[self.targetCol]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=self.testSize)

        # model
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        # evaluation
        print('Root mean square error: ', root_mean_squared_error(y_test, y_pred))
        print('R2 Score: ', r2_score(y_test, y_pred))
        
        sns.regplot(x=y_pred,y=y_test)
        plt.xlabel('Predictions')
        plt.ylabel('Actual Values')
        plt.title('Regression Plot')
        plt.show()

