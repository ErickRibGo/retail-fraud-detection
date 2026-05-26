# Detecção de Fraude no Varejo: Análise Exploratória e Insights de Negócio

[cite_start]Este repositório contém o desafio técnico desenvolvido para o processo seletivo de **Estágio em Ciência de Dados**[cite: 4]. [cite_start]O objetivo principal é conduzir uma Análise Exploratória de Dados (EDA) robusta sobre um conjunto de dados de transações de varejo [cite: 32][cite_start], investigando comportamentos fraudulentos e gerando insumos estratégicos para mitigar riscos de negócio[cite: 15, 16].

---

## 1. Contextualização do Problema e Escolha do Dataset

No setor de varejo físico e digital, a fraude não representa apenas um prejuízo financeiro direto; ela mina a confiança do cliente, eleva os custos operacionais (com *chargebacks* e disputas) e sobrecarrega os times de análise de risco. 

[cite_start]Para este desafio, foi selecionado o dataset **Retail Fraud Detection** (com 100.000 registros)[cite: 23, 24]. A escolha se justifica por:
* [cite_start]**Volume e Diversidade:** Possui uma volumetria estatisticamente representativa para identificar padrões reais[cite: 23, 24].
* [cite_start]**Variedade de Variáveis:** Contém dimensões categóricas (como tipo de dispositivo), numéricas (valores e idade de conta), temporais e comportamentais (*flags* de anomalias), permitindo análises multidimensionais aprofundadas[cite: 24].

---

## 2. Metodologia e Qualidade dos Dados

[cite_start]O pipeline da análise foi estruturado utilizando Python e as bibliotecas `pandas`, `numpy`, `matplotlib` e `seaborn`. 

### Verificação de Consistência
[cite_start]Antes da análise de padrões, foi realizada uma auditoria de qualidade na base[cite: 34]:
* **Valores Ausentes:** A execução do método `.isnull().sum()` constatou que o dataset se encontra completamente preenchido, sem registros nulos, eliminando a necessidade de técnicas de imputação.
* **Integridade das Variáveis:** As distribuições das variáveis numéricas foram revisadas via estatística descritiva (`.describe()`) para garantir que os limites lógicos fossem respeitados.

---

## 3. Formulação e Teste de Hipóteses

[cite_start]Para guiar a análise e extrair valor de negócio, foram formuladas quatro hipóteses principais[cite: 25, 36]:

### Hipótese 1: Contas criadas recentemente têm maior propensão a fraudar.
* **O que o gráfico diz (Idade da Conta por Fraude):** O boxplot revelou distribuições de quartis e medianas praticamente idênticas entre transações legítimas e fraudulentas. Na matriz de correlação, a relação linear entre `account_age_days` e `fraud_flag` é de **-0.0021** (nula).
* **Conclusão:** **Hipótese Rejeitada.** O tempo de existência da conta, isoladamente, não é um fator preditivo para o comportamento fraudulento nesta base.

### Hipótese 2: Transações internacionais concentram um índice crítico de fraudes.
* **O que o gráfico diz (Fraude em Transações Internacionais):** O gráfico de barras demonstra que a taxa média de fraude salta para quase **70%** ($0.7$) quando a transação é internacional, contra menos de 30% em transações domésticas. A matriz de correlação confirma uma forte associação positiva de **0.42**.
* **Conclusão:** **Hipótese Confirmada.** Transações internacionais representam uma zona de altíssimo risco operacional.

### Hipótese 3: O tipo de dispositivo utilizado pelo usuário influencia o risco da operação.
* **O que o gráfico diz (Fraudes por Tipo de Dispositivo):** Nos tablets e desktops, o volume de transações legítimas supera o de fraudes. Contudo, nos dispositivos **Mobile**, a quantidade de fraudes é **superior** às transações legítimas.
* **Conclusão:** **Hipótese Confirmada.** O canal móvel (Mobile) é o vetor mais vulnerável e preferido pelas ações fraudulentas.

### Hipótese 4: Transações fraudulentas envolvem valores significativamente mais agressivos/fora do padrão.
* **O que o gráfico diz (Valor das Transações por Fraude & Correlação):** O boxplot de valores mostra que as fraudes apresentam maior dispersão no terceiro quartil e uma mediana ligeiramente superior. O ponto crucial está no mapa de calor: o indicador de valor incomum (`unusual_amount_flag`) possui correlação de **0.64** com o valor nominal da transação e **0.33** com a fraude direta.
* **Conclusão:** **Hipótese Confirmada.** O comportamento do fraudador está fortemente atrelado a picos anômalos de valor de compra.

---

## 4. Conclusões e Recomendações de Negócio

[cite_start]A análise exploratória permitiu traçar com clareza o **perfil de alto risco** das transações[cite: 54, 76]:

> **Perfil Crítico:** Uma transação realizada via dispositivo **Mobile**, marcada como **Internacional** (ou local incomum) e com um **valor fora do padrão de consumo habitual** do usuário.

### Recomendações Estratégicas para o Negócio:
1. **Regras de Bloqueio e Step-Up Authentication:** Implementar uma camada obrigatória de autenticação multifator (MFA) rígida baseada em risco sempre que houver o cruzamento dos fatores de risco (Dispositivo Móvel + Transação Internacional).
2. **Otimização de Custos em Revisão Manual:** Como a idade da conta provou ter correlação nula com o comportamento fraudulento, os analistas de risco não devem priorizar o tempo de conta como critério de triagem, liberando eficiência operacional para focar em telemetria de dispositivo e geolocalização.

---
<img width="999" height="681" alt="image" src="https://github.com/user-attachments/assets/97a6bc94-5549-4cea-8613-df7656a5d582" />
<img width="1006" height="662" alt="image" src="https://github.com/user-attachments/assets/ac624a9f-bbca-4d0b-935c-51cba901248e" />
<img width="999" height="674" alt="image" src="https://github.com/user-attachments/assets/caf5d378-eee1-4d05-8dcb-189177a0d2f5" />
<img width="999" height="672" alt="image" src="https://github.com/user-attachments/assets/a1ce2f82-b7e5-466d-971c-caad1ec4372e" />
<img width="1003" height="670" alt="image" src="https://github.com/user-attachments/assets/028c1b34-7116-4a58-ad11-d3ee65c6cf2c" />
<img width="1395" height="869" alt="image" src="https://github.com/user-attachments/assets/d65138c6-009c-41f7-8b3c-4168bb093f8f" />


## 5. Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina.

### Passos para execução
1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
