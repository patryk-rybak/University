# Wykład 4

## Co to są prywatne adresy IP? Jakie pule adresów są zarezerwowane na takie adresy?

Adresy prywatne to adresy przeznaczone dla sieci lokalnych.

Pakiety z takimi adresami nie są przekazywane przez routery.

W różnych sieciach mogą być te same adresy.

Pule adresów:
- 10.0.0.0/8 (jedna sieć klasy A),
- 172.16.0.0/12 (16 sieci klasy B),
- 192.168.0.0/16 (256 sieci klasy C).

## Co robi funkcja bind()?

Serwer związuje się z danym portem funkcją bind().

## Czym różnią się porty o numerach mniejszych niż 1024 od innych?

Do związania z portem ≤ 1024 potrzebne uprawnienia administratora.

## Jakie są zadania procesora routingu, portu wejściowego, portu wyjściowego i struktury przełączającej?

(domyśłnie - z strukturą przekazywania)

**Procesor routingu**:

- Kopiuje pakiety z portów wejściowych do RAM i z RAM do portów wyjściowych. (bez struktury przełączającej)
- Tworzy tablice przekazywania i wysyła je do portów wejściowych.

**Porty wejściowe**:

- Odbiera pakiet z łącza.
- Uaktualnia nagłówek IP (TTL, suma kontrolna).
- Sprawdza, do którego portu wyjściowego go przesłać.

**Porsty wyjściowe**:

- Jeśli rozmiar pakietu jest większy niż MTU (maximum transmission unit) łącza wyjściowego

**Struktura przełączające**:

-  Przekazywać pakiety z prędkością łącza (lub zbliżoną).

## Czym się różni przełączanie pakietów w routerze za pomocą RAM od przełączania za pomocą struktury przełączającej?

Przełączanie pakietów w routerze za pomocą RAM polega na przekazywaniu pakietów przez pamięć operacyjną (RAM), gdzie każdy pakiet jest analizowany przez procesor i podejmowane są decyzje routingowe. Natomiast przełączanie za pomocą struktury przełączającej (np. ASIC) odbywa się bezpośrednio w sprzęcie, gdzie pakiety są przekazywane na podstawie wcześniej zaprogramowanych reguł w specjalnej, zoptymalizowanej strukturze, co znacznie przyspiesza proces przekazywania pakietów.

## Jakie są pożądane cechy struktury przełączającej w routerze?

Przekazywać pakiety z prędkością zbliżoną do szybkości łącza. 

## Gdzie w routerze stosuje się buforowanie? Po co?

- **Przy portach wyjściowych**
    - Zapobiegają utracie pakietów przy czasowym zwiększeniu liczby pakietów
- **Przy portach wejściowych**
    - Na wyjściu FIFO jest 
    - Jeśli przepustowość struktury przełączającej jest za mała.
    - Pakiety kierowane do zajętych łącz wyjściowych są blokowane.

## Po co w portach wyjściowych klasyfikuje się pakiety?

- Szeregowanie względem priorytetów strumien
- Szeregowanie cykliczne (round-robin): po tyle samo pakietów z każdego strumienia.

## Co to jest blokowanie początku kolejki? Gdzie występuje? Jak się go rozwiązuje?

![image](https://hackmd.io/_uploads/BkHkzURmR.png)

## Rozwiń skrót LPM

longest prefix match

## Jakie znasz struktury danych implementujące LPM? Porównaj je?

...

## Co to jest pamięć TCAM? Jak można ją zastosować do implementacji LPM?

Implementacja LPM (5)

![image](https://hackmd.io/_uploads/BkBPfIAXA.png)


## Na czym polega fragmentacja IP? Gdzie się ją stosuje i dlaczego? Gdzie łączy się fragmenty?

Jak pakiet jest większy niż MTU łącza wyjściowego to dzielimy go na fragmenty. Dzielenie odbywa się na dowolnym routerze na trasie po to, aby możliwe było przesłanie pakieciku.

Fragmenty łączone są dopiero na komputerze docelowym.

## Co to jest MTU? Na czym polega technika wykrywania wartości MTU dla ścieżki?

Max Transmission Unit - maksymalna wielkość pakietu która może przejść przez łącze.

Wysyłający może też zbadać przepustowość ustawiając bit DF (dont fragmnet) w nagłówku IP. Wtedy jeśli konieczna fragmentacja to router wyrzuca pakiecik i odsuła ICMP (destination unreachable, can’t fragment) z rozmiarem MTU kolejnego łącza.

## Jak działa szeregowanie pakietów w buforze wyjściowym routera?

Pakiety przypisywane są do strumieni (działające na zasadzie FIFO) na podstawie adresu i portu źródłowego + docelowego. Potem pakiety szeregujemy w zależności od strumienia, czyli:

- względem priorytetów strumieni
- szeregowanie cykliczne (round-robin): po tyle samo pakietów z każdego strumienia.

## Jakie są różnice pomiędzy nagłówkami IPv4 i IPv6?

Różnice:

- **Długość nagłówka**
    - IPv4: Dł. headera od 20 do 60 bytes
    - IPv6: Dł. headera stale 40 bytes
- **Fragmentacja**
    - IPv4: Fragmentacja jest wykonywana zarówno przez hosty nadawcze, jak i przez routery pośrednie. Nagłówek IPv4 zawiera pola identyfikatora fragmentu, offsetu fragmentu i flagi, które wspomagają proces fragmentacji.
    - IPv6: Fragmentacja jest realizowana wyłącznie przez nadawcę, a nie przez routery pośrednie. W IPv6 fragmentacja jest obsługiwana przez rozszerzony nagłówek fragmentacji, jeśli jest potrzebny.
- **Suma kontrolna**
    - IPv4: Nagłówek zawiera
    - IPv6: Nagłówek nie zawiera (Decyzja ta wynika z kilku powodów: wiele warstw protokołów nad- i pod-warstwowych (takich jak TCP, UDP i łącza danych) ma już swoje mechanizmy kontroli błędów)
- **Etykieta strummienia (Flow Label)**
    - IPv4: Nie posiada
    - IPv6: Etykieta strumienia (20-bitowe pole). Routery mogą wykorzystywać etykiety strumieni do podejmowania decyzji o priorytetyzacji i odpowiednim trasowaniu tych pakietów
- **Addressy IP**
    - IPv4: 32 bitowe addressy
    - IPv6: 128 bitowe addressy


## Zapisz adres IPv6 0321:0000:0000:0123:0000:0000:0000:0001 w najkrótszej możliwej postaci
```
321:0:0:123::1
```
## Co to jest tunelowanie 6in4?

Tunelowanie 6in4 to technika umożliwiająca przesyłanie pakietów IPv6 przez sieć IPv4 poprzez ich enkapsulację w pakiety IPv4. W praktyce oznacza to, że cały pakiet IPv6 jest traktowany jako dane i umieszczany w polu danych pakietu IPv4, a następnie przesyłany przez sieć IPv4. Jeśli taki pakiet IPv4 jest zbyt duży, aby przejść przez segment sieci, następuje fragmentacja IPv4, a routery pośrednie dzielą go na mniejsze części. Gdy fragmentowane pakiety IPv4 dotrą do brokera tunelu, router ten zbiera wszystkie fragmenty, składa je z powrotem w pełny pakiet IPv4, a następnie usuwa nagłówek IPv4, odzyskując oryginalny pakiet IPv6.

## Na czym polega NAT i po co się go stosuje? Jakie są jego zalety i wady

![image](https://hackmd.io/_uploads/BkauTtA7R.png)

**Zalety:**
- Rozwiązuje problem braku adresów IP
- Można zmienić adresy IP wewnątrz sieci bez powiadamiania Internetu
- Można zmienić ISP pozostawiając adresowanie IP wewnątrz sieci
**Wady:**
- Nieosiągalność komputerów z Internetu (aplikacje P2P)
- Psucie modelu warstwowego (router modyfikuje treść pakietu)

## Jaki stan musi przechowywać router z funkcją NAT?

![image](https://hackmd.io/_uploads/HJEF6FAXA.png)
