import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Load all csvs from csvs folder
data = os.listdir('csvs')
data = {csv.split('.')[0]: pd.read_csv(f'csvs/{csv}', delimiter=';') for csv in data}

# convert to dataframe
for key, rates in data.items():
    data[key] = pd.DataFrame(rates)

means = {}
# Calculate means
for key, rates in data.items():
    new_data = np.zeros((len(rates), len(rates.columns) // 3))
    for index, row in rates.iterrows():
        for i in range(0, len(row) // 3):
            mean = np.mean([row[i*3], row[i*3+1], row[i*3+2]])
            new_data[index][i] = mean
    means[key] = new_data


# change column names
for key, rates in means.items():
    columns = [f'Prompt-{i+1}' for i in range(len(rates[0]))]
    means[key] = pd.DataFrame(rates, columns=columns)

# export to csv
for key, rates in means.items():
    pd.DataFrame(rates).to_csv(f'means/{key}.csv', sep=';', index=False)


