# Wykład 2

## Z czego wynika hierarchia adresów IP? Jaki ma wpływ na konstrukcję tablic routingu?

Hierarchia adresów IP wynika z potrzeby efektywnego zarządzania nimi i routingu w sieciach. Główne czynniki to:

- **Klasy adresów IP**: Wcześniej podzielone na klasy A, B, C, D i E, co umożliwiało hierarchię.
- **Podział na sieci**: Segmentacja adresów IP na podsieci dla lepszego zarządzania.
- **Struktura CIDR**: Elastyczniejsze przydzielanie adresów dzięki zmiennej długości prefiksów.

To wpływa na konstrukcję tablic routingu poprzez:

- **Podział na podsieci**: Efektywne zarządzanie trasami i unikanie niepotrzebnego rozgłaszania.
- **Routing hierarchiczny**: Organizacja tablic zgodnie z hierarchią IP dla efektywnego przekazywania pakietów.
- **Agregacja tras**: Redukcja rozmiaru tablic routingu i poprawa wydajności.


## Notacja CIDR

CIDR (Classless Inter-Domain Routing) to sposób zapisu adresów IP i ich masek podsieci w celu skrócenia zapisu i efektywnego wykorzystania dostępnych adresów IP. W notacji CIDR adres IP jest zapisywany w formie x.x.x.x/y, gdzie "x.x.x.x" to adres IP, a "y" określa liczbę bitów maski podsieci. Na przykład, adres "192.168.1.0/24" oznacza, że pierwsze 24 bity adresu są częścią adresu sieci, a pozostałe bity to adresy hostów w tej sieci.

## Co to jest adres rozgłoszeniowy?

Adres rozgłoszeniowy to specjalny adres IP używany w sieci do przekazywania komunikatów do wszystkich urządzeń w danej sieci. Na przykład, w sieci o adresie "192.168.1.0/24", adres rozgłoszeniowy to "192.168.1.255".
(Wszystkie bity określające hosta są zapalone)

## Co to jest maska podsieci?

Maska podsieci (subnet mask) to liczba określająca, które bity w adresie IP są częścią adresu sieci, a które są częścią adresu hosta. Jest to narzędzie wykorzystywane do podziału adresów IP na część sieciową i część hostową. Maska podsieci np. "255.255.255.0", gdzie każdy bajt o wartości 255 oznacza bity adresu sieci, a każdy bajt o wartości 0 oznacza bity adresu hosta. Maska określa prefix adresu, który opisuje podsieć, do której adres należy. 

## Opisz sieci IP klasy A, B i C.

Sieci IP klasy A, B i C są podstawowymi klasami adresów IP w IPv4, różniącymi się zakresem dostępnych adresów i domyślnymi maskami podsieci:

- **Klasa A**: Adres IP zaczyna się od 0 → maska sieci = /8.
- **Klasa B**: Adres IP zaczyna się od 10 → maska sieci = /16.
- **Klasa C**: Adres IP zaczyna się od 110 → maska sieci = /24.

## Co to jest pętla lokalna (loopback)?

Pętla lokalna (loopback) to specjalny interfejs sieciowy, który umożliwia komunikację aplikacji z samym sobą. Adres IP dla pętli lokalnej zazwyczaj jest 127.0.0.1. Jest to przydatne narzędzie do testowania aplikacji sieciowych bez konieczności faktycznego korzystania z rzeczywistych interfejsów sieciowych.

## Do czego służy pole TTL w pakiecie IP? Do czego służy pole protokół?

Pole TTL (Time To Live) w pakiecie IP określa maksymalną liczbę routerów, przez które pakiet może przejść, zanim zostanie odrzucony. Jest to mechanizm zapobiegający zapętleniu się pakietów w sieci. Pole protokół w pakiecie IP określa rodzaj protokołu warstwy wyższej, którego dotyczy dany pakiet, np. TCP, UDP, ICMP itp.

## Jakie reguły zawierają tablice routingu?
Tablice routingu zawierają reguły określające, do jakich sieci należy kierować pakiety oraz przez które interfejsy je przekazywać.

## Na czym polega reguła najdłuższego pasującego prefiksu?
Reguła ta polega na wyborze trasy z tablicy routingu na podstawie najdłuższego pasującego prefiksu dla danego celu.

## Co to jest trasa domyślna?
Trasa domyślna to ta, którą router używa, gdy nie ma pasującej trasy w tablicy routingu dla określonego celu. Zazwyczaj prowadzi ona do domyślnego routera bramy lub innego punktu wyjścia z sieci.

## Do czego służy protokół ICMP? Jakie znasz typy komunikatów ICMP?
Protokół ICMP służy do komunikacji między hostami i routerami w sieci internetowej. Typowe komunikaty to "echo request" i "echo reply", używane do testowania dostępności hosta, oraz komunikaty błędów, takie jak "destination unreachable" czy "time exceeded".

## Jak działa polecenie ping?
Polecenie "ping" wysyła pakiet żądania ICMP do określonego hosta i oczekuje na odpowiedź. Jeśli host jest dostępny, odbiera pakiet i wysyła odpowiedź, potwierdzając dostępność.

## Jak działa polecenie traceroute?
Polecenie "traceroute" śledzi trasę, jaką pakiet musi przejść, aby dotrzeć do określonego celu. Wysyła ono serię pakietów z coraz większym TTL i obserwuje, przez które routery przechodzą, aż dotrze do celu.

## Dlaczego do tworzenia gniazd surowych wymagane są uprawnienia administratora?
Tworzenie gniazd surowych umożliwia odbieranie i wysyłanie pakietów bezpośrednio na poziomie warstwy sieciowej, co może stanowić zagrożenie dla bezpieczeństwa systemu. W związku z tym, aby zapobiec potencjalnym nadużyciom, dostęp do tworzenia gniazd surowych jest zazwyczaj ograniczony do użytkowników posiadających uprawnienia administratora.

## Co to jest sieciowa kolejność bajtów?
Sieciowa kolejność bajtów, znana także jako kolejność big-endian, jest konwencją określającą, w jaki sposób liczby są reprezentowane w pamięci komputera. W tej kolejności najbardziej znaczący bajt jest przechowywany na początku. Jest to ważne w kontekście komunikacji między różnymi systemami, gdzie zachowanie jednolitej kolejności bajtów jest kluczowe dla poprawnego odczytywania danych.

## Co robią funkcje socket(), recvfrom() i sendto()?
- Funkcja `socket()` tworzy nowe gniazdo i zwraca deskryptor pliku, który może być używany do komunikacji sieciowej.
- Funkcja `recvfrom()` odbiera dane z gniazda i zapisuje je do bufora, jednocześnie zwracając informacje o adresie źródłowym.
- Funkcja `sendto()` wysyła dane z bufora przez gniazdo do określonego adresu docelowego.

## Jakie informacje zawiera struktura adresowa sockaddr_in?
Struktura adresowa `sockaddr_in` zawiera informacje potrzebne do określenia adresu IP i numeru portu. Zawiera pola takie jak `sin_family` określające rodzaj adresu (np. AF_INET dla IPv4), `sin_port` zawierające numer portu w sieciowej kolejności bajtów oraz `sin_addr` zawierające adres IP hosta w postaci liczbowej.

## Co to jest tryb blokujący i nieblokujący? Co to jest aktywne czekanie?
- **Tryb blokujący**: W trybie blokującym operacje na gnieździe powodują zawieszenie wykonywania programu do momentu zakończenia operacji wejścia-wyjścia. W takim przypadku program "czeka" na zakończenie operacji, co może spowodować opóźnienia.
- **Tryb nieblokujący**: W trybie nieblokującym operacje na gnieździe nie powodują zawieszenia wykonywania programu. Jeśli operacja wejścia-wyjścia nie może być natychmiast zrealizowana, funkcje zwracają wartość błędu lub specjalną wartość, co pozwala programowi na kontynuowanie działania.

Aktywne czekanie polega na nieustannym sprawdzaniu warunku w pętli, co prowadzi do zużycia zasobów procesora bez potrzeby. Jest to niewydajna praktyka.

## Jakie jest działanie funkcji select()?
Funkcja select() służy do monitorowania zestawu deskryptorów plików pod kątem gotowości do odczytu, zapisu lub wystąpienia wyjątku. Pozwala ona na zablokowanie wykonania programu do momentu wystąpienia zdarzenia na jednym z deskryptorów. Jest często używana w programowaniu sieciowym do wielozadaniowej obsługi wielu połączeń bez konieczności tworzenia wielu wątków.
