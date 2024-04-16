#! python3
# Patryk Rybak

from numbers import Number


class VariableNotFoundException(Exception):
    pass


class DivisionByZeroException(Exception):
    pass


class InputValuesException(Exception):
    pass


class Wyrazenie:
    
    def __init__(self, wyrazenie):
        if isinstance(wyrazenie, Wyrazenie):
            self.wyrazenie = wyrazenie
        else:
            raise InputValuesException("Zle dane wejsciowe")
            
    def oblicz(self, zmienne):
        return self.wyrazenie.oblicz(zmienne)

    def __str__(self) -> str:
        return str(self.wyrazenie)

    def __add__(self, wyrazenie2):
        return Dodaj(self.wyrazenie, wyrazenie2)

    def __mul__(self, wyrazenie2):
        return Razy(self.wyrazenie, wyrazenie2)

    def uprosc(self):
        return self.wyrazenie.uprosc()

    @staticmethod
    def uprosc(wyrazenie):
        return wyrazenie.uprosc()


    
class Zmienna(Wyrazenie):

    def __init__(self, s):
        if isinstance(s, str):
            super().__init__(self)
            self.s = s
        else:
            raise InputValuesException("Zle dane wejsciowe") 

    def __str__(self) -> str:
        return self.s.center(3)

    def oblicz(self, zmienne):
        if self.s in zmienne:
            return zmienne[self.s]
        else:
            raise VariableNotFoundException("Brak przypisania wartosci do zmiennej")

    def uprosc(self):
        return self


class Stala(Wyrazenie):
    
    def __init__(self, n):
        if isinstance(n, Number):
            super().__init__(self)
            self.v = n
        else:
            raise InputValuesException("Zle dane wejsciowe")

    def __str__(self) -> str:
        return str(self.v).center(3)

    def oblicz(self, zmienne):
        return self.v

    def uprosc(self):
        return self


class Razy(Wyrazenie):

    def __init__(self, pierwsze, drugie):
        if not(isinstance(pierwsze, Wyrazenie) and isinstance(drugie, Wyrazenie)):
            raise InputValuesException("Zle dane wejsciowe")
        else:
            super().__init__(self)
            self.pierwsze = pierwsze
            self.drugie = drugie

    def __str__(self) -> str:
        return "(" + str(self.pierwsze) + " * " + str(self.drugie) + ")"

    def oblicz(self, zmienne):
        return self.pierwsze.oblicz(zmienne) * self.drugie.oblicz(zmienne)
    
    def uprosc(self):
        pierwUpro = self.pierwsze.uprosc()
        drugUpro = self.drugie.uprosc()
        if (isinstance(pierwUpro, Stala) and pierwUpro.oblicz({}) == 0) or (isinstance(drugUpro, Stala) and drugUpro.oblicz({}) == 0):
            return Stala(0)
        else:
            return Razy(pierwUpro, drugUpro)


class Podziel(Wyrazenie):
    
    def __init__(self, pierwsze, drugie):
        if not(isinstance(pierwsze, Wyrazenie) and isinstance(drugie, Wyrazenie)):
            raise InputValuesException("Zle dane wejsciowe")
        else:
            super().__init__(self)
            self.pierwsze = pierwsze
            self.drugie = drugie

    def __str__(self) -> str:
        return "(" + str(self.pierwsze) + " / " + str(self.drugie) + ")"
        
    def oblicz(self, zmienne):
        temp1 =  self.pierwsze.oblicz(zmienne)
        temp2 = self.drugie.oblicz(zmienne)
        if temp2 == 0:
            raise DivisionByZeroException("Dzielenie przez zero")
        return temp1 / temp2

    def uprosc(self):
        return Podziel(self.pierwsze.uprosc(), self.drugie.uprosc())

class Dodaj(Wyrazenie):
    
    def __init__(self, pierwsze, drugie):
        if not(isinstance(pierwsze, Wyrazenie) and isinstance(drugie, Wyrazenie)):
            raise InputValuesException("Zle dane wejsciowe")
        else:
            super().__init__(self)
            self.pierwsze = pierwsze
            self.drugie = drugie
    
    def __str__(self) -> str:
        return "(" + str(self.pierwsze) + " + " + str(self.drugie) + ")"

    def oblicz(self, zmienne):
        return self.pierwsze.oblicz(zmienne) + self.drugie.oblicz(zmienne)

    def uprosc(self):
        pierwUpro = self.pierwsze.uprosc()
        drugUpro = self.drugie.uprosc()
        if isinstance(pierwUpro, Stala) and isinstance(drugUpro, Stala):
            return Stala(pierwUpro.oblicz({}) + drugUpro.oblicz({}))
        elif isinstance(pierwUpro, Stala) and pierwUpro.oblicz({}) == 0:
            return drugUpro
        elif isinstance(drugUpro, Stala) and drugUpro.oblicz({}) == 0:
            return pierwUpro
        return Dodaj(pierwUpro, drugUpro)


class Odejmij(Wyrazenie):
    
    def __init__(self, pierwsze, drugie):
        if not(isinstance(pierwsze, Wyrazenie) and isinstance(drugie, Wyrazenie)):
            raise InputValuesException("Zle dane wejsciowe")
        else:
            super().__init__(self)
            self.pierwsze = pierwsze
            self.drugie = drugie

    def __str__(self) -> str:
        return "(" + str(self.pierwsze) + " - " + str(self.drugie) + ")"

    def oblicz(self, zmienne):
        return self.pierwsze.oblicz(zmienne) - self.drugie.oblicz(zmienne)

    def uprosc(self):
        return Odejmij(self.pierwsze.uprosc(), self.drugie.uprosc())


print("\nMul add str:")
sample1 = Zmienna("x")
sample2 = Stala(1)
print(f"sample1: {sample1}\nsample2: {sample2}\n+: {sample1 + sample2}\n*: {sample1 * sample2}")


print("\nWyjatki:")
try:
    sample = Podziel(Dodaj(Stala(1), Zmienna("x")), Stala(0))
    res = sample.oblicz({"x": 1})
except Exception as e: print(e) 
try:
    sample = Dodaj(Zmienna("x"), Zmienna("y"))
    res = sample.oblicz({"x": 1})
except Exception as e: print(e) 
try:
    sample = Zmienna(2)
except Exception as e: print(e) 


print("\nUpraszacznie:")
sample = Podziel(Razy(Dodaj(Stala(2), Stala(3)), Dodaj(Dodaj(Stala(0), Stala(0)), Zmienna("y"))), Stala(2))
print(sample)
uproszczoneSample = Wyrazenie.uprosc(sample)
print(uproszczoneSample)
