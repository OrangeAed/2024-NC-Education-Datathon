import pandas as pd
import numpy as np


path = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/NC Schools/Free & Reduced Lunch - SY 19-20 EDS - SN Data.xlsx"

frl_xlsx = pd.read_excel(path, sheet_name='LEA', skiprows=4)
frl_df = pd.DataFrame(frl_xlsx)

# select rows where

# what type in NaN?
x = frl_df["SFA Name"].isnull()
print(x)
# totals = frl_df[]


rownames = set(frl_df["SFA Name"])#.remove(np.nan)

# rownames = strings in rownames

new_rownames = []

for name in rownames:
    if type(name) != float and name != "Residential Schools":
        new_rownames.append(name)

new_rownames.sort()

# for county, num in zip(new_rownames,totals["ADM"]):
#     print(county)

# with open("./county_pop_totals", "w") as f:
#     list_of_totals = totals["ADM"].tolist()
#     for total in list_of_totals:
#         f.write(str(total) + "\n")
#     f.close()
# print(totals["ADM"])

# print(frl_df.iloc[47])

# print(totals)

sans_city = zip(new_rownames, totals["ADM"])
last_real_county = ""
new_totals = {}

for county, num in sans_city:
    if "City" in county:
        # print(county, num)
        new_totals[last_real_county] += num
    elif "Residential" in county:
        continue
    else:
        new_totals[county] = num
        last_real_county = county

new_totals["Wilson County Schools"] += 52
new_totals["Wake County Schools"] += 51
new_totals["Burke County Schools"] += 80
new_totals["Orange County Schools"] += 4193
new_totals["Charlotte-Mecklenburg Schools"] += 3029
new_totals.pop("Chapel Hill-Carrboro Schools")
# new_totals.pop("Charlotte-Mecklenburg Schools")

new_totals["Iredell-Statesville Schools"] += new_totals["Mooresville Graded School District"]
new_totals.pop("Mooresville Graded School District")
new_totals["Chowan County Schools"] = 0
# print(new_totals
# s = sorted(new_totals)
s = [*new_totals.keys()]
s.sort()
with open("county_pop_totals", "w") as f:
    for n in s:
        f.write(n + "\t" + str(new_totals[n]) + "\n")

