#! /usr/bin/env python

"""
Example code using NumPy for array manipulation
"""

import numpy as np

r0mat = np.array(100)
r1mat = np.array([-10, 20, -5])
r2mat = np.array([[16, -8], [1.5, 10]])
r3mat = np.array([[[3, 1], [2, 4]], [[5, 6], [0, 7]]])

matrices = [r0mat, r1mat, r2mat, r3mat]

for m in matrices:
    print(f"matrix has dimension {m.ndim}, \
            size {m.size}, \
            shape {m.shape}.")

# raise rank 1 to rank 3
r3mat1 = r1mat.reshape(3, 1)
print(r1mat)
print(r3mat1)

# lower rank 3 to rank 2
r2mat3 = r3mat.reshape(2, 4)
print(r3mat)
print(r2mat3)
