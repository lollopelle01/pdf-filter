from flask import Flask, request, render_template
from utils import search_in_pdf_files
import os
import shutil

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ricevi la stringa di ricerca e la sensibilità
        search_string = request.form['search_string']
        case_sensitive = 'case_sensitive' in request.form
        
        # Ricevi i file PDF caricati
        uploaded_files = request.files.getlist("pdf_files")
        pdf_paths = []

        # Salva i file in una cartella temporanea
        temp_folder = 'uploaded_pdfs'
        os.makedirs(temp_folder, exist_ok=True)
        
        try:
            for file in uploaded_files:
                file_path = os.path.join(temp_folder, file.filename)
                file.save(file_path)
                pdf_paths.append(file_path)

            # Chiama la funzione per cercare nei PDF caricati
            results = search_in_pdf_files(pdf_paths, search_string, case_sensitive)
        
        finally:
            # Rimuove la cartella temporanea dopo l'uso
            shutil.rmtree(temp_folder)

        return render_template('results.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
