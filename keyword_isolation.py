import csv
import pandas as pd


employment_needs = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/public_use-industry-skills-needs.xlsx"
employment_projections = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/Dataset 1 - Employment Projections by Industry.xlsx"
cte_demographics = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/Dataset 5 - 20-21 CTE Demographics .xlsx"

# Read the csv file
skills_needed = pd.read_excel(employment_needs, sheet_name='Industry Skills Needs')
# employment_projections = pd.read_excel(employment_projections, sheet_name='Sheet1')
cte_demographics = pd.read_excel(cte_demographics, sheet_name='EnrollmentReport', skiprows=1)


skills_list = skills_needed['skill_group_name'].to_list()
unique_skills = set(skills_list)

print(unique_skills)

cte_demographics = cte_demographics[cte_demographics['State'] == 'North Carolina']
print(cte_demographics)
# Get a list of column names
column_names = cte_demographics.columns.tolist()

tech_skills_df = skills_needed[skills_needed['skill_group_category'].str.contains('Tech Skills')]
unique_tech_skills = set(tech_skills_df["skill_group_name"])
unique_skills_not_tech = unique_skills - unique_tech_skills

for skill in unique_skills_not_tech:
    print(skill)

# print("names done")
# for name in column_names:
#     print(name)
# print(column_names)
