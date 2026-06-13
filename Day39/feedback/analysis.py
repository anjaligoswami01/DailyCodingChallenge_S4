import pandas as pd

df = pd.read_csv("feedback/day38_feedback.csv")

df = df.sort_values(
    by="frequency",
    ascending=False
)

print(df)