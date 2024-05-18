from dbConnection import client
import pandas as pd

data = client.Analytics.jobs.find({})

df = pd.DataFrame(data)


mean_salary = df.groupby('fieldOfExp')['salary'].mean().reset_index().sort_values(by='salary', ascending=False)
print("\nMean salary\n",mean_salary)

median_salary = df.groupby('fieldOfExp')['salary'].median().reset_index().sort_values(by='salary', ascending=False)
print("\nMedian salary\n",median_salary)

mode_salary = df.groupby('fieldOfExp')['salary'].agg(lambda x: x.mode()[0]).reset_index().sort_values(by='salary', ascending=False)
print("\nMode salary\n", mode_salary)


file_name = 'bruh.xlsx'


try:
    mode_salary.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')
except Exception as e:
    print("Couldn't make an Excel file BRUHHHHHHHHHHHH", e)

# print(df['dateOfScraping'].value_counts())
#
# march = df[df['dateOfScraping'].isin(['03/22/24'])]
# april = df[df['dateOfScraping'].isin(['04/12/24', '04/17/24'])]
# may = df[df['dateOfScraping'].isin(['05/17/24', '05/08/24'])]
#
# sample_size = 1600
#
#
#
# march = march.sample(sample_size)
# april = april.sample(sample_size)
# may = may.sample(sample_size)
#
# #march
# value_counts = march['fieldOfExp'].value_counts()
#
# import matplotlib.pyplot as plt
# # Plot as a pie chart
# plt.figure(figsize=(8, 6))
# patches, _ = plt.pie(value_counts, labels=None, startangle=140)
#
# plt.subplots_adjust(
#     top=0.88,
#     bottom=0.11,
#     left=0.005,
#     right=0.615,
#     hspace=0.2,
#     wspace=0.2
# )
#
# # Add legend for each category with percentages
# plt.legend(handles=patches, labels=[f'{label} ({value_counts[label]}) - {value_counts[label]/len(march)*100:.1f}%' for label in value_counts.index], loc="center left", bbox_to_anchor=(1, 0.5))
#
# plt.title('Distribution of Categories in March')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
#
#
# #april
# value_counts = april['fieldOfExp'].value_counts()
# # Plot as a pie chart
# plt.figure(figsize=(8, 6))
#
# plt.subplots_adjust(
#     top=0.88,
#     bottom=0.11,
#     left=0.005,
#     right=0.615,
#     hspace=0.2,
#     wspace=0.2
# )
#
# patches, _ = plt.pie(value_counts, labels=None, startangle=140)
#
# # Add legend for each category with percentages
# plt.legend(handles=patches, labels=[f'{label} ({value_counts[label]}) - {value_counts[label]/len(april)*100:.1f}%' for label in value_counts.index], loc="center left", bbox_to_anchor=(1, 0.5))
#
# plt.title('Distribution of Categories in April')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
#
#
# value_counts = may['fieldOfExp'].value_counts()
# # Plot as a pie chart
# plt.figure(figsize=(8, 6))
# patches, _ = plt.pie(value_counts, labels=None, startangle=140)
#
# plt.subplots_adjust(
#     top=0.88,
#     bottom=0.11,
#     left=0.005,
#     right=0.615,
#     hspace=0.2,
#     wspace=0.2
# )
#
# # Add legend for each category with percentages
# plt.legend(handles=patches, labels=[f'{label} ({value_counts[label]}) - {value_counts[label]/len(may)*100:.1f}%' for label in value_counts.index], loc="center left", bbox_to_anchor=(1, 0.5))
#
# plt.title('Distribution of Categories in May')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()