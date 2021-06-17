import pandas as pd
import basic_func as bf
import strategy as strat 

#Puxando dados
inicio = '2016-01-02'

stocks = bf.get_stocks(ativo = 'bbdc4')

# Estratégia 1

words = ["bbdc4", "ibovespa", "divida", "cor", "açoes", "restaurante", "portifolio", "inflaçao",
         "ibovespa", "economia", "credito", "mercado", "desemprego", "dinheiro", "investimento",
         "titulos", "derivativos",  "mercado financeiro", "crise", "finanças", "viajar", "petroleo",
         "politica", "dividendos", "fundos de investimento", "corretora", "empresa", "como investir",
         "renda extra", "dolar", "mineraçao", "banco", "varejo", "bolsa", "selic", "banco central",
         "alimento", "gado", "commodities", "cerveja", "estagio"]

words = pd.DataFrame(words)

## Inverso = False

retorno_1F_bbdc4 = list(range(len(words)))
retorno_1F_bbdc4 = pd.DataFrame(retorno_1F_bbdc4)
retorno_1F_bbdc4.set_index(words[0], inplace = True)

sharpe_1F_bbdc4 = list(range(len(words)))
sharpe_1F_bbdc4 = pd.DataFrame(sharpe_1F_bbdc4)
sharpe_1F_bbdc4.set_index(words[0], inplace = True)

for i in range(20,len(words)):

    trends = bf.get_google(palavra = words.iloc[i,0], startdate = inicio, overlap = 45)
    
    combined = bf.join(trends = trends, stocks = stocks)

    #Gerando os sinais
    sinal_est1 = strat.sinal1(combined = combined, inverso = False)

    #Processando sinais em retorno
    ganhoestrat, combined2 = strat.gen_return_sep(combined = combined, sinais = sinal_est1)

    retorno_1F_bbdc4.iloc[i,0] = ganhoestrat[-1]
    
    sharpe_1F_bbdc4.iloc[i,0] = bf.sharpe_aa(ganhoestrat)
    