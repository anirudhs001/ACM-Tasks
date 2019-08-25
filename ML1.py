import csv
import pandas as pd
import numpy as np 

#for calculating the mean
from statistics import mean
#for graphing
import matplotlib.pyplot as plt

#Find the Best Fit Slope
def best_fit_slope(X, y):
    m = (( (mean(X) * mean(y)) - mean(X * y)) /
         ( (mean(X)**2) - mean(X * X)))
    return m


########################
####LOAD THE DATA#######
########################

#remember the url for the training data
url_train_data = "https://raw.githubusercontent.com/ashryaagr/acm_task_dataset/master/train.csv"
#load the training data
data = pd.read_csv(url_train_data)


########################
#####WORK THE DATA######
########################

#remove the missing data
data.dropna(inplace = True)

#seperate the features and labels into seperate arrays
#note the arrays here contain strings.need to convert them to floats
X = np.array(data.drop(['x'], 1))
y = np.array(data['y'])

#convert string members to floats
X = np.array(list(map(float, X)))
y = np.array(list(map(float, y)))


#get the best fit slope
#m = best_fit_slope(X, y)

#print the slope
#print(m)

plt.plot(X)
plt.show()