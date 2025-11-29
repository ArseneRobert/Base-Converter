"""
Printare interfață console pentru aplicație.
"""

from utils.utils import determinare_optiuni_disponibile

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
    
    def showUi(self):
        """
        Afiseaza interfața console pentru aplicație.
        Input: -.
        Output: -.
        """ 

        running = True        
        ok = 0
        while running:

            Console.__print_banner()

            if ok == False:
                Console.__print_meniu_principal()

            user_option_1 = Console.__input_optiune_utilizator(0, 3, ">>> ")

            ok = user_option_1

            if ok != 0:
                Console.__print_optiuni_ext_sau_col(ok)

            numar_optiuni_disponibile = determinare_optiuni_disponibile(user_option_1)
            if user_option_1 == 0:
                user_option_2 = 0
            elif user_option_1 == 2:
                user_option_2 = 2
            else:
                user_option_2 = Console.__input_optiune_utilizator(0, numar_optiuni_disponibile, ">>> ")

            if user_option_1 == 0:
                if user_option_2 == 0:
                    print("Iesire din aplicatie...")
                    running = False

            if user_option_1 == 1:
                if user_option_2 == 1:
                    print("Ai ales Conversie număr între baze -> Impartire succesiva.")
                elif user_option_2 == 2:
                    print("Ai ales Conversie număr între baze -> Metoda substitutiei.")
                elif user_option_2 == 3:
                    print("Ai ales Conversie număr între baze -> Utilizarea unei baze intermediare.")

            if user_option_1 == 2:
                if user_option_2 == 2:
                    print("Ai ales Conversii rapide (2, 4, 8, 16).")

            if user_option_1 == 3:
                if user_option_2 == 1:
                    print("Ai ales Operatii aritmetice în diferite baze -> Adunare.")
                elif user_option_2 == 2:
                    print("Ai ales Operatii aritmetice în diferite baze -> Scadere.")
                elif user_option_2 == 3:
                    print("Ai ales Operatii aritmetice în diferite baze -> Inmultire.")
                elif user_option_2 == 4:
                    print("Ai ales Operatii aritmetice în diferite baze -> Impartire.")

            ok = 0