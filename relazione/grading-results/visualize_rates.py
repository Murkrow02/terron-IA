import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

# read all csvs from means folder
data = os.listdir('means')
data = {csv.split('.')[0]: pd.read_csv(f'means/{csv}', delimiter=';') for csv in data}

# convert to dataframe
for key, rates in data.items():
    data[key] = pd.DataFrame(rates)

means = {}
for key, rates in data.items():
    new_data = np.zeros((len(rates.columns)))
    for i in range(len(rates.columns)):
        mean = np.mean(rates[rates.columns[i]])
        new_data[i] = mean
    means[key] = new_data

# order means by key (separate the key by '-' and order by the second element)
means = dict(sorted(means.items(), key=lambda x: int(x[0].split('-')[1])))



# Function to plot histograms
def plot_histograms(data, title):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(data)), data, tick_label=[f"Prompt-{i+1}" for i in range(len(data))])
    plt.title("Grades for " + title)
    plt.ylabel('Grade Average')
    plt.xticks(rotation=45)
    plt.show()


def plot_grouped_histograms(means, models):
    """
    Plot a grouped bar chart where each prompt has bars for all models.

    Args:
        means (dict): Dictionary where keys are model names and values are lists of means per prompt.
        models (list): List of model names to use as legend.
    """
    prompts_count = len(next(iter(means.values())))  # Number of prompts (columns)
    models_count = len(models)  # Number of models
    bar_width = 0.8 / models_count  # Width of each bar
    x = np.arange(prompts_count)  # Indices for prompts

    plt.figure(figsize=(12, 6))

    # Plot each model's data with an offset for grouped bars
    for i, model in enumerate(models):
        offsets = x + i * bar_width
        plt.bar(
            offsets,
            means[model],
            bar_width,
            label=model,
            alpha=0.8
        )

    # Add labels and formatting
    plt.title("Performance Comparison Across Models")
    plt.ylabel("Grade Average")
    plt.xlabel("Prompts")
    plt.xticks(x + bar_width * (models_count - 1) / 2, [f"Prompt-{i+1}" for i in range(prompts_count)], rotation=45)
    plt.legend(title="Models")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

plot_grouped_histograms(means, list(means.keys()))

for key, rates in means.items():
    plot_histograms(rates, key)


final_means = {}
for key, rates in means.items():
    final_means[key] = np.mean(rates)

plt.figure(figsize=(10, 6))
plt.plot(list(final_means.keys()), list(final_means.values()), marker='o')
plt.title("Performance Comparison Across Models")
plt.ylabel("Grade Average")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
