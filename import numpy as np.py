import numpy as np

mylist = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
mylist[2][1] = 8777
print(mylist.ndim)
print(mylist)

#np.zeros(2) --fills a list with zeros
#np.ones(2) --fills a list with ones
#np.arange(4) --makes a index list
#np.concatenate((a, b)) --connects lists together
#a2 = a[np.newaxis, :] --and an axis