import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import statsmodels.api as sm

path = os.getcwd()
os.chdir(path+r'\data')
aufat = pd.read_csv('Austin.csv')
aufat = aufat[['# Fat','Year']]
aufatbyyr = (aufat.groupby(by=['Year']).sum()).values # 2013~2019

aupop = pd.read_excel('TXpop.xlsx')
aupop = aupop.loc[aupop['county']=='.Travis County, Texas'].values[0][4:]

k = np.asarray([np.asarray(aufatbyyr).reshape(7,),np.asarray(aupop).reshape(7,)])
audf = pd.DataFrame(data=k.T,columns=['# Fat', 'Pop'])

# normalize & plot
audf=(audf-audf.mean())/audf.std()
# fig, ax = plt.subplots()
# ax.plot(np.arange(7), audf['Pop'], label='Pop. Den')
# ax.plot(np.arange(7), audf['# Fat'], label='# Fat.')
# plt.title('Austin Population Density vs # Fatality')
# plt.legend()
# plt.show()

print(audf.dtypes)

# regression analysis
model = sm.OLS(pd.to_numeric(audf['# Fat']),pd.to_numeric(audf['Pop']))
results = model.fit()
print(results.summary())
