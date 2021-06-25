import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np

#pytrends = TrendReq(hl='pt-BR', tz=360)
## Se for puxar algum dado, descomentar isso

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

    for i in range(1, len(buy_hold)):
        gain_bh = gain_bh*(1+buy_hold.iloc[i,0])
    print(gain_bh)

    # Visualização gráfica
    grafbh = list(range(len(buy_hold)))
    grafbh[0] = 1

    for i in range(len(buy_hold)-1):
        grafbh[i+1] = grafbh[i]*(1+buy_hold.iloc[i,0])
        
    return grafbh

# Usando a estratégia do Quantifying Trading Behaviour

def sinal1(combined, inverso):
    
    dados_trends = pd.DataFrame(combined.iloc[:,0])
    
    tamanho_trends = len(dados_trends)
    
    somatorio = list(range(tamanho_trends))
    resultado = list(range(tamanho_trends))
    media_ = list(range(tamanho_trends))
        
    somatorio[0] = dados_trends.iloc[0,0]
    media_[0] = 0
    resultado[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio[i] = dados_trends.iloc[i,0] + somatorio[i-1]
        
    somatorio = pd.DataFrame(somatorio)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_[i] = somatorio.iloc[i,0]/(i+1)
    
    media_ = pd.DataFrame(media_)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado[i] = dados_trends.iloc[i,0] - media_.iloc[i-1,0]
        
    resultado = pd.DataFrame(resultado)
    
    ind = list(range(tamanho_trends))
    
    if inverso == False:
        for i in range(1,tamanho_trends):
            if resultado.iloc[i,0]>0:
                ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
            else:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"          
    else:
        for i in range(1,tamanho_trends):
            if resultado.iloc[i,0]<0:
                ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
            else:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG" 
            
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(dados_trends.index, inplace = False)
        
    return ind

# Estratégia do papaer alemão (híbrida)

def sinal2(combined, inverso):
    
    tamanho_trends = len(combined)
    
    dados_trends = combined.iloc[:,0]
    dados_trends = pd.DataFrame(dados_trends)
    
    stocks = combined.iloc[:,1]
    stocks = pd.DataFrame(stocks)
    
    # Para Trends
    
    somatorio = list(range(tamanho_trends))
    resultado = list(range(tamanho_trends))
    media_ = list(range(tamanho_trends))
        
    somatorio[0] = dados_trends.iloc[0,0]
    media_[0] = 0
    resultado[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio[i] = dados_trends.iloc[i,0] + somatorio[i-1]
        
    somatorio = pd.DataFrame(somatorio)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_[i] = somatorio.iloc[i,0]/(i+1)
    
    media_ = pd.DataFrame(media_)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado[i] = dados_trends.iloc[i,0] - media_.iloc[i-1,0]
        
    resultado = pd.DataFrame(resultado)
    
    # Para stocks
    
    somatorio2 = list(range(tamanho_trends))
    resultado2 = list(range(tamanho_trends))
    media_2 = list(range(tamanho_trends))
        
    somatorio2[0] = stocks.iloc[0,0]
    media_2[0] = 0
    resultado2[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio2[i] = stocks.iloc[i,0] + somatorio2[i-1]
        
    somatorio2 = pd.DataFrame(somatorio2)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_2[i] = somatorio2.iloc[i,0]/(i+1)
    
    media_2 = pd.DataFrame(media_2)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado2[i] = stocks.iloc[i,0] - media_2.iloc[i-1,0]
        
    resultado2 = pd.DataFrame(resultado2)
    
    # Indicador
    
    ind = list(range(tamanho_trends))
    
    if inverso == False:
        for i in range(1,tamanho_trends):
            if resultado2.iloc[i,0]>0:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                if resultado.iloc[i,0]>0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"
    else:
        for i in range(1,tamanho_trends):
            if resultado2.iloc[i,0]>0:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                if resultado.iloc[i,0]<0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(dados_trends.index, inplace = False)
        
    return ind

# Estratégia híbrida com médias móveis

def sinal3(combined, inverso, dias):
    
    tamanho_trends = len(combined)
    
    dados_trends = combined.iloc[:,0]
    dados_trends = pd.DataFrame(dados_trends)
    
    stocks = combined.iloc[:,1]
    stocks = pd.DataFrame(stocks)
    
    # Para Trends
    
    somatorio = list(range(tamanho_trends))
    resultado = list(range(tamanho_trends))
    media_ = list(range(tamanho_trends))
        
    somatorio[0] = dados_trends.iloc[0,0]
    media_[0] = 0
    resultado[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio[i] = dados_trends.iloc[i,0] + somatorio[i-1]
        
    somatorio = pd.DataFrame(somatorio)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_[i] = somatorio.iloc[i,0]/(i+1)
    
    media_ = pd.DataFrame(media_)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado[i] = dados_trends.iloc[i,0] - media_.iloc[i-1,0]
        
    resultado = pd.DataFrame(resultado)
    
    # Para stocks
    
    tam_mm = dias
    i=0
    mm = []
    
    while i < tamanho_trends - tam_mm + 1:
        grupo = stocks.iloc[i : i + tam_mm,0]
        media_grupo = sum(grupo) / tam_mm
        mm.append(media_grupo)
        i +=1
        
    for i in range(dias-1):
        mm.insert(0,0)
    
    mm = pd.DataFrame(mm)
    
    # Indicador
    
    ind = list(range(tamanho_trends))
    
    if inverso == False:
        for i in range(dias,tamanho_trends):
            if mm.iloc[i,0] - mm.iloc[i-1,0]>0:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                if resultado.iloc[i,0]>0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"
    else:
        for i in range(dias,tamanho_trends):
            if mm.iloc[i,0] - mm.iloc[i-1,0]>0:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                if resultado.iloc[i,0]<0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(dados_trends.index, inplace = False)
        
    return ind

# Estratégia com insipiração o projeto de finanças de 2020.2

def sinal4(combined, inverso, dias):
    
    tamanho = len(combined)
    
    trends = combined.iloc[:,0]
    trends = pd.DataFrame(trends)
    
    stocks = combined.iloc[:,1]
    stocks = pd.DataFrame(stocks)
    
    # Para stocks
    
    tam_mm = dias
    i=0
    mm = []
    
    while i < tamanho - tam_mm + 1:
        grupo = stocks.iloc[i : i + tam_mm,0]
        media_grupo = sum(grupo) / tam_mm
        mm.append(media_grupo)
        i +=1
        
    for i in range(dias-1):
        mm.insert(0,0)
    
    mm = pd.DataFrame(mm)
    
    # Para trends
    
    tam_mm = dias
    i=0
    mm_ = []
    
    while i < tamanho - tam_mm + 1:
        grupo_ = trends.iloc[i : i + tam_mm,0]
        media_grupo_ = sum(grupo_) / tam_mm
        mm_.append(media_grupo_)
        i +=1
        
    for i in range(dias-1):
        mm_.insert(0,0)
    
    mm_ = pd.DataFrame(mm_)
    
    # Indicador
    
    ind = list(range(tamanho))
    
    if inverso == False:
        for i in range(dias, tamanho):
            if mm.iloc[i,0] - mm.iloc[i-1,0]>0:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                if mm_.iloc[i,0] - mm_.iloc[i-1,0]>0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"
    else:
        for i in range(dias, tamanho):
            if mm.iloc[i,0] - mm.iloc[i-1,0]>0:
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                if mm_.iloc[i,0] - mm_.iloc[i-1,0]<0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"
    
    # Se a média móvel dos preços está subindo, LONG
    # Se ela estiver caindo e a média móvel das pesquisas estiver subindo, SHORT
    # Em qualquer outro cenário, LONG
                   
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(trends.index, inplace = False)
        
    return ind

def gen_return_edit(combined, sinais):
    
    combined2 = combined.merge(sinais, on = 'date', how = 'right').dropna() #Une os sinais com Trends e preços (stock)
    
    datas = list(combined2.index) #Salvando o index
    datas = datas[1:]
    
    retorno_est1 = list(range(len(combined2)-1)) #Diminui 1 em tamanho pois o primeiro dia não tem trade

    for i in range(len(combined2)-2):
        if combined2.iloc[i,2] == "buy p(t+1); sell p(t+2) - LONG":
            retorno_est1[i+1] = (combined2.iloc[i+2,1] - combined2.iloc[i+1,1])/combined2.iloc[i+1,1]
        elif combined2.iloc[i,2] == "DO NOTHING":
            retorno_est1[i+1] = 0   #Possivelmente adicionar retorno diário de uma carteira passiva
        else:
            retorno_est1[i+1] = (combined2.iloc[i+1,1] - combined2.iloc[i+2,1])/combined2.iloc[i+2,1]
        
    retorno_est1 = pd.DataFrame(retorno_est1) #Transformando os retornos diários em dataframe
    
    # Ganho acumulado da estratégia 
    gain = 1 

    for i in range(1,len(retorno_est1)):
        gain = gain*(1+retorno_est1.iloc[i,0])
    print(gain)

    # Visualização gráfica
    ganhograf = list(range(len(retorno_est1)))
    ganhograf[0] = 1

    for i in range(len(retorno_est1)-1):
        ganhograf[i+1] = ganhograf[i]*(1+retorno_est1.iloc[i,0])
        
    copia_ganhograf = ganhograf.copy()
        
    ganhograf = pd.DataFrame(ganhograf, index = datas) #Transforma a série de retornos acumulados em DF
    
    combined3 = combined2.merge(ganhograf, left_index = True, right_index = True) #Junta trends, preços, sinais e retornos
    combined3 = combined3.rename(columns = { 3: "Retornos acumulados"})
    
    return copia_ganhograf, combined3

def gen_return(combined, sinais):
    
    combined2 = combined.merge(sinais, on = 'date', how = 'right').dropna() #Une os sinais com Trends e preços (stock)
    
    datas = list(combined2.index) #Salvando o index
    datas = datas[1:]
    
    retorno_est1 = list(range(len(combined2)-1)) #Diminui 1 em tamanho pois o primeiro dia não tem trade

    for i in range(len(combined2)-2):
        if combined2.iloc[i,2] == "buy p(t+1); sell p(t+2) - LONG":
            retorno_est1[i+1] = (combined2.iloc[i+2,1] - combined2.iloc[i+1,1])/combined2.iloc[i+1,1]
        elif combined2.iloc[i,2] == "DO NOTHING":
            retorno_est1[i+1] = 0   #Possivelmente adicionar retorno diário de uma carteira passiva
        else:
            retorno_est1[i+1] = (combined2.iloc[i+1,1] - combined2.iloc[i+2,1])/combined2.iloc[i+2,1]
        
    retorno_est1 = pd.DataFrame(retorno_est1) #Transformando os retornos diários em dataframe
    
    # Ganho acumulado da estratégia 
    gain = 1 

    for i in range(1,len(retorno_est1)):
        gain = gain*(1+retorno_est1.iloc[i,0])
    print(gain)

    # Visualização gráfica
    ganhograf = list(range(len(retorno_est1)))
    ganhograf[0] = 1

    for i in range(len(retorno_est1)-1):
        ganhograf[i+1] = ganhograf[i]*(1+retorno_est1.iloc[i,0])
        
    ganhograf = pd.DataFrame(ganhograf, index = datas) #Transforma a série de retornos acumulados em DF
    
    combined3 = combined2.merge(ganhograf, left_index = True, right_index = True) #Junta trends, preços, sinais e retornos
    combined3 = combined3.rename(columns = { 3: "Retornos acumulados"})
    
    return combined3

def gen_return_flexible(combined, sinais, hold_time):
    
    combined2 = combined.merge(sinais, on = 'date', how = 'right').dropna() #Une os sinais com Trends e preços (stock)
    
    datas = list(combined2.index) #Salvando o index
    datas = datas[1:]
    
    retorno_est1 = list(range(len(combined2)-1)) #Diminui 1 em tamanho pois o primeiro dia não tem trade

    for i in range(len(combined2)-(1 + hold_time)):
        if combined2.iloc[i,2] == "buy p(t+1); sell p(t+2) - LONG":
            retorno_est1[i+1] = (combined2.iloc[i+(1+hold_time),1] - combined2.iloc[i+1,1])/combined2.iloc[i+1,1]
        elif combined2.iloc[i,2] == "DO NOTHING":
            retorno_est1[i+1] = 0   #Possivelmente adicionar retorno diário de uma carteira passiva
        else:
            retorno_est1[i+1] = (combined2.iloc[i+1,1] - combined2.iloc[i+(1+hold_time),1])/combined2.iloc[i+(1+hold_time),1]
        
    retorno_est1 = pd.DataFrame(retorno_est1) #Transformando os retornos diários em dataframe
    
    # Ganho acumulado da estratégia 
    gain = 1 

    for i in range(1,len(retorno_est1)):
        gain = gain*(1+retorno_est1.iloc[i,0])
    print(gain)

    # Visualização gráfica
    ganhograf = list(range(len(retorno_est1)))
    ganhograf[0] = 1

    for i in range(len(retorno_est1)-1):
        ganhograf[i+1] = ganhograf[i]*(1+retorno_est1.iloc[i,0])
        
    ganhograf = pd.DataFrame(ganhograf, index = datas) #Transforma a série de retornos acumulados em DF
    
    combined3 = combined2.merge(ganhograf, left_index = True, right_index = True) #Junta trends, preços, sinais e retornos
    combined3 = combined3.rename(columns = { 3: "Retornos acumulados"})
    
    return combined3

def gen_return_sep(combined, sinais):
    
    combined2 = combined.merge(sinais, on = 'date', how = 'right').dropna() #Une os sinais com Trends e preços (stock)
        
    retorno_est1 = list(range(len(combined2)-1)) #Diminui 1 em tamanho pois o primeiro dia não tem trade

    for i in range(len(combined2)-2):
        if combined2.iloc[i,2] == "buy p(t+1); sell p(t+2) - LONG":
            retorno_est1[i+1] = (combined2.iloc[i+2,1] - combined2.iloc[i+1,1])/combined2.iloc[i+1,1]
        elif combined2.iloc[i,2] == "DO NOTHING":
            retorno_est1[i+1] = 0   #Possivelmente adicionar retorno diário de uma carteira passiva
        else:
            retorno_est1[i+1] = (combined2.iloc[i+1,1] - combined2.iloc[i+2,1])/combined2.iloc[i+2,1]
        
    retorno_est1 = pd.DataFrame(retorno_est1) #Transformando os retornos diários em dataframe
    
    # Ganho acumulado da estratégia 
    gain = 1 

    for i in range(1,len(retorno_est1)):
        gain = gain*(1+retorno_est1.iloc[i,0])
    print(gain)

    # Visualização gráfica
    ganhograf = list(range(len(retorno_est1)))
    ganhograf[0] = 1

    for i in range(len(retorno_est1)-1):
        ganhograf[i+1] = ganhograf[i]*(1+retorno_est1.iloc[i,0])
      
    combined2 = combined2.iloc[1:]
    
    return ganhograf, combined2


def graph_matplot(ganhograf, ganhografteste, combined2):
    
    ganhograf = pd.DataFrame(ganhograf)
    ganhograf = ganhograf.rename(columns={ 0: 'Retorno da Estratégia 1'}) 
    ganhograf = ganhograf.set_index(combined2.index, inplace = False)
        
    ganhografteste = pd.DataFrame(ganhografteste)
    ganhografteste = ganhografteste.rename(columns={ 0: 'Retorno do Buy and Hold'}) 
    ganhografteste = ganhografteste.set_index(combined2.index, inplace = False)
    
    ganhos_combined = ganhograf.merge(ganhografteste, on = 'date', how = 'right').dropna()
    
    # Create some mock data
    t = ganhos_combined.index
    data1 = ganhos_combined['Retorno da Estratégia 1']
    data2 = ganhos_combined['Retorno do Buy and Hold']
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Retorno da Estratégia 1', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('Retorno do Buy and Hold', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    ax2.set(title='Retornos acumulados')
        
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    ganhografteste = ganhografteste.drop(ganhografteste.tail(1).index, inplace = False) # Dropei a linha adicionada  
    
    return fig

def graph_matplot_(ganhograf, ganhografteste, combined2, cor):
    
    ganhograf = pd.DataFrame(ganhograf)
    ganhograf = ganhograf.rename(columns={ 0: 'Retorno da Estratégia 1'}) 
    ganhograf = ganhograf.set_index(combined2.index, inplace = False)
        
    ganhografteste = pd.DataFrame(ganhografteste)
    ganhografteste = ganhografteste.rename(columns={ 0: 'Retorno do Buy and Hold'}) 
    ganhografteste = ganhografteste.set_index(combined2.index, inplace = False)
    
    ganhos_combined = ganhograf.merge(ganhografteste, on = 'date', how = 'right').dropna()
    
    plt.plot(ganhos_combined["Retorno da Estratégia 1"], color = cor)
    plt.plot(ganhos_combined["Retorno do Buy and Hold"], color = "black")
    plt.ylabel("Retorno")
    plt.legend(loc = 'best')

    ganhografteste = ganhografteste.drop(ganhografteste.tail(1).index, inplace = False) # Dropei a linha adicionada  
    
def graph_one(combined3, ganhografteste):
    
    ganhograf = combined3.iloc[:, 3]
    ganhograf = pd.DataFrame(ganhograf)
    ganhograf = ganhograf.rename(columns={ 0: 'Retorno da Estratégia 1'}) 
    ganhograf = ganhograf.set_index(combined3.index, inplace = False)
        
    ganhografteste = pd.DataFrame(ganhografteste)
    ganhografteste = ganhografteste.rename(columns={ 0: 'Retorno do Buy and Hold'}) 
    ganhografteste = ganhografteste.set_index(combined3.index, inplace = False)
    
    ganhos_combined = ganhograf.merge(ganhografteste, left_index = True, right_index = True).dropna()
    
    # Create some mock data
    t = ganhos_combined.index
    data1 = ganhos_combined['Retorno da Estratégia 1']
    data2 = ganhos_combined['Retorno do Buy and Hold']
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Retorno da Estratégia 1', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('Retorno do Buy and Hold', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    ax2.set(title='Retornos acumulados')
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    ganhografteste = ganhografteste.drop(ganhografteste.tail(1).index, inplace = False) # Dropei a linha adicionada  
    
    return fig

# Essa função é exatamente igual a anterior
## A diferença é que o combined3 agora tem uma coluna a mais (volume)
## Mudei isso no primeira linha do código da função

def graph_one_vol(combined3, ganhografteste):
    
    ganhograf = combined3.iloc[:, 4]
    ganhograf = pd.DataFrame(ganhograf)
    ganhograf = ganhograf.rename(columns={ 0: 'Retorno da Estratégia 1'}) 
    ganhograf = ganhograf.set_index(combined3.index, inplace = False)
        
    ganhografteste = pd.DataFrame(ganhografteste)
    ganhografteste = ganhografteste.rename(columns={ 0: 'Retorno do Buy and Hold'}) 
    ganhografteste = ganhografteste.set_index(combined3.index, inplace = False)
    
    ganhos_combined = ganhograf.merge(ganhografteste, left_index = True, right_index = True).dropna()
    
    # Create some mock data
    t = ganhos_combined.index
    data1 = ganhos_combined['Retorno da Estratégia 1']
    data2 = ganhos_combined['Retorno do Buy and Hold']
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Retorno da Estratégia 1', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('Retorno do Buy and Hold', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    ax2.set(title='Retornos acumulados')
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    ganhografteste = ganhografteste.drop(ganhografteste.tail(1).index, inplace = False) # Dropei a linha adicionada  
    
    return fig

#Estratégia do acelerador

def sinal_acelerador(combined):
    #Combined é um dataframe com preços da ação e tendência do Google
    #Inverso é a opção de inverter (true or false) os sinais gerados
    
    #Começando pela leitura da base    
    tamanho_trends = len(combined)
    
    dados_trends = combined.iloc[:,0]
    dados_trends = pd.DataFrame(dados_trends)
    
    stocks = combined.iloc[:,1]
    stocks = pd.DataFrame(stocks)
    
    #Sinal do Trends
    
    somatorio = list(range(tamanho_trends))
    resultado = list(range(tamanho_trends))
    media_ = list(range(tamanho_trends))
        
    somatorio[0] = dados_trends.iloc[0,0]
    media_[0] = 0
    resultado[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio[i] = dados_trends.iloc[i,0] + somatorio[i-1]
        
    somatorio = pd.DataFrame(somatorio)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_[i] = somatorio.iloc[i,0]/(i+1)
    
    media_ = pd.DataFrame(media_)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado[i] = dados_trends.iloc[i,0] - media_.iloc[i-1,0]
        
    resultado = pd.DataFrame(resultado) #Sinal do Trends em resultado
    
    # Para stocks
    
    somatorio2 = list(range(tamanho_trends))
    resultado2 = list(range(tamanho_trends))
    media_2 = list(range(tamanho_trends))
        
    somatorio2[0] = stocks.iloc[0,0]
    media_2[0] = 0
    resultado2[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio2[i] = stocks.iloc[i,0] + somatorio2[i-1]
        
    somatorio2 = pd.DataFrame(somatorio2)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_2[i] = somatorio2.iloc[i,0]/(i+1)
    
    media_2 = pd.DataFrame(media_2)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado2[i] = stocks.iloc[i,0] - media_2.iloc[i-1,0]
        
    resultado2 = pd.DataFrame(resultado2) #Sinal dos preços em resultado2
    
    # Indicador
    
    ind = list(range(tamanho_trends))
                                           
    for i in range(1,tamanho_trends):                         #For para iterar as decisões diárias
        if resultado2.iloc[i,0]>0:                            #Se o preço da ação subiu...
            if resultado.iloc[i,0]>0:                         #Verificação de tendência com Trends
                ind[i] = "buy p(t+1); sell p(t+2) - LONG"
            else:
                ind[i] = "DO NOTHING"
        else:                                                 #Se o preço da ação caiu...
            if resultado.iloc[i,0]>0:
                ind[i] = "DO NOTHING"
            else:
                ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
    
            
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(dados_trends.index, inplace = False)
        
    return ind

# Função utilizando o volume de negociações como validador
## Se o volume de negociações sobe mais do que o desvpad, faz a estratégia do paper
## Use a função GET_YAHOO para imputar o "combined"
    
def sinal_volume1(combined, inverso):
    
    # Para o trends
    
    dados_trends = pd.DataFrame(combined.iloc[:,0])
    
    tamanho_trends = len(dados_trends)
    
    somatorio = list(range(tamanho_trends))
    resultado = list(range(tamanho_trends))
    media_ = list(range(tamanho_trends))
        
    somatorio[0] = dados_trends.iloc[0,0]
    media_[0] = 0
    resultado[0] = 0
    
    for i in range(1,tamanho_trends): # Soma os anteriores 
        somatorio[i] = dados_trends.iloc[i,0] + somatorio[i-1]
        
    somatorio = pd.DataFrame(somatorio)
    
    for i in range(tamanho_trends): # Faz a "média" dos anteriores (o i é de hoje)
        media_[i] = somatorio.iloc[i,0]/(i+1)
    
    media_ = pd.DataFrame(media_)
    
    for i in range(1,tamanho_trends): # Hoje - média anteriores 
        resultado[i] = dados_trends.iloc[i,0] - media_.iloc[i-1,0]
        
    resultado = pd.DataFrame(resultado)
    
    ind = list(range(tamanho_trends))
    
    # Volume de negociações
    
    volume = pd.DataFrame(combined.iloc[:,2])
    
    for i in range(len(volume)):
        if volume.iloc[i,0] == 0:
            volume.iloc[i,0] = volume.iloc[i-1,0]
    
    ret_vol = list(range(len(combined)))
    
    for i in range(1, len(combined)):
        ret_vol[i] = (volume.iloc[i,0]-volume.iloc[i-1,0])/volume.iloc[i-1,0]
        
    ret_vol = pd.DataFrame(ret_vol)
    
    desvpad = ret_vol.iloc[:,0].std()
    
    # Indicador
        
    for i in range(1,len(ret_vol)):
        if ret_vol.iloc[i,0]>desvpad:
            if inverso == False:
                if resultado.iloc[i,0]>0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG"          
            else:
                if resultado.iloc[i,0]<0:
                    ind[i] = "sell p(t+1); buy p(t+2) - SHORT"
                else:
                    ind[i] = "buy p(t+1); sell p(t+2) - LONG" 
        else:
            ind[i] = "DO NOTHING"
            
    ind = pd.DataFrame(ind)
    
    ind = ind.rename(columns={ 0: 'Estratégia'}) 
    
    ind = ind.set_index(dados_trends.index, inplace = False)
    
    return ind
        
    
