import pandas
from sklearn import linear_model

df = pandas.read_csv("/Users/johnboyce/vs_code_projects/budget_manager/data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

weight = int(input("What is the weight of the vehicle in KGs?\n"))
volume = int(input("What is the volume of the engine?\n"))

predictedCO2 = regr.predict([[weight, volume]])

print(predictedCO2)