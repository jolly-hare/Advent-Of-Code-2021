from icecream import ic
import numpy as np
from scipy import ndimage

data = []
for line in open("09.input", "r"):
    data.append([int(x) for x in list(line.strip())])
data = np.pad(data, pad_width=1, mode='constant', constant_values=9)
Answer1 = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data[0])-1):
        A = data[i][j]
        B = (data[i-1][j], data[i][j-1], data[i+1][j], data[i][j+1])
        Answer1 += 1 + A if A < np.amin(B) else 0
ic(Answer1)

data = data < 9
labeled_array, num_features = ndimage.label(data)
feature_size = []
for i in range(num_features):
    feature_size.append(sum(sum(labeled_array == i+1)))
Answer2 = np.prod(sorted(feature_size, reverse=True)[:3])
ic(Answer2)
