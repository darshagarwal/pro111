import pandas as pd
import random as rd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("/Volumes/DARSH/pro111/medium_data.csv")
data = df["reading_time"].tolist()
stdev= st.stdev(data)
mean=st.mean(data)
print("stdev of population:",stdev)
print("mean of population:",mean)

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=rd.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean_dataset=st.mean(dataset)
    return mean_dataset

mean_list = [] 
for i in range(0,1000): 
  set_of_means= random_set_of_means(100)
  mean_list.append(set_of_means) 
mean_of_sample = st.mean(mean_list) 
stdev_of_sample = st.stdev(mean_list) 
print("mean of the sampling distribution: ", mean_of_sample) 
print("std_deviation of the sampling distribution: ", stdev_of_sample)

stdev_start1,stdev_end1=mean_of_sample-stdev_of_sample,mean_of_sample+stdev_of_sample
stdev_start2,stdev_end2=mean_of_sample-(2*stdev_of_sample),mean_of_sample+(2*stdev_of_sample)
stdev_start3,stdev_end3=mean_of_sample-(3*stdev_of_sample),mean_of_sample+(3*stdev_of_sample)

fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_sample,mean_of_sample],y=[0,1.5],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[stdev_start1,stdev_start1],y=[0,1.5],mode="lines",name="stdev start 1"))
fig.add_trace(go.Scatter(x=[stdev_start2,stdev_start2],y=[0,1.5],mode="lines",name="stdev start 2"))
fig.add_trace(go.Scatter(x=[stdev_start3,stdev_start3],y=[0,1.5],mode="lines",name="stdev start 3"))
fig.add_trace(go.Scatter(x=[stdev_end1,stdev_end1],y=[0,1.5],mode="lines",name="stdev end 1"))
fig.add_trace(go.Scatter(x=[stdev_end2,stdev_end2],y=[0,1.5],mode="lines",name="stdev end 2"))
fig.add_trace(go.Scatter(x=[stdev_end3,stdev_end3],y=[0,1.5],mode="lines",name="stdev end 3"))
fig .show()

z_score= (mean_of_sample-mean)/stdev
print("the z-score is =",z_score)
