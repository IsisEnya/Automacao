import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
import pandas as pd 
from info import pesquisar
import threading
from pathlib import Path


def gerar_relatorios(valor_inicial, valor_final):
    lista_dados = []
    contador = 0
    for numero in range(valor_inicial,valor_final+1):
        dados = pesquisar(numero)
        dados = dados[-1]
        dados["n_pesquisa"] = numero
        lista_dados.append(dados)
        contador += 1
        progresso_atual = (contador/((valor_final-valor_inicial)+1))*100
        string_avisos.set(f"{progresso_atual:.2f}%")
        janela.update()
    df = pd.DataFrame(lista_dados)
    caminho_arquivo = f"Relatorio_Pesquisa_de_{valor_inicial}_ate_{valor_final}.xlsx"
    print(caminho_arquivo)
    df.to_excel(caminho_arquivo, index=False)
    string_avisos.set(f"Arquivo salvo na pasta")

def iniciar_geracao_relatorios_thread():
    ci = int(input_ci.get())
    cf = int(input_cf.get())
    thread = threading.Thread(target=gerar_relatorios, args=(int(ci),int(cf)))
    thread.start()

def pegar_codigos():
    ci = input_ci.get()
    cf = input_cf.get()
    #endereco = string_endereco.get()
    if not ci.isdigit() or not cf.isdigit():
        string_avisos.set("Preencha corretamente os campos dos codigos")   
    elif int(ci) >= int(cf):
        string_avisos.set("O codigo final deve ser maior que o codigo inicial")
    #elif endereco == "Ainda não foi escolhida uma pasta para salvar o arquivo":
    #    string_avisos.set("ESCOLHA UMA PASTA PARA SALVAR O SEU ARQUIVO")
    else:
        string_avisos.set(f"Iniciando...")
        iniciar_geracao_relatorios_thread()
        


#def escolher_pasta():
#    pasta_escolhida = filedialog.askdirectory()
#    if pasta_escolhida:
#        # Faça algo com a pasta escolhida, por exemplo, exiba o caminho no console
#        string_endereco.set(f"Pasta escolhida: {pasta_escolhida}")


janela = tk.Tk()
janela.title("Automação de medicações")
#seção principal(titulo)
label_pa = tk.Label(text="Preencha as informações abaixo:", borderwidth=2, relief="solid")
label_pa.grid(row=0, column=0, padx=10,pady=10,sticky="nswe",columnspan=3)
#valores dos codigos
label_ci = tk.Label(text="Codígo Inicial")
label_ci.grid(row=1, column=0, padx=10,pady=10,sticky="nswe",columnspan=2)

label_cf = tk.Label(text="Codígo final")
label_cf.grid(row=2, column=0, padx=10,pady=10,sticky="nswe",columnspan=2)

input_ci = tk.Entry() 
input_ci.grid(row=1, column=2, padx=10,pady=10,sticky="nswe",columnspan=1)

input_cf= tk.Entry() 
input_cf.grid(row=2, column=2, padx=10,pady=10,sticky="nswe",columnspan=1)

#label_sa = tk.Label(text="Escolha o local para salvar o arquivo", borderwidth=2, relief="solid")
#label_sa.grid(row=3, column=0, padx=10,pady=10,sticky="nswe",columnspan=2)

#botao_ea = tk.Button(text="Escolher",command=escolher_pasta)
#botao_ea.grid(row=3, column=2, padx=10,pady=10,sticky="nswe",columnspan=1)

#string_endereco = tk.StringVar()
#string_endereco.set("Ainda não foi escolhida uma pasta para salvar o arquivo")
#label_ea = tk.Label(textvariable=string_endereco)
#label_ea.grid(row=4, column=0, padx=10,pady=10,sticky="nswe",columnspan=3)

string_avisos = tk.StringVar()
string_avisos.set("ainda não iniciado")
label_prog = tk.Label(textvariable=string_avisos, borderwidth=2, relief="solid")
label_prog.grid(row=5, column=0, padx=10,pady=10,sticky="nswe",columnspan=2)

botao_enviar = tk.Button(text="Iniciar",command=pegar_codigos)
botao_enviar.grid(row=5, column=2, padx=10,pady=10,sticky="nswe",columnspan=1)

janela.mainloop()