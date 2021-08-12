from tkinter import *
import mysql.connector 
sqlconnect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)
cursor = sqlconnect.cursor()
try:
    cursor.execute("USE eleicao;")
    print("candidatos selecionado!!")
except:
    cursor.execute("USE eleicao;")
    print("candidatos selecionado!")
class Urna():
    def __init__(self):
        self.tela = Tk()
        self.tela.title('Urna')
        self.tela.geometry("1280x720")
        self.tela.iconbitmap('41a997f335f00e9e9458a1327acc8790.ico')
        self.tela.resizable(False,False)
        self.textoent = ""                                            
        self.total = ""
        self.a = True
        self.frames()
        self.botões()
        self.label()
        self.entries()
        self.tela.bind("<KeyPress>",self.inserirteclado)
        self.tela.bind("<Delete>", self.delete)
        self.tela.mainloop()
    def botões(self):
        btn1 = Button(self.tela, text = "1", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(1))
        btn1.place(relx = 0.5, rely = 0.45, relwidth = 0.15, relheight = 0.16)
        btn2 = Button(self.tela, text = "2", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(2))
        btn2.place(relx = 0.65, rely = 0.45, relwidth = 0.15, relheight = 0.16)
        btn3 = Button(self.tela, text = "3", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(3))
        btn3.place(relx = 0.8, rely = 0.45, relwidth = 0.15, relheight = 0.16)
        btn4 = Button(self.tela, text = "4", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(4))
        btn4.place(relx = 0.5, rely = 0.28, relwidth = 0.15, relheight = 0.16)
        btn5 = Button(self.tela, text = "5", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(5))
        btn5.place(relx = 0.65, rely = 0.28, relwidth = 0.15, relheight = 0.16)
        btn6 = Button(self.tela, text = "6", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(6))
        btn6.place(relx = 0.8, rely = 0.28, relwidth = 0.15, relheight = 0.16)
        btn7 = Button(self.tela, text = "7", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(7))
        btn7.place(relx = 0.5, rely = 0.11, relwidth = 0.15, relheight = 0.16)
        btn8 = Button(self.tela, text = "8", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(8))
        btn8.place(relx = 0.65, rely = 0.11, relwidth = 0.15, relheight = 0.16)
        btn9 = Button(self.tela, text = "9", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(9))
        btn9.place(relx = 0.8, rely = 0.11, relwidth = 0.15, relheight = 0.16)
        btn0 = Button(self.tela, text = "0", font = "arial 21", bg = "black", fg = "white", activebackground = "#1C1C1C",bd = 4, command = lambda:self.funcBtn(0))
        btn0.place(relx = 0.65, rely = 0.62, relwidth = 0.15, relheight = 0.16)
        btnconfirma = Button(self.tela, text = "CONFIRMA", font = "arial 21", bg = "#32CD32", fg = "black", activebackground = "#006400",bd = 4, command = lambda:self.funcconfirma())
        btnconfirma.place(relx = 0.8, rely = 0.79, relwidth = 0.15, relheight = 0.16)
        btncorrige = Button(self.tela, text = "CORRIGE", font = "arial 21", bg = "#A0522D", fg = "white", activebackground = "#8B4513",bd = 4, command = lambda:self.funcapagar())
        btncorrige.place(relx = 0.65, rely = 0.79, relwidth = 0.15, relheight = 0.16)
        btnbranco = Button(self.tela, text = "BRANCO", font = "arial 21", bg = "#D3D3D3", fg = "black", activebackground = "#808080",bd = 4, command = lambda:self.funcbranco())
        btnbranco.place(relx = 0.5, rely = 0.79, relwidth = 0.15, relheight = 0.16)
    def labels1(self):
        self.lbl1 = Label(self.tela, bg = "gray")
        self.lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.lbl2 = Label(self.tela, bg = "black")
        self.lbl2.place(relx = 0.55, rely = 0.1, relwidth = 0.55, relheight = 0.8)
        self.lbl3 = Label(self.tela, bg = "white")
        self.lbl3.place(relx = 0.03, rely = 0.11, relwidth = 0.51, relheight = 0.78)
        self.lbl4 = Label(self.tela, bg = "white", fg = "black", text = "NUMERO:", font = "Arial 25")
        self.lbl4.place(relx = 0.035, rely = 0.4, relwidth = 0.15, relheight = 0.1)
    def labels2(self):
        self.lblnome = Label(self.tela, bg = "white", fg = "black", text = "NOME:", font = "Arial 24")
        self.lblnome.place(relx = 0.03, rely = 0.5, relwidth = 0.15, relheight = 0.1)
        self.lblcargo = Label(self.tela, bg = "white", fg = "black", text = "ESCRITOR", font = "Arial 30")
        self.lblcargo.place(relx = 0.1, rely = 0.2, relwidth = 0.3, relheight = 0.15)
        self.lbltextao = Label(self.tela, bg = "white", fg = "black", text = '''Aperte a tecla:
    CONFIRMAR para CONFIRMAR este voto
    CORRIGIR para REINICIAR este voto''',font = "Arial 12", justify = LEFT)
        self.lbltextao.place(relx = 0.04, rely = 0.7, relwidth = 0.35, relheight = 0.15)
    def label(self):
        self.lbltela = Label(self.tela, bg = "white", fg = "black",bd = 5)
        self.lbltela.place(relx = 0.015, rely = 0.085, relwidth = 0.46, relheight = 0.83)
    def entries(self):
        global entrada 
        entrada = StringVar()
        self.ent1 = Entry(self.lbltela,font = "arial  22", textvariable = entrada, bg = "white", fg = "black",bd = 5)
        self.ent1.place(relx = 0.38, rely = 0.4, relwidth = 0.1, relheight = 0.1)
        entrada.set('')
    def frames(self):
        frm1 = Frame(self.tela, bg = "#C0C0C0")   
        frm1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        frm2 = Frame(self.tela, bg = "#1C1C1C")   
        frm2.place(relx = 0.49, rely = 0.09, relwidth = 0.47, relheight = 0.89)
    def funcBtn(self, n):
            if len(self.textoent) <= 1:
                if self.a == True: 
                    if self.textoent == "": 
                        self.textoent = self.ent1.get()
                    else:     
                        self.textoent = self.textoent 
                    if self.textoent == "0": 
                        self.textoent = ""
                        self.ent1.delete(0, END)
                        self.ent1.insert(END, self.textoent + str(n))
                        self.textoent = self.textoent + str(n)
                        entrada.set(self.textoent)
                    else:                  
                        self.ent1.delete(0, END)
                        self.ent1.insert(END, self.textoent + str(n))
                        self.textoent = self.textoent + str(n)
                        entrada.set(self.textoent)
                else:  
                        self.textoent = ""
                        self.textoent = self.textoent + str(n)
                        entrada.set(self.textoent)
                        self.a = True
                if len(self.textoent) == 2: 
                    self.num = self.ent1.get()
                    try:
                        cursor.execute("SELECT nome FROM candidato WHERE num = '{​}​'".format(self.num))
                        for i in cursor:
                            lista = []
                            for x in i:
                                lista.append(x)
                        self.nCandi = lista[0]
                        cursor.execute("SELECT foto FROM candidato WHERE num = '{​}​'".format(self.num))
                        for i in cursor:
                            lista2 = []
                            for x in i:
                                lista2.append(x)
                        self.ftCandi = lista2[0]
                        caminho = "C:\\fotos\\"
                        self.labels2()
                        self.lblnomecand = Label(self.tela, text = self.nCandi, font = "Arial 16", bg = "white")
                        self.lblnomecand.place(relx = 0.15, rely = 0.5, relwidth = 0.3, relheight = 0.1)
                        self.img = PhotoImage(file = caminho+self.ftCandi)
                        self.lblfoto = Label(self.tela, bg = 'white', image = self.img)
                        self.lblfoto.place(relx = 0.3, rely = 0.32, relwidth = 0.1, relheight = 0.2)
                    except UnboundLocalError:
                        lblconf = Label(self.tela, text = "VOTO NULO!", font = "Arial 30", bg = "white")
                        lblconf.place(relx = 0.02, rely = 0.3, relwidth = 0.44, relheight = 0.25)
                        self.lbltextao = Label(self.tela, bg = "white", fg = "black", text = '''Aperte a tecla:
                CONFIRMAR para CONFIRMAR este voto
                CORRIGIR para REINICIAR este voto''',font = "Arial 12", justify = LEFT)
                        self.lbltextao.place(relx = 0.04, rely = 0.7, relwidth = 0.35, relheight = 0.15)
    def funcbranco(self): 
        self.lblconf = Label(self.tela, bg = 'white', text = 'VOTO EM BRANCO!', font = 'arial 40')
        self.lblconf.place(relx = 0.015, rely = 0.085, relwidth = 0.46, relheight = 0.83)
        self.labelconf = Label(self.tela, bg = 'white', text = 'CONFIRMA para confirmar;\nCORRIGE para corrigir;', font = 'arial 19')
        self.labelconf.place(relx = 0.018, rely = 0.75, relwidth = 0.4, relheight = 0.15)
    def funcconfirma(self): 
        self.lblconf = Label(self.tela, text = 'FIM!', bg = 'white', font = 'arial 50')
        self.lblconf.place(relx = 0.015, rely = 0.085, relwidth = 0.46, relheight = 0.83)
    def inserirteclado(self,evento=None): 
        if str(evento.char).isnumeric() == True: 
            self.funcBtn(evento.char)
    def delete(self,evento):
        self.funcapagar()
    def funcapagar(self): 
        self.frames()
        self.label()
        self.botões()
        self.entries()
        self.ent1.delete(0, END)
        self.ent1.insert(END, "")
        self.textoent = ""
        entrada.set(self.textoent)
Urna()
    
    
  
  

