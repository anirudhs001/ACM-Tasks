import csv
import pandas as pd
import numpy as np 

#for calculating the mean
from statistics import mean

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


#Find the Best Fit Slope
def best_fit_slope_n_const(X, y):
    m = (( (mean(X) * mean(y)) - mean(X * y)) /
         ( (mean(X)**2) - mean(X * X)))

    b = mean(y) - ( m * mean(X) )
    return m, b


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
m, b = best_fit_slope_n_const(X, y)

#create the regression line using m and b
regression_line = [(m*x)+b for x in X]

########################
######OUTPUTTING########
########################

#print the slope and intercept
print(f"slope:{m} and intercept:{b}")

#now create the graph:
  #Add the data points to the graph
plt.scatter(X,y,color='#003F72',label='data')
  #Add the regression line
plt.plot(X, regression_line, label='regression line')
  #Add the legend
plt.legend(loc=4)

#plot the graph. couldn't print it, so saving to file
plt.savefig("graph.png")
