import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import numpy as np

# Load the data
data = pd.read_csv('train (1).csv')

# Separate features and labels
X = data['Review'].values.reshape(-1, 1)  # reshape X to 2D array with a single column
y = data['Rating']

# Print class distribution before balancing
print('Class distribution before balancing:')
print(y.value_counts())

# Undersample the majority class
rus = RandomUnderSampler(random_state=0)
X_resampled, y_resampled = rus.fit_resample(X, y)

# Oversample the minority class
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X_resampled, y_resampled)

# Print class distribution after balancing
print('Class distribution after balancing:')
print(y_resampled.value_counts())

# Create a new DataFrame with the resampled data
resampled_data = pd.DataFrame({'Review': X_resampled.ravel(), 'Rating': y_resampled})

# Save the resampled data to a new CSV file
resampled_data.to_csv('balanced_train.csv', index=False)
