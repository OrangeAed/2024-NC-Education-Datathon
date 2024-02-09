import pandas as pd
import matplotlib.pyplot as plt

def cte_variety_by_t1(df):
    # plot the most frequent 'career_cluster' by 'Title I Served School' status
    df = df.groupby('career_cluster')

def agg_title1(df):
    # plot the number of title 1 schools by career cluster
    df['cte_count'] = df.groupby('agency_code')['agency_code'].transform('count')
    df.to_csv('cte_count.csv')
    # plot 'cte_count' by 'Title I Served School' status
    df = df.groupby('Title I Served School').agg({'cte_count': 'sum'}).reset_index()
    plt.bar(df['Title I Served School'], df['cte_count'])
    plt.xticks(rotation=90)
    plt.xlabel('Title I Served School')
    plt.ylabel('Number of CTE Concentrators')
    plt.title('Number of CTE Concentrators by Title I Served School in 2021')
    plt.show()
    # cte_variety_by_t1(df)
    # df = df.groupby()


def agg_conc(df):
    # plot the number of concentrators by career cluster
    df = df.groupby('career_cluster').agg({'num_concentrators': 'sum'}).reset_index()
    df = df.sort_values('num_concentrators', ascending=False)
    plt.bar(df['career_cluster'], df['num_concentrators'])
    plt.xticks(rotation=90)
    plt.xlabel('Career Cluster')
    plt.ylabel('Number of Concentrators')
    plt.title('Number of Concentrators by Career Cluster in 2021')
    plt.show()

def clean_year2021(df):
    df = df[df['year'] == 2021]
    df = df[['agency_code', 'career_cluster','num_concentrators', 'Title I Served School', 'District Name']]
    df['Title I Served School'] = df['Title I Served School'].apply(lambda x: 1 if x == 'Y' else 0)
    return df

def combine(d4, sd):
    '''Combine dataframes based on the school code. In sd, the column is "School\nCode" and in d4, the column is "agency_code".'''
    m = pd.merge(d4, sd, left_on='agency_code', right_on='School\nCode', how='inner')
    return m

def main():
    d4 = pd.read_excel('data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/Dataset 4 - 2017-2022 CTE concentrators.xlsx')
    school_data = pd.read_excel('data/The Datasets_2024 Datathon-20240208T152828Z-001/The Datasets_2024 Datathon/NC Schools/2021-22 NC School Data_2023Datathon.xlsx', sheet_name='School Performance Grades', header=2)
    school_data = school_data.iloc[2:]
    merged = combine(d4, school_data)
    df21 = clean_year2021(merged)
    merged.to_csv('merged.csv')
    df21.to_csv('cleaned.csv')
    df21.to_excel('t1_cte.xlsx')
    agg_title1(df21)
    agg_conc(df21)


if __name__ == '__main__':
    main()