"""
Printare interfață console pentru aplicație.
"""

from domain.operatii_aritmetice import adunare_in_baze, scadere_in_baze, inmultire_in_baze_cu_o_cifra, impartirea_cu_o_cifra
from utils.utils import determinare_optiuni_disponibile
from domain.conversii import conversie_impartire_succesiva, conversie_metoda_substitutiei, conversie_baza_intermediara, conversie_rapida

class Console:
    def __init__(self):
        pass

    @staticmethod
    def __print_meniu_principal():
        """
        Printare meniu principal.
        Input: -.
        Output: -.
        """ 
        print("║ 1. Conversie număr între baze.                  ║")
        print("║ 2. Conversii rapide (2, 4, 8, 16).              ║")
        print("║ 3. Operatii aritmetice în diferite baze.        ║")
        print("║ 0. Iesire din aplicatie.                        ║")
        print("╚═════════════════════════════════════════════════╝")

    @staticmethod
    def __print_banner():
        """
        Printare banner aplicatie.
        Input: -.
        Output: -.
        """ 
        print("╔═════════════════════════════════════════════════╗")
        print("║                 Convertor de baze               ║")
        print("║         Proiect realizat de: Arsene Robert      ║")
        print("║                   Grupa: 211/1                  ║")
        print("╚═════════════════════════════════════════════════╝")

    @staticmethod
    def __print_exit_banner():
        """
        Printare banner iesire aplicatie.
        Input: -.
        Output: -.
        """ 
        print("╔═════════════════════════════════════════════════╗")
        print("║            Iesire din aplicatie...              ║")
        print("╚═════════════════════════════════════════════════╝")

    @staticmethod
    def __print_optiune_expandata(i):
        """
        Printeaza optiunea selectata de utilizator impreuna cu optiunile aferente acesteia.
        Input: i - int - Numarul optiunii principale selectata de utilizator.
        Output: -.
        """
        if i == 1:
            print("║ 1. Conversie număr între baze.                  ║")
            print("║\t1. Impartire succesiva.                   ║")
            print("║\t2. Metoda substitutiei.                   ║")
            print("║\t3. Utilizarea unei baze intermediare.     ║")
        elif i == 3:
            print("║ 3. Operatii aritmetice in diferite baze.        ║")
            print("║\t1. Adunare.                               ║")
            print("║\t2. Scadere.                               ║")
            print("║\t3. Inmultire.                             ║")
            print("║\t4. Impartire.                             ║")

    @staticmethod
    def __print_optiune_colapsat(i):
        """
        Printeaza optiunea selectata de utilizator in forma colapsata.
        Input: i - int - Numarul optiunii principale selectata de utilizator.
        Output: -.
        """
        if i == 1:
            print("║ 1. Conversie număr între baze.                  ║")
        elif i == 2:
            print("║ 2. Conversii rapide (2, 4, 8, 16).              ║")
        elif i == 3:
            print("║ 3. Operatii aritmetice in diferite baze.        ║")
        elif i == 'x':
            print("Iesire din aplicatie.")

    @staticmethod
    def __print_optiuni_ext_sau_col(ok):
        """
        Printeaza optiunea selectata in modul extended iar pe cele neselectate in modul collapsed.
        Input: ok - int - Numarul otpiunii care trebuie printata extended.
        Output: -.
        """
        Console.__print_banner()
        for i in range(1, 4):
            if i == ok:
                Console.__print_optiune_expandata(i)
            else:
                Console.__print_optiune_colapsat(i)
        print("╚═════════════════════════════════════════════════╝")

    @staticmethod
    def __input_optiune_utilizator(limita_inf, limita_sup, text):
        """
        Verifica daca utilizatorul a introdus o optiune valida in functie de numarul optiunilor valabile.
        Input: limita_sup - int - Limita superioara de optiuni valide.
        Output: users_option - int - Numarul optiunii valide selectate de utilizator.    
        """
        # Verificare daca utilizatorul a introdus o valoare pana 
        # cand valoarea introdusa este valida: limita_inf <= cifra <= limita_superioara.
        while True:
            users_option = input(f"{text}")
            # Verificare daca utilizatorul a introdus un caracter care nu este un numar.
            if not users_option.isdigit():
                print("Introduceti o valoare valida!")
            else:
                users_option = int(users_option)
                # Verificare daca utilizatorul a introdus o valoare valida in functie de limita inferioara si limita superioara.
                if users_option < limita_inf or users_option > limita_sup:
                    print(f"Introduceti un numar intre {limita_inf} si {limita_sup}.")
                else:
                    # Daca utilizatorul introduce o valoare valida se iese din bucla while.
                    break
        return users_option
    
    #! 1) Impartire succesiva.
    def __conversie_impartire_succesiva_ui(self):
        """
        Printam interfața pentru conversia unui număr între baze folosind metoda împărțirii succesive.
        Input: -.
        Output: -.        
        """
        # Citim baza sursa.
        baza_sursa = Console.__input_optiune_utilizator(2, 16, "Introduceti baza sursa (2-16): ")
        # Citim numarul pe care dorim sa il convertim.
        numar_de_convertit = input("Introduceti numarul de convertit: ")
        # Citim baza destinatie.
        baza_destinatie = Console.__input_optiune_utilizator(2, 16, "Introduceti baza destinatie (2-16): ")
        print(f"\nConvertim numarul {numar_de_convertit} din baza {baza_sursa} in baza {baza_destinatie} folosind impartirea succesiva.\n")
        try:
            rezultat, pasi = conversie_impartire_succesiva(numar_de_convertit, baza_sursa, baza_destinatie)
            print("Pasi efectuati in conversie:")
            print(pasi)
            print(f"Rezultatul este: {numar_de_convertit} ({baza_sursa}) = {rezultat} ({baza_destinatie})")
        except Exception as error:
            print(f"Eroare la convertirea numarului: {error}")

    #! 2) Metoda substitutiei.
    def __conversie_metoda_substitutiei_ui(self):
        """
        Printam interfața pentru conversia unui număr între baze folosind metoda substituției.
        Input: -.
        Output: -.        
        """
        # Citim baza sursa.
        baza_sursa = Console.__input_optiune_utilizator(2, 16, "Introduceti baza sursa (2-16): ")
        # Citim numarul de convertit.
        numar_de_convertit = input("Introduceti numarul de convertit: ")
        # Citim baza destinatie.
        baza_destinatie = Console.__input_optiune_utilizator(2, 16, "Introduceti baza destinatie (2-16): ")
        print(f"\nConvertim numarul {numar_de_convertit} din baza {baza_sursa} in baza {baza_destinatie} folosind metoda substitutiei\n.")
        try:
            rezultat, pasi = conversie_metoda_substitutiei(numar_de_convertit, baza_sursa, baza_destinatie)
            print("Pasi efectuati in conversie:")
            print(pasi)
            print(f"Rezultatul este: {numar_de_convertit} ({baza_sursa}) = {rezultat} ({baza_destinatie})")
        except Exception as error:
            print(f"Eroare la convertirea numarului: {error}")
    
    #! 3) Utilizarea unei baze intermediare.
    def __conversie_baza_intermediara_ui(self):
        """
        Printam interfața pentru conversia unui număr între baze folosind o bază intermediară.
        Input: -.
        Output: -.        
        """
        # Citim baza sursa.
        baza_sursa = Console.__input_optiune_utilizator(2, 16, "Introduceti baza sursa (2-16): ")
        # Citim numarul de convertit.
        numar_de_convertit = input("Introduceti numarul de convertit: ")
        # Citim baza tinta.
        baza_destinatie = Console.__input_optiune_utilizator(2, 16, "Introduceti baza destinatie (2-16): ")
        print(f"\nConvertim numarul {numar_de_convertit} din baza {baza_sursa} in baza {baza_destinatie} folosind o baza intermediara.\n")
        try:
            rezultat, pasi = conversie_baza_intermediara(numar_de_convertit, baza_sursa, baza_destinatie)
            print("Pasi efectuati in conversie:")
            print(pasi)
            print(f"Rezultatul este: {numar_de_convertit} ({baza_sursa}) = {rezultat} ({baza_destinatie})")
        except Exception as error:
            print(f"Eroare la convertirea numarului: {error}")
    
    #! 4) Conversii rapide (2, 4, 8, 16).
    def __conversie_rapida_ui(self):
        """
        Printam interfața pentru conversia rapidă între bazele 2, 4, 8 și 16.
        Input: -.
        Output: -.
        """
        # Citim baza sursa.
        baza_sursa = Console.__input_optiune_utilizator(2, 16, "Introduceti baza sursa (2-16): ")
        # Citim numarul de convertit.
        numar_de_convertit = input("Introduceti numarul de convertit: ")
        # Citim baza tinta.
        baza_destinatie = Console.__input_optiune_utilizator(2, 16, "Introduceti baza destinatie (2-16): ")
        print(f"\nConvertim numarul {numar_de_convertit} din baza {baza_sursa} in baza {baza_destinatie} folosind o baza intermediara.\n")
        try:
            rezultat, pasi = conversie_rapida(numar_de_convertit, baza_sursa, baza_destinatie)
            print("Pasi efectuati in conversie:")
            print(pasi)
            print(f"Rezultatul este: {numar_de_convertit} ({baza_sursa}) = {rezultat} ({baza_destinatie})")
        except Exception as error:
            print(f"Eroare la convertirea numarului: {error}")

    #! 5) Adunare.
    def __adunare_in_baze_ui(self):
        """
        Printam interfața pentru adunarea a două numere în diferite baze.
        Input: -.
        Output: -.
        """
        # Baza sursa.
        baza = Console.__input_optiune_utilizator(2, 16, "Introduceti baza in care se vor aduna numerele (2-16): ")
        # Numarul 1.
        numar1 = input("Introduceti primul numar: ")
        # Numarul 2.
        numar2 = input("Introduceti al doilea numar: ")
        print(f"\nAdunam numerele {numar1} si {numar2} in baza {baza}.\n")
        try:
            rezultat, pasi = adunare_in_baze(numar1, numar2, baza)
            print("Pasi efectuati in adunare:")
            print(pasi)
            print(f"Rezultatul adunarii este: {numar1} ({baza}) + {numar2} ({baza}) = {rezultat} ({baza})")
        except Exception as error:
            print(f"Eroare la adunarea numerelor: {error}")

    #! 6) Scadere.
    def __scadere_in_baze_ui(self):
        """
        Printam interfața pentru scăderea a două numere în diferite baze.
        Input: -.
        Output: -.
        """
        # Baza sursa.
        baza = Console.__input_optiune_utilizator(2, 16, "Introduceti baza in care se vor scadea numerele (2-16): ")
        # Numarul 1.
        numar1 = input("Introduceti primul numar: ")
        # Numarul 2.
        numar2 = input("Introduceti al doilea numar: ")
        print(f"\nScadem numerele {numar1} si {numar2} in baza {baza}.\n")
        try:
            rezultat, pasi = scadere_in_baze(numar1, numar2, baza)
            print("Pasi efectuati in scadere:")
            print(pasi)
            print(f"Rezultatul scaderii este: {numar1} ({baza}) - {numar2} ({baza}) = {rezultat} ({baza})")
        except Exception as error:
            print(f"Eroare la scaderea numerelor: {error}")

    #! 7) Inmultire cu o cifra.
    def __inmultire_in_baze_cu_o_cifra_ui(self):
        """
        Printam interfața pentru înmulțirea unui număr cu o cifră în diferite baze.
        Input: -.
        Output: -.
        """
        # Baza sursa.
        baza = Console.__input_optiune_utilizator(2, 16, "Introduceti baza in care se va inmulti numarul (2-16): ")
        # Numarul.
        numar = input("Introduceti numarul: ")
        # Cifra.
        cifra = input("Introduceti cifra cu care se va inmulti numarul: ")
        print(f"\nInmultim numarul {numar} cu cifra {cifra} in baza {baza}.\n")
        try:
            rezultat, pasi = inmultire_in_baze_cu_o_cifra(numar, cifra, baza)
            print("Pasi efectuati in inmultire:")
            print(pasi)
            print(f"Rezultatul inmultirii este: {numar} ({baza}) * {cifra} ({baza}) = {rezultat} ({baza})")
        except Exception as error:
            print(f"Eroare la inmultirea numerelor: {error}")

    #! 8) Impartire.
    def __impartire_in_baze_ui(self):
        """
        Printam interfața pentru împărțirea unui număr la o cifră în diferite baze.
        Input: -.
        Output: -.
        """
        # Baza sursa.
        baza = Console.__input_optiune_utilizator(2, 16, "Introduceti baza in care se va imparti numarul (2-16): ")
        # Numarul.
        numar = input("Introduceti numarul: ")
        # Cifra.
        cifra = input("Introduceti cifra la care se va imparti numarul: ")
        print(f"\nImpartim numarul {numar} la cifra {cifra} in baza {baza}.\n")
        try:
            rezultat, rest_rezultat, pasi = impartirea_cu_o_cifra(numar, cifra, baza)
            print("Pasi efectuati in impartire:")
            print(pasi)
            print(f"Rezultatul impartirii este: {numar} ({baza}) / {cifra} ({baza}) = {rezultat} ({baza}) rest {rest_rezultat} ({baza})")
        except Exception as error:
            print(f"Eroare la impartirea numerelor: {error}")

    def showUi(self):
        """
        Afiseaza interfața console pentru aplicație.
        Input: -.
        Output: -.
        """ 
        # Se declara variabila care permite rularea programului cat timp este True. 
        # In momentul in care aceasta variabila devine False programul nu mai ruleaza.
        running = True        
        # Declaram variabila care printeaza meniul principal.
        ok = 0
        # Bucla principala a aplicatiei.
        while running:
            # Printam bannerul aplicatiei.
            Console.__print_banner()

            # Printam meniul principal daca ok == 0.
            if ok == 0:
                Console.__print_meniu_principal()

            # Citim optiunea 1 selectata de utilizator.
            user_option_1 = Console.__input_optiune_utilizator(0, 3, ">>> ")

            # Actualizam variabila ok pentru a printa optiunile in modul extins sau colapsat.
            ok = user_option_1

            # Printam optiunile in modul extins sau colapsat daca ok != 0.
            if ok != 0 and ok != 2:
                Console.__print_optiuni_ext_sau_col(ok)

            # Salvam numarul de optiuni valabile in functie de optiunea principala selectata de utilizator.
            numar_optiuni_disponibile = determinare_optiuni_disponibile(user_option_1)
            if user_option_1 == 0:
                user_option_2 = 0
            elif user_option_1 == 2:
                user_option_2 = 2
            else:
                user_option_2 = Console.__input_optiune_utilizator(0, numar_optiuni_disponibile, ">>> ")

            # Optiunea 0: Iesire din aplicatie.
            if user_option_1 == 0:
                if user_option_2 == 0:
                    self.__print_exit_banner()
                    running = False

            # Optiunea 1: Conversie număr între baze.
            if user_option_1 == 1:
                if user_option_2 == 1:
                    self.__conversie_impartire_succesiva_ui()
                elif user_option_2 == 2:
                    self.__conversie_metoda_substitutiei_ui()
                elif user_option_2 == 3:
                    self.__conversie_baza_intermediara_ui()

            # Optiunea 2: Conversii rapide (2, 4, 8, 16).
            if user_option_1 == 2:
                if user_option_2 == 2:
                    self.__conversie_rapida_ui()

            # Optiunea 3: Operatii aritmetice în diferite baze.
            if user_option_1 == 3:
                if user_option_2 == 1:
                    self.__adunare_in_baze_ui()
                elif user_option_2 == 2:
                    self.__scadere_in_baze_ui()
                elif user_option_2 == 3:
                    self.__inmultire_in_baze_cu_o_cifra_ui()
                elif user_option_2 == 4:
                    self.__impartire_in_baze_ui()

            # Resetam variabila ok pentru a printa meniul principal la urmatoarea iteratie.
            ok = 0