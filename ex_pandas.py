import pandas as pd
import numpy as np

df = pd.read_csv('../fake_job_postings.csv')

df_columns = df.columns

df2 = pd.DataFrame(data = {'job_id' : df['job_id'], 'salary_range' : df['salary_range'], 'required_education' : df['required_education']} , columns = ['job_id', 'salary_range', 'required_education'])

df3 = df2.fillna(0)

print(df3)