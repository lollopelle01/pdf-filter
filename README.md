# PDF String Search Application

Questa applicazione web consente agli utenti di cercare stringhe all'interno di uno o più file PDF in una cartella selezionata. Gli utenti possono specificare se la ricerca deve essere case-sensitive o case-insensitive e visualizzare i risultati ordinati per numero di occorrenze.

## Funzionalità

- Seleziona una cartella contenente file PDF.
- Inserisci una stringa di ricerca (parola o frase).
- Scegli se la ricerca deve essere case-sensitive.
- Visualizza i risultati con il numero di occorrenze per ciascun file PDF.

## Tecnologie utilizzate

- Flask: framework web per la creazione dell'applicazione.
- PyMuPDF e PyPDF2: librerie per la gestione e il parsing dei file PDF.

## Requisiti

Assicurati di avere installato Python 3 o superiore.

## Istruzioni per l'installazione

1. **Clona il repository**:

    ```
    git clone https://github.com/lollopelle01/pdf-filter.git
    cd pdf-filter
    ```
2. **Installa le dipendenze**
    ```
    pip install -r requirements.txt
    ```
3. **Esegui l'applicazione**
    ```
    python app.py
    ```