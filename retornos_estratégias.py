# Testando os ativos para as palavras selecionadas

import pandas as pd
import basic_func as bf
import strategy as strat 

#%% Ajeitando

inicio = '2016-01-02'

words = ["abev3", "ações", "alimentos", "ambev", "b3", "bacen", "banco", "bbdc4",
         "bitcoin", "bolsa", "bradesco", "bvsp", "cerveja", "commodity", "cor", 
         "corretora", "credito", "crise", "derivativos", "desemprego", "dinheiro",
         "divida", "dividendos", "dolar", "economia", "empresa", "estagio", "ferro",
         "financas", "fundos", "gado", "gasolina", "ibovespa", "inflacao", "investimento",
         "investir", "itau", "itub4", "jbs", "jbss3", "magazine", "mercado", "mglu3",
         "mineraca", "petr4", "petrobras", "petroleo", "politica", "portifolio", 
         "renda", "restaurante", "selic", "titulos", "vale", "vale3", "viajar",
         "vvar3", "xp"]

ativos = ["PETR4 BS Equity", "VALE3 BS Equity", "BBDC4 BS Equity", "ITUB4 BS Equity",
          "MGLU3 BS Equity", "B3SA3 BS Equity", "VVAR3 BS Equity", "JBSS3 BS Equity",
          "ABEV3 BS Equity", "BVSP"]
  
# Estratégia 1: Quantifying Trading Behaviour

## Inverso = False

retornos_petr4 = list()
retornos_vale3 = list()
retornos_bbdc4 = list()
retornos_itub4 = list()
retornos_mglu3 = list()
retornos_b3sa3 = list()
retornos_vvar3 = list()
retornos_jbss3 = list()
retornos_abev3 = list()
retornos_bvsp = list()

lista_retornos = [retornos_petr4, retornos_vale3, retornos_bbdc4, retornos_itub4,
                  retornos_mglu3, retornos_b3sa3, retornos_vvar3, retornos_jbss3,
                  retornos_abev3, retornos_bvsp]

sharpe_petr4 = list()
sharpe_vale3 = list()
sharpe_bbdc4 = list()
sharpe_itub4 = list()
sharpe_mglu3 = list()
sharpe_b3sa3 = list()
sharpe_vvar3 = list()
sharpe_jbss3 = list()
sharpe_abev3 = list()
sharpe_bvsp = list()

lista_sharpe = [sharpe_petr4, sharpe_vale3, sharpe_bbdc4, sharpe_itub4,
                  sharpe_mglu3, sharpe_b3sa3, sharpe_vvar3, sharpe_jbss3,
                  sharpe_abev3, sharpe_bvsp]

## Inverso = True

retornos_petr4_t = list()
retornos_vale3_t = list()
retornos_bbdc4_t = list()
retornos_itub4_t = list()
retornos_mglu3_t = list()
retornos_b3sa3_t = list()
retornos_vvar3_t = list()
retornos_jbss3_t = list()
retornos_abev3_t = list()
retornos_bvsp_t = list()

lista_retornos_t = [retornos_petr4_t, retornos_vale3_t, retornos_bbdc4_t, retornos_itub4_t,
                  retornos_mglu3_t, retornos_b3sa3_t, retornos_vvar3_t, retornos_jbss3_t,
                  retornos_abev3_t, retornos_bvsp_t]

sharpe_petr4_t = list()
sharpe_vale3_t = list()
sharpe_bbdc4_t = list()
sharpe_itub4_t = list()
sharpe_mglu3_t = list()
sharpe_b3sa3_t = list()
sharpe_vvar3_t = list()
sharpe_jbss3_t = list()
sharpe_abev3_t = list()
sharpe_bvsp_t = list()

lista_sharpe_t = [sharpe_petr4_t, sharpe_vale3_t, sharpe_bbdc4_t, sharpe_itub4_t,
                  sharpe_mglu3_t, sharpe_b3sa3_t, sharpe_vvar3_t, sharpe_jbss3_t,
                  sharpe_abev3_t, sharpe_bvsp_t]

# Estratégia 2: Híbrido

## Inverso = False

retornos_petr4_2 = list()
retornos_vale3_2 = list()
retornos_bbdc4_2 = list()
retornos_itub4_2 = list()
retornos_mglu3_2 = list()
retornos_b3sa3_2 = list()
retornos_vvar3_2 = list()
retornos_jbss3_2 = list()
retornos_abev3_2 = list()
retornos_bvsp_2 = list()

lista_retornos_2 = [retornos_petr4_2, retornos_vale3_2, retornos_bbdc4_2, retornos_itub4_2,
                  retornos_mglu3_2, retornos_b3sa3_2, retornos_vvar3_2, retornos_jbss3_2,
                  retornos_abev3_2, retornos_bvsp_2]

sharpe_petr4_2 = list()
sharpe_vale3_2 = list()
sharpe_bbdc4_2 = list()
sharpe_itub4_2 = list()
sharpe_mglu3_2 = list()
sharpe_b3sa3_2 = list()
sharpe_vvar3_2 = list()
sharpe_jbss3_2 = list()
sharpe_abev3_2 = list()
sharpe_bvsp_2 = list()

lista_sharpe_2 = [sharpe_petr4_2, sharpe_vale3_2, sharpe_bbdc4_2, sharpe_itub4_2,
                  sharpe_mglu3_2, sharpe_b3sa3_2, sharpe_vvar3_2, sharpe_jbss3_2,
                  sharpe_abev3_2, sharpe_bvsp_2]

## Inverso = True

retornos_petr4_2t = list()
retornos_vale3_2t = list()
retornos_bbdc4_2t = list()
retornos_itub4_2t = list()
retornos_mglu3_2t = list()
retornos_b3sa3_2t = list()
retornos_vvar3_2t = list()
retornos_jbss3_2t = list()
retornos_abev3_2t = list()
retornos_bvsp_2t = list()

lista_retornos_2t = [retornos_petr4_2t, retornos_vale3_2t, retornos_bbdc4_2t, retornos_itub4_2t,
                  retornos_mglu3_2t, retornos_b3sa3_2t, retornos_vvar3_2t, retornos_jbss3_2t,
                  retornos_abev3_2t, retornos_bvsp_2t]

sharpe_petr4_2t = list()
sharpe_vale3_2t = list()
sharpe_bbdc4_2t = list()
sharpe_itub4_2t = list()
sharpe_mglu3_2t = list()
sharpe_b3sa3_2t = list()
sharpe_vvar3_2t = list()
sharpe_jbss3_2t = list()
sharpe_abev3_2t = list()
sharpe_bvsp_2t = list()

lista_sharpe_2t = [sharpe_petr4_2t, sharpe_vale3_2t, sharpe_bbdc4_2t, sharpe_itub4_2t,
                  sharpe_mglu3_2t, sharpe_b3sa3_2t, sharpe_vvar3_2t, sharpe_jbss3_2t,
                  sharpe_abev3_2t, sharpe_bvsp_2t]


# Estratégia 3: Médias Móveis (21 dias)

## Inverso = False

retornos_petr4_3 = list()
retornos_vale3_3 = list()
retornos_bbdc4_3 = list()
retornos_itub4_3 = list()
retornos_mglu3_3 = list()
retornos_b3sa3_3 = list()
retornos_vvar3_3 = list()
retornos_jbss3_3 = list()
retornos_abev3_3 = list()
retornos_bvsp_3= list()

lista_retornos_3 = [retornos_petr4_3, retornos_vale3_3, retornos_bbdc4_3, retornos_itub4_3,
                  retornos_mglu3_3, retornos_b3sa3_3, retornos_vvar3_3, retornos_jbss3_3,
                  retornos_abev3_3, retornos_bvsp_3]

sharpe_petr4_3 = list()
sharpe_vale3_3 = list()
sharpe_bbdc4_3 = list()
sharpe_itub4_3 = list()
sharpe_mglu3_3 = list()
sharpe_b3sa3_3 = list()
sharpe_vvar3_3 = list()
sharpe_jbss3_3 = list()
sharpe_abev3_3 = list()
sharpe_bvsp_3 = list()

lista_sharpe_3 = [sharpe_petr4_3, sharpe_vale3_3, sharpe_bbdc4_3, sharpe_itub4_3,
                  sharpe_mglu3_3, sharpe_b3sa3_3, sharpe_vvar3_3, sharpe_jbss3_3,
                  sharpe_abev3_3, sharpe_bvsp_3]


## Inverso = True

retornos_petr4_3t = list()
retornos_vale3_3t = list()
retornos_bbdc4_3t = list()
retornos_itub4_3t = list()
retornos_mglu3_3t = list()
retornos_b3sa3_3t = list()
retornos_vvar3_3t = list()
retornos_jbss3_3t = list()
retornos_abev3_3t = list()
retornos_bvsp_3t = list()

lista_retornos_3t = [retornos_petr4_3t, retornos_vale3_3t, retornos_bbdc4_3t, retornos_itub4_3t,
                  retornos_mglu3_3t, retornos_b3sa3_3t, retornos_vvar3_3t, retornos_jbss3_3t,
                  retornos_abev3_3t, retornos_bvsp_3t]

sharpe_petr4_3t = list()
sharpe_vale3_3t = list()
sharpe_bbdc4_3t = list()
sharpe_itub4_3t = list()
sharpe_mglu3_3t = list()
sharpe_b3sa3_3t = list()
sharpe_vvar3_3t = list()
sharpe_jbss3_3t = list()
sharpe_abev3_3t = list()
sharpe_bvsp_3t = list()

lista_sharpe_3t = [sharpe_petr4_3t, sharpe_vale3_3t, sharpe_bbdc4_3t, sharpe_itub4_3t,
                  sharpe_mglu3_3t, sharpe_b3sa3_3t, sharpe_vvar3_3t, sharpe_jbss3_3t,
                  sharpe_abev3_3t, sharpe_bvsp_3t]

# Estratégia 4: Médias Móveis para preços e pesquisas (21 dias)

## Inverso = False

retornos_petr4_4 = list()
retornos_vale3_4 = list()
retornos_bbdc4_4 = list()
retornos_itub4_4 = list()
retornos_mglu3_4 = list()
retornos_b3sa3_4 = list()
retornos_vvar3_4 = list()
retornos_jbss3_4 = list()
retornos_abev3_4 = list()
retornos_bvsp_4 = list()

lista_retornos_4 = [retornos_petr4_4, retornos_vale3_4, retornos_bbdc4_4, retornos_itub4_4,
                  retornos_mglu3_4, retornos_b3sa3_4, retornos_vvar3_4, retornos_jbss3_4,
                  retornos_abev3_4, retornos_bvsp_4]

sharpe_petr4_4 = list()
sharpe_vale3_4 = list()
sharpe_bbdc4_4 = list()
sharpe_itub4_4 = list()
sharpe_mglu3_4 = list()
sharpe_b3sa3_4 = list()
sharpe_vvar3_4 = list()
sharpe_jbss3_4 = list()
sharpe_abev3_4 = list()
sharpe_bvsp_4 = list()

lista_sharpe_4 = [sharpe_petr4_4, sharpe_vale3_4, sharpe_bbdc4_4, sharpe_itub4_4,
                  sharpe_mglu3_4, sharpe_b3sa3_4, sharpe_vvar3_4, sharpe_jbss3_4,
                  sharpe_abev3_4, sharpe_bvsp_4]

## Inverso = True

retornos_petr4_4t = list()
retornos_vale3_4t = list()
retornos_bbdc4_4t = list()
retornos_itub4_4t = list()
retornos_mglu3_4t = list()
retornos_b3sa3_4t = list()
retornos_vvar3_4t = list()
retornos_jbss3_4t = list()
retornos_abev3_4t = list()
retornos_bvsp_4t = list()

lista_retornos_4t = [retornos_petr4_4t, retornos_vale3_4t, retornos_bbdc4_4t, retornos_itub4_4t,
                  retornos_mglu3_4t, retornos_b3sa3_4t, retornos_vvar3_4t, retornos_jbss3_4t,
                  retornos_abev3_4t, retornos_bvsp_4t]

sharpe_petr4_4t = list()
sharpe_vale3_4t = list()
sharpe_bbdc4_4t = list()
sharpe_itub4_4t = list()
sharpe_mglu3_4t = list()
sharpe_b3sa3_4t = list()
sharpe_vvar3_4t = list()
sharpe_jbss3_4t = list()
sharpe_abev3_4t = list()
sharpe_bvsp_4t = list()

lista_sharpe_4t = [sharpe_petr4_4t, sharpe_vale3_4t, sharpe_bbdc4_4t, sharpe_itub4_4t,
                  sharpe_mglu3_4t, sharpe_b3sa3_4t, sharpe_vvar3_4t, sharpe_jbss3_4t,
                  sharpe_abev3_4t, sharpe_bvsp_4t]

# Estratégia 5: Acelerador para verificar tendência

retornos_petr4_5 = list()
retornos_vale3_5 = list()
retornos_bbdc4_5 = list()
retornos_itub4_5 = list()
retornos_mglu3_5 = list()
retornos_b3sa3_5 = list()
retornos_vvar3_5 = list()
retornos_jbss3_5 = list()
retornos_abev3_5 = list()
retornos_bvsp_5 = list()

lista_retornos_5 = [retornos_petr4_5, retornos_vale3_5, retornos_bbdc4_5, retornos_itub4_5,
                  retornos_mglu3_5, retornos_b3sa3_5, retornos_vvar3_5, retornos_jbss3_5,
                  retornos_abev3_5, retornos_bvsp_5]

sharpe_petr4_5 = list()
sharpe_vale3_5 = list()
sharpe_bbdc4_5 = list()
sharpe_itub4_5 = list()
sharpe_mglu3_5 = list()
sharpe_b3sa3_5 = list()
sharpe_vvar3_5 = list()
sharpe_jbss3_5 = list()
sharpe_abev3_5 = list()
sharpe_bvsp_5 = list()

lista_sharpe_5 = [sharpe_petr4_5, sharpe_vale3_5, sharpe_bbdc4_5, sharpe_itub4_5,
                  sharpe_mglu3_5, sharpe_b3sa3_5, sharpe_vvar3_5, sharpe_jbss3_5,
                  sharpe_abev3_5, sharpe_bvsp_5]


#%% Fazendo as estratégias

for i in range(len(lista_retornos)):
    
    for j in range(len(words)):
        
        word = words[j]
        trends = pd.read_excel(f'Dados/{word}.xlsx')
        trends = trends.set_index('date')
        
        ativo = ativos[i]
        stocks = bf.alt_get_stocks(ativo = ativo)
    
        combined = bf.join(trends = trends, stocks = stocks)
                
        # Estratégia 1
        
        ## Inverso = False
        
        sinal_est1 = strat.sinal1(combined = combined, inverso = False)
    
        ganhoestrat, combined2 = strat.gen_return_sep(combined = combined, 
                                                      sinais = sinal_est1)
    
        lista_retornos[i].append(ganhoestrat[-1])
        
        sharpe = bf.sharpe_aa(ganhoestrat)
        lista_sharpe[i].append(sharpe)
        
        ## Inverso = True
        
        sinal_est1_t = strat.sinal1(combined =  combined, inverso = True)
        
        ganhoestrat_t, combined2 = strat.gen_return_sep(combined = combined, 
                                                      sinais = sinal_est1_t)
    
        lista_retornos_t[i].append(ganhoestrat_t[-1])
        
        sharpe_t = bf.sharpe_aa(ganhoestrat_t)
        lista_sharpe_t[i].append(sharpe_t)
        
        # Estratégia 2
        
        ## Inverso = False
        
        sinal_est2 = strat.sinal2(combined = combined, inverso = False)

        ganhoestrat_2, combined2_2 = strat.gen_return_sep(combined = combined, 
                                                            sinais = sinal_est2)
        
        lista_retornos_2[i].append(ganhoestrat_2[-1])
        
        sharpe_2 = bf.sharpe_aa(ganhoestrat_2)
        lista_sharpe_2[i].append(sharpe_2)
        
        ## Inverso = True
        
        sinal_est2t = strat.sinal2(combined = combined, inverso = True)

        ganhoestrat_2t, combined2_2t = strat.gen_return_sep(combined = combined, 
                                                            sinais = sinal_est2t)
        
        lista_retornos_2t[i].append(ganhoestrat_2t[-1])
        
        sharpe_2t = bf.sharpe_aa(ganhoestrat_2t)
        lista_sharpe_2t[i].append(sharpe_2t)
        
        # Estratégia 3
        
        ## Inverso = False
        
        sinal_est3 = strat.sinal3(combined = combined, inverso = False, dias = 21)

        ganhoestrat_3, combined2_3 = strat.gen_return_sep(combined = combined, 
                                                        sinais = sinal_est3)
        
        lista_retornos_3[i].append(ganhoestrat_3[-1])
        
        sharpe_3 = bf.sharpe_aa(ganhoestrat_3)
        lista_sharpe_3[i].append(sharpe_3)
        
        # Inverso = True
        
        sinal_est3t = strat.sinal3(combined = combined, inverso = True, dias = 21)

        ganhoestrat_3t, combined2_3t = strat.gen_return_sep(combined = combined, 
                                                        sinais = sinal_est3t)
        
        lista_retornos_3t[i].append(ganhoestrat_3t[-1])
        
        sharpe_3t = bf.sharpe_aa(ganhoestrat_3t)
        lista_sharpe_3t[i].append(sharpe_3t)
        
        # Estratégia 4
        
        ## Inverso = False
        
        sinal_est4 = strat.sinal4(combined = combined, inverso = False, dias = 21)

        ganhoestrat_4, combined2_4 = strat.gen_return_sep(combined = combined, 
                                                          sinais = sinal_est4)
        
        lista_retornos_4[i].append(ganhoestrat_4[-1])
        
        sharpe_4 = bf.sharpe_aa(ganhoestrat_4)
        lista_sharpe_4[i].append(sharpe_4)
        
        ## Inverso = True
        
        sinal_est4t = strat.sinal4(combined = combined, inverso = True, dias = 21)

        ganhoestrat_4t, combined2_4t = strat.gen_return_sep(combined = combined, 
                                                          sinais = sinal_est4t)
        
        lista_retornos_4t[i].append(ganhoestrat_4t[-1])
        
        sharpe_4t = bf.sharpe_aa(ganhoestrat_4t)
        lista_sharpe_4t[i].append(sharpe_4t)

        # Estratégia 5
        
        sinal_est5 = strat.sinal_acelerador(combined = combined)

        ganhoestrat_5, combined3 = strat.gen_return_edit(combined = combined, 
                                                        sinais = sinal_est5)
        
        lista_retornos_5[i].append(ganhoestrat_5[-1])
        
        sharpe_5 = bf.sharpe_aa(ganhoestrat_5)
        lista_sharpe_5[i].append(sharpe_5)
      