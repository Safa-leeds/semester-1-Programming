import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(data)
print(type(data))
# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
total_students = len(data)
# Find the mean average GPA of the students
mean_gpa = data['GPA'].mean()

# Find the standard deviation of how much sleep students get per day
standard_deviation_sleep = data['Sleep_Hours_Per_Day'].std()
# Find the maximum amount of study hours per day
max_study_hours = data['Study_Hours_Per_Day'].max()

# Sort the students by social hours per day ascending (lowest -> highest)
lowest_to_highest = data.sort_values(by='Social_Hours_Per_Day')
# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
Total_hours = data['Sleep_Hours_Per_Day'] + data['Study_Hours_Per_Day'] + data['Social_Hours_Per_Day']
# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
filtered_high_stress = data[data['Stress_Level'] == 'high']
filtered_low_stress = data[data['Stress_Level'] == 'low']
# Can you work out whether having a higher stress level leads to a higher GPA?
work_out_stress_gpa = data.groupby('Stress_Level')['GPA'].mean()