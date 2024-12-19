import pandas as pd

school_dataset = pd.read_csv('data/schools.csv')
# school_dataset = pd.read_csv("schools.csv")

# Filter schools with 80% of average_math score (total score is 800, so 80% is 640) and sort it in descending order
best_math_schools = school_dataset[['school_name', 'average_math']].query('average_math > 640').sort_values('average_math', ascending=False)

school_dataset['total_SAT'] = school_dataset['average_math'] + school_dataset['average_reading'] + school_dataset['average_writing']
top_10_schools = school_dataset[['school_name', 'total_SAT']].nlargest(10, 'total_SAT')
print(top_10_schools)


largest_std_dev = school_dataset.groupby('borough').agg(
    num_schools=("school_name", "count"),
    average_SAT=("total_SAT", 'mean'),
    std_SAT=('total_SAT', 'std')
).round(2).nlargest(1, 'std_SAT')