import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import psycopg2


def menu():
    print("[1] Print a todos os vinhos existentes")
    print("[2] Preparaçao dos dados para o dataset ")
    print("[3] Verificar quantos valores nulos existem ")
    print("[4] Criar estatísticas descritivas (apenas para colunas numéricas)")
    print("[5] Who run the fastest 10K race ever (name, birthdate, time)")
    print("[6] What 10K race had the fastest average time (event, event date)?")
    print("[7] What teams had more than 3 participants in the 2016 maratona (team)?")
    print("[8] What are the 5 runners with more kilometers in total (name, birthdate, kms)?")
    print("[9] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")
    print("[10] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")
    print("[100] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")

    print("[0] Sair do programa.")

menu()
option = int(input("Introduza o comando que pretende efetuar:\n"))

while option != 0:
    if option == 1:
        print('\n')
    elif option == 2:
        print('\n')
    elif option == 3:
        print('\n')
    elif option == 4:
        print('\n')
    elif option == 5:
        print('\n')
    elif option == 6:
        print('\n')
    elif option == 7:
        print('\n')
    elif option == 8:
        print('\n')
    elif option == 9:
        print('\n')
    elif option == 10:
        print('\n')
    elif option == 100:
        df.head()
        print(df)
        print('\n')
        print('Numero de elementos da matriz')
        print(df.size)
        print('\n')
        print('Dimensão da matriz')
        print(df.shape)
        print('\n')
        print("Tipo de variaveis e quantidade de dados em cada coluna")
        df.info()
    else:
        print("Opçao Inválida.")

    print("\n")
    menu()
    option = int(input("Introduza o comando que pretende efetuar:"))

print("Obrigado por usar este programa . Ate já ")