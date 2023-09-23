#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


# In[2]:


raw = yf.download('SPY AAPL', start='2010-01-01', end='2019-12-31')


# In[3]:


raw


# In[4]:


raw.columns


# In[5]:


get_ipython().run_line_magic('pinfo', 'raw.pipe')


# In[9]:


def fix_cols(df):
    columns = df.columns
    outer = [col[0] for col in columns]
    df.columns = outer
    return df

(raw.iloc[:,::2].pipe(fix_cols))


# In[11]:


import yfinance as yf

def fix_cols(df):
    columns = df.columns
    outer = [col[0] for col in columns]
    df.columns = outer
    return df

def tweak_data():
    raw = yf.download('SPY AAPL', start='2010-01-01', end='2019-12-31')
    
    return (raw
    .iloc[:,::2]
     .pipe(fix_cols))
    
tweak_data()

