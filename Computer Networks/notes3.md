# Wykład 3

## Co to jest cykl w routingu? Co go powoduje?

Cykl w routingu to pakiet krążący w kółko. Cykle powstają np. przez zbyt wolną propagację inforamcji o awarii sieci.

## Czym różni się tablica routingu od tablicy przekazywania?

![image](https://hackmd.io/_uploads/HJfOvQA7C.png)

## Dlaczego w algorytmach routingu dynamicznego obliczamy najkrótsze ścieżki?

Ponieważ zapobiega to powstawaniu cylki w przeciwieństwie do podejscia minimalnej przepustowości oraz w zależności od metriki pozwala na zminimalizowanie kosztów lub czasu.

## Co to jest metryka? Jakie metryki mają sens?
Metryka to funkcja pozwalająca na określanie odległości pomiędzy obiektami. W sieciach 
mają sens metryki, które optymalizują jakiś zasób.

- czas propagacji
- koszt ponieżny
- 1 -> odległość pomiędzy dwoma routerami = liczba routerów na trasie (hops)

## Czym różnią się algorytmy wektora odległości od algorytmów stanów łączy?

![image](https://hackmd.io/_uploads/rk3Y97C7R.png)
![image](https://hackmd.io/_uploads/BkXXB4AXC.png)

## Jak router może stwierdzić, że bezpośrednio podłączona sieć jest nieosiągalna?

Sąsiadujące routery co chwilę wysyłają sobie pakiety kontrolne, lub dzięki zliczaniu do  nieskończoności. Możemy też nie otrzymać od sieci żadnej informacji przez jakiś okres czasu. 

## Co to znaczy, że stan tablic routingu jest stabilny?

- kazdy router będize miał ten sam obraz sieci
- stworzone tablice przekazywania będą bez cykli
(Możliwe cykle, jeśli niektóre routery już wiedzą o awarii łącza a inne nie)

## Jak zalewać sieć informacją? Co to są komunikaty LSA?

Niekontrolowane „zalewanie“

- Nawet jeśli w grafie nie ma cykli: wiele kopii pakietu może dotrzeć do jednego routera i każda z nich zostanie przesłany dalej.
- Trzeba pamiętać, jakie informacje już rozsyłaliśmy.

Kontrolowane „zalewanie”

![image](https://hackmd.io/_uploads/BkeG6m0QA.png)

OSPF jest protokołem stanu łącza (link-state protocol) i działa w ramach pojedynczego systemu autonomicznego (AS). Szybka kowergnecja, podział sieci na areas.

LSA (Link State Advertisement) to komunikat wymieniający info o stanie łączy. Właśnie tym komunikatem zalewana jest sieć (lub area).

- Przesyłane na początku + przy zmianie + co jakiś czas (30 min.)
- LSA zawiera źródło i numer sekwencyjny
- Po 1h otrzymane LSA są wyrzucane z pamięci.

## Co wchodzi w skład wektora odległości?

**początkowo**: V = tylko sieci dostępne bezpośrednio

**potem co powien czas**: V wysylane jest do sąsiadów i na tej podstawie uaktualnia się V

tablica routingu = tablica przekazywania + informacja z V o odległościach do celu 


## W jaki sposób podczas działania algorytmu routingu dynamicznego może powstać cykl w routingu?

Jeżeli progpagacja o awarii sieci np. z routera A do np. routera B niż przekazania wektora odległości z routera B do A. Nastsąpi wtedy zliczanie do nieskończoności. 

## Co to jest problem zliczania do nieskończoności? Kiedy występuje?

Jak wyżej.

## Na czym polega technika zatruwania ścieżki zwrotnej (poison reverse)?

Jest to rozwiązanie zliczania do nieskończoności. Polega na tym, że jeżeli router chce przekazać swój wektor odległości do routera kolejnego na ścieżce do danej sieci to specjalnie dla niego zmienia on tę odległośc na nieskończoność.
(Może nie pomóc w większych sieciach)

## Po co w algorytmach wektora odległości definiuje się największą odległość w sieci (16 w protokole RIPv1)?

Jest to ostateczne rozwiązanie problemu zliczania do nieskończoności, jeżli wszsytkie inne motody zawiodą. 

(Wysyłanie również pierwszego routera na trasie (nie pomaga w większych sieciach)

(Szybsza aktualizacja w momencie wykrycia awarii)

Pakiety odwiedzające ten sam router po raz 16 są wyrzucane. 

## Po co stosuje się przyspieszone uaktualnienia?

Pomaga to przy unikaniu cykli. Szybciej informujemy o awarii. Możemy dzięki temu uniknąć 
zliczania do nieskończoności.

## Co to jest system autonomiczny (AS)? Jakie znasz typy AS?

System autonomiczny (AS) to zbiór sieci IP i routerów pod kontrolą jednej organizacji administracyjnej, która zarządza routingiem wewnątrz tego zbioru oraz udostępnia informacje o trasach do innych systemów autonomicznych. Każdy AS jest identyfikowany przez unikalny numer AS (ASN, Autonomous System Number), który jest przypisywany przez odpowiednie organizacje rejestracyjne, takie jak IANA (Internet Assigned Numbers Authority) lub RIR (Regional Internet Registries).

**AS z jednym wyjściem** - ma tylko jedno połączenie z innym AS. Mała firma lub organizacja, która ma jednego dostawcę usług internetowych (ISP).
**AS z wieloma wyjściami (nietranzytowy)** -  ma więcej niż jedno połączenie z różnymi AS-ami, ale nie świadczy usług tranzytu między tymi AS-ami.
**AS tranzytowy** - Umożliwia przesyłanie ruchu przez swoją sieć, łącząc różne AS-y.

## Czym różnią się połączenia dostawca-klient pomiędzy systemami autonomicznymi od łącz partnerskich (peering)?

dostawca-klient - relacje pieniężne

peering - łącza partnerskie

Połączenia dostawca-klient między systemami autonomicznymi obejmują przepływ ruchu, gdzie klient płaci dostawcy za dostęp do jego sieci i dalej do reszty Internetu. Łącza partnerskie (peering) natomiast to bezpłatne lub wymienne połączenia między AS-ami o podobnym rozmiarze lub zasięgu, służące wzajemnej wymianie ruchu bez opłat tranzytowych.

## Dlaczego w routingu pomiędzy systemami autonomicznymi nie stosuje się najkrótszych ścieżek?

Ze względów polityczno-ekonomicznych.

## Które trasy w BGP warto rozgłaszać i komu? A które wybierać?

Algorytm routingu pomiędzy **AS**.
Bazuje na **algorytmach wektora** odległości bo algorytm stanu łącza nie gwarantuje prywatności. 

Zawartość naszego AS trzeba rozgłosić wszystkim, bo inaczej nikt do nas nie trafi. Trasy do naszych klientów należy rozgłaszać wszystkim, bo za to nam oni płacą. Szczególnie należy je rozgłaszać naszym partnerom, bo za to nie płacimy. Trasy do naszych dostawców należy rozgłaszać jedynie naszym klientom. Trasy do naszych partnerów  rozgłaszamy zazwyczaj tylko klientom.

Innymi słowy:

- Zawartość naszego AS (prefiksy CIDR): 
    - Inaczej nikt do nas nie trafi. 
- Trasy do naszych klientów: 
    - Tak, bo klienci nam płacą, za przesyłane dane. 
    - Szczególnie warto rozgłaszać je naszym partnerom, bo to jest ruch za który nie płacimy. 
- Trasy do naszych dostawców: 
    - Naszym klientom tak. 
    - Poza tym nie: nie chcemy, żeby inni przesyłali przez nasz AS ruch do naszego dostawcy (my płacimy, nam nie płacą). 
- Trasy do naszych partnerów: 
    - Naszym klientom tak. 
    - Poza tym zazwyczaj nie. 


Wybór polega na:

Wiele możliwości dotarcia do jakiejś sieci (prefiksu CIDR) 
- Zazwyczaj wybór najkrótszej trasy (najmniejsza liczba AS). 
- Ale można zmienić taki wybór. Częsta polityka: 
    - wybierz najpierw trasę przez swojego klienta, 
    - potem przez partnera, 
    - a na końcu trasę przez dostawcę. 

## Jak BGP współpracuje z algorytmami routingu wewnątrz AS?