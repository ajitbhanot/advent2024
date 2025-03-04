# import time
# import numpy as np
import pandas as pd
# start = time.time()
# count = 0
# n = 0
#data = np.loadtxt("day2.txt",skiprows=n)
#data = np.genfromtxt("day2.txt",missing_values=0,filling_values=0)
df = pd.read_csv('day2_a.txt', delimiter=' ',header=None, names=range(8))
#print(data.shape)
# df2 = df.diff(axis=1)
df.fillna(0,inplace=True)
#print(df)
i = 0
for i in range(0,df.shape[0]):
    for j in range (0,df.shape[1]):
        print(i)
        print(j)
# # list1 = data[:,0]
# # list2 = data[:,1]
# # list1.sort()
# # list2.sort()
# # list3 = abs(list2-list1)
# # xy = (np.intersect1d(list1, list2, return_indices=False))
# #
# #
# # uniq = np.unique_counts(list2)
# # distaince_sum= 0
# # for x in np.nditer(xy):
# #     print(x)
# #     sum+= x*(np.count_nonzero(list2 == x))
# #
# # print(sum)
# #
# # end = time.time()
# # print("Execution time in seconds: ",(end-start))

