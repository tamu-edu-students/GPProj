# Quick APD data processing to get data well formatted
# Author: Jikun Liu
import pandas as pd

df1 = pd.read_csv('2013_APD_Traffic_Fatalities.csv',
                  usecols=['Type','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','XCOORD','YCOORD'])
df1.rename(columns={'Type':'Type', 'Number of Fatalities':'# Fat',
                    'XCOORD':'x','YCOORD':'y'}, inplace=True)

df2 = pd.read_csv('2014_APD_Traffic_Fatalities.csv',
                  usecols=['TYPE','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','X COORD','Y COORD'])
df2.rename(columns={'TYPE':'Type', 'Number of Fatalities':'# Fat',
                    'X COORD':'x','Y COORD':'y'}, inplace=True)

df3 = pd.read_csv('2015_APD_Traffic_Fatalities.csv',
                  usecols=['TYPE','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','X COORD','Y COORD'])
df3.rename(columns={'TYPE':'Type', 'Number of Fatalities':'# Fat',
                    'X COORD':'x','Y COORD':'y'}, inplace=True)

df4 = pd.read_csv('2016_APD_Traffic_Fatalities.csv',
                  usecols=['TYPE','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','COORD X','Y COORD'])
df4.rename(columns={'TYPE':'Type', 'Number of Fatalities':'# Fat',
                    'COORD X':'x','Y COORD':'y'}, inplace=True)

df5 = pd.read_csv('2017_APD_Traffic_Fatalities.csv',
                  usecols=['Type','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','X coord','Y coord'])
df5.rename(columns={'Type':'Type', 'Number of Fatalities':'# Fat',
                    'X coord':'x','Y coord':'y'}, inplace=True)

df6 = pd.read_csv('2018_APD_Traffic_Fatality_Data_021219.csv',
                  usecols=['Type','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','X coord','Y coord'])
df6.rename(columns={'Type':'Type', 'Number of Fatalities':'# Fat',
                    'X coord':'x','Y coord':'y'}, inplace=True)

df7 = pd.read_csv('2019_APD_Traffic_Fatality_Data.csv',
                  usecols=['Type','Number of Fatalities','Date','Month','Day',
                           'Hour','Time','X coord','Y coord'])
df7.rename(columns={'Type':'Type', 'Number of Fatalities':'# Fat',
                    'X coord':'x','Y coord':'y'}, inplace=True)

df = pd.concat([df1,df2,df3,df4,df5,df6,df7], axis=0)
df.reset_index(inplace=True, drop=True)
df['Month'].replace(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','DEC','June','July'],
                    [1,2,3,4,5,6,7,8,9,10,11,12,12,6,7],inplace=True)
df['Day'].replace(['Mon','Tue','Wed','Thu','Fri','Sat','Sun','sat','sun','Tues'],[1,2,3,4,5,6,7,6,7,2],inplace=True)
df['Type'].replace(['MOTOR VEHICLE','BICYCLE','bicycle','pedestrian'],
                   ['Motor Vehicle','Bicycle','Bicycle','Pedestrian'],inplace=True)
df['Date']=pd.to_datetime(df['Date'])
df['Year']=df['Date'].dt.year
df.to_csv('Austin.csv',index=False)
