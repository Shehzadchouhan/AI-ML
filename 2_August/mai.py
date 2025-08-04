from sklearn.datasets import fetch_california_housing

import pandas as pd

#Load California housing dataset
housing = fetch_california_housing(as_frame=True)

#Convert to DataFrame
df=housing.frame

#display first 5 rows
print(df.head())

#show dataset information
print(df.info())