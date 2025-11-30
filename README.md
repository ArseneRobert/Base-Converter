# Base-Converter

Aplicație CLI (Command Line Interface) pentru conversia numerelor între diferite baze numerice (2-16) și efectuarea operațiilor aritmetice în baze numerice diferite.

## 📋 Cuprins

- [Descriere](#descriere)
- [Funcționalități](#funcționalități)
- [Instalare](#instalare)
- [Utilizare](#utilizare)
- [Structura Proiectului](#structura-proiectului)
- [Metode de Conversie](#metode-de-conversie)
- [Operații Aritmetice](#operații-aritmetice)
- [Exemple](#exemple)

## 📖 Descriere

Base-Converter este o aplicație interactivă scrisă în Python care permite conversia numerelor între diferite sisteme de numerație (baze 2-16) și efectuarea operațiilor aritmetice în aceste baze. Aplicația oferă mai multe metode de conversie și afișează pașii detaliați pentru fiecare operație.

## ✨ Funcționalități

### 1. Conversii între baze (2-16)

- **Împărțire succesivă** - Metodă clasică de conversie prin împărțiri repetate
- **Metoda substituției** - Conversie prin calculul valorii polinomiale
- **Bază intermediară** - Conversie prin baza 10 ca intermediar
- **Conversii rapide** - Conversii directe între bazele 2, 4, 8, 16

### 2. Operații aritmetice în diferite baze

- **Adunare** - Adunarea a două numere cu transport
- **Scădere** - Scăderea a două numere cu împrumut
- **Înmulțire** - Înmulțirea cu o cifră
- **Împărțire** - Împărțirea la o cifră cu rest

## 🚀 Instalare

### Cerințe

- Python 3.7 sau mai recent

### Pași de instalare

1. Clonează repository-ul:

```bash
git clone https://github.com/ArseneRobert/Base-Converter.git
cd Base-Converter
```

2. Rulează aplicația:

```bash
python app.py
```

## 💻 Utilizare

### Pornire aplicație

```bash
python app.py
```

### Meniu principal

```
╔═════════════════════════════════════════════════╗
║                 Convertor de baze               ║
╚═════════════════════════════════════════════════╝
║ 1. Conversie număr între baze.                  ║
║ 2. Conversii rapide (2, 4, 8, 16).              ║
║ 3. Operatii aritmetice în diferite baze.        ║
║ 0. Iesire din aplicatie.                        ║
╚═════════════════════════════════════════════════╝
```

## 📁 Structura Proiectului

```
Base-Converter/
│
├── app.py                          # Punct de intrare al aplicației
├── README.md                       # Documentația proiectului
│
├── domain/                         # Logica de business
│   ├── conversii.py               # Funcții pentru conversii între baze
│   └── operatii_aritmetice.py     # Funcții pentru operații aritmetice
│
├── ui/                            # Interfața cu utilizatorul
│   └── console.py                 # Interfața consolă
│
└── utils/                         # Funcții utilitare
    └── utils.py                   # Funcții ajutătoare
```

## 🔄 Metode de Conversie

### 1. Împărțire Succesivă

Convertește un număr din orice bază în altă bază prin:

1. Convertirea numărului în baza 10
2. Împărțiri succesive la baza destinație
3. Colectarea resturilor în ordine inversă

**Exemplu:** 25₁₀ → 11001₂

```
25 ÷ 2 = 12 rest 1
12 ÷ 2 = 6  rest 0
6  ÷ 2 = 3  rest 0
3  ÷ 2 = 1  rest 1
1  ÷ 2 = 0  rest 1
Rezultat: 11001
```

### 2. Metoda Substituției

Convertește prin calculul direct al valorii polinomiale:

- Fiecare cifră este înmulțită cu puterea corespunzătoare a bazei
- Sumarea tuturor valorilor dă rezultatul în baza 10
- Conversie ulterioară în baza destinație dacă este necesar

**Exemplu:** 1A₁₆ → 26₁₀

```
1 × 16¹ = 16
A × 16⁰ = 10
Total: 16 + 10 = 26
```

### 3. Bază Intermediară

Folosește baza 10 ca bază intermediară pentru conversii:

1. Conversie din baza sursă → baza 10 (substituție)
2. Conversie din baza 10 → baza destinație (împărțire succesivă)

### 4. Conversii Rapide (2, 4, 8, 16)

Conversii directe între bazele putere de 2:

- **2 → 4**: Grupare câte 2 biți
- **2 → 8**: Grupare câte 3 biți
- **2 → 16**: Grupare câte 4 biți
- Și invers

## ➕ Operații Aritmetice

### Adunare

Adună două numere cifră cu cifră cu gestionarea transportului:

```
  1 F₁₆
+   F₁₆
-------
  1 E₁₆
```

### Scădere

Scade două numere cifră cu cifră cu gestionarea împrumutului:

```
  2 A₁₆
-   F₁₆
-------
  1 B₁₆
```

### Înmulțire cu o cifră

Înmulțește un număr cu o singură cifră:

```
  1 2₁₆
×    3₁₆
-------
  3 6₁₆
```

### Împărțire la o cifră

Împarte un număr la o singură cifră cu rest:

```
1 E₁₆ ÷ 2₁₆ = F₁₆ rest 0
```

## 📝 Exemple

### Conversie din baza 10 în baza 2

```
Input: 25 (baza 10)
Destinație: baza 2
Output: 11001
```

### Conversie din baza 16 în baza 10

```
Input: FF (baza 16)
Destinație: baza 10
Output: 255
```

### Adunare în baza 16

```
Input: F + F (baza 16)
Output: 1E
```

### Conversie rapidă 2 → 16

```
Input: 11111111 (baza 2)
Output: FF (baza 16)
Pași: 1111 → F, 1111 → F
```

## 🛠️ Funcții Principale

### `domain/conversii.py`

- `validare_numar_in_baza(numar, baza)` - Validează dacă numărul este valid în baza specificată
- `conversie_la_baza_10(numar, baza)` - Convertește din orice bază în baza 10
- `conversie_de_la_baza_10(numar, baza)` - Convertește din baza 10 în orice bază
- `conversie_impartire_succesiva(numar, baza_sursa, baza_dest)` - Conversie prin împărțire
- `conversie_metoda_substitutiei(numar, baza_sursa, baza_dest)` - Conversie prin substituție
- `conversie_baza_intermediara(numar, baza_sursa, baza_dest)` - Conversie prin baza 10
- `conversie_rapida(numar, baza_sursa, baza_dest)` - Conversii rapide între 2, 4, 8, 16

### `domain/operatii_aritmetice.py`

- `adunare_in_baze(numar1, numar2, baza)` - Adunare cu transport
- `scadere_in_baze(numar1, numar2, baza)` - Scădere cu împrumut
- `inmultire_in_baze_cu_o_cifra(numar, cifra, baza)` - Înmulțire cu o cifră
- `impartirea_cu_o_cifra(numar, cifra, baza)` - Împărțire la o cifră

## 🔍 Validări

Aplicația include validări complete:

- Verificare cifre valide pentru baza specificată (0-9, A-F)
- Verificare baze valide (2-16)
- Prevenirea împărțirii la zero
- Verificare scădere negativă

## 📄 Licență

Acest proiect este open-source și disponibil pentru utilizare educațională.

## 👤 Autor

**Arsene Robert**

- GitHub: [@ArseneRobert](https://github.com/ArseneRobert)

## 🤝 Contribuții

Contribuțiile sunt binevenite! Pentru modificări majore:

1. Fork repository-ul
2. Creează un branch pentru feature-ul tău
3. Commit modificările
4. Push pe branch
5. Deschide un Pull Request
