import insperdata as insp
import strategy as strat 

inicio = '2017-01-01'

trends = insp.get_google(palavra = "ambev", startdate = inicio, overlap = 45)

stocks = insp.get_stocks(ativo = "abev")

combined = insp.join(trends = trends, stocks = stocks)


buyhold = strat.buy_hold(combined)

sinal_est1 = strat.sinal1(dados = trends, inverso = False)

ganhoestrat, combined2 = strat.strategy1(combined = combined, sinais = sinal_est1)

sharpe_ratio = insp.sharpe_aa(ganhoestrat)
print(f'Índice de Sharpe anualizado da estratégia: {sharpe_ratio}')
sharpe_r = insp.sharpe_aa(buyhold)
print(f'Índice de Sharpe anualizado do buy and hold: {sharpe_r}')

grafico = strat.graph(ganhoestrat, buyhold, combined2)


grafico.show()

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()

