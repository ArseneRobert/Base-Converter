"""
Functii utilitare.
"""

def determinare_optiuni_disponibile(users_option):
    """
    Determina numarul de optiuni dispobilie utilizatorului in functie de numarul primei optiuni selectate.
    Input: users_option - int = numarul optiunii principale selectate de utilizator.
    Output: int - Numarul de optiuni valabile pentru optiunea principala selectata.
    """
    # Verificam cazurile in care optiunea principala nu are optiuni secundare.
    if users_option == 0:
        return 0
    if users_option == 2:
        return 2
    # Declaram un dictionar in care salvam numarul de optiuni secundare valabile pentru fiecare optiune principala.
    optiuni_disponibile_dict = {
        "1": 3,
        "3": 4
    }
    return optiuni_disponibile_dict[f"{users_option}"]
