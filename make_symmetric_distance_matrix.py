# libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('df3.csv')
#print(data)
#data = data
data.drop(data.columns[[0]], axis=1, inplace=True)
print(data)
print(len(data))

# result_array = np.array([])
# for line in data_array:
#     result = do_stuff(line)
#     result_array = np.append(result_array, result)

## Construct a DISTANCE MATRIX

# this code makes the upper triangle
arr = data.set_index(['Item1','Item2'])['Count'].unstack().values
#show only first 8x8 sub matrix
print(arr[:8,:8])
print(arr.shape)

arr2 = np.triu(arr) + np.triu(arr,1).T
print(arr2[:8,:8])


# export distance dataframe to a csv file
arr3 = pd.DataFrame(arr2)
arr3.to_csv('sym_dist_matrix.csv')