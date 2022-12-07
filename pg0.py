import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

path = os.getcwd()
os.chdir(path+r'\data')
aucam = pd.read_csv('Camera_Traffic_Counts.csv',usecols=['Intersection Name','Speed Average (Miles Per Hour)'])
aucam = aucam.loc[aucam['Speed Average (Miles Per Hour)'] > 35]
camg = aucam.groupby('Intersection Name').count()
camg.to_csv('35cam.csv')
