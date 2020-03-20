class Wezel():
    def __init__(self,dane=None):
        self.dane=dane
        self.prawy=None
        self.lewy=None
    def suma_poddrzewa(self,dane):
        suma=self.dane
        if self.prawy!=None:
            suma+=self.prawy.suma_poddrzewa(self.prawy.dane)
        if self.lewy!=None:
            suma+=self.lewy.suma_poddrzewa(self.lewy.dane)
        return suma
    def ilosc_wezlow_poddrzewa(self,dane):
        ilosc = 1
        if self.prawy != None:
            ilosc += self.prawy.ilosc_wezlow_poddrzewa(self.prawy.dane)
        if self.lewy != None:
            ilosc += self.lewy.ilosc_wezlow_poddrzewa(self.lewy.dane)
        return ilosc
    def mediana(self,dane):
        lista=[int(self.dane)]
        if self.prawy != None:
            lista.extend(self.prawy.mediana(self.prawy.dane))
        if self.lewy != None:
            lista.extend(self.lewy.mediana(self.lewy.dane))
        return lista
wartosci=[int(5),int(3),int(7),int(2),int(5),int(1),int(0),int(2),int(8),int(5)]
W=[i for i in range(10)]
for z,wartosc in enumerate(wartosci):
    W[z]=Wezel()
    W[z].dane=wartosc
W[0].prawy,W[0].lewy=W[2],W[1]
W[1].prawy,W[1].lewy=W[4],W[3]
W[2].prawy,W[2].lewy=W[6],W[5]
W[6].prawy,W[6].lewy=W[8],W[7]
W[8].lewy=W[9]
print("Dla jakiego numeru wezla policzyc sume, srednia i mediane w poddrzewie? Wezly sa ponumerowane w zakresie od 0-9")
x=input()
print("suma wartosci poddrzewa wynosi; ")
print(W[int(x)].suma_poddrzewa(W[int(x)].dane))
print("srednia wartosc to: ")
print(W[int(x)].suma_poddrzewa(W[int(x)].dane)/W[int(x)].ilosc_wezlow_poddrzewa(W[int(x)].dane))
print("mediana wynosi")
lista_posortowana=sorted(W[int(x)].mediana(W[int(x)].dane))
a=len(lista_posortowana)
if a%2==1:
    print(lista_posortowana[int(a/2)])
else:
    print((lista_posortowana[int(a/2)-1]+lista_posortowana[int(a/2)])/2)



