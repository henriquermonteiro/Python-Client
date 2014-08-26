import model
import main
import tkinter as tk

class View:
    def __init__(self):
        frame = tk.Tk()
        b_ger = tk.Button(frame)
        b_car = tk.Button(frame)

        buildgeral()
        buildcarteira()


    def buildgeral(self):
        geral = tk.Frame(self.frame)
        
        g_scroll = tk.Scrollbar(geral)
        g_scroll.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)

        listframe = tk.Frame(geral)
        listframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        
        g_list_id = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        g_list_id.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        g_list_name = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        g_list_name.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        g_list_price = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        g_list_price.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

        g_scroll.config(command=listframe.yview)

        g_listen = tk.Button(geral)
        g_listen.pack(side=tk.SW)
        g_listen['command'] = requestlistener

        g_refresh = tk.Button(geral)
        g_refresh.pack(side=tk.SE)
        g_refresh['command'] = refreshgeral

        self.geral = geral
        self.g_list = {}

        self.g_list['id_g'] = g_list_id
        self.g_list['name_g'] = g_list_name
        self.g_list['price_g'] = g_list_price
        
        return

    def buildcarteira(self):
        carteira = tk.Frame(self.frame)
        
        c_scroll = tk.Scrollbar(carteira)
        c_scroll.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)

        listframe = tk.Frame(carteira)
        listframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        
        c_list_id = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        c_list_id.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_name = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        c_list_name.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_price = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        c_list_price.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_quant = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set)
        c_list_quant.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        
        c_scroll.config(command=listframe.yview)

        

        self.carteira = carteira
        self.c_list = {}

        self.c_list['id_c'] = c_list_id
        self.c_list['name_c'] = c_list_name
        self.c_list['price_c'] = c_list_price
        self.c_list['quant_c'] = c_list_price
        
        return
        
        
    def notifycompletion(self, operation):


    def updatevalues(self, identifier, value):


    def refreshgeral(self):
        

    def registeroperation(self):


    def requestlistener(self):



    
