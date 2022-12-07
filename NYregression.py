import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import statsmodels.api as sm

path = os.getcwd()
os.chdir(path+r'\data')
nyfat = pd.read_csv('NY.csv')
# aufat = pd.read_csv('Austin.csv')

nyfatsum = nyfat[['# Fat', 'Year']].groupby('Year').sum()
# aufatsum = aufat[['# Fat', 'Year']].groupby('Year').sum()

nycbnds = gpd.read_file('nycborobounds.geojson')
nyfatboro = nyfat.copy()
nyfatboro = nyfatboro[['x','y','# Fat','Year']]
nyboro = gpd.GeoDataFrame(nyfatboro, geometry=gpd.points_from_xy(nyfatboro.x, nyfatboro.y), crs={'init': 'epsg:4326'})
nyjoin = gpd.sjoin(nycbnds,nyboro)
fatbyyrbr = (nyjoin[['boro_name','# Fat','Year']].groupby(by=['Year','boro_name']).sum()).values[:40]

nypop = pd.read_excel('NYpop.xlsx')
nypop1 = nypop.iloc[:,3:].copy()
nypop1['county']=nypop.iloc[:,0]
bxpop = nypop1.loc[nypop1['county']=='.Bronx County, New York'].values
kgpop = nypop1.loc[nypop1['county']=='.Kings County, New York'].values
mnpop = nypop1.loc[nypop1['county']=='.New York County, New York'].values
qnpop = nypop1.loc[nypop1['county']=='.Queens County, New York'].values
rmpop = nypop1.loc[nypop1['county']=='.Richmond County, New York'].values
popls = [bxpop,kgpop,mnpop,qnpop,rmpop]
popbyyrbr = []
for i in range(8):
    for j in range(5):
        popbyyrbr.append(popls[j][0][i])

k = np.asarray([np.asarray(fatbyyrbr).reshape(40,),np.asarray(popbyyrbr).reshape(40,)])
nydf = pd.DataFrame(data=k.T,columns=['# Fat', 'Pop'])

# normalize & plot
nydf=(nydf-nydf.mean())/nydf.std()
# fig, ax = plt.subplots()
# ax.plot(np.arange(40), nydf['Pop'], label='Pop. Den')
# ax.plot(np.arange(40), nydf['# Fat'], label='# Fat.')
# plt.title('NYC Population Density vs # Fatality')
# plt.legend()
# plt.show()

# regression analysis
model = sm.OLS(nydf['# Fat'],sm.add_constant(nydf['Pop']))
results = model.fit()
print(results.summary())

# aufat = pd.read_csv('Austin.csv')
# aufat = aufat[['# Fat','Year']]
# aufatbyyr = (aufat.groupby(by=['Year']).sum()).values # 2013~2019
# aupop = pd.read_excel('TXpop.xlsx')
# aupop = aupop.loc[aupop['county']=='.Travis County, Texas'].values[0][4:]
# k = np.asarray([np.asarray(aufatbyyr).reshape(7,),np.asarray(aupop).reshape(7,)])
# audf = pd.DataFrame(data=k.T,columns=['# Fat', 'Pop'])
# audf=(audf-audf.mean())/audf.std()
# # to give austin equal weight, concat 5 times austin df
# df = pd.concat([nydf,audf])
# for _ in range(4):
#     df = pd.concat([df,audf.copy()])

# fig, ax = plt.subplots()
# ax.plot(np.arange(75), df['Pop'], label='Pop. Den')
# ax.plot(np.arange(75), df['# Fat'], label='# Fat.')
# plt.title('Combined Population Density vs # Fatality')
# plt.legend()
# plt.show()
#
# model = sm.OLS(pd.to_numeric(df['# Fat']),sm.add_constant(pd.to_numeric(df['Pop'])))
# results = model.fit()
# print(results.summary())
