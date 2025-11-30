"""
Functii pentru conversii.
"""

def validare_numar_in_baza(numar, baza):
    """
    Valideaza daca un numar este valid intr-o baza data.
    Input: numar - str = numarul care trebuie validat.
           baza - int = baza in care trebuie validat numarul.
    Output: bool - True daca numarul este valid in baza data, False altfel.
    """
    cifre_valide = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    for cifra in numar:
        if cifra.upper() not in cifre_valide[:baza]:
            return False
    return True

def conversie_impartire_succesiva(numar_decimal, baza_destinatie):
    """
    Converteste un numar din baza 10 in alta baza folosind metoda impartirii succesive.
    Input: numar_decimal - int = numarul in baza 10 care trebuie convertit.
           baza_destinatie - int = baza in care trebuie convertit numarul.
    Output: str - Numarul convertit in baza destinatie.
    """
    if not validare_numar_in_baza(str(numar_decimal), 10):
        raise ValueError(f"Numarul {numar_decimal} nu este valid in baza 10.")
    
    numar_decimal = int(numar_decimal)
    if numar_decimal == 0:
        return "0"
    cifre = "0123456789ABCDEF"
    rezultat = ""
    contor_pasi = 1
    pasi = ""
    while numar_decimal > 0:
        numar_decimal_inainte = numar_decimal
        rest = numar_decimal % baza_destinatie
        rezultat = cifre[rest] + rezultat
        numar_decimal //= baza_destinatie
        pasi += f"Pasul {contor_pasi}: {numar_decimal_inainte} / {baza_destinatie} = {numar_decimal} rest {cifre[rest]}\n"
        contor_pasi += 1
    pasi += "Resturile citite de jos in sus formeaza numarul convertit.\n"
    rezultat = rezultat[::-1]
    return rezultat, pasi

def conversie_metoda_substitutiei(numar_baza_sursa, baza_sursa):
    """
    Converteste un numar dintr-o baza in baza 10 folosind metoda substitutiei.
    Input: numar_baza_sursa - str = numarul in baza sursa care trebuie convertit.
           baza_sursa - int = baza din care trebuie convertit numarul.
    Output: int - Numarul convertit in baza 10.
    """
    if not validare_numar_in_baza(numar_baza_sursa, baza_sursa):
        raise ValueError(f"Numarul {numar_baza_sursa} nu este valid in baza {baza_sursa}.")
    
    cifre = "0123456789ABCDEF"
    numar_baza_sursa = numar_baza_sursa.upper()
    lungime_numar = len(numar_baza_sursa)
    rezultat = 0
    contor_pasi = 1
    pasi = ""
    for index, cifra in enumerate(numar_baza_sursa):
        valoare_cifra = cifre.index(cifra)
        putere = lungime_numar - index - 1
        valoare_suma = valoare_cifra * (baza_sursa ** putere)
        rezultat += valoare_suma
        pasi += f"Pasul {contor_pasi}: {cifra} * ({baza_sursa}^{putere}) = {valoare_suma} +\n"
        contor_pasi += 1
    pasi += f"Suma valorilor: {rezultat}\n"
    return rezultat, pasi

def conversie_baza_intermediara(numar_baza_sursa, baza_sursa, baza_destinatie):
    """
    Converteste un numar dintr-o baza in alta baza folosind o baza intermediara (baza 10).
    Input: numar_baza_sursa - str = numarul in baza sursa care trebuie convertit.
           baza_sursa - int = baza din care trebuie convertit numarul.
           baza_destinatie - int = baza in care trebuie convertit numarul.
    Output: str - Numarul convertit in baza destinatie.
    """
    # Convertim mai intai numarul din baza sursa in baza 10.
    numar_baza_10, pasi_substitutiei = conversie_metoda_substitutiei(numar_baza_sursa, baza_sursa)
    # Apoi convertim numarul din baza 10 in baza destinatie.
    numar_baza_destinatie, pasi_impartirii = conversie_impartire_succesiva(numar_baza_10, baza_destinatie)
    pasi = f"Conversie din baza {baza_sursa} in baza 10 folosind metoda substitutiei:\n{pasi_substitutiei}\n"
    pasi += f"Conversie din baza 10 in baza {baza_destinatie} folosind metoda impartirii succesive:\n{pasi_impartirii}\n"
    return numar_baza_destinatie, pasi
    