import PyPDF2

def search_in_pdf_files(pdf_paths, search_string, case_sensitive=False):
    results = []

    for pdf_path in pdf_paths:
        occurrences = 0

        # Apri e leggi il PDF
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Cerca in ogni pagina del PDF
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()

                # Modifica la ricerca in base alla sensibilità al maiuscolo/minuscolo
                if not case_sensitive:
                    text = text.lower()
                    search_string = search_string.lower()

                # Conta le occorrenze della stringa nella pagina
                occurrences += text.count(search_string)

        # Aggiungi ai risultati solo se ci sono occorrenze
        if occurrences > 0:
            results.append((pdf_path.split('/')[-1], occurrences))

    # Ordina i risultati per numero di occorrenze in ordine decrescente
    results.sort(key=lambda x: x[1], reverse=True)
    return results
