import pandas as pd
import psycopg2

pd.set_option('display.max_columns', None)  # para poder visualizar todas as colunas no display
pd.set_option('display.width', 1000)  # para a largura do display ser de dimensao 1000

df = pd.read_excel('races.xlsx')
df.columns = df.columns.str.replace(' ', '_')  # torna mais facil a utilizaçao das colunas

def menu():
  print("[1] Create connection to the PostgreSQL for Paulo")
  print("[2] Create connection to the PostgreSQL for Miguel")
  print("[3] Create connection to the PostgreSQL for Luis")
  print("[4] Head, Size and Shape of Dataset")

  print("[0] Let´s work with PostgreSQL and Python.")


menu()
option = int(input("Insert the command that you want to execute:\n"))

while option != 0:
  if option == 1:
    con = psycopg2.connect(
      database="fced_paulo_portela",  # your database is the same as your username
      user="fced_paulo_portela",  # your username
      password="!Pnp2186tenis",  # your password
      host="dbm.fe.up.pt",
      port=5433,  # the database host
      options='-c search_path=ex_employees'  # use the schema you want to connect to
    )
    print(con)
  elif option == 2:
    con = psycopg2.connect(
      database="username",  # your database is the same as your username
      user="username",  # your username
      password="password",  # your password
      host="dbm.fe.up.pt",  # the database host
      options='-c search_path=schema'  # use the schema you want to connect to
    )
    print(con)
  elif option == 3:
    con = psycopg2.connect(
      database="username",  # your database is the same as your username
      user="username",  # your username
      password="password",  # your password
      host="dbm.fe.up.pt",  # the database host
      options='-c search_path=schema'  # use the schema you want to connect to
    )
    print(con)
  elif option == 4:
    print(df.head)
    print('\n')
    print('Numero de elementos da matriz')
    print(df.size)
    print('\n')
    print('Dimensão da matriz')
    print(df.shape)
    print('\n')
  else:
    print("Invalid Option")

  print("\n")
  menu()
  option = int(input("Insert the command that you want to execute:"))





