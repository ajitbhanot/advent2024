from functools import reduce
import time
import numpy as np
start = time.time()
count = 0
n = 0
data = np.loadtxt("day1a.txt",skiprows=n)
list1 = data[:,0]
list2 = data[:,1]
list1.sort()
list2.sort()
list3 = abs(list2-list1)
xy = (np.intersect1d(list1, list2, return_indices=False))


uniq = np.unique_counts(list2)
distaince_sum= 0
for x in np.nditer(xy):
    print(x)
    sum+= x*(np.count_nonzero(list2 == x))

print(sum)

end = time.time()
print("Execution time in seconds: ",(end-start))
