Co zrobić przed pierwszym użyciem programu?
-----------
1. W folderze 'config' w pliku 'ip_list.txt' wpisz adresy ip urządzeń które chcialbyś monitorować
2. W tym samym folderze w pliku 'config.ini', wpisz w polu 'sender_email' mail, z którego chciałbyś wysyłać maila 
   z informacją o statusie urządzeń. W polu 'reciever_email' wpisz maila, na którego chciałbyś wysyłac mail.
   W polu 'password' wpisz hasło do maila, z którego ma być wysyłany mail. 
   Zalecam stworzenie 'throwaway' maila, z którego będzie wysyłana wiadomość.
3. W polu 'time' pod [Scanning interval (in seconds)] - wpisz co ile sekund program ma wysyłać pakiety i sprawdzać 
   status urządzeń. Im większa będzie ta liczba tym mniejsza dokładność.
4. Podaj swój 'chat_id' telegrama aby dostawać infromacje na Telegramie. Bot został już stworzony na potrzeby programu.
   Instrukcja jak znaleźć swój 'chat_id' w Telegramie znajduje się w pliku 'config.ini'.
   Zmienna 'token' to numer identyfikacyjny bota w telegramie. Jeśli chcesz użyć innego bota, musisz podać jego 'token'.
5. Zmienna 'counter' określa po ilu cyklach skanowania sieci, zareportować zmianę statusu urządzenia. 
   Ta zmienna została stworzona ponieważ urządzenia podłączone do sieci mogą czasami rozłączyć się na kilka sekund i 
   potem z powrtotem połączyć. Program zauważy tą zmianę ale nie chcemy dostawać informacj o każdym małym rozłączeniu i
   ponownym połączniu. Jeśli przykładowo nastąpi zmiana statusu jednego z urządzeń z 'ONLINE' na 'OFFLINE',
   przy zmiennej 'counter' = 4, program poczeka jeszcze aż miną 4 cykle skanowania zanim prześle informację o zmianie statusu.
   Jeśli przed upływem tych 4 cykli program wróci do statusu 'ONLINE', nie zostanie wysłana informacje o zmianie.
   Jeśli natomiast po upływie 4 cykli status nadal będzie 'OFFLINE', odpowiedznia informacja zostanie przesłana na maila i Telegrama.
   Zwiększenie wartości zmiennej 'counter' będzie skutkowało tym, że program będzie mniej wrażliwy na zmiany. 
   Domyślnie wartość została ustawiona na 4.

Jak korzystać z programu?
------------
1. Kliknij na plik o nazwie run_scanner.bat (po wcześniejszym ustawieniu wszystkich parametrów wg instrukcji powyżej)
2. 


Wymagania do poprawnego działania programu
---------
1. Zainstalowny python
2. W razie gdyby brakowało któreś z bibliotek - uruchom plik 'install_dependencies.bat'
