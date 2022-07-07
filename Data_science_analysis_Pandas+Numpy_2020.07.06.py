import pandas as pd
import numpy as np
import array
#%%
print(np.__version__)
#%%
df = pd.read_csv('Pandas_prac/data/table.csv')
#%%
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'],name= 'This is a series',dtype='float64')
s.values
s.name
s.dtype
s_index=list(s.index)
print([attr for attr in dir(s) if not attr.startswith('__')])
#%%Dataframe
df2 = pd.DataFrame({'col1':list('abcde'),'col2':range(5,10),'col3':[1.3,2.5,3.6,4.6,5.8]},
                  index=['one','two','three','four','five']
    )

df2['col1']
df2.values
df2.shape
df2.mean()
#%% index align
df3=df2.drop(index='three',columns='col3')

del df2["col2"]
df2['col2']= [5,6,7,8,9]
df2.pop('col2')
#%%
df3= pd.DataFrame({'A':[1,2,3],'B':['a','b','c']},index=[1,2,3])
C=pd.Series(list("def"))
df3.assign(C=pd.Series(list("def")))

#%% Data
df = pd.read_csv('Pandas_prac/data/table.csv')
df.tail()
df['Weight'].unique()
df['Weight'].nunique()
df["Physics"].count()
df["Physics"].value_counts()
df.info()
df.describe()

df["Physics"].describe()
df['Math'].idxmax()
df['Math'].nlargest(5)

df['Math'].clip(33,80)
df['Address'].replace(['street_1','srteet_2'],['one','two'])
df.replace({'Address':{'street_1':'one','street_2':'two'}})

df['Math'].apply(lambda x: str(x) + '!')
df.apply(lambda x: x.apply(lambda x: str(x) + '!'))

df.set_index('Math').sort_index(ascending=True)
df.sort_values(by='Class').head()

