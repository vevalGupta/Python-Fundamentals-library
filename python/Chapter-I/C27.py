import os;os.system('cls')
"""
Hospital Patient Data Analysis
"""
import numpy as np

patients = np.array([
    [101, 45, 120, 200],  # [PatientID, Age, BP, Cholesterol]
    [102, 60, 150, 250],
    [103, 35, 110, 180],
    [104, 70, 160, 300],
    [105, 55, 140, 220]
], dtype=np.float64)

# Columns for readability
PID, AGE, BP, CHOL = 0, 1, 2, 3

# 1) Patients above age 50 (boolean indexing)
above_50_mask = patients[:, AGE] > 50
patients_above_50 = patients[above_50_mask]

# 2) Average BP and cholesterol
avg_bp = patients[:, BP].mean()
avg_chol = patients[:, CHOL].mean()

# 3) Transpose the data (attributes as rows)
patients_T = patients.T  # shape: (4, 5)

# 4) Normalize cholesterol by dividing each value by max cholesterol
chol = patients[:, CHOL]
max_chol = chol.max()
chol_normalized = chol / max_chol  # values in [0, 1]
# If you wish to use linalg for unit-vector normalization instead:
# chol_normalized_l2 = chol / np.linalg.norm(chol)

# 5) Generate 5 random patient ages between 20 and 80
rng = np.random.default_rng(seed=42)  # seed for reproducibility
random_ages = rng.integers(20, 81, size=5)

# ---- OUTPUT ----
np.set_printoptions(precision=2, suppress=True)
print("Patients > 50 years:\n", patients_above_50.astype(int))
print("\nAverage BP:", round(avg_bp, 2))
print("Average Cholesterol:", round(avg_chol, 2))
print("\nTransposed (rows=attributes, cols=patients):\n", patients_T.astype(int))
print("\nCholesterol normalized by max:\n", np.round(chol_normalized, 3))
print("\nRandom ages (20–80):\n", random_ages)

