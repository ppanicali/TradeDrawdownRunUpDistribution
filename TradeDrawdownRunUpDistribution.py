# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:51:39 2022

@author: Paolo Panicali
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Symbol='EURUSD'
Trades=99999



DataPath='C:\\Users\\mercu\\OneDrive\\Documenti\\'+Symbol +'_Trades.csv'

#carica dati dal file in df
path_load=DataPath
df = pd.read_csv(path_load,sep=";",decimal=",", engine='python')



df_profit=df[df['OutCome'] =='PROFIT'] 
df_loss=df[df['OutCome'] =='LOSS'] 

##df_profit["DrawDown"] = pd.to_numeric(df_profit["DrawDown"])
##df_loss["RunUp"] = pd.to_numeric(df_loss["RunUp"])

DDown = df_profit['DrawDown']
RUp=df_loss['RunUp']
%matplotlib ipympl
## RUN THIS FOR DRAWDOWNS
plt.hist(DDown,alpha=0.5,bins=np.arange(0,80,1),color='blue', label='Draw Down')
plt.margins(x=0, y=0)
plt.gca().set(title=Symbol+' Draw Down Distribution', ylabel='Total Profit Trades: '+str(len(df_profit)));
plt.ylim(0,80)
plt.legend();

### RUND THIS FOR RUNUPS
#plt.hist(RUp,alpha=0.5,bins=np.arange(0,80,1),color='red', label='Run Up')
#plt.margins(x=0, y=0)
#plt.gca().set(title=Symbol+' Run Up Distribution', ylabel='Total Loss Trades: '+str(len(df_profit)));
#plt.ylim(0,80)
#plt.legend();
