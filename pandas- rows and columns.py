#--------.iloc[] → position-based selection--------#
import pandas as pd
data={
    'product': ['laptop', 'mouse', 'keyboard', 'monitor'],
    'price': [60000, 800, 1500, 12000 ],
    'quantity': [2, 5, 3, 2]
}
df= pd.DataFrame(data)
print(df)

#Select one row:
print(df.iloc[0]) #1st row
print(df.iloc[1]) #2st row
print(df.iloc[2]) #3st row
print(df.iloc[3]) #4st row 

#Select multiple rows:
print(df.iloc[0:2])

#Select a specific cell:
print(df.iloc[1, 2])

'''Task 1
Get the third row.'''
print(df.iloc[2])

'''Task 2
Get the first two rows.'''
print(df.iloc[0:2])

'''Task 3
Get the price of the keyboard.'''
print(df.iloc[2,1])

'''Task 4
Get the quantity of the monitor.'''
print(df.iloc[3,2])

'''Task 5 ⭐
Get only the first two rows and the first two columns.'''
print(df.iloc[0:2, 0:2])



#--------.loc[] → label/index-based selection--------#
import pandas as pd
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [60000, 800, 1500, 12000],
    "Quantity": [2, 5, 3, 2]
}
cf = pd.DataFrame(
    data,
    index=["A", "B", "C", "D"]
)
print(cf)

#Get a row using its label:
print(cf.loc["C"])

#Get a specific value:
print(cf.loc["C","Price"])

#Select multiple rows:
print(cf.loc[["A","C"]])

'''Task 1: Get the B row.'''
print(cf.loc["B"])

'''Task 2: Get the D row.'''
print(cf.loc["D"])

'''Task 3: Get the price of C.'''
print(cf.loc["C","Price"])

'''Task 4: Get the quantity of A.'''
print(cf.loc["A","Quantity"])

'''Task 5 ⭐: Get rows A and D, but only the Product and Price columns.'''
print(cf.loc[["A","D"],["Product","Price"]])
