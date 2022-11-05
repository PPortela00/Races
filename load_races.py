import pandas as pd
import psycopg2
from datetime import datetime

pd.set_option('display.max_columns', None)  # para poder visualizar todas as colunas no display
pd.set_option('display.width', 1000)  # para a largura do display ser de dimensao 1000

races = pd.read_excel('races.xlsx')
races.columns = races.columns.str.replace(' ', '_')  # torna mais facil a utilizaçao das colunas
races = races[races['age_class'].notna()]       #remove the NA values for the column Age_Class
races = races.drop(labels=[19, 20, 21, 22])     #remove lines which name are ".." and "57655662"


def menu():
  print("[1] Create connection to the PostgreSQL for Paulo")
  print("[2] Create connection to the PostgreSQL for Miguel")
  print("[3] Create connection to the PostgreSQL for Luis")
  print("[4] Head, Size and Shape of Dataset")
  print("[5] Remove all data from the database")
  print("[6] Add all data to the database")
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
      options='-c search_path=public'  # use the schema you want to connect to
    )
    print(con)
  elif option == 2:
    con = psycopg2.connect(
      database="fced_carlos_veloso",  # your database is the same as your username
      user="fced_carlos_veloso",  # your username
      password="tartaruga",  # your password
      host="dbm.fe.up.pt",  # the database host
      port=5433,  # the database host
      options='-c search_path=public'  # use the schema you want to connect to
    )
    print(con)
  elif option == 3:
    con = psycopg2.connect(
      database="fced_luis_henriques",  # your database is the same as your username
      user="fced_luis_henriques",  # your username
      password="henriques_luis_fced",  # your password
      host="dbm.fe.up.pt",  # the database host
      port=5433,  # the database host
      options='-c search_path=schema'  # use the schema you want to connect to
    )
    print(con)
  elif option == 4:
    print('\n')
    print(races.head(5))
    print('\n')
    print('Numero de elementos da matriz')
    print(races.size)
    print('\n')
    print('Dimensão da matriz')
    print(races.shape)
    print('\n')
    print(races.isnull().sum())
    print('\n')
  elif option == 5:
    cur = con.cursor()
    cur.execute('DELETE FROM sex')
    cur.execute('DELETE FROM nation')
    cur.execute('DELETE FROM runner')
    cur.execute('DELETE FROM age_class')
    cur.execute('DELETE FROM distance')
    cur.execute('DELETE FROM event')
    cur.execute('DELETE FROM classification')
    con.commit()
    print('All data was deleted with success')
  elif option == 6:

    # SEX
    sex = races[['sex']]
    sex_dic = dict()
    lst_sex = list()
    n = 1

    for index, row in sex.iterrows():
      if row['sex'] not in sex_dic.values():
        sex_dic[n] = row['sex']
        t = f"INSERT INTO sex VALUES ({n}, '{sex_dic[n]}');"
        lst_sex.append(t)
        n += 1

    for i in range(len(lst_sex)):
      cur = con.cursor()
      cur.execute(lst_sex[i])

    # NATION
    nation = races[['nation']]
    nation_dic = dict()
    lst_nation = list()
    n = 1

    for index, row in nation.iterrows():
      if row['nation'] not in nation_dic.values():
        nation_dic[n] = row['nation']
        t = f"INSERT INTO nation VALUES ({n}, '{nation_dic[n]}');"
        lst_nation.append(t)
        n += 1

    for i in range(len(lst_nation)):
      cur = con.cursor()
      cur.execute(lst_nation[i])

    # AGE CLASS
    age_class = races[['age_class']]
    ageclass_dic = dict()
    lst_age_class = list()
    n = 1

    for index, row in age_class.iterrows():
      if row['age_class'] not in ageclass_dic.values():
        ageclass_dic[n] = row['age_class']
        t = f"INSERT INTO age_class VALUES ({n}, '{ageclass_dic[n]}');"
        lst_age_class.append(t)
        n += 1

    for i in range(len(lst_age_class)):
      cur = con.cursor()
      cur.execute(lst_age_class[i])

    # DISTANCE
    distance = races[['distance']]
    distance_dic = dict()
    lst_distance = list()
    n = 1

    for index, row in distance.iterrows():
      if row['distance'] not in distance_dic.values():
        distance_dic[n] = row['distance']
        t = f"INSERT INTO distance VALUES ({n}, '{distance_dic[n]}');"
        lst_distance.append(t)
        n += 1

    for i in range(len(lst_distance)):
      cur = con.cursor()
      cur.execute(lst_distance[i])


    #EVENT
    event = races[['event', 'event_year', 'distance']]
    event_dic = dict()
    lst_event = list()
    n = 1

    for index, row in event.iterrows():
      u = [row['event'], row['event_year'],list(distance_dic.keys())[list(distance_dic.values()).index(row['distance'])]]
      if u not in event_dic.values():
        event_dic[n] = u
        t = f"INSERT INTO event VALUES ({n}, '{event_dic[n][0]}', {int(event_dic[n][1])}, {int(event_dic[n][2])});"
        lst_event.append(t)
        n += 1

    for i in range(len(lst_event)):
      cur = con.cursor()
      cur.execute(lst_event[i])

    #RUNNER
    runner = races[['name', 'birth_date', 'sex', 'nation']]
    runner_dic = dict()
    lst_runner = list()
    n = 1

    for index, row in runner.iterrows():
      t = [row['name'].replace("'", " "), row['birth_date'],list(sex_dic.keys())[list(sex_dic.values()).index(row['sex'])],list(nation_dic.keys())[list(nation_dic.values()).index(row['nation'])]]
      if t not in runner_dic.values():
        runner_dic[n] = t
        t = f"INSERT INTO runner VALUES ({n}, '{runner_dic[n][0]}', '{datetime.strptime(str(runner_dic[n][1]), '%d/%m/%Y').strftime('%Y-%m-%d')}', {runner_dic[n][2]}, {runner_dic[n][3]});"
        lst_runner.append(t)
        n += 1

    for i in range(len(lst_runner)):
      cur = con.cursor()
      cur.execute(lst_runner[i])

    # CLASSIFICATION
    classification = races[
      ['name', 'birth_date', 'sex', 'nation', 'event', 'event_year', 'distance', 'bib', 'place', 'place_in_class',
       'official_time', 'net_time', 'age_class',
       'team']]

    lst_classification = list()
    for index, row in classification.iterrows():
      run = [row['name'].replace("'", " "), row['birth_date'],list(sex_dic.keys())[list(sex_dic.values()).index(row['sex'])],list(nation_dic.keys())[list(nation_dic.values()).index(row['nation'])]]
      eve = [row['event'], row['event_year'], list(distance_dic.keys())[list(distance_dic.values()).index(row['distance'])]]
      t = [list(runner_dic.keys())[list(runner_dic.values()).index(run)],
           list(event_dic.keys())[list(event_dic.values()).index(eve)],
           row['bib'], row['place'], row['place_in_class'], row['official_time'], row['net_time'],
           list(ageclass_dic.keys())[list(ageclass_dic.values()).index(row['age_class'])],
           row['team']]
      lst_classification.append(t)

    for n in range(len(lst_classification)):
      cur = con.cursor()
      cur.execute(f"INSERT INTO classification VALUES ({lst_classification[n][0]}, {lst_classification[n][1]}, {lst_classification[n][2]}, {lst_classification[n][3]}, {lst_classification[n][4]}, '{str(pd.to_timedelta(lst_classification[n][5]))[7:]}', '{str(pd.to_timedelta(lst_classification[n][6]))[7:]}', {lst_classification[n][7]}, '{lst_classification[n][8]}');")

    con.commit()
    con.close()

    print('All data was inserted with success')
  else:
    print("Invalid Option")

  print("\n")
  menu()
  option = int(input("Insert the command that you want to execute:"))




