from dbConnection import client
import pandas as pd

data = client.Analytics.jobs.find({})

df = pd.DataFrame(data)

print(df['dateOfScraping'].value_counts())

march = df[df['dateOfScraping'].isin(['03/22/24'])]
april = df[df['dateOfScraping'].isin(['04/12/24', '04/17/24'])]
may = df[df['dateOfScraping'].isin(['05/17/24', '05/08/24'])]

sample_size = 1600

march = march.sample(sample_size)
april = april.sample(sample_size)
may = may.sample(sample_size)



