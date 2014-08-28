import model
import main
import tkinter as tk

class View:
    def __init__(self, main):
        this.main = main
        frame = tk.Tk()
        b_ger = tk.Button(frame)
        b_car = tk.Button(frame)
        
        b_ger.grid(row=0, column=1, sticky = tk.S+tk.E)
        b_car.grid(row=0, column=2, sticky = tk.S+tk.W)
        
        b_ger['command'] = modegeral
        b_car['command'] = modecarteira
        
        self.window = frame

        buildgeral()
        buildcarteira()
        
        modegeral()

        mainloop()
        
    def modegeral(self):
        self.carteira.grid_forget()
        self.geral.grid(row=1, column=0, rowspan=7, columnspan=5, sticky = tk.N+tk.S+tk.W+tk.E)
        
    def modecarteira(self):
        self.geral.grid_forget()
        self.carteira.grid(row=1, column=0, rowspan=7, columnspan=5, sticky = tk.N+tk.S+tk.W+tk.E)

    def buildgeral(self):
        geral = tk.Frame(self.frame)
        
        g_scroll = tk.Scrollbar(geral)
        g_scroll.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)

        listframe = tk.Frame(geral)
        listframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        
        g_list_id = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
        g_list_id.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        g_list_name = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
        g_list_name.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        g_list_price = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
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
        c_scroll.grid(row = 0, column = 4, sticky = tk.N+tk.S+tk.W, rowspan = 6)

        listframe = tk.Frame(carteira)
        listframe.grid(row = 0, column = 1, sticky = tk.N+tk.S+tk.W+tk.E, columnspam = 3, rowspan = 6)
        
        c_list_id = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
        c_list_id.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_name = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
        c_list_name.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_price = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
        c_list_price.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_quant = tk.Listbox(listframe, yscrollcommand=tkinter.g_scroll.set, selectmode=tk.SINGLE)
        c_list_quant.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        
        c_scroll.config(command=listframe.yview)

        c_spins = {}
        c_spins['id'] = tk.Spinbox(carteira)
        c_spins['id'].grid(row=6, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        
        c_spins['cv'] = tk.Spinbox(carteira, values=('Compra', 'Venda'))
        c_spins['cv'].grid(row=6, column=2, sticky = tk.N+tk.S+tk.W+tk.E)
        
        c_spins['quant'] = tk.Spinbox(carteira, from_=0, to=100000, increment=1)
        c_spins['quant'].grid(row=6, column=3, sticky = tk.N+tk.S+tk.W+tk.E)
        
        c_spins['price'] = tk.Spinbox(carteira, from_=0, to=10000000, increment=0.1)
        c_spins['price'].grid(row=7, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        
        g_reg = tk.Button(carteira)
        g_reg.grid(row=7, column=3, sticky = tk.N+tk.S+tk.W+tk.E)
        g_reg['command'] = registeroperation

        self.carteira = carteira
        self.c_list = {}

        self.c_list['id_c'] = c_list_id
        self.c_list['name_c'] = c_list_name
        self.c_list['price_c'] = c_list_price
        self.c_list['quant_c'] = c_list_price
        
        self.c_spins = c_spins
        
        return
        
        
    def notifycompletion(self, operation):
        top = tk.Toplevel()
        
        info = 'Sua operação de '
        
        if operation.compra:
            info += 'compra'
        else:
            info += 'venda'
        
        info += ' foi concluída. O montante transacionado foi de ' + opration.quantity + ' a um preço unitário de ' + opration.price
        
        msg = Message(top, text=info)
        msg.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
        

    def updatevalues(self, identifier, value):
        for i in range(self.g_list['id_g'].size()):
		if(identifier == self.g_list['id_g'].get(i)):
			self.g_list['price_g'].delete(i)
			self.g_list['price_g'].insert(i, value)
			#return 'true'
	#return 'false'
                

    def refreshgeral(self):
        lista = self.main.updatedlist()
        
        self.g_list.clear()
        
        for k, v in lista:
            self.g_list['id_g'] = k
            self.g_list['name_g'] = v.name
            self.g_list['price_g'] = v.price
        
        return
    
    

    def registeroperation(self):
        if self.c_spins['id'].get() != '' and self.c_spins['quantity'].get() != 0 and self.c_spins['price'].get() != 0:
            iscompra = self.c_spins['cv'].get() == 'Compra'
            operation = model.Operacao(self.c_spins['id'].get(), iscompra, self.c_spins['price'].get(), self.c_spins['quantity'].get())
            
            print(operation)
            
            self.main.addoperation(operation)
            

    def requestlistener(self):
        selected = self.g_list['id_g'].curselection()
        
        if(len(selected) > 0):
            identifier = selected[0]
            print(identifier)
            self.main.listento(identifier)


    
