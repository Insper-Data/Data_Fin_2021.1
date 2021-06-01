import basic_func as insp
import strategy as strat 

#Puxando dados
inicio = '2017-01-01'

trends = insp.get_google(palavra = "vvar3", startdate = inicio, overlap = 45)

stocks = insp.get_stocks(ativo = "vvar3")

combined = insp.join(trends = trends, stocks = stocks)

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


#Testando o sinal do acelerador

sinal_teste = strat.sinal_acelerador(combined = combined)

combined3 = strat.gen_return(combined = combined, sinais = sinal_teste)

plim_acelerador = strat.graph_one(combined3, buyhold)

plim_acelerador.show() 