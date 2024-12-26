#rinomina tutti i file di una cartella con la data e l'ora a cui sono stati salvati
import os
from datetime import datetime
import re

# Specifica il percorso della cartella
folder_path = "/Users/iltempe/Pictures/AI content/immagini"

# Pattern per identificare i file già rinominati con data e ora
date_time_pattern = re.compile(r"^\d{8}_\d{6}")

def rename_files_by_date(folder_path):
    try:
        # Verifica che il percorso esista
        if not os.path.exists(folder_path):
            print(f"La cartella '{folder_path}' non esiste.")
            return
        
        # Scorri tutti i file nella cartella
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Controlla che sia un file (non una directory)
            if os.path.isfile(file_path):
                # Controlla se il file è già rinominato
                if date_time_pattern.match(filename):
                    print(f"Saltato: {filename} (già rinominato)")
                    continue
                
                # Ottieni la data di modifica del file
                mod_time = os.path.getmtime(file_path)
                formatted_time = datetime.fromtimestamp(mod_time).strftime("%Y%m%d_%H%M%S")
                
                # Estrai l'estensione del file
                _, file_extension = os.path.splitext(filename)

                # Crea il nuovo nome del file
                new_name = f"{formatted_time}{file_extension}"
                new_path = os.path.join(folder_path, new_name)

                # Rinomina il file
                os.rename(file_path, new_path)
                print(f"Rinominato: {filename} -> {new_name}")

        print("Tutti i file non già rinominati sono stati rinominati con successo!")
    except Exception as e:
        print(f"Errore: {e}")

# Chiama la funzione
rename_files_by_date(folder_path)