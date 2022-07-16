from tkinter import ttk
from tkinter import *
from six.moves import tkinter as tk
from tkinter.messagebox import *
root = tk.Tk()
variable = tk.StringVar()

TypeConstScal = [[1,1,1,1,1,1,1,1,1,1,1,1],[2,2,1,2,2,2,1],[2,1,2,2,1,2,2],[2,2,3,2,3],[2,2,1,2,2,2,1],[2,1,2,2,2,1,2],[1,2,2,2,1,2,2],[2,2,2,1,2,2,1],[2,2,1,2,2,1,2],[2,1,2,2,1,2,2],[1,2,2,1,2,2,2],[1,3,1,2,1,2,2],[2,2,2,2,1,2,1],[2,1,2,2,1,3,1],[2,1,2,2,2,2,1],[2,2,2,2,2,2],[3,2,1,1,3,2],[1,3,1,2,1,3,1],[3,2,2,3,2]]
TypeNameScal = ["cromatica", "mayor", "menor", "pentatonica","jónico","dórico","frigio","lidio","mixolidio","Eelico","locrio","frigia dominante","lidia aumentada","menor armónica","menor melodica","escala de tonos enteros","blues","doble armónica","pentatonica menor"]
TypeConstChord = [[4,3],[3,4],[4,3,3],[4,3,7],[3,4,3],[4,3,4],[3,4,4],[4,4],[3,3],[2,5],[5,2]]
TypeNameChord = ["mayor","menor","mayor con septima","con novena","menor septima","Maj7","Maj7 menor","aumentado","disminuido","con segunda suspendida","con cuarta suspendida"]
TypeConstInter = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14]]
TypeNameInter =["primera justa","segunda menor","segunda mayor","tercera menor","tercera mayor","cuarta justa","cuarta aumentada/quinta disminuida","quinta justa","sexta menor","sexta mayor","septima menor","septima mayor","octava justa","octava aumentada","novena mayor"]

def usar_intervalo(a, c, d,i):
    e = len(d)
    if(i<len(a)):
        if(e > (c+a[i])):
            f = c+a[i]
            return d[c] + "," + usar_intervalo(a, f, d, i+1) 
        elif (e <= (c+a[i])):
            f = -(len(d)-(c))+a[i]
            return d[c] + "," + usar_intervalo(a, f, d, i+1)
    else:
        return d[c]
def definition(b):
    if(b == Cromaticsharp[7] or b == Cromaticsharp[2] or b == Cromaticsharp[9] or b == Cromaticsharp[11] or b == Cromaticsharp[1] or b == Cromaticsharp[3] or b == Cromaticsharp[6] or b == Cromaticsharp[8] or b == Cromaticsharp[10]):
        return Cromaticsharp
    else:
        return Cromaticbemol

class Scale():
    def __init__(self, a = TypeConstScal[0], b = Cromaticsharp[0]):
        self.tipo = a
        self.reposo = b
        self.cromatic = definition(self.reposo)
    def construir1(self):
        self.c = self.cromatic.index(self.reposo)
        self.res = usar_intervalo(self.tipo, self.c, self.cromatic, 0)
        return self.res.split(',')
    def imprimir1(self):
        self.aux = TypeConstScal.index(self.tipo)
        return "Tu escala de "+self.reposo+" "+TypeNameScal[self.aux]+" es "+str(self.construir1())
class Chord():
    def __init__(self, a = TypeConstChord[0], b = Cromaticsharp[0]):
        self.tipo = a
        self.tonica = b
        self.cromatic = definition(self.tonica)
    def construir2(self):
        self.c = self.cromatic.index(self.tonica)
        self.res = usar_intervalo(self.tipo, self.c, self.cromatic, 0)
        return self.res.split(',')
    def imprimir2(self):
        self.aux = TypeConstChord.index(self.tipo)
        return "Tu acorde de "+self.tonica+" "+TypeNameChord[self.aux]+" es "+str(self.construir2())
class Interval():
    def __init__(self, a = TypeConstInter[1], b = Cromaticsharp[0]):
        self.tipo = a
        self.reposo = b
        self.cromatic = definition(self.reposo)
    def construir4(self):
        self.c = self.cromatic.index(self.reposo)
        self.res = usar_intervalo(self.tipo, self.c, self.cromatic, 0)
        return self.res.split(',')
    def imprimir4(self):
        self.aux = TypeConstInter.index(self.tipo)
        return "Tu intevalo de "+TypeNameInter[self.aux]+" sobre "+self.reposo+" es "+str(self.construir4())  
class ModularChord():
    def __init__(self, a = TypeConstChord[0], b = Cromaticsharp[0], em = TypeConstInter[1]):
        self.tipo = a
        self.tonica = b
        self.inter = em
        self.cromatic = definition(self.tonica)
    def construir5(self):
        self.c = self.cromatic.index(self.tonica)
        self.res = usar_intervalo(self.tipo, self.c, self.cromatic, 0)
        self.res = self.res.split(',')
        self.aux = self.res
        self.aux2 = self.res
        for i in range(0,len(self.res),1):
            self.z = self.cromatic.index(self.res[i]) 
            self.aux[i] = usar_intervalo(self.inter, self.z,self.cromatic,0)
            self.aux[i] = self.aux[i].split(',')
            self.aux[i].pop(0)
            #self.aux[i] = str(self.aux[i])
    def imprimir5(self):
        self.construir5()
        self.aux2 = TypeConstChord.index(self.tipo)
        return "Tu acorde de "+self.tonica+" "+TypeNameChord[self.aux2]+" subido "+str(self.inter)+" semitonos es "+str(self.aux)+" y se llama "+ str(self.aux[0])+" "+TypeNameChord[self.aux2]

note = Cromaticsharp[0]
def select0():
    global note
    note=Cromaticsharp[0]
def select1():
    global note
    note=Cromaticsharp[1]
def select2():
    global note
    note=Cromaticsharp[2]
def select3():
    global note
    note=Cromaticsharp[3]
def select4():
    global note
    note=Cromaticsharp[4]
def select5():
    global note
    note=Cromaticsharp[5]
def select6():
    global note
    note=Cromaticsharp[6]
def select7():
    global note
    note=Cromaticsharp[7]
def select8():
    global note
    note=Cromaticsharp[8]
def select9():
    global note
    note=Cromaticsharp[9]
def select10():
    global note
    note=Cromaticsharp[10]
def select11():
    global note
    note=Cromaticsharp[11]
def select01():
    global note
    note=Cromaticbemol[1]
def select00():
    global note
    note=Cromaticbemol[0]
def select02():
    global note
    note=Cromaticbemol[2]
def select03():
    global note
    note=Cromaticbemol[3]
def select04():
    global note
    note=Cromaticbemol[4]
def select05():
    global note
    note=Cromaticbemol[5]
def select06():
    global note
    note=Cromaticbemol[6]
def select07():
    global note
    note=Cromaticbemol[7]
def select08():
    global note
    note=Cromaticbemol[8]
def select09():
    global note
    note=Cromaticbemol[9]
def select010():
    global note
    note=Cromaticbemol[10]
def select011():
    global note
    note=Cromaticbemol[11]
chordv = 0
def chordmod0():
    global chordv
    chordv = 0
def chordmod1():
    global chordv
    chordv = 1
def chordmod2():
    global chordv
    chordv = 2
def chordmod3():
    global chordv
    chordv = 3
def chordmod4():
    global chordv
    chordv = 4
def chordmod5():
    global chordv
    chordv = 5
def chordmod6():
    global chordv
    chordv = 6
def chordmod7():
    global chordv
    chordv = 7
def chordmod8():
    global chordv
    chordv = 8
def chordmod9():
    global chordv
    chordv = 9
def chordmod10():
    global chordv
    chordv = 10
def chordmod11():
    global chordv
    chordv = 11

def Creator():
    root.destroy()
    window = tk.Tk()
    application = Work(window)
    window.mainloop()

class Product():
    def __init__(self, root):
        self.wind = root
        self.wind.title("Music Reference (consultor de escalas, acordes, tonalidades, intervalos y modulación)")  
        frame1 = LabelFrame(self.wind, text = 'Elige la nomenclatura en la que deseas trabajar')
        frame1.grid(row = 1, column =0, columnspan = 50, pady = 20)
        ttk.Radiobutton(frame1, text = 'Inglesa', variable = variable,value = 1, command = self.noming).grid(row = 2, column = 0)
        ttk.Radiobutton(frame1, text = 'Española', variable = variable,value = 2, command = self.nomesp).grid(row = 3, column = 0)
        ttk.Button(frame1, text = 'Listo', command = Creator).grid(row = 4, column = 0)
    def noming(self):
        global Cromaticsharp
        global Cromaticbemol
        Cromaticsharp = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
        Cromaticbemol = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
    def nomesp(self):
        global Cromaticsharp
        global Cromaticbemol
        Cromaticsharp = ["do","do#","re","re#","mi","fa","fa#","sol","sol#","la","la#","si"]
        Cromaticbemol = ["do","reb","re","mib","mi","fa","solb","sol","lab","la","sib","si"]
        
class Work(Scale, Chord, Interval, ModularChord):        
    def __init__(self, window):
        self.wind = window
        self.wind.title("Music Reference (consultor de escalas, acordes, tonalidades, intervalos y modulación)")  
        frame3 = LabelFrame(self.wind, text = 'Por favor, elige la nota sobre la que deseas construir')
        frame3.grid(row = 3, column =0, columnspan = 50, pady = 20)
        ttk.Button(frame3, text = Cromaticsharp[0], command = select0).grid(row = 4, column = 0)
        ttk.Button(frame3, text = Cromaticsharp[1], command = select1).grid(row = 4, column = 1)
        ttk.Button(frame3, text = Cromaticsharp[2], command = select2).grid(row = 4, column = 2)
        ttk.Button(frame3, text = Cromaticsharp[3], command = select3).grid(row = 4, column = 3)
        ttk.Button(frame3, text = Cromaticsharp[4], command = select4).grid(row = 4, column = 4)
        ttk.Button(frame3, text = Cromaticsharp[5], command = select5).grid(row = 4, column = 5)
        ttk.Button(frame3, text = Cromaticsharp[6], command = select6).grid(row = 4, column = 6)
        ttk.Button(frame3, text = Cromaticsharp[7], command = select7).grid(row = 4, column = 7)
        ttk.Button(frame3, text = Cromaticsharp[8], command = select8).grid(row = 4, column = 8)
        ttk.Button(frame3, text = Cromaticsharp[9], command = select9).grid(row = 4, column = 9)
        ttk.Button(frame3, text = Cromaticsharp[10], command = select10).grid(row = 4, column = 10)
        ttk.Button(frame3, text = Cromaticsharp[11], command = select11).grid(row = 4, column = 11)
        ttk.Button(frame3, text = Cromaticbemol[0], command = select00).grid(row = 5, column = 0)
        ttk.Button(frame3, text = Cromaticbemol[1], command = select01).grid(row = 5, column = 1)
        ttk.Button(frame3, text = Cromaticbemol[2], command = select02).grid(row = 5, column = 2)
        ttk.Button(frame3, text = Cromaticbemol[3], command = select03).grid(row = 5, column = 3)
        ttk.Button(frame3, text = Cromaticbemol[4], command = select04).grid(row = 5, column = 4)
        ttk.Button(frame3, text = Cromaticbemol[5], command = select05).grid(row = 5, column = 5)
        ttk.Button(frame3, text = Cromaticbemol[6], command = select06).grid(row = 5, column = 6)
        ttk.Button(frame3, text = Cromaticbemol[7], command = select07).grid(row = 5, column = 7)
        ttk.Button(frame3, text = Cromaticbemol[8], command = select08).grid(row = 5, column = 8)
        ttk.Button(frame3, text = Cromaticbemol[9], command = select09).grid(row = 5, column = 9)
        ttk.Button(frame3, text = Cromaticbemol[10], command = select010).grid(row = 5, column = 10)
        ttk.Button(frame3, text = Cromaticbemol[11], command = select011).grid(row = 5, column = 11)
        frame2 = LabelFrame(self.wind, text = 'Por favor, elige tu estructura correspondiente a cada acción')
        frame2.grid(row = 5, column =0, columnspan = 20, pady = 20) 
        frame4 = LabelFrame(frame2, text = 'Por favor, elige el tipo de escala')
        frame4.grid(row = 7, column =0, columnspan = 20, pady = 20) 
        ttk.Button(frame4, text = TypeNameScal[0], command = self.impes0).grid(row = 8, column = 1)
        ttk.Button(frame4, text = TypeNameScal[1], command = self.impes1).grid(row = 8, column = 2)
        ttk.Button(frame4, text = TypeNameScal[2], command = self.impes2).grid(row = 8, column = 3)
        ttk.Button(frame4, text = TypeNameScal[3], command = self.impes3).grid(row = 8, column = 4)
        ttk.Button(frame4, text = TypeNameScal[4], command = self.impes4).grid(row = 8, column = 5)
        ttk.Button(frame4, text = TypeNameScal[5], command = self.impes5).grid(row = 8, column = 6)
        ttk.Button(frame4, text = TypeNameScal[6], command = self.impes6).grid(row = 8, column = 7)
        ttk.Button(frame4, text = TypeNameScal[7], command = self.impes7).grid(row = 8, column = 8)
        ttk.Button(frame4, text = TypeNameScal[8], command = self.impes8).grid(row = 8, column = 9)
        ttk.Button(frame4, text = TypeNameScal[9], command = self.impes9).grid(row = 9, column = 1)
        ttk.Button(frame4, text = TypeNameScal[10], command = self.impes10).grid(row = 9, column = 2)
        ttk.Button(frame4, text = TypeNameScal[11], command = self.impes11).grid(row = 9, column = 3)
        ttk.Button(frame4, text = TypeNameScal[12], command = self.impes12).grid(row = 9, column = 4)
        ttk.Button(frame4, text = TypeNameScal[13], command = self.impes13).grid(row = 9, column = 5)
        ttk.Button(frame4, text = TypeNameScal[14], command = self.impes14).grid(row = 9, column = 6)
        ttk.Button(frame4, text = TypeNameScal[15], command = self.impes15).grid(row = 9, column = 7)
        ttk.Button(frame4, text = TypeNameScal[16], command = self.impes16).grid(row = 9, column = 8)
        ttk.Button(frame4, text = TypeNameScal[17], command = self.impes17).grid(row = 9, column = 9)
        ttk.Button(frame4, text = TypeNameScal[18], command = self.impes18).grid(row = 9, column = 10)
        frame5 = LabelFrame(frame2, text = 'Por favor, elige el tipo de acorde')
        frame5.grid(row = 10, column = 0, columnspan = 20, pady = 20) 
        ttk.Button(frame5, text = TypeNameChord[0], command = self.impch0).grid(row = 11, column = 1)
        ttk.Button(frame5, text = TypeNameChord[1], command = self.impch1).grid(row = 11, column = 2)
        ttk.Button(frame5, text = TypeNameChord[2], command = self.impch2).grid(row = 11, column = 3)
        ttk.Button(frame5, text = TypeNameChord[3], command = self.impch3).grid(row = 11, column = 4)
        ttk.Button(frame5, text = TypeNameChord[4], command = self.impch4).grid(row = 11, column = 5)
        ttk.Button(frame5, text = TypeNameChord[5], command = self.impch5).grid(row = 11, column = 6)
        ttk.Button(frame5, text = TypeNameChord[6], command = self.impch6).grid(row = 11, column = 7)
        ttk.Button(frame5, text = TypeNameChord[7], command = self.impch7).grid(row = 11, column = 8)
        ttk.Button(frame5, text = TypeNameChord[8], command = self.impch8).grid(row = 11, column = 9)
        ttk.Button(frame5, text = TypeNameChord[9], command = self.impch9).grid(row = 11, column = 10)
        ttk.Button(frame5, text = TypeNameChord[10], command = self.impch10).grid(row = 11, column = 11)
        frame7 = LabelFrame(frame2, text = 'Elige el intervalo a utilizar en una nota')
        frame7.grid(row = 15, column = 0, columnspan = 20, pady = 20) 
        ttk.Button(frame7, text = TypeNameInter[0], command = self.impint0).grid(row = 16, column = 1)
        ttk.Button(frame7, text = TypeNameInter[1], command = self.impint1).grid(row = 16, column = 2)
        ttk.Button(frame7, text = TypeNameInter[2], command = self.impint2).grid(row = 16, column = 3)
        ttk.Button(frame7, text = TypeNameInter[3], command = self.impint3).grid(row = 16, column = 4)
        ttk.Button(frame7, text = TypeNameInter[4], command = self.impint4).grid(row = 16, column = 5)
        ttk.Button(frame7, text = TypeNameInter[5], command = self.impint5).grid(row = 16, column = 6)
        ttk.Button(frame7, text = TypeNameInter[6], command = self.impint6).grid(row = 16, column = 7)
        ttk.Button(frame7, text = TypeNameInter[7], command = self.impint7).grid(row = 17, column = 1)
        ttk.Button(frame7, text = TypeNameInter[8], command = self.impint8).grid(row = 17, column = 2)
        ttk.Button(frame7, text = TypeNameInter[9], command = self.impint9).grid(row = 17, column = 3)
        ttk.Button(frame7, text = TypeNameInter[10], command = self.impint10).grid(row = 17, column = 4)
        ttk.Button(frame7, text = TypeNameInter[11], command = self.impint11).grid(row = 17, column = 5)
        ttk.Button(frame7, text = TypeNameInter[12], command = self.impint12).grid(row = 17, column = 6)
        ttk.Button(frame7, text = TypeNameInter[13], command = self.impint13).grid(row = 17, column = 7)
        ttk.Button(frame7, text = TypeNameInter[14], command = self.impint14).grid(row = 17, column = 8)
        frame8 = LabelFrame(frame2, text = 'Elige el tipo de acorde y luego el intervalo a utilizar')
        frame8.grid(row = 18, column = 0, columnspan = 20, pady = 20) 
        ttk.Button(frame8, text = TypeNameChord[0], command = chordmod0).grid(row = 19, column = 1)
        ttk.Button(frame8, text = TypeNameChord[1], command = chordmod1).grid(row = 19, column = 2)
        ttk.Button(frame8, text = TypeNameChord[2], command = chordmod2).grid(row = 19, column = 3)
        ttk.Button(frame8, text = TypeNameChord[3], command = chordmod3).grid(row = 19, column = 4)
        ttk.Button(frame8, text = TypeNameChord[4], command = chordmod4).grid(row = 19, column = 5)
        ttk.Button(frame8, text = TypeNameChord[5], command = chordmod5).grid(row = 19, column = 6)
        ttk.Button(frame8, text = TypeNameChord[6], command = chordmod6).grid(row = 19, column =7)
        ttk.Button(frame8, text = TypeNameChord[7], command = chordmod7).grid(row = 19, column = 8)
        ttk.Button(frame8, text = TypeNameChord[8], command = chordmod8).grid(row = 19, column =9 )
        ttk.Button(frame8, text = TypeNameChord[9], command = chordmod9).grid(row = 19, column = 10)
        ttk.Button(frame8, text = TypeNameChord[10], command = chordmod10).grid(row = 19, column = 11)
        ttk.Button(frame8, text = TypeNameInter[0], command = self.impmod0).grid(row = 20, column = 1)
        ttk.Button(frame8, text = TypeNameInter[1], command = self.impmod1).grid(row = 20, column = 2)
        ttk.Button(frame8, text = TypeNameInter[2], command = self.impmod2).grid(row = 20, column = 3)
        ttk.Button(frame8, text = TypeNameInter[3], command = self.impmod3).grid(row = 20, column = 4)
        ttk.Button(frame8, text = TypeNameInter[4], command = self.impmod4).grid(row = 20, column = 5)
        ttk.Button(frame8, text = TypeNameInter[5], command = self.impmod5).grid(row = 20, column = 6)
        ttk.Button(frame8, text = TypeNameInter[6], command = self.impmod6).grid(row = 20, column = 7)
        ttk.Button(frame8, text = TypeNameInter[7], command = self.impmod7).grid(row = 21, column = 1)  
        ttk.Button(frame8, text = TypeNameInter[8], command = self.impmod8).grid(row = 21, column = 2)  
        ttk.Button(frame8, text = TypeNameInter[9], command = self.impmod9).grid(row = 21, column = 3)  
        ttk.Button(frame8, text = TypeNameInter[10], command = self.impmod10).grid(row = 21, column = 4)  
        ttk.Button(frame8, text = TypeNameInter[11], command = self.impmod11).grid(row = 21, column = 5)  
        ttk.Button(frame8, text = TypeNameInter[12], command = self.impmod12).grid(row = 21, column = 6)  
        ttk.Button(frame8, text = TypeNameInter[13], command = self.impmod13).grid(row = 21, column = 7)  
        ttk.Button(frame8, text = TypeNameInter[14], command = self.impmod14).grid(row = 21, column = 8)
        self.blank = ttk.Label(self.wind, text="")
        self.blank.grid(row=22, column=1,columnspan=50)
        
    def impes0(self):
        Scale.__init__(self,TypeConstScal[0], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes1(self):
        Scale.__init__(self,TypeConstScal[1], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes2(self):
        Scale.__init__(self,TypeConstScal[2], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes3(self):
        Scale.__init__(self,TypeConstScal[3], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes4(self):
        Scale.__init__(self,TypeConstScal[4], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes5(self):
        Scale.__init__(self,TypeConstScal[5], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes6(self):
        Scale.__init__(self,TypeConstScal[6], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes7(self):
        Scale.__init__(self,TypeConstScal[7], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes8(self):
        Scale.__init__(self,TypeConstScal[8], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes9(self):
        Scale.__init__(self,TypeConstScal[9], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes10(self):
        Scale.__init__(self,TypeConstScal[10], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes11(self):
        Scale.__init__(self,TypeConstScal[11], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes12(self):
        Scale.__init__(self,TypeConstScal[12], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes13(self):
        Scale.__init__(self,TypeConstScal[13], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes14(self):
        Scale.__init__(self,TypeConstScal[14], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes15(self):
        Scale.__init__(self,TypeConstScal[15], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes16(self):
        Scale.__init__(self,TypeConstScal[16], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes17(self):
        Scale.__init__(self,TypeConstScal[17], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impes18(self):
        Scale.__init__(self,TypeConstScal[18], note)
        self.aux= self.imprimir1()
        self.imprimirfinal()
    def impch0(self):
        Chord.__init__(self,TypeConstChord[0], note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch1(self):
        Chord.__init__(self,TypeConstChord[1],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch2(self):
        Chord.__init__(self,TypeConstChord[2],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch3(self):
        Chord.__init__(self,TypeConstChord[3],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch4(self):
        Chord.__init__(self,TypeConstChord[4],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch5(self):
        Chord.__init__(self,TypeConstChord[5],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch6(self):
        Chord.__init__(self,TypeConstChord[6],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch7(self):
        Chord.__init__(self,TypeConstChord[7],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch8(self):
        Chord.__init__(self,TypeConstChord[8],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch9(self):
        Chord.__init__(self,TypeConstChord[9],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impch10(self):
        Chord.__init__(self,TypeConstChord[10],note)
        self.aux = self.imprimir2()
        self.imprimirfinal()
    def impint0(self):
        Interval.__init__(self,TypeConstInter[0], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint1(self):
        Interval.__init__(self,TypeConstInter[1], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint2(self):
        Interval.__init__(self,TypeConstInter[2], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint3(self):
        Interval.__init__(self,TypeConstInter[3], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint4(self):
        Interval.__init__(self,TypeConstInter[4], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint5(self):
        Interval.__init__(self,TypeConstInter[5], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint6(self):
        Interval.__init__(self,TypeConstInter[6], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint7(self):
        Interval.__init__(self,TypeConstInter[7],note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint8(self):
        Interval.__init__(self,TypeConstInter[8], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint9(self):
        Interval.__init__(self,TypeConstInter[9],note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint10(self):
        Interval.__init__(self,TypeConstInter[10], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint11(self):
        Interval.__init__(self,TypeConstInter[11], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint12(self):
        Interval.__init__(self,TypeConstInter[12], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint13(self):
        Interval.__init__(self,TypeConstInter[13],note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impint14(self):
        Interval.__init__(self,TypeConstInter[14], note)
        self.aux = self.imprimir4()
        self.imprimirfinal()
    def impmod0(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[0])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod1(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[1])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod2(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[2])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod3(self):
        ModularChord.__init__(self, TypeConstChord[chordv],note, TypeConstInter[3])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod4(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[4])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod5(self):
        ModularChord.__init__(self, TypeConstChord[chordv],note, TypeConstInter[5])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod6(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[6])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod7(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[7])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod8(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[8])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod9(self):
        ModularChord.__init__(self, TypeConstChord[chordv],note, TypeConstInter[9])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod10(self):
        ModularChord.__init__(self, TypeConstChord[chordv],note, TypeConstInter[10])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod11(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[11])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod12(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[12])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod13(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[13])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    def impmod14(self):
        ModularChord.__init__(self, TypeConstChord[chordv], note, TypeConstInter[14])
        self.aux = self.imprimir5()
        self.imprimirfinal()
    
    def imprimirfinal(self):
        self.blank['text'] = self.aux
        #print(self.aux)

if __name__ == "__main__":
    application = Product(root)
    root.mainloop()