import tkinter as tk
from tkinter import filedialog
import csv
import os

class Conversor:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de CSV para TXT by Matheus")
        self.root.geometry("430x430")

        # Configurações de estilo para os widgets
        self.estilo_btn = {'font': ('Helvetica', 10), 'width': 20, 'height': 2}
        self.estilo_label = {'font': ('Helvetica', 10)}

        self.btn_selecionar_arquivo = tk.Button(root, text="Selecione o arquivo CSV", command=self.selecionar_arquivo, **self.estilo_btn)
        self.btn_selecionar_arquivo.pack(pady=20)

        self.label_arquivo_selecionado = tk.Label(root, text="Nenhum arquivo selecionado", **self.estilo_label)
        self.label_arquivo_selecionado.pack(pady=20)

        self.btn_converter = tk.Button(root, text="Converter", command=self.converter, **self.estilo_btn)
        self.btn_converter.pack(pady=20)

        self.status = tk.Label(root, text="", **self.estilo_label)
        self.status.pack(pady=12)

        self.btn_sair = tk.Button(root, text="Sair", command=root.destroy, **self.estilo_btn)
        self.btn_sair.pack(pady=20)

    def selecionar_arquivo(self):
        self.nome_arquivo_entrada = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")))
        
        if self.nome_arquivo_entrada:
            caminho_base, _ = os.path.splitext(self.nome_arquivo_entrada)
            self.nome_arquivo_saida = f'{caminho_base}.txt'
            nome_arquivo_mostrado = os.path.basename(self.nome_arquivo_entrada)
            self.label_arquivo_selecionado.config(text=f"Arquivo selecionado: {nome_arquivo_mostrado}")
        else:
            self.label_arquivo_selecionado.config(text="Nenhum arquivo selecionado")

    def converter(self):
        if self.nome_arquivo_entrada and self.nome_arquivo_saida:
            with open(self.nome_arquivo_entrada, mode='r') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)
                
                with open(self.nome_arquivo_saida, mode='w', encoding='utf-8') as arquivo_txt:
                    for linha in leitor_csv:
                        arquivo_txt.write(';'.join(linha) + '\n')
            self.status.config(text='Conversão concluída, verifique o arquivo na pasta do csv selecionado.')
        else:
            self.status.config(text='Nenhum arquivo selecionado, selecione um csv.')

if __name__ == "__main__":
    root = tk.Tk()
    app = Conversor(root)
    root.mainloop()
