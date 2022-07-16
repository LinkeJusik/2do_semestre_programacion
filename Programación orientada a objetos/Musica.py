Cromaticsharp = ["do","do#","re","re#","mi","fa","fa#","sol","sol#","la","la#","si"]
Cromaticbemol = ["do","reb","re","mib","mi","fa","solb","sol","lab","la","sib","si"]

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
        print("Tu escala de",self.reposo,TypeNameScal[self.aux],"es",self.construir1())

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
        print("Tu acorde de",self.tonica,TypeNameChord[self.aux],"es",self.construir2())

class Tonalidad(Scale):
    def __init__(self, a = TypeConstScal[1], b = Cromaticsharp[0]):
        self.tipo = a
        self.tipo.pop()
        self.reposo = b
        self.cromatic = definition(self.reposo)
    def acord(self):
        self.res = self.construir1()
        for i in range(0,len(self.res),1):
            self.aux = usar_intervalo([2,2], i, self.res, 0)
            print(self.aux.split(','))
    def imprimir3(self):
        self.aux = TypeConstScal.index(self.tipo)
        print("Tu escala de",self.reposo,TypeNameScal[self.aux],"es",self.construir1())
        print("Y los acordes contruidos sobre esta escala son: ")
        self.acord()

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
        print("Tu intevalo de",TypeNameInter[self.aux],"sobre",self.reposo,"es",self.construir4())
         
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
        print("Tu acorde de",self.tonica,TypeNameChord[self.aux2],"subido",self.inter,"semitonos es",self.aux,"y se llama", self.aux[0],TypeNameChord[self.aux2])


        
Ecroma = Scale(TypeConstScal[0], Cromaticsharp[5])
#Ecroma.imprimir1()
Emayor = Scale(TypeConstScal[1], Cromaticsharp[0])
#Emayor.imprimir1()
Epentatonica = Scale(TypeConstScal[3], Cromaticsharp[0])
Epentatonica.imprimir1()
Emenor = Scale(TypeConstScal[2], Cromaticsharp[9])
#Emenor.imprimir1()
Efrigio = Scale(TypeConstScal[6], Cromaticsharp[4])
#Efrigio.imprimir1()

Cmayor = Chord(TypeConstChord[0], Cromaticsharp[7])
#Cmayor.imprimir2()
Cmenor = Chord(TypeConstChord[1], Cromaticsharp[5]) 
#Cmenor.imprimir2()
Cmayor7 = Chord(TypeConstChord[2], Cromaticsharp[7])
#Cmayor7.imprimir2()
Cadd9 = Chord(TypeConstChord[3], Cromaticsharp[0])
#Cadd9.imprimir2()

Tmayor = Tonalidad(TypeConstScal[1], Cromaticsharp[0])
#Tmayor.imprimir3()
Tmenor = Tonalidad(TypeConstScal[2], Cromaticsharp[9])
#Tmenor.imprimir3()
Tdefecto = Tonalidad()
#Tdefecto.imprimir3()

InterQuintaJusta = Interval(TypeConstInter[7],Cromaticsharp[7])
#InterQuintaJusta.imprimir4()
InterSeptimaMayor = Interval(TypeConstInter[11],Cromaticsharp[10])
#InterSeptimaMayor.imprimir4()

CMayor4 = ModularChord(TypeConstChord[3], Cromaticsharp[0],TypeConstInter[8])
#CMayor4.imprimir5()