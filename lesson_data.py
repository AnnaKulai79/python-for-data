import pandas as pd

months = ['jan', 'feb', 'mar', 'apr']
sales = {
    'revenue': [100, 200, 150, 400],
    'items_sold': [23, 15, 43, 55],
    'new_clients': [10, 15, 18, 40]
}

df = pd.DataFrame(data=sales, index=months)
print(df)

vector = [1, 2, 3]
print(vector * 2)#  [1, 2, 3, 1, 2, 3]
series = pd.Series([1, 2, 3])
print(series * 2)
# 0    2
# 1    4
# 2    6
series_str = pd.Series(["a", "b", "c"])
print(series_str[0])# a
months1 = ['jan', 'feb', 'mar', 'apr']
sales1 = [100, 200, 150, 400]
data = pd.Series(data=sales1, index=months1)
print(data["feb"])

print(df.head(2))
print(df.tail(2))
print(df["revenue"])
df.info()
print(df.shape)# (4, 3)
print(df.columns)
print(df.describe())
print(df.dtypes)
df.revenue = pd.to_numeric(df.revenue)
print(df.loc[["feb", "apr"]])

movies_df = pd.read_csv('data/movies_metadata.csv')
pd.options.display.max_rows = 5
# print(movies_df.to_string())
print(pd.options.display.max_rows)