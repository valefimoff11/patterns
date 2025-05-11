import pandas as pd

data = {
     'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
     'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
              'Manchester', 'Cairo', 'Osaka'],
     'age': [41, 28, 33, 34, 38, 31, 37],
     'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]


df = pd.DataFrame(data=data, index=row_labels)

print(df)

cities = df['city']
print(cities)
print(df.city)

print("uuuu")
print(df.iloc[3:5, [1, 2]])

print(df[3:5])