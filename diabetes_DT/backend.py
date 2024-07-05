import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

def trainModel():
    # reading csv file and extracting class column to y.
    x = pd.read_csv("C:/MINI-PROJ/diabetes_prediction/org_data.csv")
    a = np.array(x)
    y = a[:,8] # classes having 0 and 1
    # extracting two features
    x = np.column_stack((x.Pregnancies,x.Glucose,x.BloodPressure,x.SkinThickness,x.Insulin,x.BMI,x.DiabetesPedigreeFunction,x.Age))
    # 569 samples and 2 features
    x.shape   
    clf = DecisionTreeClassifier()

    # fitting x samples and y classes 
    clf.fit(x, y)
    return clf
def predictData(l):
    clf=trainModel()
    test=np.array(l)
    return(clf.predict(test.reshape(1,-1)))
    