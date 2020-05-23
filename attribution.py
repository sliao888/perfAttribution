import pandas as pd
import numpy as np


class Attribution():
    
    def __init__(self, date, fundDataPath, marketDataPath):
        """[This class contains the methods to calculate performance attribution]

        Args:
            fundData ([str]): [path to Fund Data csv]
            marketData ([str]): [path to Market Data csv]
        """
        self.fundDataPath = fundDataPath
        self.marketDataPath = marketDataPath

        # bring in the data into DataFrames
        self.fundData = pd.read_csv(self.fundDataPath)
        self.marketData = pd.read_csv(self.marketDataPath)

    def formatFundData(self):
        data = self.fundData.groupby('Sector')

        
if __name__ == '__main__':

    fundDataPath = r'C:\Users\simon\Documents\Python Scripts\perfAttribution\Data\BrinsonTask_FundData.csv'
    marketDataPath = r'C:\Users\simon\Documents\Python Scripts\perfAttribution\Data\BrinsonTask_MarketData.csv'

    test = Attribution(date='2019-31-03', fundDataPath=fundDataPath, marketDataPath=marketDataPath)