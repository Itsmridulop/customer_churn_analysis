import pandas as pd
        
class General:
    def __init__(self, data):
        self.data = data
        
    def getSpecificCol(self, colNumber: int):
        if colNumber not in range(len(self.data.columns)):
            raise ValueError('Invalid Column Number')
        return self.data.iloc[:, colNumber]
            
    def getDataOnCondition(self, condition: str):
        try:
            res = self.data.query(condition)
            return res
        except:
            raise ValueError('Invalid Condition')