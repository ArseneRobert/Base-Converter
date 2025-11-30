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

def conversie_la_baza_10(numar_baza_sursa, baza_sursa):
    """
    Converteste un numar dintr-o baza in baza 10.
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
    for index, cifra in enumerate(numar_baza_sursa):
        valoare_cifra = cifre.index(cifra)
        putere = lungime_numar - index - 1
        rezultat += valoare_cifra * (baza_sursa ** putere)
    return rezultat

def conversie_de_la_baza_10(numar_decimal, baza_destinatie):
    """
    Converteste un numar din baza 10 in alta baza.
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
    while numar_decimal > 0:
        rest = numar_decimal % baza_destinatie
        rezultat = cifre[rest] + rezultat
        numar_decimal //= baza_destinatie
    return rezultat

def conversie_impartire_succesiva(numar_de_convertit, baza_sursa, baza_destinatie):
    """
    Conversteste un numar din baza p in baza q folosind metoda impartirii succesive.
    Input: numar_de_convertit - int = numarul in baza p care trebuie convertit.
              baza_sursa - int = baza din care trebuie convertit numarul.
              baza_destinatie - int = baza in care trebuie convertit numarul.
    Output: str - Numarul convertit in baza destinatie.
    """
    if not validare_numar_in_baza(str(numar_de_convertit), baza_sursa):
        raise ValueError(f"Numarul {numar_de_convertit} nu este valid in baza {baza_sursa}.")
    
    numar_decimal = conversie_la_baza_10(numar_de_convertit, baza_sursa)
    numar_decimal = int(numar_decimal)

    if numar_decimal == 0:
        return "0", "Numarul este 0, nu avem pasi de afisat.\n"
    
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

def conversie_metoda_substitutiei(numar_de_convertit, baza_sursa, baza_destinatie):
    """
    Input: numar_de_convertit - str = numarul in baza sursa care trebuie convertit.
           baza_sursa - int = baza din care trebuie convertit numarul.
    Output: int - Numarul convertit in baza destinatie.
    """
    if not validare_numar_in_baza(numar_de_convertit, baza_sursa):
        raise ValueError(f"Numarul {numar_de_convertit} nu este valid in baza {baza_sursa}.")
    
    if numar_de_convertit == "0":
        return "0", "Numarul este 0, nu avem pasi de afisat.\n"
    
    if baza_destinatie == 10 and baza_sursa == 10:
        rezultat = conversie_la_baza_10(numar_de_convertit, baza_sursa)
        pasi = f"Numarul in baza 10 este: {rezultat}\n"
        return rezultat, pasi

    cifre = "0123456789ABCDEF"
    numar_de_convertit = numar_de_convertit.upper()
    lungime_numar = len(numar_de_convertit)
    rezultat = 0
    contor_pasi = 1
    pasi = ""
    for index, cifra in enumerate(numar_de_convertit):
        valoare_cifra = cifre.index(cifra)
        putere = lungime_numar - index - 1
        valoare_suma = valoare_cifra * (baza_sursa ** putere)
        rezultat += valoare_suma
        pasi += f"Pasul {contor_pasi}: {cifra} * ({baza_sursa}^{putere}) = {valoare_suma} +\n"
        contor_pasi += 1
    pasi += f"Suma valorilor: {rezultat}\n"
    rezultat_in_baza_destinatie = conversie_de_la_baza_10(rezultat, baza_destinatie)
    pasi += f"Numarul in baza {baza_destinatie} este: {rezultat_in_baza_destinatie}\n"
    return rezultat_in_baza_destinatie, pasi

def conversie_baza_intermediara(numar_de_convertit, baza_sursa, baza_destinatie):
    """
    Converteste un numar dintr-o baza in alta baza prin conversie intermediara in baza 10.
    Input: numar_de_convertit - str = numarul in baza sursa care trebuie convertit.
           baza_sursa - int = baza din care trebuie convertit numarul.
           baza_destinatie - int = baza in care trebuie convertit numarul.
    Output: str - Numarul convertit in baza destinatie.
    """
    numar_in_baza_10, pasi_substitutie = conversie_metoda_substitutiei(numar_de_convertit, baza_sursa, 10)
    if baza_destinatie == 10:
        pasi_substitutie += "Numarul este deja in baza 10, nu este nevoie de conversie.\n"
        return numar_in_baza_10, pasi_substitutie
    numar_in_baza_destinatie, pasi_impartire = conversie_impartire_succesiva(numar_in_baza_10, 10, baza_destinatie)
    pasi = f"Conversie din baza {baza_sursa} in baza 10:\n{pasi_substitutie}\n"
    pasi += f"Conversie din baza 10 in baza {baza_destinatie}:\n{pasi_impartire}\n"
    return numar_in_baza_destinatie, pasi

def conversie_rapida(numar_de_convertit, baza_sursa, baza_destinatie):  
    """
    Converteste rapid intre bazele 2, 4, 8 si 16.
    Input: numar_de_convertit - str = numarul in baza sursa care trebuie convertit.
           baza_sursa - int = baza din care trebuie convertit numarul.
           baza_destinatie - int = baza in care trebuie convertit numarul.
    Output: str - Numarul convertit in baza destinatie.    
    """
    if baza_sursa not in [2, 4, 8, 16] or baza_destinatie not in [2, 4, 8, 16]:
        raise ValueError("Conversiile rapide sunt suportate doar intre bazele 2, 4, 8 si 16.")
    
    if not validare_numar_in_baza(numar_de_convertit, baza_sursa):
        raise ValueError(f"Numarul {numar_de_convertit} nu este valid in baza {baza_sursa}.")
    
    conversii_directe = {
        (2, 4): 2,
        (4, 2): 0.5,
        (2, 8): 3,
        (8, 2): 1/3,
        (2, 16): 4,
        (16, 2): 0.25,
        (4, 8): 1.5,
        (8, 4): 2/3,
        (4, 16): 2,
        (16, 4): 0.5,
        (8, 16): 1,
        (16, 8): 1
    }

    if baza_sursa == baza_destinatie:
        return numar_de_convertit, "Baza sursa si baza destinatie sunt aceleasi, numarul ramane neschimbat.\n"
    
    if baza_sursa < baza_destinatie:
        factor = conversii_directe[(baza_sursa, baza_destinatie)]
        grupare = int(factor)
        numar_de_convertit = numar_de_convertit.zfill(((len(numar_de_convertit) + grupare - 1) // grupare) * grupare)
        rezultat = ""
        pasi = ""
        for i in range(0, len(numar_de_convertit), grupare):
            grup = numar_de_convertit[i:i+grupare]
            valoare = conversie_la_baza_10(grup, baza_sursa)
            cifra_in_baza_destinatie = conversie_de_la_baza_10(int(valoare), baza_destinatie)
            rezultat += cifra_in_baza_destinatie
            pasi += f"Grup: {grup} (baza {baza_sursa}) -> {valoare} (baza 10) -> {cifra_in_baza_destinatie} (baza {baza_destinatie})\n"
        return rezultat.lstrip("0"), pasi
    else:
        factor = conversii_directe[(baza_destinatie, baza_sursa)]
        grupare = int(factor)
        rezultat = ""
        pasi = ""
        for cifra in numar_de_convertit:
            valoare_in_baza_10 = conversie_la_baza_10(cifra, baza_sursa)
            grup_in_baza_sursa = conversie_de_la_baza_10(int(valoare_in_baza_10), baza_destinatie)
            grup_in_baza_sursa = grup_in_baza_sursa.zfill(grupare)
            rezultat += grup_in_baza_sursa
            pasi += f"Cifra: {cifra} (baza {baza_sursa}) -> {valoare_in_baza_10} (baza 10) -> {grup_in_baza_sursa} (baza {baza_destinatie})\n"
        return rezultat.lstrip("0"), pasi