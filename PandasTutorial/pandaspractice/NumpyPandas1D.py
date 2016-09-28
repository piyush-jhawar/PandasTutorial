import pandas as pd
from math import sqrt

# daily_engage = pd.read_csv("C:\Users\Piyush\Downloads\daily_engagement_full.csv")
# print len(daily_engage['acct'].unique())

# += operates inplace while + does not

def sqrt_method(values):
    return sqrt(values)

sqrtans = pd.Series([4,9,16,25,36,49,64])
print sqrtans.apply(sqrt_method)








