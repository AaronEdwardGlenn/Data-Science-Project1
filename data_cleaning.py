# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:03:43 2020

@author: aaron
"""

import pandas as pd

df = pd.read_csv('glassdoor.csv')

filt = (df['Salary Estimate'] != '-1')
df = df[filt]

salary = df['Salary Estimate'].apply(lambda x: x.split(' ')[0])

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])


minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

df['min_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis =1)
filt = df['Location'].str.contains('Remote')
df.loc[filt, 'Location'] = 'Remote, Remote'
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])


df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Location == x.Headquarters else 0, axis=1)

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

filt = df['age'] == -1

df['age'].loc[filt] = 0                                 

df['python_yn'] = df['Job Description'].apply(lambda x: True if 'python' in x.lower() else False)

df['aws_yn'] = df['Job Description'].apply(lambda x: True if 'aws' in x.lower() else False)
df['excel_yn'] = df['Job Description'].apply(lambda x: True if 'excel' in x.lower() else False)
df['R_yn'] = df['Job Description'].apply(lambda x: True if 'R' in x.lower() else False)

df_out = df.drop(['Unnamed: 0'], axis=1)

df_out.to_csv('cleaned_data.csv')