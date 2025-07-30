#Handling the Missing data in Pandas
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Documents\\missing_data.xlsx")
# df = pd.DataFrame(d)
# print(df)


# To remove the missing data = dropna()
#  To fill with default values = fillna()

# print(df.dropna())             # Removes all the missing rows in the table
# df.dropna(inplace=True)          # Inplace represents to modify the original DataFrame directly without creating the new one
# print(df)
# df['Math'].dropna()
# print(df)
# df.loc[:,['Math','Science']].dropna()
# print(df.fillna("Missing"))
# print(df['Math'].fillna(40))
# print(df.loc[:,['Math','Science','English']].fillna(67))
# print(df)
# print(df['Math'].fillna(df['Math'].mean()))
# print(df['Math'].mean())
# df[['Math','Science','English']] = df[['Math','Science','English']].fillna(67)
# print(df)

# Method 1:
# df['Math'].fillna(50,inplace=True)
# # print(df)
# df['Science'].fillna(56,inplace=True)
# # print(df)
# df['English'].fillna(86,inplace=True)
# # print(df)

#Method 2:
# df.fillna({'Math':50,'Science':67,'English':89},inplace=True)
# print(df)

# For Same Column Different Names
# missing_index = df[df['Name'].isna()].index
# names_to_fill = ["Pooja","Varun"]
# for i,idx in enumerate(missing_index):
#     df.loc[idx,'Name'] = names_to_fill[i]
# print(df)

# df['Total'] = 0
# df['Total'] = df['Math'] + df['Science'] + df['English']
# print(df)

# df.to_excel("C:\\Users\\Admin\\Documents\\correct_data.xlsx",index=False)
# print(df)

#Remove Duplicates from the DataFrame
# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Documents\\correct_data.xlsx")
# df = pd.DataFrame(d)
# print(df.duplicated())                #return the boolean value True where the duplicates are found else return False
# df.drop_duplicates(inplace=True)        #removes the duplicate rows from the table
# print(df)

# import pandas as pd
# d = pd.read_excel("C:\\Users\\Admin\\Documents\\correct_data.xlsx")
# df = pd.DataFrame(d)
# print(df.duplicated())
# df.drop_duplicates(inplace=True)
# df.to_excel("C:\\Users\\Admin\\Documents\\corrected_data.xlsx",index=False)
# print(df)

#Data Filtering using conditions in Python
import pandas as pd
d = pd.read_excel("C:\\Users\\Admin\\Documents\\correct_data.xlsx")
df = pd.DataFrame(d)
# print(df.loc[df['Name'].str.contains('a')])
# print(df.loc[(df['Math']>50) & (df['Science']>50)])
# print(df.loc[(df['Math']>50) | (df['Science']>50)])
# print(df.loc[df['Name'].str.startswith('s')])
# print(df.loc[df['Name'].str.endswith('a')])
























