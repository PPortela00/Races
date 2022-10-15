import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np

pd.set_option('display.max_columns', None)  # para poder visualizar todas as colunas no display
pd.set_option('display.width', 1000)  # para a largura do display ser de dimensao 1000

df = pd.read_csv("all_races.csv", on_bad_lines='skip', delimiter=';')
df.columns = df.columns.str.replace(' ', '_')  # torna mais facil a utilizaçao das colunas


def menu():
    print("[1] Print a todos os vinhos existentes")
    print("[2] Preparaçao dos dados para o dataset ")
    print("[3] Verificar quantos valores nulos existem ")
    print("[4] Criar estatísticas descritivas (apenas para colunas numéricas)")
    print("[5] Histograma que apresenta todos os componentes do vinho branco e tinto ")
    print("[6] Distribuiçao do vinho Tinto e do Vinho Branco tendo em conta a qualidade ")
    print("[7] Correlaçao existente entre a qualidade e os diversos atributos")
    print("[8] HeatMap (exibe as correlaçoes entre a qualidade e os diversos atributos)")
    print("[9] HeatMap (exibe a diferença de correlação entre o vinho tinto e o vinho branco) ")
    print("[10] Covariância existente entre a qualidade e os diversos atributos")
    print("[11] Stripplots do vinho tinto (carateristicas para as quais apresentou maior correlaçao)")
    print("[12] Stripplots do vinho branco (carateristicas para as quais apresentou maior correlaçao) ")
    print("[13] Regplots que expressam correlações interessantes entre diversos componentes do vinho tinto ")
    print("[14] Regplots que expressam correlações interessantes entre diversos componentes do vinho branco")
    print("[15] Scatterplots")
    print("[16] Normalizaçao ")
    print("[17] Standardizaçao")
    print("[18]  ")

    print("[0] Sair do programa.")

menu()
option = int(input("Introduza o comando que pretende efetuar:\n"))

while option != 0:
    if option == 1:
        df.head()
        print(df)
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
    else:
        print("Opçao Inválida.")

    print("\n")
    menu()
    option = int(input("Introduza o comando que pretende efetuar:"))

print("Obrigado por usar este programa . Ate já ")