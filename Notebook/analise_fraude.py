import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# =========================
# CARREGAMENTO DO DATASET
# =========================

df = pd.read_csv(
    r"C:\Users\erick\Documents\PROJETO V1\data\retail_fraud_detection_100k.csv"
)

# =========================
# EXPLORAÇÃO INICIAL
# =========================

print("\n===== PRIMEIRAS LINHAS =====")
print(df.head())

print("\n===== INFORMAÇÕES GERAIS =====")
print(df.info())

print("\n===== ESTATÍSTICAS DESCRITIVAS =====")
print(df.describe())

print("\n===== VALORES NULOS =====")
print(df.isnull().sum())

print("\n===== COLUNAS DO DATASET =====")
print(df.columns)

# =========================
# ANÁLISE DE FRAUDES
# =========================

print("\n===== QUANTIDADE DE FRAUDES =====")
print(df['fraud_flag'].value_counts())

print("\n===== PORCENTAGEM DE FRAUDES =====")
print(df['fraud_flag'].value_counts(normalize=True) * 100)

# =========================
# DISTRIBUIÇÃO DE FRAUDES
# =========================

sns.countplot(x='fraud_flag', data=df)

plt.title('Distribuição de Fraudes')
plt.xlabel('Fraude')
plt.ylabel('Quantidade')

plt.show()

# =========================
# FRAUDES INTERNACIONAIS
# =========================

sns.barplot(
    x='is_international',
    y='fraud_flag',
    data=df
)

plt.title('Fraude em Transações Internacionais')
plt.xlabel('Transação Internacional')
plt.ylabel('Média de Fraudes')

plt.show()

# =========================
# VALOR DAS TRANSAÇÕES
# =========================

sns.boxplot(
    x='fraud_flag',
    y='transaction_amount',
    data=df
)

plt.title('Valor das Transações por Fraude')
plt.xlabel('Fraude')
plt.ylabel('Valor da Transação')

plt.show()

# =========================
# IDADE DA CONTA
# =========================

sns.boxplot(
    x='fraud_flag',
    y='account_age_days',
    data=df
)

plt.title('Idade da Conta por Fraude')
plt.xlabel('Fraude')
plt.ylabel('Dias da Conta')

plt.show()

# =========================
# TIPO DE DISPOSITIVO
# =========================

sns.countplot(
    x='device_type',
    hue='fraud_flag',
    data=df
)

plt.title('Fraudes por Tipo de Dispositivo')
plt.xlabel('Tipo de Dispositivo')
plt.ylabel('Quantidade')

plt.show()

# =========================
# CORRELAÇÃO
# =========================

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(14, 8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title('Mapa de Correlação')

plt.show()

print("\n===== ANÁLISE FINALIZADA COM SUCESSO =====")