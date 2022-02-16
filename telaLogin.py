

from tkinter import * 
class main:
	
	def __init__(self):
		self.window = Tk()
		self.window_config()
		self.widgets_window()
		self.window.mainloop()

	#Configurações da Janela
	def window_config(self):
		self.window.title('Login')
		self.window.resizable(True, True)
		self.window.config(bg='#555555')
		self.window.minsize(350, 350)
		self.window.maxsize(500, 500)
	
	#WidGets que contém a Janela.
	def widgets_window(self):
		#Label Email
		self.lbl = Label(self.window, text='Email', bg='#555555',
		fg='white', font='arial 10')
		self.lbl.place(relx=0.01, rely=0.1)
		
		
		#Campo de Texto - Email.
		self.cx_email = Entry(self.window, width=55)
		self.cx_email.place(relx=0.02, rely=0.18)
		
		
		#Label Senha.
		self.lbl_senha = Label(self.window, text='Senha',
		fg='white', bg='#555555', font='arial 10')
		self.lbl_senha.place(relx=0.01, rely=0.28)
		
		
		#Campo de Entrada - Senha 
		self.cx_senha = Entry(self.window, width=55)
		self.cx_senha.place(relx=0.02, rely=0.37)
		
		
		#Botão Validar 
		self.btn_valid = Button(self.window, text='Validar', font='arial 10',
		width=25, command=self.autentica)
		self.btn_valid.place(relx=0.2, rely=0.50)
		
		
		#Label - Autenticação.
		self.lbl_autentica = Label(self.window, text='Status',
		fg='white', bg='#555555', font='arial 10')
		self.lbl_autentica.pack(side='bottom')
		
	#Autenticação	
	def autentica(self):
		email = self.cx_email.get()
		senha = self.cx_senha.get()
		
		if email == 'ffabio17@yahoo.com':
			if senha == 'jr2922jr':
				self.lbl_autentica['font'] = 'arial 10 bold'
				self.lbl_autentica['fg'] = 'white'
				self.lbl_autentica['text'] = 'Validado com Sucesso'
				self.cx_email.delete(0, END)
				self.cx_senha.delete(0, END)
		else:
			self.lbl_autentica['font'] = 'arial 10 bold'
			self.lbl_autentica['fg'] = 'red'
			self.lbl_autentica['text'] = 'Erro de Validação'

#Instância da Classe Principal.
objeto = main()
	
