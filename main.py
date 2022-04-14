import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.types import Integer

engine = create_engine('sqlite:///成绩单', echo=False)

file = "成绩单表格.xlsx"
df = pd.read_excel(file, header=None)
df1 = df.iloc[:, :4]
df1.set_axis(["name", "score", "grades", "year"], axis=1, inplace=True)
df2 = df.iloc[:, 4:]
df2.set_axis(["name", "score", "grades", "year"], axis=1, inplace=True)
df = pd.concat([df1, df2])
df.dropna(inplace=True)
# print(df)
# a = df[df.isnull().T.any()]
# print(a)
# df = df.loc[:, ["score", "year"]]
# a = df.groupby(["year"]).sum()
# print(a)
# print(a.columns)

df.to_sql('users', con=engine, if_exists="replace", dtype={"score": Integer()})
print(engine.execute("SELECT * FROM users").fetchall())
# print(engine.execute("select * from sqlite_master").fetchall())
