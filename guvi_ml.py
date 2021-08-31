#PREDICT CAR TYPE
#ML using DecisionTree to predict car type for 
#data input of seat and horsepower 

#import
import sklearn
from sklearn import tree

#data
features = [[2,100],[6,25],[1,300],[1,1000],[4,100],[10,100]]
#[seats,horsepower]
label = [1,2,1,1,2,2]
#1 - Sports/Race Car and 2 - Family Car

#ML
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,label)

#test
print(clf.predict([[1,140]]))
print(clf.predict([[4,140]]))
#Output of this ML model is  1 or 2

#Success