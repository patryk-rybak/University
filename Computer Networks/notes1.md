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

### Rodzaje Multipleksowania

1. **Multipleksowanie w dziedzinie czasu (TDM - Time Division Multiplexing)**:
   - Polega na przesyłaniu różnych sygnałów w różnych okresach czasu w ramach tego samego kanału.
   - Każdy sygnał ma przypisany okres czasu, w którym może być transmitowany.
   - Stosuje się go w sieciach telekomunikacyjnych, takich jak linie telefoniczne, gdzie kilka połączeń jest przesyłanych przez ten sam kabel.

2. **Multipleksowanie w dziedzinie częstotliwości (FDM - Frequency Division Multiplexing)**:
   - Działa przez przypisanie różnym sygnałom różnych częstotliwości w kanale transmisyjnym.
   - Każdy sygnał zajmuje oddzielny zakres częstotliwości.
   - Stosowane w analogowych systemach transmisji, takich jak radiowozy, gdzie różne stacje radiowe korzystają z różnych częstotliwości.

## Zastosowanie Multipleksowania

- **Optymalizacja wykorzystania zasobów**: Multipleksacja pozwala na efektywne wykorzystanie dostępnych zasobów, takich jak pasmo, czas czy częstotliwość, dzieląc je między różne sygnały.
- **Zwiększenie przepustowości**: Umożliwia przesyłanie większej ilości danych przez ten sam kanał, co prowadzi do zwiększenia przepustowości komunikacji.
- **Ograniczenie kosztów**: Dzięki wykorzystaniu jednego kanału do przesyłania wielu sygnałów, koszty infrastruktury mogą być znacznie obniżone w porównaniu do wykorzystania osobnych kanałów dla każdego sygnału.
- **Współdzielenie zasobów**: W środowiskach, gdzie zasoby są ograniczone, multipleksacja pozwala na współdzielenie tych zasobów między wieloma użytkownikami lub aplikacjami.

## Porównaj ze sobą rodzaje routingu

### Routing źródłowy:
- **Opis**: Nagłówek pakietu zawiera całą trasę do celu.
- **Zalety**:
  - Pełna kontrola nad trasą pakietów przez źródło danych.
  - Elastyczność w wyborze ścieżki w zależności od aktualnych warunków sieciowych.
- **Wady**:
  - Wymaga większej przepustowości, ponieważ każdy pakiet musi zawierać pełną ścieżkę.
  - Wrażliwe na zmiany w topologii sieci.

### Wykorzystujący tablice routingu:
- **Opis**: Router utrzymuje pewien stan nazywany tablicą routingu. Zawiera ona zbiór reguł typu „jeśli adres docelowy pasuje do wzorca A, przekaż pakiet do sąsiedniego routera X“.
- **Jak ustawiać tablice routingu?**: Tablice routingu są konfigurowane przez administratorów sieci lub automatycznie aktualizowane przez protokoły routingu.
- **Zalety**:
  - Efektywność i skalowalność, ponieważ decyzje routingowe są podejmowane lokalnie przez routery na podstawie informacji w tablicach routingu.
  - Odporność na zmiany w topologii sieci, ponieważ routery mogą dynamicznie aktualizować tablice routingu na podstawie protokołów routingu.

### Wirtualne przełączanie obwodów:
- **Opis**: Nadawca najpierw wysyła pakiet(y) kontrolny ustanawiający ścieżkę do celu i konfigurujący routery, czasem rezerwujący część łącza. Kolejne pakiety przesyłane są tą samą ścieżką.
- **Zalety**:
  - Niskie opóźnienia i stała przepustowość, ponieważ wirtualny obwód jest ustalany i rezerwowany przed przesyłaniem danych.
  - Efektywne wykorzystanie zasobów, ponieważ wirtualne obwody mogą być ponownie używane przez różne połączenia.

![image](https://hackmd.io/_uploads/rJJlBtcQR.png)


## Co to jest komunikacja pełnodupleksowa, półdupleksowa i simpleksowa?

W skrócie, komunikacja pełnodupleksowa umożliwia dwukierunkową transmisję danych w czasie rzeczywistym, komunikacja półdupleksowa umożliwia jednokierunkową transmisję danych w danym momencie, a komunikacja simpleksowa umożliwia jednokierunkową transmisję danych bez możliwości odpowiedzi.

## Do czego służy polecenie traceroute? Co pokazuje?

### Polecenie `traceroute`

Polecenie `traceroute` (lub `tracert` w systemach Windows) służy do śledzenia ścieżki, jaką pakiet danych przebywa od komputera źródłowego do docelowego w sieci internetowej. Głównym celem `traceroute` jest identyfikacja wszystkich routerów (przełączników) znajdujących się na trasie pakietu oraz pomiar czasu potrzebnego na przejście pakietu przez każdy z tych routerów.

Kiedy uruchamiasz polecenie `traceroute`, wysyłane są specjalne pakiety ICMP (protokół kontrolny komunikatu internetowego), które mają ograniczoną czasowo żywotność. Każdy router na trasie pakietu, zanim go odrzuci, zmniejsza licznik czasu życia (TTL) o jeden. Gdy TTL osiągnie zero, router odrzuca pakiet i wysyła komunikat ICMP "czas przekroczony" z powrotem do źródła. Dzięki temu polecenie `traceroute` może śledzić trasę pakietu poprzez analizę tych komunikatów "czas przekroczony".

Podsumowując, polecenie `traceroute` służy do:

1. Identyfikacji wszystkich routerów (przełączników) na trasie pakietu od komputera źródłowego do docelowego.
2. Pomiaru czasu potrzebnego na przejście pakietu przez każdy z tych routerów.
3. Diagnozowania problemów związanych z trasą pakietu w celu zlokalizowania i eliminacji ewentualnych awarii lub opóźnień w sieci.

## Po co stosuje się bufory w routerach? Co to jest przeciążenie?

Bufory w routerach pozwalają na tymczasowe przechowywanie pakietów w przypadku, gdy ruch sieciowy przekracza zdolność routera do przetwarzania danych w czasie rzeczywistym. Dzięki buforom routery mogą przetwarzać pakiety zgodnie z ich kolejnością przychodzenia, zamiast odrzucać nadmiarowe pakiety.


## Jakie są przyczyny opóźnień pakietów?

### Przyczyny opóźnień pakietów:

1. **Kolejkowanie w buforach**: Przekroczenie przepustowości routera może skutkować tymczasowym przechowywaniem pakietów w buforach, co prowadzi do opóźnień.

2. **Routowanie**: Wyszukiwanie optymalnej trasy dla pakietów może spowodować opóźnienia, szczególnie w dużych sieciach.

3. **Wartość TTL**: Zbyt niska wartość czasu życia (TTL) może skutkować odrzuceniem pakietu, co może wynikać z zapętlenia się pakietu lub zbyt małej wartości TTL.

4. **Kongestia sieci**: Przekroczenie przepustowości sieci może prowadzić do kongestii, czyli zatoru w ruchu sieciowym, co skutkuje opóźnieniami w przekazywaniu pakietów.

5. **Bufory podręczne**: Węzły sieciowe używają buforów podręcznych do tymczasowego przechowywania pakietów, co może wprowadzać opóźnienia, gdy pakiety są zatrzymywane przed dalszym przekazaniem.

## Co to jest BDP? Co to jest czas propagacji?

BDP (Bandwidth-Delay Product) to iloczyn przepustowości łącza danych (wyrażonej w bitach na sekundę) oraz czasu propagacji (wyrażonego w sekundach) między dwoma punktami końcowymi łącza. Oznacza to, że BDP określa ilość danych, która może znajdować się jednocześnie na łączu między nadawcą a odbiorcą, zanim odbiorca potwierdzi otrzymanie pierwszego pakietu.

Czas propagacji to czas potrzebny na przesłanie pakietu z jednego punktu do drugiego w sieci. Obejmuje on czas potrzebny na propagację sygnału przez medium transmisyjne (np. światłowód, przewód miedziany) oraz opóźnienia związane z przetwarzaniem węzłów sieciowych (np. routery, przełączniki)

BDP (bandwidth-delay product): iloczyn przepustowości i RTT
= „ile możemy wysłać zanim dostaniemy odpowiedź od odbiorcy“.

## Wyjaśnij pojęcia: komunikacja simpleksowa, półdupleksowa, pełnodupleksowa.

- **Simpleksowa**: Nie ma możliwości przesyłania informacji w dwóch kierunkach. Nadajnik i odbiornik nie mogą zamienić się rolami, a transmisja odbywa się tylko w jednym kierunku. Przełącznik jest mechaniczny i w stanie spoczynku ustawiony na odbiór, co blokuje możliwość nadawania.
  
- **Półdupleksowa**: To mniej zaawansowana forma komunikacji pełnodupleksowej, gdzie przesyłanie i odbieranie informacji odbywa się naprzemiennie, co może prowadzić do spadku przepustowości.
  
- **Pełnodupleksowa**: Informacje są przesyłane w obu kierunkach jednocześnie, bez spadku przepustowości.

## Co umożliwia protokół IP? Co to znaczy, że protokół realizuje zasadę best effort?

Protokół IP (Internet Protocol) umożliwia przesyłanie danych między różnymi urządzeniami w sieci komputerowej. Jest to protokół warstwy sieciowej, odpowiedzialny za adresowanie i routowanie pakietów danych między różnymi sieciami.

Zasada "best effort" oznacza, że protokół IP nie gwarantuje dostarczenia pakietów danych w określonym czasie ani w określonym porządku. Protokół IP podejmuje "najlepsze wysiłki" w celu przesłania pakietów do ich docelowego miejsca, ale nie oferuje żadnych gwarancji co do niezawodności, szybkości ani kolejności dostarczania pakietów.

## Jakie są zalety i wady zasady end-to-end?

** a jakie wady?? **

Wszystkie dodatkowe cechy (np. niezawodne przesyłanie danych)
implementowane w urządzeniach końcowych (komputerach) → łatwa
ewolucja, niski koszt innowacyjności.

## Po co wprowadza się porty?

- **Identyfikacja usług**: Porty pozwalają na identyfikację konkretnych usług lub aplikacji działających na urządzeniu, co umożliwia skierowanie danych do właściwego miejsca.

- **Rozróżnienie aplikacji**: Dzięki portom wiele aplikacji może działać jednocześnie na jednym urządzeniu, ponieważ każda aplikacja może korzystać z innego portu do komunikacji.

- **Bezpieczeństwo**: Porty mogą być wykorzystywane do konfiguracji zasad bezpieczeństwa, takich jak zapora ogniowa, która kontroluje ruch sieciowy na poziomie portów, zapewniając ochronę przed nieautoryzowanym dostępem.

## Wyjaśnij pojęcie enkapsulacji i dekapsulacji.

Termin odnoszący się do struktury protokołu komunikacyjnego. Warstwa niższa opakowuje dane przekazane przez warstwę wyższą danego protokołu po stronie nadawczej we własne nagłówki i ew. stopki, które są wymagane do poprawnego przesyłania danych. Po stronie odbiorczej wykonywane jest działanie odwrotne prowadzące do wyodrębnienia danych z warstwy najwyższej przenoszącej dane użytkowe, zwanej warstwą aplikacji.
