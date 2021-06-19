import basic_func as bf

## Puxando a palavra do GT

inicio = '2016-01-01'

# Ativos
petrobras = bf.get_google(palavra = "petrobras", startdate = inicio, overlap = 45)
petr4 = bf.get_google(palavra = "petr4", startdate = inicio, overlap = 45)

vale = bf.get_google(palavra = "vale", startdate = inicio, overlap = 45)
vale3 = bf.get_google(palavra = "vale3", startdate = inicio, overlap = 45)

bradesco = bf.get_google(palavra = "bradesco", startdate = inicio, overlap = 45)
bbdc4 = bf.get_google(palavra = "bbdc4", startdate = inicio, overlap = 45)

itau = bf.get_google(palavra = "itau", startdate = inicio, overlap = 45)
itub4 = bf.get_google(palavra = "itub4", startdate = inicio, overlap = 45)

magazine = bf.get_google(palavra = "magazine", startdate = inicio, overlap = 45)
mglu3 = bf.get_google(palavra = "mglu3", startdate = inicio, overlap = 45)

b3 = bf.get_google(palavra = "b3", startdate = inicio, overlap = 45)
b3sa3 = bf.get_google(palavra = "b3sa3", startdate = inicio, overlap = 45)

varejo = bf.get_google(palavra = "varejo", startdate = inicio, overlap = 45)
vvar3 = bf.get_google(palavra = "vvar3", startdate = inicio, overlap = 45)

jbs = bf.get_google(palavra = "jbs", startdate = inicio, overlap = 45)
jbss3 = bf.get_google(palavra = "jbss3", startdate = inicio, overlap = 45)

ambev = bf.get_google(palavra = "ambev", startdate = inicio, overlap = 45)
abev3 = bf.get_google(palavra = "abev3", startdate = inicio, overlap = 45)

ibovespa = bf.get_google(palavra = "ibovespa", startdate = inicio, overlap = 45)
bvsp = bf.get_google(palavra = "bvsp", startdate = inicio, overlap = 45)

# Palavras do paper
divida = bf.get_google(palavra = "divida", startdate = inicio, overlap = 45)

cor = bf.get_google(palavra = "cor", startdate = inicio, overlap = 45)

ações = bf.get_google(palavra = "ações", startdate = inicio, overlap = 45)

restaurante = bf.get_google(palavra = "restaurante", startdate = inicio, overlap = 45)

portifolio = bf.get_google(palavra = "portifolio", startdate = inicio, overlap = 45)

inflacao = bf.get_google(palavra = "inflacao", startdate = inicio, overlap = 45)

economia = bf.get_google(palavra = "economia", startdate = inicio, overlap = 45)

credito = bf.get_google(palavra = "credito", startdate = inicio, overlap = 45)

mercado = bf.get_google(palavra = "mercado", startdate = inicio, overlap = 45)

desemprego = bf.get_google(palavra = "desemprego", startdate = inicio, overlap = 45)

dinheiro = bf.get_google(palavra = "dinheiro", startdate = inicio, overlap = 45)

investimento = bf.get_google(palavra = "investimento", startdate = inicio, overlap = 45)

titulos = bf.get_google(palavra = "titulos", startdate = inicio, overlap = 45)

derivativos = bf.get_google(palavra = "derivativos", startdate = inicio, overlap = 45)

financeiro = bf.get_google(palavra = "financeiro", startdate = inicio, overlap = 45)

crise = bf.get_google(palavra = "crise", startdate = inicio, overlap = 45)

financas = bf.get_google(palavra = "financas", startdate = inicio, overlap = 45)

viajar = bf.get_google(palavra = "viajar", startdate = inicio, overlap = 45)

petroleo = bf.get_google(palavra = "petroleo", startdate = inicio, overlap = 45)

politica = bf.get_google(palavra = "politica", startdate = inicio, overlap = 45)

dividendos = bf.get_google(palavra = "dividendos", startdate = inicio, overlap = 45)

# Palavras proprias
fundos = bf.get_google(palavra = "fundos", startdate = inicio, overlap = 45)

xp = bf.get_google(palavra = "xp", startdate = inicio, overlap = 45)

corretora = bf.get_google(palavra = "corretora", startdate = inicio, overlap = 45)

empresa = bf.get_google(palavra = "empresa", startdate = inicio, overlap = 45)

investir = bf.get_google(palavra = "investir", startdate = inicio, overlap = 45)

bitcoin = bf.get_google(palavra = "bitcoin", startdate = inicio, overlap = 45)

renda = bf.get_google(palavra = "renda", startdate = inicio, overlap = 45)

dolar = bf.get_google(palavra = "dolar", startdate = inicio, overlap = 45)

gasolina = bf.get_google(palavra = "gasolina", startdate = inicio, overlap = 45)

mineracao = bf.get_google(palavra = "mineracao", startdate = inicio, overlap = 45)

ferro = bf.get_google(palavra = "ferro", startdate = inicio, overlap = 45)

banco = bf.get_google(palavra = "banco", startdate = inicio, overlap = 45)

bolsa = bf.get_google(palavra = "bolsa", startdate = inicio, overlap = 45)

selic = bf.get_google(palavra = "selic", startdate = inicio, overlap = 45)

bacen = bf.get_google(palavra = "bacen", startdate = inicio, overlap = 45)

alimentos = bf.get_google(palavra = "alimentos", startdate = inicio, overlap = 45)

gado = bf.get_google(palavra = "gado", startdate = inicio, overlap = 45)

commodity = bf.get_google(palavra = "commodity", startdate = inicio, overlap = 45)

cerveja = bf.get_google(palavra = "cerveja", startdate = inicio, overlap = 45)

estagio = bf.get_google(palavra = "estagio", startdate = inicio, overlap = 45)

## Passando as listas para o excel
abev3.to_excel("abev3.xlsx")
alimentos.to_excel("alimentos.xlsx")
ambev.to_excel("ambev.xlsx")
ações.to_excel("ações.xlsx")
b3.to_excel("b3.xlsx")
bacen.to_excel("bacen.xlsx")
banco.to_excel("banco.xlsx")
bbdc4.to_excel("bbdc4.xlsx")
bitcoin.to_excel("bitcoin.xlsx")
bolsa.to_excel("bolsa.xlsx")
bradesco.to_excel("bradesco.xlsx")
bvsp.to_excel("bvsp.xlsx")
cerveja.to_excel("cerveja.xlsx")
commodity.to_excel("commodity.xlsx")
cor.to_excel("cor.xlsx")
corretora.to_excel("corretora.xlsx")
credito.to_excel("credito.xlsx")
crise.to_excel("crise.xlsx")
derivativos.to_excel("derivativos.xlsx")
desemprego.to_excel("desemprego.xlsx")
dinheiro.to_excel("dinheiro.xlsx")
divida.to_excel("divida.xlsx")
dividendos.to_excel("dividendos.xlsx")
dolar.to_excel("dolar.xlsx")
economia.to_excel("economia.xlsx")
empresa.to_excel("empresa.xlsx")
estagio.to_excel("estagio.xlsx")
ferro.to_excel("ferro.xlsx")
financas.to_excel("financas.xlsx")
fundos.to_excel("fundos.xlsx")
gado.to_excel("gado.xlsx")
gasolina.to_excel("gasolina.xlsx")
ibovespa.to_excel("ibovespa.xlsx")
inflacao.to_excel("inflacao.xlsx")
investimento.to_excel("investimento.xlsx")
investir.to_excel("investir.xlsx")
itau.to_excel("itau.xlsx")
itub4.to_excel("itub4.xlsx")
jbs.to_excel("jbs.xlsx")
jbss3.to_excel("jbss3.xlsx")
magazine.to_excel("magazine.xlsx")
mercado.to_excel("mercado.xlsx")
mglu3.to_excel("mglu3.xlsx")
mineracao.to_excel("mineraca.xlsx")
petr4.to_excel("petr4.xlsx")
petrobras.to_excel("petrobras.xlsx")
petroleo.to_excel("petroleo.xlsx")
politica.to_excel("politica.xlsx")
portifolio.to_excel("portifolio.xlsx")
renda.to_excel("renda.xlsx")
restaurante.to_excel("restaurante.xlsx")
selic.to_excel("selic.xlsx")
titulos.to_excel("titulos.xlsx")
vale.to_excel("vale.xlsx")
vale3.to_excel("vale3.xlsx")
varejo.to_excel("varejo.xlsx")
viajar.to_excel("viajar.xlsx")
vvar3.to_excel("vvar3.xlsx")
xp.to_excel("xp.xlsx")













