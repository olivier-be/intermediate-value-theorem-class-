from math import sqrt
class TVI:
    def __init__(self,a,puissance_a,b,puissance_b,c,puissance_c,d,puissance_d,valeur_chercher):
        self._tabpuissance=[puissance_a,puissance_b,puissance_c,puissance_d]
        self._tababcd=[a, b, c, d]
        self._tababcd_prime = [self._tababcd[i] * self._tabpuissance[i] for i in range(4)]
        self._tabpuissance_prime=[self._tabpuissance[i] - 1 for i in range(4)]
        self._TVI=False
        self._r1=0
        self._r2=0
        self._chr=valeur_chercher
        self._signe_segmenttab= ["0"] * 3
        self.z=[puissance_a,puissance_b,puissance_c,puissance_d]
        self._tab_variation=["0"]*3
        self._degre=puissance_a
        """ while self._tabpuissance==self.z:
            for i in range(len(self._tabpuissance)-1):
                if self._tabpuissance[i]>self._tabpuissance[i+1]:
                    temp=self._tabpuissance[i+1]
                    tempp=self._tababc[i+1]
                    self._tabpuissance[i+1]=self._tabpuissance[i]
                    self._tababc[i + 1]=self._tababc[i]
                    self._tababc[i]=tempp
                    self._tabpuissance[i]=temp
                """

    def __eq__(self,a):
        if type(a)==bool:
            return True
        else:
            assert 1==2,("l'égaliter comparar un bool a un ",type(a))
    def __str__(self):
        self.TVI()
        if self._TVI==True:
            print("True TVI")
            return("True TVI")

        else :
            print("TVI False")
            return("TVI False")

    def racine(self,puissance,abcd):
        if puissance[0]>0 or puissance[1]>0 or puissance[2]>0 or puissance[3]>0:
            d= abcd[1] * abcd[1] - (4 * abcd[0] * abcd[2])
            print(d)
            if d>0:
                self._r1= (-abcd[1] - sqrt(d)) / (2 * abcd[0])
                self._r2 = (-abcd[1] + sqrt(d)) / (2 * abcd[0])
                print((-self._tababcd_prime[1] + sqrt(d)) / (2 * abcd[0]))
            elif d == 0:
                self._r1 = (-abcd[1] - sqrt(d)) / (2 * abcd[0])
                self._r2 = self._r1
            print("racine", self._r1, self._r2)


    def signe_segment(self):
        z=self.cathegorie_segment()
        for i in range(0, 3):
            print(i)
            if self._tababcd[0] > 0:
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
    def tab_variation(self):
        for i in range (len(self._signe_segmenttab)):
            if self._signe_segmenttab[i]=="+":
                self._tab_variation[i]="croissant"
            else:
                self._tab_variation[i] = "decroissant"


    def cathegorie_segment (self):
        if self._degre==3:
            self.racine(self._tabpuissance_prime,self._tababcd_prime)
        elif self._degre==2:
            self.racine( self._tabpuissance,self._tababcd)
        if self._r1==self._r2:
            return("1 racine")
        elif self._r1!=self._r2 and self._tababcd[1]*self._tababcd[1]-(4 * self._tababcd[0] * self._tababcd[2])<0:
            return ("sans racine")
        else:
            return("deux racines distinctes")

    def fonction(self,inconue):
        return self._tababcd[0] * inconue ** self._tabpuissance[0] + self._tababcd[1] * inconue ** self._tabpuissance[1] + self._tababcd[2] * inconue ** self._tabpuissance[2]

    def TVI(self):
        self.signe_segment()
        comp=0
        print("on sait que:")
        print("f est continue car c'est un polynome")
        if (self._chr<=self.fonction(self._r1) and self._signe_segmenttab[0]=="-") or (self._chr>=self.fonction(self._r1) and self._signe_segmenttab[0]=="+") :
            print("le nombre a pour intervalle ]",self._signe_segmenttab[0],"inf;", self._r1, "]")
            comp+=1
        if  (self._chr<=self.fonction(self._r2) and self._signe_segmenttab[2]=="-") or (self._chr>=self.fonction(self._r2) and self._signe_segmenttab[2]=="+"):
            print("le nombre a pour intervalle[ ",self._r2, ";", self._signe_segmenttab[2], "inf[")
            comp += 1
        if self.fonction(self._r1)< self.fonction(self._r2):
            if self._chr>=self.fonction(self._r1) and self._chr<=self.fonction(self._r2):
                print("le nombre a pour intervalle[ ",self._r1, ";", self._r2, "]")
                comp += 1
        else:
            if self._chr>=self.fonction(self._r2) and self._chr<=self.fonction(self._r1):
                print("le nombre a pour intervalle[ ",self._r1, ";", self._r2, "]")
                comp += 1
        print("la valeur apprait {} fois".format(comp))
        if comp>0:
            self._TVI=True
