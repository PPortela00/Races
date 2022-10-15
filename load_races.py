import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import psycopg2

pd.set_option('display.max_columns', None)  # para poder visualizar todas as colunas no display
pd.set_option('display.width', 1000)  # para a largura do display ser de dimensao 1000

df = pd.read_csv("all_races.csv", on_bad_lines='skip', delimiter=',')
df.columns = df.columns.str.replace(' ', '_')  # torna mais facil a utilizaçao das colunas

con = psycopg2.connect(
  database="fced_paulo_portela",             # your database is the same as your username
  user="fced_paulo_portela",                 # your username
  password="!Pnp2186tenis",             # your password
  host="dbm.fe.up.pt",
  port = 5433,            # the database host
  options='-c search_path=Ex_Employees'  # use the schema you want to connect to
)

"""con = psycopg2.connect(
  database="username",             # your database is the same as your username
  user="username",                 # your username
  password="password",             # your password
  host="dbm.fe.up.pt",             # the database host
  options='-c search_path=schema'  # use the schema you want to connect to
)

con = psycopg2.connect(
  database="username",             # your database is the same as your username
  user="username",                 # your username
  password="password",             # your password
  host="dbm.fe.up.pt",             # the database host
  options='-c search_path=schema'  # use the schema you want to connect to
)
"""