# import pandas as pd
# l = [10,20,30,40]
# pd.Series(l)
# print(pd.Series(l,index=['i','ii','iii','iv']))

# import pandas as pd
# d = {'name':['Vismitha','niveditha','neha'],'percentage':[90,100,80]}
# print(pd.DataFrame(d))

#Empty Series
# import pandas as pd
# print(pd.Series())               #Output:Series([],dtype:object)

# Series Using array
# import pandas as pd
# import numpy as np
# s = np.array([10,20,30,40,50])
# l = pd.Series(s)
# print(l)

#Series using lists
# import pandas as pd
# l = 10,20,30,40
# s = pd.Series(l,index=[1,2,3,4])
# print(s)

#Series using dictionary
# import pandas as pd
# d = {'a':10,'b':20,'c':30,'d':40}
# s = pd.Series(d)
# print(s)

#List of Tuples
# import pandas as pd
# t = [('a',10),('b',20),('c',30),('d',40)]
# s = pd.Series(t)
# print(s)

#Loading the data from the excel file
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Downloads\\sample_sales_report.xlsx")
# df = pd.DataFrame(d)
# print(df)

#Loading the data from the csv file
# import pandas as pd
# d = pd.read_csv("C:\\Users\\Admin\\Downloads\\packet.csv")
# df = pd.DataFrame(d)
# print(df)

#Create the DataFrame using Dictionary
# import pandas as pd
# d = {'Students':['Sundeep','Saradhi','Raju','Ramu'],'Rollno':[101,102,103,104],'Telugu':[90,80,75,86],'English':[90,98,78,78]}
# df = pd.DataFrame(d)
# print(df)

#Create the Dataframe using list of tuples
# import pandas as pd
# d = [('Sundeep',101,90),('Saradhi',102,80),('Raju',103,75),('Ramu',104,78)]
# df = pd.DataFrame(d)
# print(df)

#Attributes of Series in Python
# import pandas as pd
# s = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'],name="Numbers")
# print(s.index)  # Output:RangeIndex(start=0,stop=5,step=1)
# print(s.array)    #Output: <NumpyExtensionArray> [10,20,30,40,50] Length :5,dtype:int64
# print(s.values)     # Output: [10 20 30 40 50]
# print(s.dtype)        # int64

# import pandas as pd
# s = pd.Series([10.5,20.5,30.5,40.5,50.5],index=['a','b','c','d','e'],name="Float")
# print(s.dtype)   #float64
# print(s.shape)     #(5,)
# print(s.ndim)        #1
# print(s.nbytes)        #Output: 40 (gives how much space occupied by the values)
# print(s.memory_usage())  #Output: 80(gives how much space occupied by both the index and the values)
# print(s.memory_usage(index=False))   #Output:40 (gives how much space occupied by the values only because index is assigned as False)
# print(s.size)             #Output:5 (size of array)
# print(s.name)               #Output:Float
# print(s.empty)              #Output: False because already s is having 5 elements and is not empty

#Mathematical Functions on Series in Pandas
# import pandas as pd
# a = pd.Series([10,20,30,40,50])
# b = pd.Series([5,4,3,2,1])
# print(a.add(b))
# print(a.subtract(b))
# print(a.multiply(b))
# print(a.divide(b))
# print(a.mod(b))
# print(a.pow(b))
# print(a.le(b))
# print(a.gt(b))
# c = b
# print(b.eq(c))














