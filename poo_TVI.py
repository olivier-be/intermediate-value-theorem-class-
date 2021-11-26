from math import sqrt
class TVI:
    def __init__(self,a,puissance_a,b,puissance_b,c,puissance_c,valeur_chercher):
        self._tabpuissance=[puissance_a,puissance_b,puissance_c]
        self._tababc=[a,b,c]
        self._tababc_prime = [self._tababc*self._tabpuissance[i] for i in range(3)]
        self._puissance_prime=[self._tabpuissance[i]-1 for i in range(3)]
        self._TVI=False
        self.r1=0
        self.r2=0
        self._chr=valeur_chercher
        self._signe_segmenttab= ["0"] * 3

    def __eq__(self,a):
        if type(a)==bool:
            return True
        else:
            assert 1==2,("l'égaliter comparar un bool a un ",type(a))
    def __str__(self):
        if TVI==True:
            return("True")
        else :
            return("TVI False")

    def racine(self):
        if self._tabpuissance[0]>0 or self._tabpuissance[1]>0 or self._tabpuissance[2]>0 :
            d=self._tababc[1]*self._tababc[1]-(4*self._tababc[0]*self._tababc[2])
            if d>0:
                self._r1=(-self._tababc[1]-sqrt(d))/(2*self._tababc[0])
                self._r2 = (-self._tababc[1]+sqrt(d)) / (2 * self._tababc[0])
            if d == 0:
                self._r1 = (-self._tababc[1] - sqrt(d)) / (2 * self._tababc[0])
                self._r2 = self._r1

    def signe_segment(self):
        z=self.cathegorie_segment()
        for i in range(0, 2, 2):
            if self._tababc[i] > 0:
                self._signe_segmenttab[i] = "+"
            else:
                self._signe_segmenttab[i] = "-"
        if z==("1 racine"):
            self._signe_segmenttab[1]="0"
        elif z==("sans racine"):
            self._signe_segmenttab[1] =self._signe_segmenttab[0]
        elif z==("deux racines distinctes"):
            if self._signe_segmenttab[0] == "+":
                self._signe_segmenttab[1] ="-"
            else:
                self._signe_segmenttab[1] ="+"

    def cathegorie_segment (self):
        self.racine()
        if self._r1==self._r2:
            return("1 racine")
        elif self._r1!=self._r2 and self._tababc[1]*self._tababc[1]-(4*self._tababc[0]*self._tababc[2])<0:
            return ("sans racine")
        else:
            return("deux racines distinctes")

    def fonction(self,inconue):
        return self._tababc[0]*inconue**self._tabpuissance[0]+self._tababc[1]*inconue**self._tabpuissance[1]+self._tababc[2]*inconue**self._tabpuissance[2]

    def TVI(self):
        comp=0
        print("on sait que:")
        print("f est continue car c'est un polynome")
        if self._chr>self.fonction(self.r1):
            print("le nombre a pour intervalle]",self._signe_segmenttab[0],"+inf;",self.r1,"]")
            comp+=1
        elif self._chr>self.fonction(self.r2):
            print("le nombre a pour intervalle[", self.r2,";",self._signe_segmenttab[2],"inf[")
            comp += 1
        elif self._chr>self.fonction(self.r1) and self._chr<self.fonction(self.r2):
            print("le nombre a pour intervalle[", self.r1, ";", self.r2,"]")
            comp += 1
        print("la valeur apprait {} de fois",format(comp))