import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf
from pandas import DataFrame
from plotly.subplots import make_subplots
from pytrends import dailydata
from pytrends.request import TrendReq
from datetime import date, datetime
import math

pytrends = TrendReq(hl='pt-BR', tz=360)


### Ganho seguindo o Buy and Hold

def buy_hold(combined):
        
    buy_hold = list(range(len(combined)-1)) 

    for i in range(len(combined)-2):
        buy_hold[i+1] = (combined.iloc[i+1,1] - combined.iloc[i,1])/combined.iloc[i,1]
        
    buy_hold.append(0) #Adicionei mais uma linha pra fazer com que os index batessem. Tem que vir antes de pd
    buy_hold = pd.DataFrame(buy_hold) 
    buy_hold = buy_hold.rename(columns={ 0: 'Retorno da Estratégia'}) 
    buy_hold = buy_hold.set_index(combined.index, inplace = False)
    buy_hold.drop(buy_hold.tail(1).index, inplace = True) # Dropei a linha adicionada 

    # Ganho acumulado do buy and hold
    gain_bh = 1

    for i in range(len(buy_hold)):
        gain_bh = gain_bh*(1+buy_hold.iloc[i,0])
    print(gain_bh)

    # Visualização gráfica
    grafbh = list(range(len(buy_hold)))
    grafbh[0] = 1

    for i in range(len(buy_hold)-1):
        grafbh[i+1] = grafbh[i]*(1+buy_hold.iloc[i,0])
        
    return grafbh

def sinal1(dados, inverso):
    
    tamanho = len(dados)
    
    somatorio = list(range(tamanho))
    resultado = list(range(tamanho))
    media_ = list(range(tamanho))
        
    somatorio[0] = dados.iloc[0,0]
    media_[0] = 0
    resultado[0] = 0
    
    for i in range(1,tamanho): # Soma os anteriores 
        somatorio[i] = dados.iloc[i,0] + somatorio[i-1]
        
    somatorio = pd.DataFrame(somatorio)
    
    for i in range(tamanho): # Faz a "média" dos anteriores (o i é de hoje)
        media_[i] = somatorio.iloc[i,0]/(i+1)
    
    media_ = pd.DataFrame(media_)
    
    for i in range(1,tamanho): # Hoje - média anteriores 
        resultado[i] = dados.iloc[i,0] - media_.iloc[i-1,0]
        
    resultado = pd.DataFrame(resultado)
    
    ind = list(range(tamanho))
    
    if inverso == False:
        for i in range(1,tamanho):
            if resultado.iloc[i,0]>0:
                ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
            else:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"          
    else:
        for i in range(1,tamanho):
            if resultado.iloc[i,0]<0:
                ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
            else:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG" 
            
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(dados.index, inplace = False)
        
    return ind

def strategy1(combined, sinais):
    
    combined2 = combined.merge(sinais, on = 'date', how = 'right').dropna()
    
    retorno_est1 = list(range(len(combined2)-1)) 

    for i in range(len(combined2)-2):
        if combined2.iloc[i,2] == "buy p(t+1); sell p(t+2) - LONG":
            retorno_est1[i+1] = (combined2.iloc[i+2,1] - combined2.iloc[i+1,1])/combined2.iloc[i+1,1]
        else:
            retorno_est1[i+1] = (combined2.iloc[i+1,1] - combined2.iloc[i+2,1])/combined2.iloc[i+2,1]
        
    retorno_est1.append(0) #Adicionei mais uma linha pra fazer com que os index batessem. Tem que vir antes de pd
    retorno_est1 = pd.DataFrame(retorno_est1) 
    retorno_est1 = retorno_est1.rename(columns={ 0: 'Retorno da Estratégia'}) 
    retorno_est1 = retorno_est1.set_index(combined2.index, inplace = False)
    retorno_est1.drop(retorno_est1.tail(1).index, inplace = True) # Dropei a linha adicionada   

    # Ganho acumulado da estratégia 1
    gain = 1 

    for i in range(1,len(retorno_est1)):
        gain = gain*(1+retorno_est1.iloc[i,0])
    print(gain)

    # Visualização gráfica
    ganhograf = list(range(len(retorno_est1)))
    ganhograf[0] = 1

    for i in range(len(retorno_est1)-1):
        ganhograf[i+1] = ganhograf[i]*(1+retorno_est1.iloc[i,0])
    
    return ganhograf, combined2

def graph(ganhograf, ganhografteste, combined2):
        
    ganhograf.append(ganhograf[len(ganhograf)-1])
    ganhograf = pd.DataFrame(ganhograf)
    ganhograf = ganhograf.rename(columns={ 0: 'Retorno da Estratégia 1'}) 
    ganhograf = ganhograf.set_index(combined2.index, inplace = False)
    ganhograf = ganhograf.drop(ganhograf.tail(1).index, inplace = False) # Dropei a linha adicionada      

    ganhografteste.append(ganhografteste[len(ganhografteste)-1])
    ganhografteste = pd.DataFrame(ganhografteste)
    ganhografteste = ganhografteste.rename(columns={ 0: 'Retorno do Buy and Hold'}) 
    ganhografteste = ganhografteste.set_index(combined2.index, inplace = False)
    ganhografteste = ganhografteste.drop(ganhografteste.tail(1).index, inplace = False) # Dropei a linha adicionada  
    
    ganhos_combined = ganhograf.merge(ganhografteste, on = 'date', how = 'right').dropna()
    
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": False}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=ganhos_combined.index, y=ganhos_combined['Retorno da Estratégia 1'], name="Retorno da Estratégia 1",
                   mode = 'lines', line_color='#34B6F0')
    )

    fig.add_trace(
        go.Scatter(x=ganhos_combined.index, y=ganhos_combined['Retorno do Buy and Hold'], name="Retorno do Buy and Hold",
                  mode = 'lines', line_color = "#1a3668")
    )

    # Add figure title
    fig.update_layout(
        title_text=("Retorno do Buy and Hold e da Estratégia")
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Data")

    # Set y-axes titles
    fig.update_yaxes(title_text= 'Retorno', secondary_y=False)

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
            ), 
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'

    )
        
    return fig 