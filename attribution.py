import pandas as pd
import numpy as np
from functools import reduce
    

class _baseAttribution():
    
    def __init__(self, date, fundDataPath, marketDataPath):
        """[This class cleans up the data before calculating performance attribution.]

        Args:
            date ([str]): [date for attribution]
            fundData ([str]): [path to Fund Data csv]
            marketData ([str]): [path to Market Data csv]
        """
        self.date = date
        self.date_obj = pd.to_datetime(self.date)
        self.fundDataPath = fundDataPath
        self.marketDataPath = marketDataPath

        # Bring in the data into DataFrames. Format dates as Datetime.
        # Because of internation datetime formatting difference, use 
        # infer_datetime_format=True.
        self.fundData = pd.read_csv(self.fundDataPath, 
                                    parse_dates=['AsOfDate'], 
                                    infer_datetime_format=True)
        self.marketData = pd.read_csv(self.marketDataPath, 
                                      parse_dates=['AsOfDate'], 
                                      infer_datetime_format=True)

        # Filter for the data for the date.
        self.fundData = self.fundData[self.fundData['AsOfDate'].isin([self.date_obj])]
        self.marketData = self.marketData[self.marketData['AsOfDate'].isin([self.date_obj])]

    def formatFundData(self):
        """[Prepare the fund data. Set the sector as the index.
            Calculates the percentage PnL and percentage of starting market value.]

        Returns:
            [DataFrame]: [Returns reformatted DataFrame for the fund.]
        """

        # Sum up the PnL and market values by date and sector.
        data = self.fundData.groupby(['Sector'])['MTD Pnl', 'Start of Month Market Value'].sum()
        
        # Calculate MTD Return.
        data['MTD Return'] = data['MTD Pnl'] /  data['Start of Month Market Value']

        # Calculate Percent of starting market value.
        data['Start of Month Market Value'] = data['Start of Month Market Value'] \
                                                / data['Start of Month Market Value'].sum()

        # Drop MTD Pnl and rename columns.
        data.drop(labels='MTD Pnl', axis=1, inplace=True)
        data.columns = ['Port_Weight', 'Port_MTD_Return']

        return data

    def formatMarketData(self):
        """[Prepare the market data. Set the sector as the index.
            Althought the market data is already percent weight,
            we recompute the percentage because the market data
            sometimes has rounding error and the total market value
            percent only sums to 99%.]

        Returns:
            [DataFrame]: [Returns reformatted DataFrame for the Market.]
        """        
        
        # Set the sector to be the index.
        data = self.marketData.set_index(['Sector'])

        # Calculate percent of starting market value.
        data['Start of Month Weight'] = data['Start of Month Weight'] \
                                        / data['Start of Month Weight'].sum()
        
        # Drop the AsOfDate column and rename columns.
        data.drop(labels='AsOfDate', axis=1, inplace=True)
        data.columns = ['Market_Weight', 'Market_MTD_Return']

        return data


class attribution(_baseAttribution):
    def __init__(self, date, fundDataPath, marketDataPath):
        """[This class performs the performance attribution calculation.]

        Args:
            date ([str]): [date for attribution]
            fundData ([str]): [path to Fund Data csv]
            marketData ([str]): [path to Market Data csv]
        """        
        super().__init__(date, fundDataPath, marketDataPath)
        self.fundDataFinal = self.formatFundData()
        self.marketDataFinal = self.formatMarketData()
    
    def industryMTDAttribution(self):
        """[Computes allocation effect and selection effect for MTD industry attribution.]

        Returns:
            [DataFrame]: [Returns Industry MTD Attribution.]
        """        
        data = pd.merge(self.fundDataFinal, self.marketDataFinal, how='outer',
                        left_index=True, right_index=True)
        data.fillna(0, inplace=True)
        data['Rel_Return'] = data['Port_MTD_Return'] - data['Market_MTD_Return']
        data['Rel_Weight'] = data['Port_Weight'] - data['Market_Weight']
        data['Allocation_Effect'] = data['Rel_Weight'] * data['Market_MTD_Return']
        data['Selection_Effect'] = (data['Market_Weight'] * data['Rel_Return']) + \
                                    (data['Rel_Weight'] * data['Rel_Return'])
        data['Total_Effect'] = data['Allocation_Effect'] + data['Selection_Effect']
        data = data[['Port_MTD_Return', 'Market_MTD_Return', 'Rel_Return',
                     'Port_Weight', 'Market_Weight', 'Rel_Weight',
                     'Allocation_Effect', 'Selection_Effect', 'Total_Effect']]
        
        return data

if __name__ == '__main__':

    fundDataPath = r'C:\Users\simon\Documents\Python Scripts\perfAttribution\Data\BrinsonTask_FundData.csv'
    marketDataPath = r'C:\Users\simon\Documents\Python Scripts\perfAttribution\Data\BrinsonTask_MarketData.csv'

    test = attribution(date='2019-04-30', fundDataPath=fundDataPath, marketDataPath=marketDataPath)