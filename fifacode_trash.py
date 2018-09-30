import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('fifa.csv', sep=',',header=None)
np_data=np.array(data)
#print(np_data.shape) 8848,19
#print(np_data.size) 168112
df=pd.DataFrame(data)
#print(df.head())
print(sorted(np.array(df[1:100][1])))
x=input()
