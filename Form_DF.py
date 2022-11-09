import pandas as pd
import numpy as np
from datetime import datetime


def Frame_Converter(df):
    fun_df=df
    # Converting Date format from object to datetime format
    fun_df['Date']=list(map(lambda x : datetime.strptime(x,'%Y-%m-%d'),fun_df['Date']))
    
    # Converting object data type of IsHoliday column into numeric data type
    fun_df['Holiday']=list(map(lambda x:1 if x == True else 0,fun_df['IsHoliday']))

    # Converting object data type of Type column into numeric data type using dummy encoder
    # Type=pd.get_dummies(fun_df['Type'],drop_first=True)
    fun_df['Type']=fun_df['Type'].replace({'A':1,'B':2,'C':3})
    
    # Joining Type with df using concat function
    # fun_df=pd.concat([fun_df,Type],axis=1)

    # Dropping IsHoliday,Type Columns from DataFrame
    # fun_df.drop(['IsHoliday','Type'],axis=1,inplace=True)
    fun_df.drop(['IsHoliday'],axis=1,inplace=True)

    # converting days and months from numerics to categories
    fun_df['Year']=fun_df['Date'].dt.year
    fun_df['Month']=fun_df['Date'].dt.month
    fun_df['Day']=fun_df['Date'].dt.day
    fun_df['WeakOfYear']=fun_df['Date'].dt.isocalendar().week

    return fun_df