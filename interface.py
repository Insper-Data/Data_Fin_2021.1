import pandas as pd #para manusar dados
from tkinter import * #para fazer a interface com o usuÃ¡rio
import numpy as np #tambÃ©m usada para manusear dados
import matplotlib.pyplot as plt #para fazer grÃ¡ficos
import tkinter as tk #também usado na interface
from tkinter import messagebox #também usado na interface
from tabulate import tabulate #fazer tabela
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import insperdata as insp
import strategy as strat 
import agg as agg

#%%
assets = list(range(81))
df_fin = pd.read_excel("dados fin.xlsx")
df_assets = pd.DataFrame(df_fin.iloc[0,:].dropna())
for i in range(81):
    assets = df_assets.index
    


#%%

#Função que fecha a janela
def botao_close():
    janela.withdraw()
    janela.quit()
    janela.destroy()

#Interface - Primeira Janela
janela = Tk()
janela.title("Insper Data - Itaú Asset Management - 2021.1")
janela.geometry("800x200")
janela["bg"]="white"

lb1 = Label(janela, text = "Olá, investidor! Bem-vindo a nosso programa!", font=("helvetica",15))
lb2 = Label(janela, text = "Vamos ver a rentabilidade do algotrading baseado no Google Trends", font=("helvetica",15))
lb1.pack(fill = X)
lb2.pack(fill = X)

bt = Button(janela,text="Bora maximizar o sharpe meo!",font=("helvetica",20), command = botao_close)
bt.pack(side = BOTTOM)
janela.mainloop()

#%%
#Segunda janela

# Update the listbox
def update(data):
	# Clear the listbox
	my_list.delete(0, END)
	# Add toppings to listbox
	for item in data:
		my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
	# Delete whatever is in the entry box
	my_entry.delete(0, END)
	# Add clicked list item to entry box
	my_entry.insert(0, my_list.get(ANCHOR))

# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = my_entry.get()
	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)
	# update our listbox with selected items
	update(data)				

def botao_close_2():
    global palavra_google
    global ticker_stock
    global inicio
     palavra_google = str(ed1.get())
    ticker_stock = str(my_entry.get())
    inicio = str(ed3.get())
    figure1 = agg.retorno_acumulado(inicio, palavra_google, ticker_stock) #Chamado do gráfico da estratégia
    bar1 = FigureCanvasTkAgg(figure1, janela)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    
janela = Tk()
janela.title("Insper Data - Itaú Asset Management - 2021.1")
janela.geometry("800x600")
janela["bg"]="white"

lb1 = Label(janela,text="Vamos analisar a tendência de qual palavra?",font=("helvetica",15))
lb1.pack(fill=X)
ed1 = Entry(janela)
ed1.pack()

#Escolha da ação (ativo)
lb2 = Label(janela,text="E de qual ação da B3?",font=("helvetica",15))
lb2.pack(fill=X)
my_entry = Entry(janela)
my_entry.pack()
# Create a listbox
my_list = Listbox(janela, width = 30)
my_list.pack(pady = 40)
# Create a list of pizza toppings
toppings = assets
# Add the toppings to our list
update(toppings)
# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)
# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

lb3 = Label(janela,text="A partir de qual data?",font=("helvetica",15))
lb3.pack(fill=X)
ed3 = Entry(janela)
ed3.pack()


bt = Button(janela, text= "Gerar gráfico de retorno acumulado", command= botao_close_2)
bt.pack(side = BOTTOM)

bt = Button(janela, text= "Sair", command= botao_close)
bt.pack(side = RIGHT)

janela.mainloop()

print("Hello World")
