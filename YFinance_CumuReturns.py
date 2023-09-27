#!/usr/bin/env python
# coding: utf-8

# In[14]:


import import_ipynb
from YFLD import *
import pandas as pd


# In[15]:


aapl=(raw
     .iloc[:,::2]
     .pipe(fix_cols))
aapl


# In[16]:


(aapl.Close.plot())


# In[17]:


(aapl.Close.sub(aapl.Close[0]).div(aapl.Close[0]).plot())


# In[19]:


(aapl.Close.pct_change().add(1).cumprod().sub(1).plot())


# In[20]:


get_ipython().run_line_magic('pinfo', 'np.cumprod')


# In[25]:


def calc_cum_returns(df, col):
    ser = df[col]
    return( ser
          .sub(ser[0])
          .div(ser[0])
          )
(aapl.pipe(calc_cum_returns, 'Close').plot())


# In[26]:


def get_returns(df):
    return calc_cum_returns(df, 'Close')

get_returns(aapl)


# In[27]:


(lambda df: get_returns(df))(aapl)


# In[30]:


(aapl.assign(cum_returns=(lambda df: calc_cum_returns(df, 'Close'))))


# In[34]:


def my_bar(ser, ax):
    ax.bar(ser.index, ser)
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b-%y'))
    ax.xaxis.set_minor_locator(dates.DayLocator())
    return ser
    
fig, ax = plt.subplots(figsize = (10,4))
_ = (aapl.pipe(calc_cum_returns, 'Close').iloc[-100:].pipe(my_bar, ax))


# # Volatility

# ## goals
# * more complicated pandas
# * learn about rolling operations

# In[36]:


(aapl.Close.mean())


# In[37]:


(aapl.Close.std())


# In[40]:


(aapl.assign(pct_change_close=aapl.Close.pct_change()).pct_change_close.std())


# In[41]:


(aapl.assign(close_vol=aapl.rolling(30).Close.std(),per_vol=aapl.Close.pct_change().rolling(30).std()).iloc[:,-2:].plot(subplots=True))


# In[45]:


(aapl.assign(pct_change_close=aapl.Close.pct_change()).resample('15D').std())


# In[46]:


(aapl.assign(pct_change_close=aapl.Close.pct_change()).rolling(window=15, min_periods=15).std())


# In[52]:


(aapl.assign(pct_change=aapl.Close.pct_change()).rolling(window=15, min_periods=15).std()['pct_change'].plot())


# ### calculations by rolling and grouping
# 

# # Challenge
# ## Plot the rolling volatitlity over 30-day sliding windows for 2015-2019

# In[62]:


(aapl.assign(pct_change=aapl.Close.pct_change()).rolling(window=30, min_periods=30).pct_change.std().loc["2015":"2019"]
 .plot()

)


# In[ ]:





# In[ ]:




