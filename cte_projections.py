import pandas
import json

class CTE_Projections:
    def __init__(self):
        self.projection_df, self.pathways_data = self.get_data()
        self.cte_jobs = None
    def get_data(self):
        projection_data = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/Dataset 1 - Employment Projections by Industry.xlsx"
        pathways_data = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/cte_pathways_skills.json"

        projection_df = pandas.read_excel(projection_data, "Sheet1")
        with open(pathways_data) as pathways_file:
            pathways = json.load(pathways_file)
            print(pathways)
        return projection_df, pathways



    def total_jobs(self, is_current: bool):
        self.cte_jobs = {}
        for cte_pathway in self.pathways_data:
            self.cte_jobs[cte_pathway] = self.projection_df[self.projection_df["Industry Title"] in self.pathways_data[cte_pathway]["jobs"]]["2021"]

        return self.cte_jobs





if __name__ == "__main__":
    c = CTE_Projections()
    print(c.total_jobs(True))
