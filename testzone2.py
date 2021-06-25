import basic_func as bf
import strategy as strat 
import pandas as pd

#Puxando dados
inicio = '2016-01-02'

trends = pd.read_excel(f'Dados/cerveja.xlsx')
trends = trends.set_index('date')

stocks = bf.get_stocks(ativo = "abev")

combined = bf.join(trends = trends, stocks = stocks)

#Gerando os sinais
sinal_est1 = strat.sinal1(combined = combined, inverso = True)

#Processando sinais em retorno
ganhoestrat, combined2 = strat.gen_return_sep(combined = combined, sinais = sinal_est1)

#Benchmark Buy-n-Hold
buyhold = strat.buy_hold(combined)

#Graficando
plim = strat.graph_matplot_(ganhoestrat, buyhold, combined2, cor = "red")

#Testando o sinal híbrido

sinal_teste = strat.sinal2(combined = combined, inverso = True)

ganho_teste, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_matplot_(ganho_teste, buyhold, combined2_teste, cor = "green")

#Testando o sinal das médias móveis

sinal_teste = strat.sinal3(combined = combined, inverso = True, dias = 21)

ganho_teste1, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_matplot_(ganho_teste1, buyhold, combined2_teste, cor = "blue")

#Testando o sinal das médias móveis para preços e pesquisas (projeto 2020.2)

sinal_teste = strat.sinal4(combined = combined, inverso = True, dias = 21)

ganho_teste2, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_matplot_(ganho_teste2, buyhold, combined2_teste, cor = "purple")

#Testando o sinal do acelerador

sinal_teste = strat.sinal_acelerador(combined = combined)

combined3 = strat.gen_return(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_one(combined3, buyhold)

###
sinal_est5 = strat.sinal_acelerador(combined = combined)

ganhoestrat_5, combined3 = strat.gen_return_edit(combined = combined, sinais = sinal_est5)

plim_acelerador = strat.graph_matplot_(ganhoestrat_5, buyhold, combined3, cor = "yellow")
