import pandas as pd
        
class General:
    def __init__(self, data):
        self.data = data
        
    def getSpecificCol(self, colNumber):
        return self.data.iloc[:, colNumber]
            
    def getDataOnCondition(self, condition):
        # if isinstance(condition, str):
            return self.data.query(condition)
            print('input',condition)
        # else:
            # return self.data[condition]