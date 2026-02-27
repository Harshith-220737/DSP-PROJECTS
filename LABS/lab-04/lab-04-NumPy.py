import numpy as np
import pandas as pd # type: ignore

print("----- Broadcasting Example 1 -----")
np.random.seed(1234)
A = np.random.randint(1, 10, (3, 4))
B = np.random.randint(1, 10, (3, 1))
print("A:\n", A)
print("B:\n", B)
print("A + B:\n", A + B)

print("\n----- Broadcasting Example 2 (Not Compatible) -----")
np.random.seed(4321)
A2 = np.random.randint(1, 10, (4, 4))
B2 = np.random.randint(1, 10, (2, 1))
print("A2:\n", A2)
print("B2:\n", B2)
print("Shapes:", A2.shape, B2.shape)

print("\n----- newaxis Difference Matrix -----")
A = np.array([3, 11, 4, 5])
B = np.array([5, 0, 3])
diff_matrix = A[:, np.newaxis] - B
print(diff_matrix)

print("\n----- Reshape Example -----")
foo = np.arange(1, 9)
print(foo.reshape(2, 4))

print("\n----- Transpose Example -----")
bar = np.array([[1,2,3,4],[5,6,7,8]])
print(bar.T)

print("\n----- Boolean Indexing -----")
foo = np.array([[3,9,7],[2,0,3],[3,3,1]])
mask = foo == 3
print("Mask:\n", mask)
foo[mask] = 0
print("Updated Array:\n", foo)

print("\n----- Logical Operators -----")
b1 = np.array([False, False, True, True])
b2 = np.array([False, True, False, True])
print("AND:", b1 & b2)
print("OR:", b1 | b2)
print("XOR:", b1 ^ b2)

print("\n----- NaN Example -----")
bot = np.ones((3,4))
bot[[0,2],[1,2]] = np.nan
print(bot)
print("NaN Positions:\n", np.isnan(bot))

print("\n----- Random Generator Examples -----")
rng = np.random.default_rng(123)
print("Integers with replacement:", rng.integers(1,7,3))
print("Choice without replacement:", rng.choice(10,3,replace=False))
foo = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
print("Permutation:\n", rng.permutation(foo, axis=0))
print("Uniform sample:\n", rng.uniform(1.0,2.0,(2,2)))
print("Normal sample:", rng.normal(0,1,2))
print("Binomial sample:\n", rng.binomial(10,0.25,(3,2)))

print("\n----- High School Reunion Problem -----")
dailywts = 185 - np.arange(5*7)/5
weekend_avg = (dailywts[5::7] + dailywts[6::7]) / 2
print("Average weekend weights:", weekend_avg)

print("\n----- Mean, Median, Std -----")
arr = np.array([1,2,3,4,5])
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std:", np.std(arr))

print("\n----- DataFrame from NumPy Array -----")
data = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(data, columns=["A","B","C"])
print(df)

print("\n----- Cumulative Sum Column -----")
df["Cumsum_A"] = df["A"].cumsum()
print(df)

print("\n----- Matrix Multiplication -----")
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])
print(np.matmul(m1, m2))

print("\n----- Random Array Unique Values -----")
rand_arr = np.random.randint(1,10,10)
print("Array:", rand_arr)
print("Unique:", np.unique(rand_arr))

print("\n----- Transpose DataFrame -----")
print(df.T)

print("\n----- 3x3 Matrix from 2 to 10 -----")
mat = np.arange(2,11).reshape(3,3)
print(mat)

print("\n----- Null Vector Size 10, Sixth Value = 11 -----")
vec = np.zeros(10)
vec[6] = 11
print(vec)

print("\n----- Array Values 12 to 38 -----")
print(np.arange(12,39))

print("\n----- Common Values Between Two Arrays -----")
arr1 = np.array([0,10,20,40,60])
arr2 = np.array([10,30,40])
print(np.intersect1d(arr1, arr2))

print("\n----- Set Difference Between Two Arrays -----")
arr1 = np.array([0,10,20,40,60,80])
arr2 = np.array([10,30,40,50,70,90])
print(np.setdiff1d(arr1, arr2))

print("\n----- Compare Two Arrays Element-wise -----")
a = np.array([1,2])
b = np.array([4,5])
print("a > b:", a > b)
print("a >= b:", a >= b)
print("a < b:", a < b)
print("a <= b:", a <= b)

print("\n----- 3D Diagonal Ones Array -----")
diag3d = np.eye(3)
print(diag3d)

print("\n----- 4th Element of Array -----")
arr = np.array([[2,4,6],[6,8,10]])
print("Fourth element:", arr.flat[3])

print("\n----- Convert 1D Arrays as Columns to 2D -----")
a = np.array([10,20,30])
b = np.array([40,50,60])
col_stack = np.column_stack((a,b))
print(col_stack)

print("\n----- Multiply (3,4) Array Elements by 3 -----")
orig = np.arange(12).reshape(3,4)
print("Original:\n", orig)
print("New:\n", orig * 3)