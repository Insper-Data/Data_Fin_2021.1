import basic_func as bf
import strategy as strat 

#Puxando dados
inicio = '2016-01-02'

trends = bf.get_google(palavra = "abev3", startdate = inicio, overlap = 45)

stocks = bf.get_stocks(ativo = "abev3")

combined = bf.join(trends = trends, stocks = stocks)

#Gerando os sinais
sinal_est1 = strat.sinal1(combined = combined, inverso = False)

#Processando sinais em retorno
ganhoestrat, combined2 = strat.gen_return_sep(combined = combined, sinais = sinal_est1)

#Benchmark Buy-n-Hold
buyhold = strat.buy_hold(combined)

#Graficando
plim = strat.graph_matplot(ganhoestrat, buyhold, combined2)

plim.show()

#Testando o sinal híbrido

sinal_teste = strat.sinal2(combined = combined, inverso = False)

ganho_teste, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_matplot(ganho_teste, buyhold, combined2_teste)

plim_acelerador.show()

#Testando o sinal das médias móveis

sinal_teste = strat.sinal3(combined = combined, inverso = False, dias = 21)

ganho_teste, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_matplot(ganho_teste, buyhold, combined2_teste)

plim_acelerador.show()

#Testando o sinal das médias móveis para preços e pesquisas (projeto 2020.2)

sinal_teste = strat.sinal4(combined = combined, inverso = False, dias = 21)

ganho_teste, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_matplot(ganho_teste, buyhold, combined2_teste)

plim_acelerador.show()

#Testando o sinal do acelerador

sinal_teste = strat.sinal_acelerador(combined = combined)

combined3 = strat.gen_return(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_one(combined3, buyhold)

plim_acelerador.show() 

# Testando o sinal1 do validado pelo volume

stocks_y = bf.get_yahoo("^BVSP")

combined_y = bf.join(trends = trends, stocks = stocks_y)

buyhold_y = strat.buy_hold(combined_y)

sinal_teste = strat.sinal_volume1(combined = combined_y, inverso = False)
    # N sei pq mas o inverso ser True ou False n muda o resultado

combined3_y = strat.gen_return(combined = combined_y, sinais = sinal_teste)

plim_acelerador = strat.graph_one_vol(combined3_y, buyhold_y)

plim_acelerador.show() 

