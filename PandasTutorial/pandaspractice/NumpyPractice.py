import numpy as np
from pandas import Series, DataFrame 
import pandas as pd 
from numpy import size
# list1 = [1,2,3,4,5,6,7,8,9,10]
# #print np.array(list1).mean()
# a = np.array(list1)
# print np.array(list1).mean(axis=0)
# print a.shape
# 
# # print a[-2:1:-1]
# 
# b = "HelpA"
# # print b[-5]
# 
# # print "abcd"[-1:0:-1] #= "dcb"
# btwod = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[7,8,9,10,11,19]])
# # print btwod[0:2,0:3]
# # print btwod.dtype
# # print btwod.shape
# # print btwod.argmax()
# # print btwod[0].argmax()
# btwodslice = btwod[0,0:4].copy()
# # print btwodslice
# btwodslice[:] = 100
# # print btwod
# 
# 
# a = np.array(range(5))
# print a
# b = np.array(range(5))
# print b
# 
# b = a + b
# print b
# print a
series1 = Series([1,12,3,4,5,26,7,88,9,10],index=['a','b','c','d','e','f','g','h','i','k'])
# print series1.sort_values()

# print series1.add(Series([1,2]),fill_value=0)
# print series1.add(Series([1,2])).dropna()

# series2 =  series1.add(Series([1,2],index=['a','h'])).dropna()
series2 =  series1.add(Series([1,2],index=['a','h']),fill_value=0)
# print series2

series2 = series2.reindex(['101','102','c','d','105','f','107','h','i','110','s','u'],fill_value=0)

# print np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]).shape


df1 = DataFrame(data=np.random.randint(0,1000,size=(5,4)), index=list("ABCDE"), columns=['Number','Value','d','t'])
# print df1


u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv("C:\Users\Piyush\Downloads\ml-100k\u.user",sep='|',names=u_cols)
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('C:\Users\Piyush\Downloads\ml-100k\u.data',sep='\t', names=r_cols)
# print ratings
#, sep='\t'
# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('C:\Users\Piyush\Downloads\ml-100k\u.item', sep='|', names=m_cols,usecols=range(5))
# print movies.head(2)
# print users.head(10)
# # print users.info()
# # print users.describe()
# # print users.head()
# # print users[users.age>25].head()
# users = users.set_index("user_id")
# print users.head(4)
# print users.iloc[4]
#converters={'salary': lambda x: float(x.replace('$', ''))}

headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('C:\Users\Piyush\Downloads\city-of-chicago-salaries.csv', header=0,names=headers,converters={'salary': lambda x: float(x.replace('$', ''))})
# print chicago.head()
# by_dept = chicago.groupby('department')
# print by_dept.sum()
print "==="
# print by_dept.mean()
# print  by_dept.title.nunique().sort_values(ascending=False)

# print by_dept.title.nunique().sort_values(ascending=False)
def ranker(df):
    """Assigns a rank to each employee based on salary, with 1 being the highest paid.
    Assumes the data is DESC sorted."""
    df['dept_rank'] = np.arange(len(df)) + 1
    return df
chicago.sort_values('salary', ascending=False, inplace=True)
# print chicago.head(3)
chicago = chicago.groupby('department').apply(ranker)
print chicago.head(20)