# Área de testes

import basic_func as bf
import strategy as strat 

#%% Puxando dados
inicio = '2016-01-02'

trends = bf.get_google(palavra = "abev3", startdate = inicio, overlap = 45)

stocks = bf.get_stocks(ativo = "BVSP")

combined = bf.join(trends = trends, stocks = stocks)

#%% Buy and Hold

buyhold = strat.buy_hold(combined)

#%% Estraégias

# Estratégia 1

## Gerando sinais
sinal_est1 = strat.sinal1(combined = combined, inverso = False)

## Processando sinais em retorno
ganhoestrat, combined2 = strat.gen_return_sep(combined = combined, sinais = sinal_est1)

## Graficando
grafico = strat.graph_matplot(ganhoestrat, buyhold, combined2)

grafico.show()

# Estratégia 2

sinal_est2 = strat.sinal2(combined = combined, inverso = False)

ganho_est2, combined2 = strat.gen_return_sep(combined = combined, sinais = sinal_est2)

grafico = strat.graph_matplot(ganho_est2, buyhold, combined2)

grafico.show()

# Estratégia 3

sinal_est3 = strat.sinal3(combined = combined, inverso = False, dias = 21)

ganho_est3, combined2= strat.gen_return_sep(combined = combined, sinais = sinal_est3)

grafico = strat.graph_matplot(ganho_est3, buyhold, combined2)

grafico.show()

# Estratégia 4

sinal_est4 = strat.sinal4(combined = combined, inverso = False, dias = 21)

ganho_est4, combined2_est4 = strat.gen_return_sep(combined = combined, sinais = sinal_est4)

grafico  = strat.graph_matplot(ganho_est4, buyhold, combined2_est4)

grafico.show()

# Estratégia 5

sinal_est5 = strat.sinal5(combined = combined)

combined3 = strat.gen_return(combined = combined, sinais = sinal_est5)

grafico = strat.graph_one(combined3, buyhold)

grafico.show() 

# Estratégia 6

stocks_y = bf.get_yahoo("^BVSP")

combined_y = bf.join(trends = trends, stocks = stocks_y)

buyhold_y = strat.buy_hold(combined_y)

sinal_est6 = strat.sinal6(combined = combined_y, inverso = False)
    # N sei pq mas o inverso ser True ou False n muda o resultado

combined3_y = strat.gen_return(combined = combined_y, sinais = sinal_est6)

grafico = strat.graph_one_vol(combined3_y, buyhold_y)

grafico.show() 
