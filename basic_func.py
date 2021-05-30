import pandas as pd
import yfinance as yf
from pandas import DataFrame
from pytrends.request import TrendReq
from datetime import date, datetime
import math

pytrends = TrendReq(hl='pt-BR', tz=360)

# Função Google Trends Daily Data

def get_datas(startdate, overlap):
    
    #Datas
    hoje = date.today()
    startdate = datetime.strptime(startdate, '%Y-%m-%d').date()

    startord = startdate.toordinal()
    hojeord = hoje.toordinal()

    qtde = math.floor(((hojeord-startord)-overlap-(268-overlap))/(268-overlap)+2)

    datas = list(range(qtde))

    for i in range(qtde):
        if i < qtde-1:
            end = startord + 267
            x = str(date.fromordinal(startord))
            y = str(date.fromordinal(end))
            datas[i] = x + ' ' + y
            startord = startord + 268 - overlap
        else:
            x = str(date.fromordinal(startord))
            y = str(hoje)
            datas[i] = x + ' ' + y
            
    return datas, qtde


def get_google(palavra, startdate, overlap):
    
    #Datas
    datas, qtde = get_datas(startdate, overlap)
    
    #Obter dados do pytrends
    kw_list = [palavra]
    dataframes = list(range(qtde))
    for i in range(qtde):
        pytrends.build_payload(kw_list, cat=0, timeframe = datas[i] , geo='BR', gprop='')
        dataframes[i] = pytrends.interest_over_time()
    
    #Padronização dos dataframes
    mult = list(range(qtde-1))
    newdf = dataframes

    for i in range(qtde-1):
        x = newdf[i+1]
        y = newdf[i]
        mult[i] = y.iloc[-overlap:, 0].max()/x.iloc[0:overlap-1, 0].max()
        newdf[i+1] = newdf[i+1]*mult[i]
        
    #Unindo os dataframes
    for i in range(qtde-1):
        if i < qtde:
            newdf[i].drop(newdf[i].tail(overlap).index, inplace = True)
            
    superdf_ = newdf[0]

    for i in range(qtde-1):
        superdf_ = pd.concat([superdf_, newdf[i+1]])

    superdf_ = superdf_.drop("isPartial", 1)
    
    maximo = superdf_.iloc[:,0].max()

    superdf = list(range(len(superdf_)))

    superdf = pd.DataFrame(superdf)

    for i in range(len(superdf_)):
        superdf.iloc[i,0] = superdf_.iloc[i,0]*100/maximo

    superdf = superdf.set_index(superdf_.index, inplace = False)

    superdf = superdf.rename(columns={ 0: palavra})
    
    return superdf
   
### Função Dados Financeiros

df_fin = pd.read_excel("dados fin.xlsx")
df_assets = pd.DataFrame(df_fin.iloc[0,:].dropna())

#%%
def get_stocks(ativo):
        
    search = df_assets[df_assets.index.str.contains(ativo.upper())]
    search.reset_index()
    display(search)

    indice = int(input("Digite a posição (nº) do ativo desejado: "))
    ticker = search.index[indice]
    
    df_fin1 = df_fin.drop(0) #Tira a segunda linha do df

    index_column = df_fin1.columns.get_loc(ticker) #Pega a localização do ticker escolhido

    time = pd.DataFrame(df_fin1[ticker].dropna()) #Pega as datas do ticker

    price = pd.DataFrame(df_fin1.iloc[:,index_column + 1].dropna()) # Pega os preços dos tickers

    time_price = pd.concat([time, price], axis = 1) #Junta as datas com os preços

    colunas = list(time_price.columns) #Nome da coluna 

    time_price = time_price.rename(columns={ colunas[0]: 'date', colunas[1]: 'Price'}) #Muda o nome da coluna
    time_price['date'] = pd.to_datetime(time_price['date']) #Arrumando a data
    time_price = time_price.set_index('date')

    return time_price

def alt_get_stocks(ativo):
     
    search = df_assets[df_assets.index.str.contains(ativo)]
    search.reset_index()
    indice = 0
    ticker = search.index[indice]
        
    df_fin1 = df_fin.drop(0) #Tira a segunda linha do df

    index_column = df_fin1.columns.get_loc(ticker) #Pega a localização do ticker escolhido

    time = pd.DataFrame(df_fin1[ticker].dropna()) #Pega as datas do ticker

    price = pd.DataFrame(df_fin1.iloc[:,index_column + 1].dropna()) #Pega os preços dos tickers

    time_price = pd.concat([time, price], axis = 1) #Junta as datas com os preços

    colunas = list(time_price.columns) #Nome da coluna 

    time_price = time_price.rename(columns={ colunas[0]: 'date', colunas[1]: 'Price'}) #Muda o nome da coluna
    time_price['date'] = pd.to_datetime(time_price['date']) #Arrumando a data
    time_price = time_price.set_index('date')

    return time_price

def get_yahoo(ticker_name):
    stock = yf.Ticker(ticker_name)
    
    hist = stock.history(period="max")
    hist = hist.drop(columns = ['Open','High', 'Low', 'Dividends', 'Stock Splits'])
    hist = hist.rename_axis('date')
    
    yahoodf = DataFrame(hist)
    
    return yahoodf

def join(trends, stocks):
    combined = trends.merge(stocks, on = 'date', how = 'right').dropna()

    colunas_comb = list(combined.columns) #Nome da coluna 

    combined = combined.rename(columns={colunas_comb[0]: 'Pesquisas'}) #Muda o nome da coluna
    
    return combined

def retorno(time_price):
    preço = list(range(len(time_price))) 
    for i in range(len(time_price)):
        preço[i]=time_price.iloc[i, 0]

    retorno = list(range(len(preço)-1))
    for i in range(1,len(preço)-1):
        retorno[i]= (preço[i]-preço[i-1])/preço[i-1]
    
    return retorno

def sharpe_aa(dados):
    dados = pd.DataFrame(dados)
    dados = dados.drop(0)
    
    r = list(range(len(dados)-1))
    
    for i in range(len(dados)-1):
        r[i] = (dados.iloc[i+1,0]-dados.iloc[i,0])/dados.iloc[i,0]
    
    r = pd.DataFrame(r)
    
    sharpe = r.iloc[:,0].mean()/r.iloc[:,0].std()
    sharpe_anualizado = (252**(1/2))*sharpe
    
    return sharpe_anualizado



