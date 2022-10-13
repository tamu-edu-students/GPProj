# Quick NYPD data processing to get data well formatted
# Author: Jikun Liu
import pandas as pd
df = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv',
                  usecols=['CRASH DATE','CRASH TIME','LATITUDE','LONGITUDE','NUMBER OF PERSONS KILLED',
                           'CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2',
                           'VEHICLE TYPE CODE 1','VEHICLE TYPE CODE 2'])
df = df.loc[df['NUMBER OF PERSONS KILLED']>=1]
df.dropna(subset=['CRASH DATE', 'CRASH TIME', 'NUMBER OF PERSONS KILLED', 'LATITUDE', 'LONGITUDE'],inplace=True)
df.rename(columns={'CRASH DATE':'Date','CRASH TIME':'Time','NUMBER OF PERSONS KILLED':'# Fat',
                   'LONGITUDE':'x','LATITUDE':'y','CONTRIBUTING FACTOR VEHICLE 1':'factor1',
                   'CONTRIBUTING FACTOR VEHICLE 2':'factor2','VEHICLE TYPE CODE 1':'type1','VEHICLE TYPE CODE 2':'type2'}, inplace=True)
df['Date']=pd.to_datetime(df['Date'])
df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['Day']=df['Date'].dt.weekday
df['Hour']=pd.to_datetime(df['Time']).dt.hour
df.reset_index(inplace=True, drop=True)
df.to_csv('NY.csv',index=False)
