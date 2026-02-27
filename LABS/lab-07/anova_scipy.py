# Import required library
from scipy import stats

# Given data
A = [23, 20, 22, 21]
B = [30, 28, 27, 29]
C = [35, 33, 34, 36]

# Perform One-Way ANOVA
f_stat, p_value = stats.f_oneway(A, B, C)

# Print results
print("F-statistic:", f_stat)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("There is a significant difference between groups")
else:
    print("Fail to Reject Null Hypothesis")
    print("No significant difference between groups")