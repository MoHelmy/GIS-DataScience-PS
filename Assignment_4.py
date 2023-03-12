## To run this script, the file "Sask_RM_data.csv" has to be in the same directry with the script
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns


# Please go to Palette_training_4 GitHub repo and
# 1. Read Sask_RM_data.csv.

# 2. Rename column namse Crop Year, Canola - bu/ac, Spring Wheat - bu/ac with
# Year, Canola, SpringWheat respectively.

# 1. Read csv file by using pandas

## Your code here - down ##
fl = "Sask_RM_Data.csv"
df = pd.read_csv(fl)

print(df.head())
## Your code here - up ##


# 2. Rename columns

## Your code here - down ##
df = df.rename({'Crop Year': 'Year', 'Canola - bu/ac': 'Canola', 'Spring Wheat - bu/ac': 'SpringWheat'}, axis=1)
print(df.head())
## Your code here - up ##

## Question 2 (65 points)

# 1. How many missing values in each column?

## Your code here - down ##
print("1. How many missing values in each column?")
print(df.isna().sum())
## Your code here - up ##


# 2. Find unique values of RMs(Rural Municipalities).

## Your code here - down ##
print("2. Find unique values of RMs(Rural Municipalities).")
RMU = df.RM.unique()
#print(RMU)
## Your code here - up ##

# 3. Use groupby() and find top 10 RMs in terms of average Canola yield through 10 years.

## Your code here - down ##
print("3. Use groupby() and find top 10 RMs in terms of average Canola yield through 10 years.")
dfc = df.groupby("RM")['Canola'].mean()
print(dfc.sort_values().head(10))
## Your code here - up ##

# 4. Use groupby() function and find worst 10 RMs in terms of average Spring Wheat through 10 years.

## Your code here - down ##
print("4. Use groupby() function and find worst 10 RMs in terms of average Spring Wheat through 10 years.")
dfw = df.groupby("RM")['SpringWheat'].mean()
print(dfw.sort_values().head(10))
#print(dfw.sort_values("SpringWheat", ascending=[True]).head(10))
## Your code here - up ##

# 5. Use groupby() function and find worst 3 best years in terms of average Spring Wheat.

## Your code here - down ##
print("5. Use groupby() function and find worst 3 best years in terms of average Spring Wheat.")
dfy = df.groupby("Year")['SpringWheat'].mean()
print(dfy.sort_values(ascending=[True]).head(3))

## Your code here - up ##

# 6. Use groupby() function and find worst 3 years in terms of average Spring Wheat through 10 years.

## Your code here - down ##
print("6. Use groupby() function and find worst 3 years in terms of average Spring Wheat through 10 years.")
avg_production_year = df.groupby('Year')['SpringWheat'].mean()
print(avg_production_year.sort_values().head(3))

## Your code here - up ##


## Question 3 (10 points)
# This task is independent exploratory data analysis. Find key insights from the dataset and share your code by creating new cells.

# Lowest year in Canola vs. Top year in Spring Wheat
dfsw = df.groupby("Year")['SpringWheat'].mean()
print("Top year in Spring Wheat:")
print(dfsw.sort_values().head(1))

dfc = df.groupby("Year")['Canola'].mean()
print("Top year in Canola:")
print(dfc.sort_values().head(1))