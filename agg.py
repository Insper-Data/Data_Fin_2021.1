import basic_func as insp
import strategy as strat 

def retorno_acumulado(inicio, palavra, ativo, sinal):
    startdate = inicio
    overlap = 45
    
    trends = insp.get_google(palavra, startdate, overlap)
    stocks = insp.alt_get_stocks(ativo)   
    combined = insp.join(trends = trends, stocks = stocks)  
    
    buyhold = strat.buy_hold(combined)  
    sinal_est = strat.sinal(combined = combined, inverso = False)
    
    ganhoestrat, combined2 = strat.strategy1(combined = combined, sinais = sinal_est)
    plim = strat.graphmat(ganhoestrat, buyhold, combined2)
    
    return plim


    
    

