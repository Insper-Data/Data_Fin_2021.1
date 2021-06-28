# Passando os resultados para o Excel

import pandas as pd

# Retorno

df = pd.DataFrame(lista_retornos)
writer = pd.ExcelWriter('1F.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()

df2 = pd.DataFrame(lista_retornos_t)
writer = pd.ExcelWriter('1T.xlsx', engine='xlsxwriter')
df2.to_excel(writer)
writer.save()

df3 = pd.DataFrame(lista_retornos_2)
writer = pd.ExcelWriter('2F.xlsx', engine='xlsxwriter')
df3.to_excel(writer)
writer.save()

df4 = pd.DataFrame(lista_retornos_2t)
writer = pd.ExcelWriter('2T.xlsx', engine='xlsxwriter')
df4.to_excel(writer)
writer.save()

df5 = pd.DataFrame(lista_retornos_3)
writer = pd.ExcelWriter('3F.xlsx', engine='xlsxwriter')
df5.to_excel(writer)
writer.save()

df6 = pd.DataFrame(lista_retornos_3t)
writer = pd.ExcelWriter('3T.xlsx', engine='xlsxwriter')
df6.to_excel(writer)
writer.save()

df7 = pd.DataFrame(lista_retornos_4)
writer = pd.ExcelWriter('4F.xlsx', engine='xlsxwriter')
df4.to_excel(writer)
writer.save()

df8 = pd.DataFrame(lista_retornos_4t)
writer = pd.ExcelWriter('4T.xlsx', engine='xlsxwriter')
df8.to_excel(writer)
writer.save()

df9 = pd.DataFrame(lista_retornos_5)
writer = pd.ExcelWriter('5.xlsx', engine='xlsxwriter')
df9.to_excel(writer)
writer.save()

# Sharpe

df = pd.DataFrame(lista_sharpe)
writer = pd.ExcelWriter('s1T.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()

df2 = pd.DataFrame(lista_sharpe_t)
writer = pd.ExcelWriter('s1F.xlsx', engine='xlsxwriter')
df2.to_excel(writer)
writer.save()

df3 = pd.DataFrame(lista_sharpe_2)
writer = pd.ExcelWriter('s2F.xlsx', engine='xlsxwriter')
df3.to_excel(writer)
writer.save()

df4 = pd.DataFrame(lista_sharpe_2t)
writer = pd.ExcelWriter('s2T.xlsx', engine='xlsxwriter')
df4.to_excel(writer)
writer.save()

df5 = pd.DataFrame(lista_sharpe_3)
writer = pd.ExcelWriter('s3F.xlsx', engine='xlsxwriter')
df5.to_excel(writer)
writer.save()

df6 = pd.DataFrame(lista_sharpe_3t)
writer = pd.ExcelWriter('s3T.xlsx', engine='xlsxwriter')
df6.to_excel(writer)
writer.save()

df7 = pd.DataFrame(lista_sharpe_4)
writer = pd.ExcelWriter('s4F.xlsx', engine='xlsxwriter')
df4.to_excel(writer)
writer.save()

df8 = pd.DataFrame(lista_sharpe_4t)
writer = pd.ExcelWriter('s4T.xlsx', engine='xlsxwriter')
df8.to_excel(writer)
writer.save()

df9 = pd.DataFrame(lista_sharpe_5)
writer = pd.ExcelWriter('s5.xlsx', engine='xlsxwriter')
df9.to_excel(writer)
writer.save()