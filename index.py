import gd_scrapper as gs 
import pandas as pd 

path = "C:/Users/aaron/Documents/GitHub/chromedriver"

df = gs.get_jobs('data scientist',15, False, path, 15)

df.to_csv('glassdoor.csv')
