# Importing the libraries
import pandas as pd
from apyori import apriori
# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
#appending the list of transactions from the dataset
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
# Training Apriori algorithm on the dataset
rule_list = apriori(transactions, min_support = 0.003, min_confidence = 0.3, min_lift = 3, min_length = 2)
#Generating the list of rules
results = list(rule_list)
#Printing the list of rules
for i in results:
    pair=i[0]
    items=[x for x in pair]
    print(str(items[0])+"->"+str(items[1]))
    print("Support:"+str(i[1]))
    print("Confidence:"+ str(i[2][0][2]))
    print("Lift:"+ str(i[2][0][3]))
    print()
'''The number of generated rules depends on the values of hyperparameters.
We can increase the minimum confidence value and find the rules accordingly.'''

