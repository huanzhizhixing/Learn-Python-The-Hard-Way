"""
Python 2.7.13 |Anaconda 4.3.1 (32-bit)| (default, Dec 19 2016, 13:36:02) [MSC v.1500 32 bit (Intel)]
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

data = randn(2,3)
Traceback (most recent call last):

  File "<ipython-input-1-895be91fa71d>", line 1, in <module>
    data = randn(2,3)

NameError: name 'randn' is not defined


import numpy as np

data = randn(2,3)
Traceback (most recent call last):

  File "<ipython-input-3-895be91fa71d>", line 1, in <module>
    data = randn(2,3)

NameError: name 'randn' is not defined


data = np.randn(2,3)
Traceback (most recent call last):

  File "<ipython-input-4-29db7cab0715>", line 1, in <module>
    data = np.randn(2,3)

AttributeError: 'module' object has no attribute 'randn'


data = np.random.randn(2,3)

data
Out[6]: 
array([[-0.63247784,  2.20781414, -0.43163705],
       [-0.37628697, -0.67372968, -0.1390752 ]])

data*10
Out[7]: 
array([[ -6.32477836,  22.07814141,  -4.31637046],
       [ -3.76286972,  -6.73729681,  -1.39075204]])

data+data
Out[8]: 
array([[-1.26495567,  4.41562828, -0.86327409],
       [-0.75257394, -1.34745936, -0.27815041]])

data.shape
Out[9]: (2, 3)

data.dtype
Out[10]: dtype('float64')
data1 = np.random.randn(3,4)

data1
Out[12]: 
array([[ 1.64410911, -0.08414913, -0.81095468, -0.85095549],
       [-0.68970799, -0.36535146, -0.53683746, -0.62033126],
       [ 0.47395795, -1.41059856, -0.2366747 , -0.81300927]])

data1 * 10
Out[13]: 
array([[ 16.44109108,  -0.84149134,  -8.10954684,  -8.50955491],
       [ -6.89707995,  -3.65351458,  -5.3683746 ,  -6.20331265],
       [  4.73957949, -14.10598564,  -2.36674702,  -8.13009275]])

data1 + data1
Out[14]: 
array([[ 3.28821822, -0.16829827, -1.62190937, -1.70191098],
       [-1.37941599, -0.73070292, -1.07367492, -1.24066253],
       [ 0.9479159 , -2.82119713, -0.4733494 , -1.62601855]])

data1 = [6,7.5,8,0,1]

arr1 = np.array(data1)

arr1
Out[17]: array([ 6. ,  7.5,  8. ,  0. ,  1. ])

data2 = [[1,2,3,4],[5,6,7,8]]

arr2 = np.array(data2)

arr2
Out[20]: 
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])

arr2.sharp
Traceback (most recent call last):

  File "<ipython-input-21-49ccbf056b6a>", line 1, in <module>
    arr2.sharp

AttributeError: 'numpy.ndarray' object has no attribute 'sharp'


arr2.shape
Out[22]: (2, 4)

arr2.ndim
Out[23]: 2

arr2.shape
Out[24]: (2, 4)

aarr1.dtype
Traceback (most recent call last):

  File "<ipython-input-25-cd8296e6d5ff>", line 1, in <module>
    aarr1.dtype

NameError: name 'aarr1' is not defined


arr1.dtype
Out[26]: dtype('float64')

arr2.dtype
Out[27]: dtype('int32')

np.zeros(10)
Out[28]: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

np.zeros((3,6))
Out[29]: 
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])

np.empty((2,3,2))
Out[30]: 
array([[[ 1.64410911, -0.08414913],
        [-0.81095468, -0.85095549],
        [-0.68970799, -0.36535146]],

       [[-0.53683746, -0.62033126],
        [ 0.47395795, -1.41059856],
        [-0.2366747 , -0.81300927]]])

np.arange(15)
Out[31]: array([ 0,  1,  2, ..., 12, 13, 14])

arr1 = np.array([1,2,3],dtype=np.float64)

arr2 = np.array([1,2,3],dtype=np.int32)

arr1
Out[34]: array([ 1.,  2.,  3.])

arr2
Out[35]: array([1, 2, 3])

arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])

arr
Out[37]: array([  3.7,  -1.2,  -2.6,   0.5,  12.9,  10.1])

arr.astype(np.int32)
Out[38]: array([ 3, -1, -2,  0, 12, 10])

numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.sting)
Traceback (most recent call last):

  File "<ipython-input-39-4100c84d91d4>", line 1, in <module>
    numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.sting)

AttributeError: 'module' object has no attribute 'sting'


numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.sting_)
Traceback (most recent call last):

  File "<ipython-input-40-22947880ce01>", line 1, in <module>
    numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.sting_)

AttributeError: 'module' object has no attribute 'sting_'


numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.string_)

numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.string)
Traceback (most recent call last):

  File "<ipython-input-42-441552fd750e>", line 1, in <module>
    numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.string)

AttributeError: 'module' object has no attribute 'string'


numeric_strings = np.array(['1.25','-9.5','42'],dtype=np.string_)

numeric_strings.astype(float)
Out[44]: array([  1.25,  -9.5 ,  42.  ])

int_array = np.arange(10)

int_array
Out[46]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

calibers = np.array([.22,.270,.357,.380,.44,.50],dtype = np.float64]
  File "<ipython-input-47-af7098623606>", line 1
    calibers = np.array([.22,.270,.357,.380,.44,.50],dtype = np.float64]
                                                                       ^
SyntaxError: invalid syntax


calibers = np.array([.22,.270,.357,.380,.44,.50],dtype = np.float64])
  File "<ipython-input-48-e494df52b63e>", line 1
    calibers = np.array([.22,.270,.357,.380,.44,.50],dtype = np.float64])
                                                                       ^
SyntaxError: invalid syntax


calibers = np.array([.22,.270,.357,.380,.44,.50],dtype = np.float64)

int_array.satype(calibers.dtype)
Traceback (most recent call last):

  File "<ipython-input-50-60930988387d>", line 1, in <module>
    int_array.satype(calibers.dtype)

AttributeError: 'numpy.ndarray' object has no attribute 'satype'


int_array.astype(calibers.dtype)
Out[51]: array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])

empty_uint32 = np.empty(8,dtype='u4')

empty_uint32
Out[53]: array([0, 0, 0, 0, 0, 0, 0, 0], dtype=uint32)

arr=  np.array([1.,2.,3.],[4.,5.,6.]])
  File "<ipython-input-54-6f3a94b88358>", line 1
    arr=  np.array([1.,2.,3.],[4.,5.,6.]])
                                        ^
SyntaxError: invalid syntax


arr=  np.array([[1.,2.,3.],[4.,5.,6.]])

arr
Out[56]: 
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])

arr
Out[57]: 
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])

arr * arr
Out[58]: 
array([[  1.,   4.,   9.],
       [ 16.,  25.,  36.]])

arr - arr
Out[59]: 
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])

1/arr
Out[60]: 
array([[ 1.        ,  0.5       ,  0.33333333],
       [ 0.25      ,  0.2       ,  0.16666667]])

arr**0.5
Out[61]: 
array([[ 1.        ,  1.41421356,  1.73205081],
       [ 2.        ,  2.23606798,  2.44948974]])

arr = np.arange(10)

arr
Out[63]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[5]
Out[64]: 5

arr[0]
Out[65]: 0

arr[5:8]
Out[66]: array([5, 6, 7])

arr[5:8]=12

array
Traceback (most recent call last):

  File "<ipython-input-68-a7cf24f7419f>", line 1, in <module>
    array

NameError: name 'array' is not defined


arr
Out[69]: array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])

arr_slice = arr[5:8]

arr_slice[1]=12345

arr
Out[72]: array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,     9])

arr_slice[:]=64

arr
Out[74]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[2]
Out[76]: array([7, 8, 9])

arr2d[0][2]
Out[77]: 3

ar2d[0,2]
Traceback (most recent call last):

  File "<ipython-input-78-fb4415ad7d83>", line 1, in <module>
    ar2d[0,2]

NameError: name 'ar2d' is not defined


arr2d[0,2]
Out[79]: 3

arr2d[0][2]
Out[80]: 3

arr3d=np.array([[[1,2,4],[4,5,6]],[[7,8,9],[10,11,12]]])

arr3d
Out[82]: 
array([[[ 1,  2,  4],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

arr3d[0]
Out[83]: 
array([[1, 2, 4],
       [4, 5, 6]])

arr3d[0][1]
Out[84]: array([4, 5, 6])

arr3d[0,0,1]
Out[85]: 2


old_values=arr3d[0].copy()

arr3d[0]
Out[87]: 
array([[1, 2, 4],
       [4, 5, 6]])

arr3d[0]=42

arr3d
Out[89]: 
array([[[42, 42, 42],
        [42, 42, 42]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

arr3d[0]=old_values

arr3d
Out[91]: 
array([[[ 1,  2,  4],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

arr3d[1,0]
Out[92]: array([7, 8, 9])

arr[1:6]
Out[93]: array([ 1,  2,  3,  4, 64])

arr
Out[94]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])

arr2d
Out[95]: 
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

arr2d[:2}
  File "<ipython-input-96-d4eb2e458fad>", line 1
    arr2d[:2}
            ^
SyntaxError: invalid syntax


arr2d[:2]
Out[97]: 
array([[1, 2, 3],
       [4, 5, 6]])

arr2d[:2,1:]
Out[98]: 
array([[2, 3],
       [5, 6]])

arr2d[1,:2]
Out[99]: array([4, 5])

arr2d
Out[100]: 
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

arr2d[1,:2]
Out[101]: array([4, 5])

arr2d[2,1:]
Out[102]: array([8, 9])

arr2d[1,:2]
Out[103]: array([4, 5])

arr2d[2,:1]
Out[104]: array([7])

arr2d[:,:1]
Out[105]: 
array([[1],
       [4],
       [7]])

arr2d[:2,1:]
Out[106]: 
array([[2, 3],
       [5, 6]])

arr2d
Out[107]: 
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

data = np.random.randn(7,4)

data
Out[110]: 
array([[-0.73074491, -0.59673514,  0.92469024, -1.16006346],
       [ 0.74096615,  1.2269315 ,  0.78240714,  0.3004154 ],
       [-0.46689427, -0.11113354,  0.33839061, -2.45553145],
       ..., 
       [-1.20552841, -0.69248681, -0.77995381,  1.93769837],
       [-0.15505515,  0.92210411,  1.07491592,  0.16673457],
       [-1.60200782, -0.61363886, -0.9097595 , -0.90570414]])

names
Out[111]: 
array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], 
      dtype='|S4')

names =='Bob'
Out[112]: array([ True, False, False,  True, False, False, False], dtype=bool)

data >=0
Out[113]: 
array([[False, False,  True, False],
       [ True,  True,  True,  True],
       [False, False,  True, False],
       ..., 
       [False, False, False,  True],
       [False,  True,  True,  True],
       [False, False, False, False]], dtype=bool)

data[names=='Bob']
Out[114]: 
array([[-0.73074491, -0.59673514,  0.92469024, -1.16006346],
       [-1.41344124, -0.86227991, -0.72394583, -0.83976213]])

data[names=='Bob',2:]
Out[115]: 
array([[ 0.92469024, -1.16006346],
       [-0.72394583, -0.83976213]])

data[names=='Bob',3]
Out[116]: array([-1.16006346, -0.83976213])

array([-1.428,0.769])
Traceback (most recent call last):

  File "<ipython-input-117-13b4c3873fee>", line 1, in <module>
    array([-1.428,0.769])

NameError: name 'array' is not defined


names != 'Bob'
Out[118]: array([False,  True,  True, False,  True,  True,  True], dtype=bool)

data[-(names == 'Bob')]
__main__:1: DeprecationWarning: numpy boolean negative, the `-` operator, is deprecated, use the `~` operator or the logical_not function instead.
Out[119]: 
array([[ 0.74096615,  1.2269315 ,  0.78240714,  0.3004154 ],
       [-0.46689427, -0.11113354,  0.33839061, -2.45553145],
       [-1.20552841, -0.69248681, -0.77995381,  1.93769837],
       [-0.15505515,  0.92210411,  1.07491592,  0.16673457],
       [-1.60200782, -0.61363886, -0.9097595 , -0.90570414]])

mask = (names == 'Bob)   |   (names =='will')
  File "<ipython-input-120-b41150bc9e9a>", line 1
    mask = (names == 'Bob)   |   (names =='will')
                                              ^
SyntaxError: invalid syntax


mask = (names == 'Bob)|(names =='will')
  File "<ipython-input-121-1f903bcb873b>", line 1
    mask = (names == 'Bob)|(names =='will')
                                        ^
SyntaxError: invalid syntax


mask = (names == 'Bob)|(names =='will')
  File "<ipython-input-122-1f903bcb873b>", line 1
    mask = (names == 'Bob)|(names =='will')
                                        ^
SyntaxError: invalid syntax


mask = (names == 'Bob)|(names =='Will')
  File "<ipython-input-123-494687ba6166>", line 1
    mask = (names == 'Bob)|(names =='Will')
                                        ^
SyntaxError: invalid syntax


mask = (names == 'Bob) or (names =='Will')
  File "<ipython-input-124-97546b700e2e>", line 1
    mask = (names == 'Bob) or (names =='Will')
                                           ^
SyntaxError: invalid syntax


mask = (names == 'Bob') or (names =='Will')
Traceback (most recent call last):

  File "<ipython-input-125-08dfba412889>", line 1, in <module>
    mask = (names == 'Bob') or (names =='Will')

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()


mask = (names == 'Bob') | (names =='Will')

mask
Out[127]: array([ True, False,  True,  True,  True, False, False], dtype=bool)

data[mask]
Out[128]: 
array([[-0.73074491, -0.59673514,  0.92469024, -1.16006346],
       [-0.46689427, -0.11113354,  0.33839061, -2.45553145],
       [-1.41344124, -0.86227991, -0.72394583, -0.83976213],
       [-1.20552841, -0.69248681, -0.77995381,  1.93769837]])

data[data<0] = 0

data
Out[130]: 
array([[ 0.        ,  0.        ,  0.92469024,  0.        ],
       [ 0.74096615,  1.2269315 ,  0.78240714,  0.3004154 ],
       [ 0.        ,  0.        ,  0.33839061,  0.        ],
       ..., 
       [ 0.        ,  0.        ,  0.        ,  1.93769837],
       [ 0.        ,  0.92210411,  1.07491592,  0.16673457],
       [ 0.        ,  0.        ,  0.        ,  0.        ]])

arr = np.empty((8,4))

arr
Out[132]: 
array([[  1.60218491e-306,   4.45039387e-308,   1.37961302e-306,
          6.39757117e-308],
       [  5.28471593e-308,   9.79101760e-307,   7.78792402e-308,
          6.39722315e-308],
       [  9.34613864e-307,   6.67535739e-308,   6.95354255e-308,
          4.45028353e-308],
       ..., 
       [  4.45053392e-308,   4.45028353e-308,   4.45028353e-308,
          4.45028353e-308],
       [  4.45028353e-308,   1.22381778e-307,   1.22381778e-307,
          1.22381778e-307],
       [  4.45028353e-308,   4.45028353e-308,   6.39726135e-308,
          0.00000000e+000]])

for i in range(8):
    arr[i] = i
arr

Out[133]: 
array([[ 0.,  0.,  0.,  0.],
       [ 1.,  1.,  1.,  1.],
       [ 2.,  2.,  2.,  2.],
       ..., 
       [ 5.,  5.,  5.,  5.],
       [ 6.,  6.,  6.,  6.],
       [ 7.,  7.,  7.,  7.]])

arr[[4,3,0,6]]
Out[134]: 
array([[ 4.,  4.,  4.,  4.],
       [ 3.,  3.,  3.,  3.],
       [ 0.,  0.,  0.,  0.],
       [ 6.,  6.,  6.,  6.]])



arr[[-3,-5,-7]]
Out[135]: 
array([[ 5.,  5.,  5.,  5.],
       [ 3.,  3.,  3.,  3.],
       [ 1.,  1.,  1.,  1.]])

arr = np.arange(32).reshape((8,4))

arr
Out[137]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       ..., 
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])

arr[[1,5,7,2],[0,3,1,2]]
Out[138]: array([ 4, 23, 29, 10])

arr[[1,5,7,2]][:,[0,3,1,2]]
Out[139]: 
array([[ 4,  7,  5,  6],
       [20, 23, 21, 22],
       [28, 31, 29, 30],
       [ 8, 11,  9, 10]])

arr[np.ix_([1,5,7,2],[0,3,1,2])]
Out[140]: 
array([[ 4,  7,  5,  6],
       [20, 23, 21, 22],
       [28, 31, 29, 30],
       [ 8, 11,  9, 10]])

arr = np.arange(15).reshape(3,5)

arr
Out[142]: 
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

arr.T
Out[143]: 
array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])

arr = np.random.randn(6.3)
__main__:1: VisibleDeprecationWarning: using a non-integer number instead of an integer will result in an error in the future

arr
Out[145]: 
array([ 0.10803387,  1.86586011, -0.6555269 , -1.09888123,  0.67273642,
        1.52435575])

arr = np.random.randn(6,3)

arr
Out[147]: 
array([[ 1.31076653, -0.05405776,  0.59558262],
       [ 0.37844283, -1.62855707,  0.80849307],
       [ 1.24124235,  0.86749108, -1.80538345],
       [-0.14230263, -0.0703719 ,  0.38897384],
       [-0.12477745,  0.55898402, -0.77892081],
       [ 1.13455986, -0.3689972 ,  0.01685006]])

np.dot(arr.T,arr)
Out[148]: 
array([[ 4.725056  , -0.08879009, -1.09332307],
       [-0.08879009,  3.8612354 , -3.38402174],
       [-1.09332307, -3.38402174,  5.02609132]])

arr = np.arange(16).reshape((2,2,4))

arr
Out[150]: 
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])

arr.transpose(1,0,2)
Out[151]: 
array([[[ 0,  1,  2,  3],
        [ 8,  9, 10, 11]],

       [[ 4,  5,  6,  7],
        [12, 13, 14, 15]]])

arr
Out[152]: 
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])

aa.swapaxes(1,2)
Traceback (most recent call last):

  File "<ipython-input-153-ecd2c8892999>", line 1, in <module>
    aa.swapaxes(1,2)

NameError: name 'aa' is not defined


arr.swapaxes(1,2)
Out[154]: 
array([[[ 0,  4],
        [ 1,  5],
        [ 2,  6],
        [ 3,  7]],

       [[ 8, 12],
        [ 9, 13],
        [10, 14],
        [11, 15]]])

		
		
		
		
		
		
		
		
		
		
		




 
import numpy as np
arr = np.arange(10)
arr
Out[11]:
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [14]:

np.sqrt(arr)
np.sqrt(arr)
Out[14]:
array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ,
        2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ])
In [16]:

arr
np.exp(arr)
Out[16]:
array([  1.00000000e+00,   2.71828183e+00,   7.38905610e+00,
         2.00855369e+01,   5.45981500e+01,   1.48413159e+02,
         4.03428793e+02,   1.09663316e+03,   2.98095799e+03,
         8.10308393e+03])
In [19]:

y
x = np.random.randn(8)
y = np.random.randn(8)
x
y
Out[19]:
array([-0.29993461,  0.31901239,  0.22948294, -0.77151342, -0.39717314,
       -0.13143562, -2.14396077,  0.20904906])
In [20]:

x
x
Out[20]:
array([-1.20031516, -0.3895713 ,  0.73150672,  0.40635057, -0.99016745,
        0.69240673,  0.17837956,  0.28746425])
In [21]:

y
y
Out[21]:
array([-0.29993461,  0.31901239,  0.22948294, -0.77151342, -0.39717314,
       -0.13143562, -2.14396077,  0.20904906])
In [24]:

arr
arr = np.random.randn(7)*5
arr
Out[24]:
array([-0.18264528, -4.79233246, -5.23162139,  9.88116325, -2.28938587,
       -4.35381274,  5.80593841])
In [26]:

ys
points = np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)
ys
Out[26]:
array([[-5.  , -5.  , -5.  , ..., -5.  , -5.  , -5.  ],
       [-4.99, -4.99, -4.99, ..., -4.99, -4.99, -4.99],
       [-4.98, -4.98, -4.98, ..., -4.98, -4.98, -4.98],
       ..., 
       [ 4.97,  4.97,  4.97, ...,  4.97,  4.97,  4.97],
       [ 4.98,  4.98,  4.98, ...,  4.98,  4.98,  4.98],
       [ 4.99,  4.99,  4.99, ...,  4.99,  4.99,  4.99]])
In [27]:

,title
from matplotlib.pyplot import imshow,title
In [28]:

import matplotlib as plt
z = np.sqrt(xs**2+ys**2)
z
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
plt.title('Image plot of $\sqrt{x^2+y^2} $for a grid of values')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-28-78a00af7f1c7> in <module>()
      2 z = np.sqrt(xs**2+ys**2)
      3 z
----> 4 plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
      5 plt.title('Image plot of $\sqrt{x^2+y^2} $for a grid of values')

AttributeError: 'module' object has no attribute 'imshow'
"""
