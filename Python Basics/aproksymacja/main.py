#! python3
import matplotlib.pyplot as plt
import pandas as pd
import math

# oblicza wartosc wielomianu p w punkcie x
def P(x, p):
    w = 0
    for i in range(len(p)): w += pow(x, i) * p[i]
    return w

#oblicza wartosc k-tego c
def ck(p, dates2):
    licznik = 0
    mianownik = 0
    for v in dates2:
        licznik += v * pow(P(v, p), 2)
        mianownik += pow(P(v, p), 2)
    return licznik / mianownik
 
# oblicza wartosc k-tego d
def dk(p_1, p_2, dates2):
    licznik = 0
    mianownik = 0
    for v in dates2:
        licznik += pow(P(v, p_1), 2)
        mianownik += pow(P(v, p_2), 2)
    return licznik / mianownik

# oblicza wartosc lewej strony wzoru rekurencyjnego
def left_side(c, p):
    temp = [ i for i in p]
    pt = [p[i] * c for i in range(len(p))]
    temp.insert(0, 0)
    for i in range(len(pt)): temp[i] -= pt[i]
    return temp

# oblicza wartosc prawej strony wzoru rekurencyjnego
def right_side(d, p):
    return [t * d for t in p]

# oblicza roznice lewej i prawej stronie we wzorze rekurencyjnym  
def poly_sub(l, r):
    temp = [i for i in l]
    for i in range(len(r)):
        temp[i] -= r[i]
    return temp

# wylicza wartosc k-tego a
def ak(p, vals, version, dates):
    licznik = 0
    mianownik = 0
    for i in range(0, len(dates)):
        if vals[i] == 0:
            vals[i] += 0.01
        if version: licznik += math.log(vals[i], math.e) * P(dates[i], p)
        else: licznik += vals[i] * P(dates[i], p)
        mianownik += pow(P(dates[i], p), 2)
    return licznik / mianownik

# oblicza wszystkie p, c, d
def find_all_pk_c_d(dates2, m):
    cc = []
    dd = []
    Ps = []
    Ps.append([1])
    cc.append(ck([1], dates2))
    Ps.append([-cc[0], 1])
    for i in range(2, m + 1):
        cc.append(ck(Ps[i - 1], dates2))
        dd.append(dk(Ps[i - 1], Ps[i - 2], dates2))
        L = left_side(cc[i - 1], Ps[i - 1])
        R = right_side(dd[i - 2], Ps[i - 2])
        Ps.append(poly_sub(L, R))
    return (Ps, cc, dd)

# wyznaczam postac w* oblicza wszytkie a
def finds_w_a(m, Ps, vals, version, dates):
    aa = []
    w = [0 for i in range(m + 1)]
    for i in range(m + 1):
        aa.append(ak(Ps[i], vals, version, dates))
        for j in range(len(Ps[i])):
            w[j] += aa[i] * Ps[i][j]
    return (w, aa)

# oblicza wartosc w* w punkcie x
def W_Clen(x, m, aa, cc, dd):
    # wyrownuje indeksy na potrzebu alg. clen
    cc.append(0)
    dd.append(0)
    dd.append(0)
    b_n_2 = 0
    b_n_1 = 0
    for i in range(m, -1, -1):
        temp = aa[i] + ((x - cc[i]) * b_n_1) - (dd[i] * b_n_2)
        b_n_2 = b_n_1
        b_n_1 = temp
    return temp


def draw(m, indicators):

    df = pd.read_csv('COVID-19_w_Polsce_-_Wzrost.csv')
    
    for i in indicators:

        vals = list(df[i])[:-1]
        dates = [i for i in range(len(df['Data'].tolist()))][:-1]
        
        while len(dates) > len(vals): vals.append(vals[-1])

        if str(vals[-1]) == 'nan': vals[-1] = vals[-2] 

        Ps, cc, dd = find_all_pk_c_d(dates, m)
        w1, aa1 = finds_w_a(m, Ps, vals, 0, dates)
        w2, aa2 = finds_w_a(m, Ps, vals, 1, dates)

        fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout = True)

        ax1.plot(dates, vals, 'o', markersize=1, label=i)
        ax2.plot(dates, vals, 'o', markersize=1, label=i)

        ax1.plot(dates, [W_Clen(i, m, aa1, cc, dd) for i in dates])
        ax2.plot(dates, [pow(math.e, W_Clen(i, m, aa2, cc, dd)) for i in dates])

        fig.suptitle(i, fontsize=15)
        ax1.set_title('polynomial')
        ax2.set_title('exp')
    plt.show()



if __name__ == '__main__':

    # ['Suma zgonów', 'Suma wyzdrowień', 'Liczba nieaktywnych przypadków', 'Liczba aktywnych przypadków']
    indicators = ['Suma zgonów']
    m = 4 # stopien wielomianu
    draw(m, indicators)


    
