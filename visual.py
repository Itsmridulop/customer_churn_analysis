import seaborn as sns
import matplotlib.pyplot as plt

class Visual:
    def __init__(self, data):
        self.data = data
    
    def bar_plot(self, xlable: str | None, ylable: str | None, colName: str, title: str | None):
        if colName not in self.data.columns:
            raise ValueError('Invalid Column Name')
        sns.barplot(x=self.data[colName].value_counts().keys().tolist(), y=self.data[colName].value_counts().tolist())
        if title:
            plt.title(title)
        if xlable:
            plt.xlabel(xlable)
        if ylable:
            plt.ylabel(ylable)
        plt.show()
    
    def hist_plot(self, colName: str, title: str | None, bins: int | None):
        if colName not in self.data.columns:
            raise ValueError('Invalid Column Name')
        sns.histplot(self.data[colName], bins=bins)
        if title:
            plt.title(title)
        plt.show()

    def scatter_plot(self, xColName: str | None, yColName: str | None, title: str | None):
        if xColName not in self.data.columns or yColName not in self.data.columns:
            raise ValueError('Invalid Column Name')
        sns.scatterplot(x=self.data[xColName], y=self.data[yColName])
        if title:
            plt.title(title)
        plt.xlabel(xColName)
        plt.ylabel(yColName)
        plt.show()

    def box_plot(self, xCol: str | None, yCol: str | None, title: str | None):
        if xCol not in self.data.columns or yCol not in self.data.columns:
            raise ValueError('Invalid Column Name')
        if xCol:
            sns.boxplot(self.data[xCol])
        if yCol:
            sns.boxplot(self.data[yCol])
        if xCol and yCol:
            sns.boxplot(x=self.data[xCol], y=self.data[yCol])
        if title:
            plt.title(title)
        plt.show()