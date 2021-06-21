import pandas as pd
import basic_func as bf
import strategy as strat 

#Puxando dados
inicio = '2016-01-02'

abev3 = pd.read_excel("dados/abev3.xlsx")
abev3 = abev3.set_index('date')

stocks = bf.get_stocks(ativo = "abev3")

combined = bf.join(trends = abev3, stocks = stocks)

### Inverso = False
#### Pegar o sharpe e o inverso = True
#### Fazer para os outros

# Estratégia 1
sinal_est1 = strat.sinal1(combined = combined, inverso = False)

ganhoestrat, combined2 = strat.gen_return_sep(combined = combined, sinais = sinal_est1)

# Estratégia 2
sinal_est2 = strat.sinal2(combined = combined, inverso = False)

ganhoestrat2, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_est2)

# Estratégia 3
sinal_est3 = strat.sinal3(combined = combined, inverso = False, dias = 21)

ganhoestrat3, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_est3)

# Estratéfgia 4
sinal_est4 = strat.sinal4(combined = combined, inverso = False, dias = 21)

ganhoestrat4, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_est4)

# Estratégia 5
sinal_est5 = strat.sinal_acelerador(combined = combined)

ganhoestrat5, combined2_teste = strat.gen_return_sep(combined = combined, sinais = sinal_est5)




