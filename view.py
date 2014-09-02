import model
import main
import tkinter as tk
import tkinter.messagebox as message

class View:
        
    def __init__(self, main):
        self.main = main
        frame = tk.Tk()
        b_ger = tk.Button(frame)
        b_car = tk.Button(frame)
        
        b_ger.grid(row=0, column=1, sticky = tk.S+tk.E)
        b_car.grid(row=0, column=2, sticky = tk.S+tk.W)
        
        b_ger['command'] = self.modegeral
        b_car['command'] = self.modecarteira
        
        b_ger['text'] = 'Geral'
        b_car['text'] = 'Carteira'
        
        self.window = frame

        self.buildgeral()
        self.buildcarteira()
        
        self.modegeral()
    
    def start(self):
        self.window.mainloop()
    
    def modegeral(self):
        self.carteira.grid_forget()
        self.geral.grid(row=1, column=0, rowspan=7, columnspan=5, sticky = tk.N+tk.S+tk.W+tk.E)
        
    def modecarteira(self):
        self.geral.grid_forget()
        self.carteira.grid(row=1, column=0, rowspan=7, columnspan=5, sticky = tk.N+tk.S+tk.W+tk.E)
        

    def buildgeral(self):
        geral = tk.Frame(self.window)
        
        g_scroll = tk.Scrollbar(geral)
        g_scroll.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)

        listframe = tk.Frame(geral)
        listframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        
        g_list_id = tk.Listbox(listframe, yscrollcommand=g_scroll.set, selectmode=tk.SINGLE)
        g_list_id.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        g_list_name = tk.Listbox(listframe, yscrollcommand=g_scroll.set, selectmode=tk.SINGLE)
        g_list_name.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        g_list_price = tk.Listbox(listframe, yscrollcommand=g_scroll.set, selectmode=tk.SINGLE)
        g_list_price.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

#        g_scroll.config(command=listframe.yview)

        g_listen = tk.Button(geral)
        g_listen.pack(side=tk.BOTTOM)
        g_listen['text'] = 'Monitorar'
        g_listen['command'] = self.requestlistener

        g_refresh = tk.Button(geral)
        g_refresh.pack(side=tk.BOTTOM)
        g_refresh['text'] = 'refresh'
        g_refresh['command'] = self.refreshgeral

        self.geral = geral
        g_list = {}

        g_list['id_g'] = g_list_id
        g_list['name_g'] = g_list_name
        g_list['price_g'] = g_list_price
        
        print(g_list)
        
        self.g_list = g_list
        
        print(self.g_list)
        
        return

    def buildcarteira(self):
        carteira = tk.Frame(self.window)
        
        c_scroll = tk.Scrollbar(carteira)
        c_scroll.grid(row = 0, column = 4, sticky = tk.N+tk.S+tk.W, rowspan = 6)

        listframe = tk.Frame(carteira)
        listframe.grid(row = 0, column = 1, sticky = tk.N+tk.S+tk.W+tk.E, columnspan = 3, rowspan = 6)
        
        c_list_id = tk.Listbox(listframe, yscrollcommand=c_scroll.set, selectmode=tk.SINGLE)
        c_list_id.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_name = tk.Listbox(listframe, yscrollcommand=c_scroll.set, selectmode=tk.SINGLE)
        c_list_name.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_price = tk.Listbox(listframe, yscrollcommand=c_scroll.set, selectmode=tk.SINGLE)
        c_list_price.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

        c_list_quant = tk.Listbox(listframe, yscrollcommand=c_scroll.set, selectmode=tk.SINGLE)
        c_list_quant.grid(row=0, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
        
#        c_scroll.config(command=listframe.yview)

        c_spins = {}
        c_spins['id'] = tk.Spinbox(carteira)
        c_spins['id'].grid(row=6, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        
        c_spins['cv'] = tk.Spinbox(carteira, values=('Compra', 'Venda'))
        c_spins['cv'].grid(row=6, column=2, sticky = tk.N+tk.S+tk.W+tk.E)
        
        c_spins['quant'] = tk.Spinbox(carteira, from_=0, to=1000, increment=1)
        c_spins['quant'].grid(row=6, column=3, sticky = tk.N+tk.S+tk.W+tk.E)
        
        c_spins['price'] = tk.Spinbox(carteira, from_=0, to=1000, increment=1)
        c_spins['price'].grid(row=7, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        
        g_reg = tk.Button(carteira)
        g_reg.grid(row=7, column=3, sticky = tk.N+tk.S+tk.W+tk.E)
        g_reg['command'] = self.registeroperation
        g_reg['text'] = 'Registrar'

        self.carteira = carteira
        self.c_list = {}

        self.c_list['id_c'] = c_list_id
        self.c_list['name_c'] = c_list_name
        self.c_list['price_c'] = c_list_price
        self.c_list['quant_c'] = c_list_quant
        
        self.c_spins = c_spins
        
        return
        
        
    def notifycompletion(self, operation):
        print('Try to notify')
        
        info = 'Sua operacao de '
        
        if operation.compra:
            info += 'compra'
        else:
            info += 'venda'
        
        info += ' foi concluida. O montante transacionado foi de ' + operation.quantity + ' a um preco unitario de ' + operation.price
        
        print(info)
        
        message.showinfo(title='Operacao completada', message=info)
        

    def updatevalues(self, identifier, value):
        for i in range(self.g_list['id_g'].size()):
            if identifier == self.g_list['id_g'].get(i):
                self.g_list['price_g'].delete(i)
                self.g_list['price_g'].insert(i, value)
                break
                
        for i in range(self.c_list['id_c'].size()):
            if identifier == self.c_list['id_c'].get(i):
                self.c_list['price_c'].delete(i)
                self.c_list['price_c'].insert(i, value)
		#return 'true'
	#return 'false'
                

    def refreshgeral(self):
        lista = self.main.updatedlist()
        
        self.g_list['id_g'].delete(0, tk.END)
        self.g_list['name_g'].delete(0, tk.END)
        self.g_list['price_g'].delete(0, tk.END)
        
        #print(lista)
        print(self.g_list)
        
        for v in lista.values():
            self.g_list['id_g'].insert(tk.END, v.ref_id)
            self.g_list['name_g'].insert(tk.END, v.name)
            self.g_list['price_g'].insert(tk.END, v.price)
        
        return
    
    

    def registeroperation(self):
        if self.c_spins['id'].get() != '' and self.c_spins['quant'].get() != 0 and self.c_spins['price'].get() != 0:
            iscompra = self.c_spins['cv'].get() == 'Compra'
            operation = model.Operacao(self.c_spins['id'].get(), iscompra, self.c_spins['price'].get(), self.c_spins['quant'].get())
            
            print(operation.encodexml())
            
            self.main.addoperation(operation)
            

    def requestlistener(self):
        selected = self.g_list['id_g'].curselection()
        
        if(len(selected) > 0):
            identifier = self.g_list['id_g'].get(tk.ACTIVE)
            #print(identifier)
            emp = self.main.listento(identifier)
            
            self.c_list['id_c'].insert(tk.END, emp.ref_id)
            self.c_list['name_c'].insert(tk.END, emp.name)
            self.c_list['price_c'].insert(tk.END, emp.price)
            self.c_list['quant_c'].insert(tk.END, emp.quantity)
            
            ax = (emp.ref_id)
            
            t1 = self.c_spins['id']['values']
            print(t1)
            print(len(t1))
            if type(t1) == str:
                if(len(t1)) == 0:
                    t = (ax, )
                else:
                    t = t1.split(' ') + [ ax ]
            else:
                t = t1 + (ax, )
            print(t)
            print(len(t))
            self.c_spins['id']['values'] = t

    
