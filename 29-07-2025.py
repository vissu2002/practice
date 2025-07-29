#Indexing and Slicing DataFrames in Pandas
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Downloads\\sample_sales_report.xlsx")
# df = pd.DataFrame(d)
# print(df.head())  # gives the first 5 rows if nothing is specified
# print(df.head(9))  #gives the first 9 rows
# print(df.tail())     #gives last 5 rows if nothing is specified
# print(df.tail(6))      #gives the last 6 rows
# print(df.describe())     #gives the count,mean,std,min,25%,50%,75%,max values of each column
# print(df.columns)          #gives every column name
# print(df.shape)               #gives no of rows and columns
# print(df['Name'].head())          #gives starting 5 name in the table
# print(df[['Name','Product']].head(3))   #gives name,product of first 3 rows in the table
# print(df['Name'].tail())                    #gives the last 5 names
# print(df[1:8])                                #Slicing
# print(df[1:8:2])
# print(df[['ID','Name','Product']][1:5])
# for index,rows in df.iterrows():
#     print(index,rows)
#     print(index,rows[['ID','Name']])

#Sorting DataFrames
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Downloads\\sample_sales_report.xlsx")
# df = pd.DataFrame(d)
# # print(df.sort_values("ID",ascending=False))
# print(df.sort_values(['Name','ID'],ascending=[1,0]))  #Here 1 means Name comes in ascending order and 0 in descending order

#Manipulating DataFrames in pandas(Add column and drop column)
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Downloads\\student_marks.xlsx")
# df = pd.DataFrame(d)
# #Inserting the column
# # print(df)
# df['Total_marks'] = 0
# # print(df)
# df['Total_marks'] = df['Maths'] + df['Science'] + df['English'] + df['History']
# # print(df)
# #Deleting the column
# df = df.drop(columns='Total_marks')
# print(df)

# Exporting the DataFrame to excel,csv and text file in pandas
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Downloads\\student_marks.xlsx")
# df = pd.DataFrame(d)
# print(df)
# df['Total'] = df['Maths'] + df['Science'] + df['English'] + df['History']
# print(df)
# df.to_excel("C:\\Users\\Admin\\Downloads\\Updated_Marks.xlsx",index=False)
# print(df)
# df.to_csv("C:\\Users\\Admin\\Downloads\\New_Marks.csv",index=False)
# print(df)
# df.to_csv("C:\\Users\\Admin\\Downloads\\New_Marks.txt",index=False,sep='\t')
# print(df)

#Understanding loc[] and iloc[] in pandas
import pandas as pd
d = pd.read_excel("C:\\Users\\Admin\\Downloads\\Updated_Marks.xlsx")
df = pd.DataFrame(d)
# print(df)
# print(df.loc[3,'Name'])  #gives the 3rd row name in the table
# print(df.loc[0:4,['Name','Total']])  #gives only the name and total from 0 to 4th index
# print(df.loc[0:6,'Name':'Total'])      #gives from Name to total i.e from 0 to 6th index
# print(df.iloc[0:6,1:7])                  #0:6 means it will give the rows from 0 to 5 index,1:7 means it will give the column name from 1st column to 6th column
# print(df.iloc[[0,7]])                      # gives the row for only 0th and 7th index only
print(df.iloc[:,[0,5]])


# The main difference between loc[] and iloc[] is ,
# For Indexing : loc[] will give the index value i.e for example 0:6 means it will return from 0 to 6th index
#                iloc[] will give the index value i.e for example 0:6 means it will return from 0 to 5th index only
# For naming : In loc[], we can consider the strings also.
#              In iloc[], we won't consider the strings for column recognition.


















