import pandas as pd #type: ignore
import statsmodels.api as sm #type: ignore
from statsmodels.formula.api import ols #type: ignore

data = {
    "Diet": ["A","A","A","B","B","B","C","C","C"],
    "Weight_Loss": [5,6,4,8,7,9,3,2,4]
}

df = pd.DataFrame(data)

model = ols("Weight_Loss ~ C(Diet)", data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

# Correct way to get p-value
p_value = anova_table.loc["C(Diet)", "PR(>F)"]

print("\nP-value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Diet has significant effect on weight loss")
else:
    print("Fail to Reject Null Hypothesis")
    print("Diet has no significant effect")