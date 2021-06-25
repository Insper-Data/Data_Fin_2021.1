import random
import pandas as pd
from pytrends.request import TrendReq
from datetime import date, datetime
import math
import strategy as strat
import basic_func as bf
#import testzone as tz

#pytrends = TrendReq(hl='pt-BR', tz=360)
## Se for puxar algo do Trends, descomentar isso

# Fazendo resamples dos períodos e testando o sharpe
## Colocar o tamanho em porcentagem (ex: 10% do tamanho total da amostra)

def sharpe_test_1(combined, tam_p, qtde, inverso):
    
    # Para o sinal 1
    
    n = round(len(combined)*tam_p)
    vector1 = list(range(qtde))
    df = pd.DataFrame(range(n))
    
    combined['index'] = combined.index
    
    for i in range(qtde):
        
        ind = random.randint(1, len(combined)-n-2)
        
        df = df.assign(date = 0)
    
        for j in range(n):
            df.iloc[j,0] = combined.iloc[ind+j,0]
            df.iloc[j,1] = combined.iloc[ind+j,2]
            
        df.set_index("date", inplace = True)
            
        sin = strat.sinal1(combined = df, inverso = inverso)
        df_ = bf.join(df,sin)
        
        retorno = pd.DataFrame(range(n))
        
        for j in range(1,n):
            if df_.iloc[j,1] == "buy p(t+1); sell p(t+2) - LONG":
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+2,1] - combined.iloc[ind+j+1,1])/combined.iloc[ind+j+1,1]
            else:
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+1,1] - combined.iloc[ind+j+2,1])/combined.iloc[ind+j+2,1]
        
        retorno.drop(retorno.tail(1).index, inplace = True)    
        retorno.drop(retorno.tail(1).index, inplace = True)    
            
        vector1[i] = (retorno.iloc[:,0].mean()/retorno.iloc[:,0].std())*(252**(1/2))
    
    vector1 = pd.DataFrame(vector1)
    
    return vector1
    
def sharpe_test_2(combined, tam_p, qtde, inverso):
    
    # Para o sinal 2
    
    n = round(len(combined)*tam_p)
    vector2 = list(range(qtde))
    df = pd.DataFrame(range(n))
    
    combined['index'] = combined.index
    
    for i in range(qtde):
        
        ind = random.randint(1, len(combined)-n-2)
        
        df = df.assign(preco = 0)
        df = df.assign(date = 0)

        for j in range(n):
            df.iloc[j,0] = combined.iloc[ind+j,0]
            df.iloc[j,1] = combined.iloc[ind+j,1]
            df.iloc[j,2] = combined.iloc[ind+j,2]
            
        df.set_index("date", inplace = True)
            
        sin = strat.sinal2(combined = df, inverso = inverso)
        df_ = bf.join(df,sin)
        
        retorno = pd.DataFrame(range(n))
        
        for j in range(1,n):
            if df_.iloc[j,1] == "buy p(t+1); sell p(t+2) - LONG":
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+2,1] - combined.iloc[ind+j+1,1])/combined.iloc[ind+j+1,1]
            else:
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+1,1] - combined.iloc[ind+j+2,1])/combined.iloc[ind+j+2,1]
        
        retorno.drop(retorno.tail(1).index, inplace = True)    
        retorno.drop(retorno.tail(1).index, inplace = True)    
            
        vector2[i] = (retorno.iloc[:,0].mean()/retorno.iloc[:,0].std())*(252**(1/2))
    
    vector2 = pd.DataFrame(vector2)
    
    return vector2
    
def sharpe_test_3(combined, tam_p, qtde, dias, inverso):
    
    # Para o sinal 3
    
    n = round(len(combined)*tam_p)
    vector3 = list(range(qtde))
    df = pd.DataFrame(range(n))
    
    combined['index'] = combined.index
    
    for i in range(qtde):
        
        ind = random.randint(1, len(combined)-n-2)
        
        df = df.assign(preco = 0)
        df = df.assign(date = 0)

        for j in range(n):
            df.iloc[j,0] = combined.iloc[ind+j,0]
            df.iloc[j,1] = combined.iloc[ind+j,1]
            df.iloc[j,2] = combined.iloc[ind+j,2]
            
        df.set_index("date", inplace = True)
            
        sin = strat.sinal3(combined = df, inverso = inverso, dias = dias)
        df_ = bf.join(df,sin)
        
        retorno = pd.DataFrame(range(n))
        
        for j in range(1,n):
            if df_.iloc[j,1] == "buy p(t+1); sell p(t+2) - LONG":
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+2,1] - combined.iloc[ind+j+1,1])/combined.iloc[ind+j+1,1]
            else:
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+1,1] - combined.iloc[ind+j+2,1])/combined.iloc[ind+j+2,1]
        
        retorno.drop(retorno.tail(1).index, inplace = True)    
        retorno.drop(retorno.tail(1).index, inplace = True)    
            
        vector3[i] = (retorno.iloc[:,0].mean()/retorno.iloc[:,0].std())*(252**(1/2))
    
    vector3 = pd.DataFrame(vector3)
    
    return vector3
    
def sharpe_test_4(combined, tam_p, qtde, dias, inverso):
    
    # Para o sinal 4
    
    n = round(len(combined)*tam_p)
    vector4 = list(range(qtde))
    df = pd.DataFrame(range(n))
    
    combined['index'] = combined.index
    
    for i in range(qtde):
        
        ind = random.randint(1, len(combined)-n-2)
        
        df = df.assign(preco = 0)
        df = df.assign(date = 0)

        for j in range(n):
            df.iloc[j,0] = combined.iloc[ind+j,0]
            df.iloc[j,1] = combined.iloc[ind+j,1]
            df.iloc[j,2] = combined.iloc[ind+j,2]
            
        df.set_index("date", inplace = True)
            
        sin = strat.sinal4(combined = df, inverso = inverso, dias = dias)
        df_ = bf.join(df,sin)
        
        retorno = pd.DataFrame(range(n))
        
        for j in range(1,n):
            if df_.iloc[j,1] == "buy p(t+1); sell p(t+2) - LONG":
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+2,1] - combined.iloc[ind+j+1,1])/combined.iloc[ind+j+1,1]
            else:
                retorno.iloc[j-1,0] = (combined.iloc[ind+j+1,1] - combined.iloc[ind+j+2,1])/combined.iloc[ind+j+2,1]
        
        retorno.drop(retorno.tail(1).index, inplace = True)    
        retorno.drop(retorno.tail(1).index, inplace = True)    
            
        vector4[i] = (retorno.iloc[:,0].mean()/retorno.iloc[:,0].std())*(252**(1/2))
    
    vector4 = pd.DataFrame(vector4)
    
    return vector4

# Sharpe ajustado
    
def sharpe_aj(combined2):
    
    count = 0

    for i in range(len(combined2)):
        if combined2.iloc[i,2] == "buy p(t+1); sell p(t+2) - LONG":
            count = count + 1

    long_ratio = count/len(combined2)

    r = list(range(len(combined2)-1))
    
    for i in range(len(combined2)-1):
        r[i] = (combined2.iloc[i+1,1]-combined2.iloc[i,1])/combined2.iloc[i,1]

    r = pd.DataFrame(r)

    adj_sharpe = (-(1-long_ratio)*r.iloc[:,0].mean()+r.iloc[:,0].mean()*long_ratio)/r.iloc[:,0].std()

    adj_sharpe_anualizado = (252**(1/2))*adj_sharpe

    return adj_sharpe_anualizado

# Avaliar a normalização
## Via correlação média
    
def av_corr_med(insert):
    if insert == 1:
        palavra = tz.trends.columns[0]

        kw_list = [palavra]
        
        startdate = tz.inicio # Tem que inserir a data de início de novo
        
        # Pegando as datas

        hoje = date.today()
        startdate = datetime.strptime(startdate, '%Y-%m-%d').date()
        
        startord = startdate.toordinal()
        hojeord = hoje.toordinal()
        
        qtde_ = math.ceil((hojeord - startord)/269)
        
        datas_ = list(range(qtde_))
        
        for i in range(qtde_):
            if i < qtde_-1:
                end_ = startord + 267
                x_ = str(date.fromordinal(startord))
                y_ = str(date.fromordinal(end_))
                datas_[i] = x_ + " " + y_
                startord = startord + 268
            else:
                x_ = str(date.fromordinal(startord))
                y_ = str(hoje)
                datas_[i] = x_ + " " + y_
                            
            # Arrumar pros 7 dias depois
                    
        # Pegando as janelas sem normalizar
        
        sem_norm = list(range(qtde_))
        
        for i in range(qtde_):
            pytrends.build_payload(kw_list, cat=0, timeframe=datas_[i], geo='BR', gprop='')
            sem_norm[i] = pytrends.interest_over_time()
            sem_norm[i] = sem_norm[i].drop('isPartial', 1)
            
        # Concatenando as janelas de forma não normalizada
            
        comb_sem = sem_norm[0]
        
        for i in range(qtde_-1):
            comb_sem = pd.concat([comb_sem, sem_norm[i+1]])
            
        comb_sem = pd.DataFrame(comb_sem)
        
        # Combinando as janelas não normalizadas com aquelas normalizadas
        
        comb_ = tz.trends.merge(comb_sem, on = 'date', how = 'left').dropna()
        
        colunas_comb_ = list(comb_.columns)  
        
        comb_ = comb_.rename(columns={ colunas_comb_[0]: 'Overlapping', colunas_comb_[1]:'Original'}) 
        
        # Índice de correlação
        
        comeco = 0
        
        correla = list(range(qtde_-1))
        
        for i in range(qtde_-1):
            fim = comeco + 266
            correla[i] = comb_.iloc[comeco:fim,0].corr(comb_.iloc[comeco:fim,1])
            comeco = comeco + 267
            
        correla = pd.DataFrame(correla)
        
        print(correla)
        print(correla.mean())
        
                    
