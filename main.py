import pandas

dataFrame = pandas.read_csv("data.csv", delimiter=";", header=None, names=["name", "age", "city"])

for row in dataFrame.itertuples(index=False):
    print(f'Cliente: {row.name} - Idade: {row.age} - Cidade: {row.city}')