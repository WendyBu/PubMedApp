import pandas as pd
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
pd.options.display.max_columns = 30

engine = create_engine('sqlite:///test.db', echo=False)

df1 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user1data.csv", sep="\t")
df2 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user2data.csv", sep="\t")
df3 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user3data.csv", sep="\t")
df4 = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/user4data.csv", sep="\t")

df = df1.append([df2, df3, df4], ignore_index=True)
print(df.shape)
print(df)

df.to_sql('paper', con=engine, index=True, if_exists='replace')

user = pd.read_csv("/Users/yiwenbu/GTClass/prototype/PubMedApp/temp/usrinfo.csv", sep="\t", header=0)
print(user)
print(user.columns)
print(user.shape)

user.to_sql('user', con=engine, index=True, if_exists='replace')



