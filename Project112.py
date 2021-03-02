import pandas as pd
import statistics
import plotly.express as pe
import random
import numpy as np

df = pd.read_csv("savings_data.csv")
bigData = df["quant_saved"].tolist()

fig = pe.scatter(df,y='quant_saved')
fig.show()

mean1 = statistics.mean(bigData)
median1 = statistics.median(bigData)
mode1 = statistics.mode(bigData)
print("The mean of the big data is ",mean1)
print("The median of the big data is ",median1)
print("The mode of the big data is ",mode1)

dataset1 = []
dataset2 = []
def random_set_of_means(counter):
  
    
  for i in range(0, counter):
      random_index1 = random.randint(0, len(bigData) - 1)
      value1 = bigData[random_index1]
      dataset1.append(value1)
        
      random_index2 = random.randint(0, len(bigData) - 1)
      value2 = bigData[random_index1]
      dataset2.append(value2)

  mean1 = statistics.mean(dataset1)
  mean2 = statistics.mean(dataset2)
  return mean1
  return mean2

def show_fig(mean_list):
  sampling_mean1 = statistics.mean(mean_list)
  sampling_median1 = statistics.median(mean_list)
  sampling_mode1 = statistics.mode(mean_list)
  sampling_mean2 = statistics.mean(mean_list)
  sampling_median2 = statistics.median(mean_list)
  sampling_mode2 = statistics.mode(mean_list)

  print("The mean of the first sample is ", sampling_mean1)
  print("The median of the first sample is ", sampling_median1)
  print("The mode of the first sample is ", sampling_mode1)
  print("The mean of the second sample is ", sampling_mean2)
  print("The median of the second sample is ", sampling_median2)
  print("The mode of the second sample is ", sampling_mode2)  


  correlation = np.corrcoef(dataset1, dataset2)
  print("The correlation between the 1st sample set and the second one is: ", correlation[0,1])

def setup():
  mean_list = []

  for i in range(0, 100):
    set_of_means = random_set_of_means(30)
    mean_list.append(set_of_means)

  show_fig(mean_list)

setup()
