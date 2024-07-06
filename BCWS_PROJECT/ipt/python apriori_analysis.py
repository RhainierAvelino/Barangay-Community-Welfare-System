import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the Excel file
file_path = 'datasets.csv.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the first few rows of the dataframe to understand its structure
print(data.head())

# Preprocess the data to the required format for Apriori algorithm
# Converting the data to one-hot encoded format
basket = pd.get_dummies(data, prefix='', prefix_sep='').groupby(level=0, axis=1).max()

# Apply Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.1, use_colnames=True)

# Generate the association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the rules
print(rules)
