import apendice as ap
import matplotlib.pyplot as plt
import testzone as tz

# Plotando os sharp_test

combined = tz.combined

## Sinal 1

vector1 = ap.sharpe_test_1(combined = combined, tam_p = 0.1, qtde = 200, inverso = False)

plt.hist(vector1.iloc[:,0], bins = 40)
plt.ylabel('Quantas vezes')
plt.xlabel('Sharpe')
plt.title('Para o Sinal 1')
plt.show()

## Sinal 2

vector2 = ap.sharpe_test_2(combined = combined, tam_p = 0.1, qtde = 200, inverso = False)

plt.hist(vector2.iloc[:,0], bins = 40)
plt.ylabel('Quantas vezes')
plt.xlabel('Sharpe')
plt.title('Para o Sinal 2')
plt.show()

## Sinal 3

vector3 = ap.sharpe_test_3(combined = combined, tam_p = 0.1, qtde = 200, inverso = False, dias = 17)

plt.hist(vector3.iloc[:,0], bins = 40)
plt.ylabel('Quantas vezes')
plt.xlabel('Sharpe')
plt.title('Para o Sinal 3')
plt.show()

## Sinal 4

vector4 = ap.sharpe_test_4(combined = combined, tam_p = 0.1, qtde = 200, inverso = False, dias = 17)

plt.hist(vector4.iloc[:,0], bins = 40)
plt.ylabel('Quantas vezes')
plt.xlabel('Sharpe')
plt.title('Para o Sinal 4')
plt.show()

# Avaliando a normalização via correlação média
## Se quer ver a avaliação, insira 1

ap.av_corr_med(insert = 0)








