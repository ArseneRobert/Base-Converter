"""
Operatii aritmetice in baze numerice diferite.
Module ce contine functii pentru adunare, scadere, inmultire si impartire in baze numerice diferite.
"""

from domain.conversii import conversie_la_baza_10, conversie_impartire_succesiva, conversie_metoda_substitutiei, validare_numar_in_baza

def adunare_in_baze(numar1, numar2, baza):
    """
    Aduna doua numere in baza specificata.
    Input: str - numar1, str - numar2, int - baza
    Output: str - Rezultatul adunarii in baza specificata.
    """
    # Validam numerele in baza specificata
    if not validare_numar_in_baza(numar1, baza) and not validare_numar_in_baza(numar2, baza):
        raise ValueError(f"Numerele {numar1} si {numar2} nu sunt valide in baza {baza}.")

    if not validare_numar_in_baza(numar1, baza):
        raise ValueError(f"Numarul {numar1} nu este valid in baza {baza}.")

    if not validare_numar_in_baza(numar2, baza):
        raise ValueError(f"Numarul {numar2} nu este valid in baza {baza}.")
    
    # Pregatim numerele pentru adunare invertindu-le si transformandu-le in uppercase
    numar1 = str(numar1).upper()
    numar1 = numar1[::-1]
    numar2 = str(numar2).upper()
    numar2 = numar2[::-1]

    # Egalizam lungimile numerelor prin completare cu zerouri
    if len(numar1) > len(numar2):
        numar2 += '0' * (len(numar1) - len(numar2))
    elif len(numar2) > len(numar1):
        numar1 += '0' * (len(numar2) - len(numar1))

    # Realizam adunarea cifra cu cifra cu gestionarea transportului 
    pasi = ""
    contor_pasi = 1
    numar_rezultat = ""
    transport = 0
    cifre = "0123456789ABCDEF"
    for i in range(len(numar1)):
        transport_initial = transport
        valoare_cifra1 = cifre.index(numar1[i])
        valoare_cifra2 = cifre.index(numar2[i])
        suma_cifre = valoare_cifra1 + valoare_cifra2 + transport
        valoare_numar_rezultat = suma_cifre % baza
        transport = suma_cifre // baza
        numar_rezultat += cifre[valoare_numar_rezultat]
        # Salvam pasii efectuati
        pasi += f"Pasul {contor_pasi}: {cifre[valoare_cifra1]} + {cifre[valoare_cifra2]} + transport {transport_initial} = {suma_cifre} => {suma_cifre} % {baza} = {cifre[valoare_numar_rezultat]} rest {suma_cifre // baza} => Cifra rezultat: {cifre[valoare_numar_rezultat]}, Transport: {transport}\n"
        contor_pasi += 1

    # Daca mai ramane transport, il adaugam ca cifra cea mai semnificativa
    if transport > 0:
        numar_rezultat += cifre[transport]
        pasi += f"Pasul {contor_pasi}: Adaugam transportul ramas {transport} ca cifra cea mai semnificativa.\n"
    
    # Inversam rezultatul pentru a obtine numarul corect
    numar_rezultat = numar_rezultat[::-1]
    pasi += f"Numarul rezultat este obtinut prin citirea cifrelor de jos in sus: {numar_rezultat}\n"
    return numar_rezultat, pasi

def scadere_in_baze(numar1, numar2, baza):
    """
    Scade doua numere in baza specificata.
    Input: str - numar1, str - numar2, int - baza
    Output: str - Rezultatul scaderii in baza specificata.
    """
    # Validam numerele in baza specificata
    if not validare_numar_in_baza(numar1, baza) and not validare_numar_in_baza(numar2, baza):
        raise ValueError(f"Numerele {numar1} si {numar2} nu sunt valide in baza {baza}.")

    if not validare_numar_in_baza(numar1, baza):
        raise ValueError(f"Numarul {numar1} nu este valid in baza {baza}.")

    if not validare_numar_in_baza(numar2, baza):
        raise ValueError(f"Numarul {numar2} nu este valid in baza {baza}.")
    
    if conversie_la_baza_10(numar1, baza) < conversie_la_baza_10(numar2, baza):
        raise ValueError(f"Scaderea nu este posibila deoarece {numar1} < {numar2} in baza {baza}.")
    
    # Pregatim numerele pentru scadere invertindu-le si transformandu-le in uppercase
    numar1 = str(numar1).upper()
    numar1 = numar1[::-1]
    numar2 = str(numar2).upper()
    numar2 = numar2[::-1]

    # Egalizam lungimile numerelor prin completare cu zerouri
    if len(numar1) > len(numar2):
        numar2 += '0' * (len(numar1) - len(numar2))
    elif len(numar2) > len(numar1):
        numar1 += '0' * (len(numar2) - len(numar1))

    # Realizam scaderea cifra cu cifra cu gestionarea imprumutului
    pasi = ""
    contor_pasi = 1
    numar_rezultat = ""
    imprumut = 0
    cifre = "0123456789ABCDEF"
    for i in range(len(numar1)):
        imprumut_initial = imprumut
        valoare_cifra1 = cifre.index(numar1[i])
        valoare_cifra2 = cifre.index(numar2[i])
        valoare_cifra1 -= imprumut
        if valoare_cifra1 < valoare_cifra2:
            valoare_cifra1 += baza
            imprumut = 1
        else:
            imprumut = 0
        diferenta_cifre = valoare_cifra1 - valoare_cifra2
        numar_rezultat += cifre[diferenta_cifre]
        # Salvam pasii efectuati
        pasi += f"Pasul {contor_pasi}: {cifre[valoare_cifra1 + (imprumut * baza)]} - {cifre[valoare_cifra2]} - imprumut {imprumut_initial} = {diferenta_cifre} => Cifra rezultat: {cifre[diferenta_cifre]}, Imprumut: {imprumut}\n"
        contor_pasi += 1
    
    # Inversam rezultatul pentru a obtine numarul corect
    numar_rezultat = numar_rezultat[::-1].lstrip('0')
    if numar_rezultat == "":
        numar_rezultat = "0"
    pasi += f"Numarul rezultat este obtinut prin citirea cifrelor de jos in sus: {numar_rezultat}\n"
    return numar_rezultat, pasi

def inmultire_in_baze_cu_o_cifra(numar, cifra, baza):
    """
    Inmulteste un numar cu o cifra in baza specificata.
    Input: str - numar, str - cifra, int - baza
    Output: str - Rezultatul inmultirii in baza specificata.
    """
    # Validam numerele in baza specificata
    if not validare_numar_in_baza(numar, baza) and not validare_numar_in_baza(cifra, baza):
        raise ValueError(f"Numerele {numar} si {cifra} nu sunt valide in baza {baza}.")

    if not validare_numar_in_baza(numar, baza):
        raise ValueError(f"Numarul {numar} nu este valid in baza {baza}.")

    if not validare_numar_in_baza(cifra, baza) or len(cifra) != 1:
        raise ValueError(f"Cifra {cifra} nu este valida in baza {baza}.")

    # Pregatim numerele pentru inmultire invertindu-le si transformandu-le in uppercase
    numar = str(numar).upper()
    numar = numar[::-1]
    cifra = cifra.upper()

    # Realizam inmultirea cifra cu cifra cu gestionarea transportului
    pasi = ""
    contor_pasi = 1
    cifre = "0123456789ABCDEF"
    valoare_cifra = cifre.index(cifra)
    rezultat_partial = ""
    transport = 0
    for i in range(len(numar)):
        transport_initial = transport
        valoare_cifra_numar = cifre.index(numar[i])
        produs = valoare_cifra_numar * valoare_cifra + transport
        valoare_numar_rezultat = produs % baza
        transport = produs // baza
        rezultat_partial += cifre[valoare_numar_rezultat]
        # Salvam pasii efectuati
        pasi += f"Pasul {contor_pasi}: {cifre[valoare_cifra_numar]} * {cifre[valoare_cifra]} + transport {transport_initial} = {produs} => {produs} % {baza} = {cifre[valoare_numar_rezultat]} rest {produs // baza} => Cifra rezultat: {cifre[valoare_numar_rezultat]}, Transport: {transport}\n"
        contor_pasi += 1

    # Daca mai ramane transport, il adaugam ca cifra cea mai semnificativa
    if transport > 0:
        rezultat_partial += cifre[transport]
        pasi += f"Pasul {contor_pasi}: Adaugam transportul ramas {transport} ca cifra cea mai semnificativa.\n"
    
    # Inversam rezultatul pentru a obtine numarul corect
    rezultat_partial = rezultat_partial[::-1]
    pasi += f"Numarul rezultat este obtinut prin citirea cifrelor de jos in sus: {rezultat_partial}\n"
    return rezultat_partial, pasi

def impartirea_cu_o_cifra(numar, cifra, baza):
    """
    Imparte un numar la o cifra in baza specificata.
    Input: str - numar, str - cifra, int - baza
    Output: str - Rezultatul impartirii in baza specificata.
    """
    # Validam numerele in baza specificata
    if not validare_numar_in_baza(numar, baza) and not validare_numar_in_baza(cifra, baza):
        raise ValueError(f"Numerele {numar} si {cifra} nu sunt valide in baza {baza}.")

    if not validare_numar_in_baza(numar, baza):
        raise ValueError(f"Numarul {numar} nu este valid in baza {baza}.")

    if not validare_numar_in_baza(cifra, baza) or len(cifra) != 1:
        raise ValueError(f"Cifra {cifra} nu este valida in baza {baza}.")

    cifre = "0123456789ABCDEF"

    # Verificam daca cifra este zero pentru a evita impartirea la zero
    if cifre.index(cifra.upper()) == 0:
        raise ValueError("Impartirea la zero nu este permisa.")
    
    # Pregatim numerele pentru impartire transformandu-le in uppercase
    numar = str(numar).upper()
    rezultat = ""
    rest = 0
    pasi = ""
    contor_pasi = 1
    valoare_cifra_divizor = cifre.index(cifra.upper())
    for cifra_numar in numar:
        valoare_cifra_numar = cifre.index(cifra_numar)
        dividend = rest * baza + valoare_cifra_numar
        numar_rezultat = dividend // valoare_cifra_divizor
        rest = dividend % valoare_cifra_divizor
        rezultat += cifre[numar_rezultat]
        # Salvam pasii efectuati
        pasi += f"Pasul {contor_pasi}: ({rest} * {baza} + {cifre[valoare_cifra_numar]}) / {cifre[valoare_cifra_divizor]} = {dividend} / {cifre[valoare_cifra_divizor]} = {cifre[numar_rezultat]} rest {rest}\n"
        contor_pasi += 1
    # Salvam restul final
    rest_rezultat = rest
    # Eliminam zerourile initiale din rezultat
    rezultat = rezultat.lstrip('0')
    pasi += f"Numarul rezultat este obtinut prin citirea cifrelor de sus in jos: {rezultat}\n"
    return rezultat, rest_rezultat, pasi