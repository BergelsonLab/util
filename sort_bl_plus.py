import pandas as pd
import csv

all_bl = pd.read_csv("/Users/andrei/BLAB_DATA/all_basiclevel/all_basiclevel.csv", dtype={'month': str, 'subj': str})

# all_bl["edited"] = ""

problems = pd.DataFrame(columns=all_bl.columns.values)

drop_rows = []
for i, row in all_bl.iterrows():
    if "+" in row['basic_level'] and row['basic_level'][0].isupper() and row['month'] == "06":
        problems = problems.append(row)
        drop_rows.append(i)

all_bl = all_bl.drop(drop_rows)

# problems.to_csv("problems.csv", index=False)
final = problems.append(all_bl)
final.to_csv("all_bl_propername_sorted.csv", index=False, quoting=csv.QUOTE_ALL)