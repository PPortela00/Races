import pandas as pd
import psycopg2
import xlrd
import openpyxl
from sqlalchemy import create_engine

con = psycopg2.connect(
      database="fced_carlos_veloso",  # your database is the same as your username
      user="fced_carlos_veloso",  # your username
      password="tartaruga",  # your password
      host="dbm.fe.up.pt",  # the database host
      port=5433,  # the database host
      options='-c search_path=public'  # use the schema you want to connect to
      )
    #print(con)


#cur = con.cursor()
races = pd.read_excel('races.xlsx')
#df.to_sql(name='nation', con=con)

#NATION
nation = races[['nation']]
nation_dic = dict()
lst_nation = list()
n = 1

for index, row in nation.iterrows():
      if row['nation'] not in nation_dic.values():
            nation_dic[n] = row['nation']
            key = n
            t = f"INSERT INTO nation VALUES ({key}, '{nation_dic[key]}');"
            lst_nation.append(t)
            n += 1

for i in range(len(lst_nation)):
      cur = con.cursor()
      cur.execute(lst_nation[i])

#AGE CLASS
age_class = races[['age_class']]
ageclass_dic = dict()
lst_age_class = list()
n = 1

for index, row in age_class.iterrows():
      if row['age_class'] not in ageclass_dic.values():
            ageclass_dic[n] = row['age_class']
            key = n
            t = f"INSERT INTO age_class VALUES ({key}, '{ageclass_dic[key]}');"
            lst_age_class.append(t)
            n += 1

for i in range(len(lst_age_class)):
      cur = con.cursor()
      cur.execute(lst_age_class[i])

#DISTANCE
distance = races[['distance']]
distance_dic = dict()
lst_distance = list()
n = 1

for index, row in distance.iterrows():
      if row['distance'] not in distance_dic.values():
            distance_dic[n] = row['distance']
            key = n
            t = f"INSERT INTO distance VALUES ({key}, '{distance_dic[key]}');"
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
      t = [row['event'], row['event_year'],list(distance_dic.keys())[list(distance_dic.values()).index(row['distance'])]]
      if row['event'] not in event_dic.values():
            event_dic[n] = t
            key = n
            t = f"INSERT INTO event VALUES ({key}, '{event_dic[key][0]}', {int(event_dic[key][1])}, {int(event_dic[key][2])});"
            lst_event.append(t)
            n += 1

for i in range(len(lst_event)):
      cur = con.cursor()
      cur.execute(lst_event[i])

con.commit()
con.close()


#races = openpyxl.load_workbook("races.xlsx")
#col_names = ["nation"]


#nation = races[['nation']]
#for row in nation:
 #   cur.execute(
  #      "INSERT INTO users VALUES ({key}, '{nation_dic[key]}')",
   #     row
    #)


#conn.commit()
#con.close()

