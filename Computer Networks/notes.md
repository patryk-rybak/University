# Wykład 1

## Co to jest protokół komunikacyjny? Dlaczego wprowadza się warsty protokołów?

Protokół komunikacyjny to zestaw zasad i reguł określających sposób, w jaki urządzenia komunikują się ze sobą w sieci komputerowej. Te zasady definiują, jak dane są przesyłane, odbierane, adresowane i przetwarzane przez urządzenia w sieci.

Warstwy protokołów wprowadza się w celu zorganizowania i uporządkowania procesu komunikacji w sieci. Każda warstwa protokołu ma swoje określone zadania i działa niezależnie od pozostałych warstw. Warstwy protokołów pomagają w zarządzaniu złożonymi procesami komunikacyjnymi, dzięki czemu proces komunikacji jest bardziej zrozumiały i zarządzalny.

## Wymień warstwy internetowego modelu warstwowego. Jakie są zadania każdej z nich?


### Model TCP/IP

1. **Warstwa aplikacji (Application Layer)**
   - **Zadania**: Oferuje usługi bezpośrednio dla aplikacji użytkownika, takie jak HTTP (przeglądanie internetu), SMTP (poczta elektroniczna), FTP (transfer plików).

2. **Warstwa transportowa (Transport Layer)**
   - **Zadania**: Zapewnia niezawodną (TCP) lub szybką (UDP) transmisję danych między aplikacjami na różnych urządzeniach. Odpowiada za segmentację danych, kontrolę przepływu, oraz zapewnienie integralności i niezawodności transmisji.

3. **Warstwa internetowa (Internet Layer)**
   - **Zadania**: Przesyła dane między różnymi sieciami, zajmuje się adresowaniem IP, routingiem danych, fragmentacją i ponownym składaniem pakietów. Główny protokół: IP.

4. **Warstwa dostępu do sieci (Network Access Layer)**
   - **Zadania**: Odpowiada za fizyczne połączenie z siecią oraz kontrolę transmisji danych na poziomie sprzętu. Zawiera technologie takie jak Ethernet, Wi-Fi, DSL.

### Model OSI

1. **Warstwa aplikacji (Application Layer)**
   - **Zadania**: Interakcja z aplikacjami, dostarczanie usług sieciowych dla użytkownika, takie jak e-mail, FTP, WWW.

2. **Warstwa prezentacji (Presentation Layer)**
   - **Zadania**: Tłumaczenie danych między formatem używanym przez aplikacje a formatem sieciowym, kodowanie, dekodowanie, kompresja, szyfrowanie.

3. **Warstwa sesji (Session Layer)**
   - **Zadania**: Zarządzanie sesjami komunikacyjnymi między aplikacjami, ustanawianie, utrzymanie, synchronizacja i zakończenie sesji.

4. **Warstwa transportowa (Transport Layer)**
   - **Zadania**: Podobnie jak w TCP/IP, zapewnia niezawodną (TCP) lub szybką (UDP) transmisję danych między aplikacjami na różnych urządzeniach. Segmentacja, kontrola przepływu, integralność i niezawodność transmisji.

5. **Warstwa sieciowa (Network Layer)**
   - **Zadania**: Routing, adresowanie logiczne, fragmentacja i ponowne składanie pakietów. Główny protokół: IP.

6. **Warstwa łącza danych (Data Link Layer)**
   - **Zadania**: Zarządzanie transmisją danych w obrębie jednej sieci lokalnej (LAN), detekcja i korekcja błędów, sterowanie dostępem do medium transmisyjnego. Przykłady: Ethernet, Wi-Fi.

7. **Warstwa fizyczna (Physical Layer)**
   - **Zadania**: Przesyłanie surowych bitów przez medium transmisyjne (kable, fale radiowe), definicja fizycznych specyfikacji urządzeń, kodowanie sygnałów.

### Porównanie warstw TCP/IP i OSI

| Model TCP/IP                   | Model OSI                   |
|--------------------------------|-----------------------------|
| **Warstwa aplikacji**          | **Warstwa aplikacji**       |
|                                | **Warstwa prezentacji**     |
|                                | **Warstwa sesji**           |
| **Warstwa transportowa**       | **Warstwa transportowa**    |
| **Warstwa internetowa**        | **Warstwa sieciowa**        |
| **Warstwa dostępu do sieci**   | **Warstwa łącza danych**    |
|                                | **Warstwa fizyczna**        |

Model TCP/IP jest bardziej uproszczony, z mniejszą liczbą warstw, co sprawia, że jest łatwiejszy do implementacji i zrozumienia w praktyce. Model OSI, choć bardziej szczegółowy, jest rzadziej stosowany w praktyce, ale nadal używany jako narzędzie edukacyjne do zrozumienia koncepcji sieciowych.

## Jakie warstwy są zaimplementowane na komputerach a jakie na routerach?

** Nwm, czy to jest dobrze. Rabini są niezdecydowanie. **

Na komputerach, zarówno w przypadku modelu TCP/IP, jak i OSI, zazwyczaj są implementowane tylko trzy warstwy: aplikacji, transportowa i czasami sieciowa. Warstwy niższe, czyli dostępu do sieci, oraz fizyczna, są zazwyczaj zarządzane przez sprzęt sieciowy, takie jak karty sieciowe, przełączniki (switches), czy modemy.

Router, będący urządzeniem przeznaczonym do przekazywania danych między różnymi sieciami, implementuje warstwy sieciową, transportową i czasami aplikacji. Warstwy niższe, czyli dostępu do sieci oraz fizyczną, są również zaimplementowane na routerze, ponieważ router jest bezpośrednio połączony z siecią.

## Czym różni się model warstwowy TCP/IP od OSI?

**Model TCP/IP** składa się z **4 warstw** (aplikacji, transportowej, internetowej, dostępu do sieci), jest **bardziej praktyczny i uproszczony**, używany szeroko **w Internecie**. **Model OSI** ma **7 warstw** (aplikacji, prezentacji, sesji, transportowej, sieciowej, łącza danych, fizycznej), jest **bardziej szczegółowy i teoretyczny**, często wykorzystywany jako **narzędzie edukacyjne**.

## Co jest potrzebne do zbudowania dwukierunkowego niezawodnego kanału?

Do zbudowania **dwukierunkowego niezawodnego kanału komunikacyjnego** potrzebne są:

1. **Warstwa fizyczna**: Fizyczne medium do transmisji danych (kable, fale radiowe) oraz urządzenia nadawczo-odbiorcze (karty sieciowe, routery).
2. **Protokół kontroli transmisji**: Protokół zapewniający niezawodność transmisji, taki jak **TCP**, który wykorzystuje potwierdzenia odbioru (ACK), retransmisje i kontrolę przepływu.
3. **Dwukierunkowa komunikacja**: Możliwość przesyłania danych w obu kierunkach (**full-duplex**).
4. **Numerowanie sekwencji**: Numerowanie segmentów danych dla poprawnej rekonstrukcji strumienia danych.
5. **Mechanizmy wykrywania i korekcji błędów**: Wykrywanie błędów (np. sumy kontrolne) i ich korekcja dla zapewnienia integralności danych.
6. **Buforowanie danych**: Zarządzanie buforami danych w obu kierunkach, retransmisje utraconych danych, kontrola przepływu.

## Porównaj wady i zalety przełączania obwodów i przełączania pakietów.

### Przełączanie obwodów (Circuit Switching)

**Zalety**:
1. **Stała przepustowość**: Gwarantowana przepustowość, ponieważ obwód jest rezerwowany na cały czas trwania połączenia.
2. **Niskie opóźnienia**: Stałe opóźnienie transmisji po zestawieniu obwodu, ponieważ wszystkie dane przechodzą tą samą trasą.
3. **Przewidywalność**: Stabilna jakość połączenia, co jest ważne dla aplikacji wymagających stałej przepustowości, takich jak rozmowy telefoniczne.

**Wady**:
1. **Marnotrawstwo zasobów**: Zasoby sieciowe są zarezerwowane na cały czas trwania połączenia, nawet jeśli nie są wykorzystywane.
2. **Skalowalność**: Trudności ze skalowaniem sieci, ponieważ liczba jednoczesnych połączeń jest ograniczona przez liczbę dostępnych obwodów.
3. **Czas zestawienia połączenia**: Opóźnienia związane z zestawianiem i zwalnianiem obwodów przed i po transmisji danych.

### Przełączanie pakietów (Packet Switching)

**Zalety**:
1. **Efektywność wykorzystania zasobów**: Zasoby sieciowe są wykorzystywane tylko wtedy, gdy są potrzebne, co zwiększa efektywność.
2. **Skalowalność**: Łatwiejsze skalowanie sieci, ponieważ wiele połączeń może współdzielić te same zasoby.
3. **Elastyczność**: Dane mogą być przesyłane przez różne ścieżki, co zwiększa odporność na awarie i przeciążenia w sieci.

**Wady**:
1. **Zmienna przepustowość i opóźnienia**: Przepustowość i opóźnienia mogą się zmieniać w zależności od obciążenia sieci.
2. **Konieczność buforowania**: Pakiety mogą przychodzić w różnej kolejności, co wymaga buforowania i odpowiedniego składania danych po stronie odbiorcy.
3. **Złożoność zarządzania ruchem**: Wymaga bardziej zaawansowanych mechanizmów zarządzania ruchem, takich jak protokoły routingu i zarządzanie kolejkami.

## Jakie znasz rodzaje multipleksowania? Po co i kiedy się je stosuje?
