# importing the module
import pandas as pd
from dbConnection import kursachJobs, client

data = kursachJobs.find({})

df = pd.DataFrame(data)

file_name = 'jobs.xlsx'





try:
    df.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')
except Exception as e:
    print("Couldn't make an Excel file BRUHHHHHHHHHHHH", e)



value_counts = df['fieldOfExp'].value_counts()
import matplotlib.pyplot as plt
# Plot as a pie chart
plt.figure(figsize=(8, 6))
patches, _ = plt.pie(value_counts, labels=None, startangle=140)

# Add legend for each category with percentages
plt.legend(handles=patches, labels=[f'{label} ({value_counts[label]}) - {value_counts[label]/len(df)*100:.1f}%' for label in value_counts.index], loc="center left", bbox_to_anchor=(1, 0.5))

plt.title('Distribution of Categories')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

client.close()