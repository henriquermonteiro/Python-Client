import model
import main
import tkinter as tk

class View:
    def __init__(self):
        frame = tk.TK()
        
        b_geral = tk.Button(frame)
        b_carteira = tk.Button(frame)
        
        b_listento = tk.Button(frame)
        
        list_id = tk.Listbox(frame)
        list_name = tk.Listbox(frame)
        
        b_geral['text'] = "Geral"
        b_carteira['text'] = "Carteira"
        b_listento['text'] = "Listen"
        
        b_geral['command'] = self.modegeral
        b_carteira['command'] = self.modecarteira
        b_listento['command'] = self.requestlistener
        
        

    def notifycompletion(self, operation):
        text = "Operação de " + " concluída. "

    def updatevalues(self, identifier, value):


    def registeroperation(self):


    def requestlistener(self):


    def modegeral(self):
        
        
    def modecarteira(self):
