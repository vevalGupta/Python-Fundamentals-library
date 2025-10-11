"""
Hospital Patient Data Analysis
A hospital maintains patient records in NumPy arrays
"""
import os;os.system('cls')
import numpy as np
records = np.array([
    [101, 45, 120, 200],
    [102, 60, 150, 250],
    [103, 35, 110, 180],
    [104, 70, 160, 300],
    [105, 55, 140, 220]
])

# Q-1) Extract all patients above age 50 using boolean indexing
above_50 = records[records[:, 1] > 50]
print(f"Patients above age 50:\n{above_50}")

# Q-2) Find the average blood pressure and cholesterol level using NumPy functions
avg_bloodp = np.mean(records[:, 2])
avg_chol = np.mean(records[:, 3])
print(f"Average Blood Pressure: {avg_bloodp}")
print(f"Average Cholesterol Level: {avg_chol}")

# Q-3) Transpose the data to view attributes as rows instead of columns
transposed_data = records.T
print(f"Transposed Data:\n{transposed_data}")

# Q-4) Normalize cholesterol values (divide each cholesterol by the maximum value)
cholesterol = records[:, 3]
max_cholesterol = cholesterol.max()
normalized_cholesterol = cholesterol / max_cholesterol
print(f"Normalized Cholesterol Values: {normalized_cholesterol}")

# Q-5) Generate 5 random patient ages between 20–80 using NumPy’s random module
random_ages = np.random.randint(20, 81, size=5)
print(f"Random Patient Ages (20–80): {random_ages}")