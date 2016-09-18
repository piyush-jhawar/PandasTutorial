import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import load_iris
from sklearn import metrics
iris = load_iris()
# print iris
# print iris.data
X = iris.data
y = iris.target

print X.shape
print y.shape

#Begin ML
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X, y)

print logreg.predict(X)

print metrics.accuracy_score()
from sklearn.cross_validation import train_test_split




# knn = KNeighborsClassifier(n_neighbors=1)
# 
# print knn
# knn.fit(X, y)
# # print knn.predict([3,5,4,2])
# X_new = [[3,5,4,2],[5,4,3,2]]
# print knn.predict(X_new)
# 
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X, y)
# print knn.predict(X_new)



# style.use('ggplot')
# 
# web_stats = {'Day':[1,2,3,4,5,6],
#              'Visitors':[43,53,34,45,64,34],
#              'Bounce_Rate':[65,72,62,64,54,66]}
# df = pd.DataFrame(web_stats)
# # print df[['Visitors','Bounce_Rate']]
# print df.Visitors.tolist()
# print df.set_index('Day')


