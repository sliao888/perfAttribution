import pandas as pd
import numpy as np


class Attribution():
    
    def __init__(self, fundData, marketData):
        """[This class contains the methods to calculate performance attribution]

        Args:
            fundData ([str]): [path to Fund Data csv]
            marketData ([str]): [path to Market Data csv]
        """
        self.fundData = fundData
        self.marketData = marketData

    # def getFundData(self):
        

if __name__ == '__main__':

    fundDataPath = r'C:\Users\simon\Documents\Python Scripts\perfAttribution\Data\BrinsonTask_FundData.csv'
    marketDataPath = r'C:\Users\simon\Documents\Python Scripts\perfAttribution\Data\BrinsonTask_MarketData.csv'

    test = Attribution(fundData=fundDataPath, marketData=marketDataPath)