# importing the module
import pandas as pd
from dbConnection import kursachJobs, client

data = kursachJobs.find({})

df = pd.DataFrame(data)

file_name = 'jobs.xlsx'

counts = df['fieldOfExp'].value_counts()

print(counts)

try:
    df.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')
except Exception as e:
    print("Couldn't make an Excel file BRUHHHHHHHHHHHH", e)


client.close()