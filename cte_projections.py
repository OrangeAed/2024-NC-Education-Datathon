import pandas
import json

class CTE_Projections:
    def __init__(self):
        self.projection_df, self.pathways_data = self.get_data()
        self.cte_jobs = None
        self.combine_projections_json_dump = None
    def get_data(self):
        projection_data = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/Dataset 1 - Employment Projections by Industry.xlsx"
        pathways_data = "data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/cte_pathways_skills.json"

        projection_df = pandas.read_excel(projection_data, "Sheet1")
        with open(pathways_data) as pathways_file:
            pathways = json.load(pathways_file)
            # print(pathways)
        return projection_df, pathways

    def total_jobs(self, is_current: bool):
        self.cte_jobs = {}
        for cte_pathway in self.pathways_data:
            jobs = self.pathways_data[cte_pathway]["jobs"]
            relevant_job_rows = self.projection_df[self.projection_df["Industry Title"].isin(jobs)]
            t = type(relevant_job_rows)
            job_totals = relevant_job_rows.iloc[:, (4 if is_current else 5)]
            # if

            job_totals_int = [(0 if t == '*' else t) for t in job_totals.tolist()]
            self.cte_jobs[cte_pathway] = sum(job_totals_int)

        return self.cte_jobs

    def combine_projections(self):
        cte_jobs_2021 = self.total_jobs(True)
        cte_jobs_2030 = self.total_jobs(False)
        df, pathway = self.get_data()

        print(len(pathway))

        for i, path in enumerate(pathway):
            pathway[path]["jobs_2021"] = cte_jobs_2021[path]
            pathway[path]["jobs_2030"] = cte_jobs_2030[path]

        # print(pathway)

        self.combine_projections_json_dump = json.dumps(pathway, indent=4)

        with open("projection.json", "w") as f:
            f.write(self.combine_projections_json_dump)



        # print(pathway)

if __name__ == "__main__":
    c = CTE_Projections()
    # print(c.total_jobs(True))
    c.combine_projections()
