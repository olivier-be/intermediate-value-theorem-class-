from math import sqrt
class TVI:
    def __init__(self, a, power_x_of_a, b, power_x_of_b, c, power_x_of_c, d, power_x_of_d, valeur_search, interval1, interval2, intervalac,langue):
        self._tabpower=[power_x_of_a, power_x_of_b, power_x_of_c, power_x_of_d]
        self._tababcd=[a, b, c, d]
        self._tababcd_prime = [self._tababcd[i] * self._tabpower[i] for i in range(4)]
        self._tabpower_prime=[self._tabpower[i] - 1 for i in range(4)]
        self._TVI=False
        self._r1=-1
        self._r2=1
        self._shr=valeur_search
        self._signe_segmenttab= ["0"] * 3
        self.z=[power_x_of_a, power_x_of_b, power_x_of_c, power_x_of_d]
        self._tab_variation=["0"]*3
        self._degre=power_x_of_a
        self._interval=interval1
        self._interval2=interval2
        self._intervalb=intervalac
        self._languefr=["on sait que:","f est continue car c'est un polynome","le nombre a pour intervalle ]","la valeur apprait {} fois","l'égaliter comparar un type TVI a un ","racine","1 racine","deux racine distincte"]
        self._langueus=["we know that:","f is continuous because it was an polynomail","the number search have for interval","the value appear {} time","the egalty compared TVI to","root","1 root","whitout root","two root distinct"]
        self._languechoice=["a","a","a","a","a","a""a","a","a","a","a","a","a""a","a","a","a"]
        self._no_root=False
        self._z=0
        self._d=0
        while self._tabpower==self._tabpower.sort(reverse=True):
            for i in range(len(self._tabpower)-1):
                if self._tabpower[i]>self._tabpower[i+1]:
                    temp=self._tabpower[i+1]
                    tempp=self._tababcd[i+1]
                    self._tabpower[i+1]=self._tabpower[i]
                    self._tababcd[i + 1]=self._tababcd[i]
                    self._tababcd[i]=tempp
                    self._tabpower[i]=temp


        if langue=="FR"or langue=="fr":
            self._languechoice=self._languefr
        elif langue=="US"or langue=="UK"or langue=="us"or langue=="uk":
            self._languechoice=self._langueus
        print(self._languechoice[7])

    def __eq__(self,a):
        if type(a)==TVI:
            #if a.
            return True
        else:
            assert 1==2,(self._languechoice[4],type(a))
    def __str__(self):
        self.TVI()
        if self._TVI==True:
            print("True TVI")
            return("True TVI")

        else :
            print("TVI False")
            return("TVI False")

    def root(self, power, abcd):

        if power[0]>0 or power[1]>0 or power[2]>0 or power[3]>0:
            self._d= abcd[1] * abcd[1] - (4 * abcd[0] * abcd[2])
            print(self._d)
            if self._d>0:
                self._r1= (-abcd[1] - sqrt(self._d)) / (2 * abcd[0])
                self._r2 = (-abcd[1] + sqrt(self._d)) / (2 * abcd[0])
                print((-self._tababcd_prime[1] + sqrt(self._d)) / (2 * abcd[0]))
                print(self._languechoice[6], self._r1, self._r2)
            elif self._d == 0:
                self._r1 = (-abcd[1] - sqrt(self._d)) / (2 * abcd[0])
                self._r2 = self._r1
                print(self._languechoice[6], self._r1, self._r2)
            elif self._d<0:
                self._no_root=True


    def sign_segment(self):
        print(self._r1)
        z=self.cathegorie_segment()
        for i in range(0, 3):
            print(i)
            if self._no_root==True:
                if self._tababcd[0] > 0 :
                    self._signe_segmenttab[i] = "+"
                else:
                    self._signe_segmenttab[i] = "-"
                if z == (self._languechoice[5]):
                    self._signe_segmenttab[1] = "0"
                elif z == (self._languechoice[6]):
                    self._signe_segmenttab[1] = self._signe_segmenttab[0]
            else:
                if self._tababcd[0] > 0 :
                    self._signe_segmenttab[i] = "-"
                else:
                    self._signe_segmenttab[i] = "+"
                if self._signe_segmenttab[0] == "+":
                    self._signe_segmenttab[1] = "-"
                    self._signe_segmenttab[2] = "-"
                else:
                    self._signe_segmenttab[1] = "+"
                    self._signe_segmenttab[2] = "+"

    def tab_variation(self):
        for i in range (len(self._signe_segmenttab)):
            if self._signe_segmenttab[i]=="+":
                self._tab_variation[i]="croissant"
            else:
                self._tab_variation[i] = "decroissant"


    def cathegorie_segment (self):
        print("aaaa",self._tababcd_prime[1]*self._tababcd_prime[1]-(4 * self._tababcd_prime[0] * self._tababcd_prime[2]),self._tababcd[1]*self._tababcd[1]-(4 * self._tababcd[0] * self._tababcd[2]))
        if (self._tababcd_prime[1]*self._tababcd_prime[1]-(4 * self._tababcd_prime[0] * self._tababcd_prime[2])>=0 and self._degre==3) or (self._tababcd[1]*self._tababcd[1]-(4 * self._tababcd[0] * self._tababcd[2])>=0 and self._degre==2) :
            print("tttttttttttttt")
            if self._degre==3 and (self._tababcd_prime[1] * self._tababcd_prime[1] - (4 * self._tababcd_prime[0] * self._tababcd_prime[2]))>0 :
                self.root(self._tabpower_prime, self._tababcd_prime)
            elif self._degre==2 and (self._tababcd[1] * self._tababcd[1] - (4 * self._tababcd[0] * self._tababcd[2]))>0 :
                self.root(self._tabpower, self._tababcd)
            if self._r1==self._r2:
                return(self._languechoice[5])
        else:
            print("rrrrrrrrrrrr",(self._r1),-1*2)
            print(self._tabpower)
            while ((self.fonction(self._r1) < self._shr)and (self.fonction(self._r2) < self._shr)):
                self._r1 = self._r1 * 2
                self._r2 = self._r2 * 2
                print("v",self._r1,self._r2)
            print("test",self.fonction(-0.99993896484375))
            print("rre",self._r1 , self._r2)
            while self._r2 - self._r1 > 0.0001:
                self._z = (self._r2 - abs(self._r1)) / 2
                if self.fonction(self._r1)-self._shr * self.fonction(self._z)-self._shr <= 0:
                    self._r2 = self._z
                else:
                    self._r1 = self._z
                print(self._z,self._r2)
            return (self._languechoice[7])
    def fonction(self, x):
        for i in range(len(self._tabpower)):
            if self._tabpower[i]<0:
                self._tabpower[i]=0
        return self._tababcd[0] * x ** self._tabpower[0] + self._tababcd[1] * x ** self._tabpower[1] + self._tababcd[2] * x ** self._tabpower[2]+self._tababcd[3] * x ** self._tabpower[3]
    def TVI(self):
        self.sign_segment()
        comp=0
        print(self._r1)
        print(self._languechoice[0])
        print(self._languechoice[1])
        if self._no_root==True:
            if (self._shr <= self.fonction(self._r1) and self._signe_segmenttab[0] == "-" and (
                    self._interval < self._r1) or self._intervalb == False) or (
                    self._shr >= self.fonction(self._r1) and self._signe_segmenttab[0] == "+" and (
                    self._interval > self._r1) or self._intervalb == False):
                print(self._languechoice[2], "]", self._signe_segmenttab[0], "inf;", self._r1, "]")
                comp += 1
            if (self._shr <= self.fonction(self._r2) and self._signe_segmenttab[2] == "-" and (
                    self._interval < self._r2) or self._intervalb == False) or (
                    self._shr >= self.fonction(self._r2) and self._signe_segmenttab[2] == "+" and (
                    self._interval > self._r2) or self._intervalb == False):
                print(self._languechoice[2], "[", self._r2, ";", self._signe_segmenttab[2], "inf[")
                comp += 1
            if self.fonction(self._r1) < self.fonction(self._r2) and (
                    ((self._interval < self._r1) and ((self._interval < self._r2))) or self._intervalb == False):
                if self._shr >= self.fonction(self._r1) and self._shr <= self.fonction(self._r2):
                    print(self._languechoice[2], "[", self._r1, ";", self._r2, "]")
                    comp += 1
            else:
                if self._shr>=self.fonction(self._r2) and self._shr<=self.fonction(self._r1) and (((self._interval > self._r1) and ((self._interval > self._r2))) or self._intervalb == False):
                    print(self._languechoice[2] ,self._r1, ";", self._r2, "]")
        else:
            if self.fonction(self._r1)>self._shr and(((self._interval > self._r1) and ((self._interval > self._r2))) or self._intervalb == False):
                print(self._languechoice[2], "[", self._r2, ";", self._signe_segmenttab[2], "inf[")
                comp += 1
            if self.fonction(self._r1)<self._shr and (((self._interval > self._r1) and ((self._interval > self._r2))) or self._intervalb == False):
                print(self._languechoice[2], self._signe_segmenttab[0], "inf;", self._r1, "]")
                comp += 1
        print(self._languechoice[3].format(comp))
        if comp>0:
            self._TVI=True
