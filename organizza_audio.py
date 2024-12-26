#organizza tutti i file mp3 e wav sulla scrivania della folder produzioni AI del MAC

import os
import shutil

def organize_audio_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"La cartella sorgente '{source_folder}' non esiste.")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Cerca tutti i file .wav e .mp3 nella cartella sorgente
    files = [f for f in os.listdir(source_folder) if f.endswith('.wav') or f.endswith('.mp3')]

    # Raggruppa i file con lo stesso nome (senza estensione)
    file_groups = {}
    for file in files:
        base_name = os.path.splitext(file)[0]  # Ottieni il nome senza estensione
        if base_name not in file_groups:
            file_groups[base_name] = []
        file_groups[base_name].append(file)

    # Crea sottocartelle e sposta i file
    for base_name, group_files in file_groups.items():
        subfolder_path = os.path.join(source_folder, base_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        for file in group_files:
            original_path = os.path.join(source_folder, file)
            new_path = os.path.join(subfolder_path, file)
            shutil.move(original_path, new_path)

        # Copia la sottocartella nella cartella di destinazione
        shutil.copytree(subfolder_path, os.path.join(destination_folder, base_name))

        # Elimina la sottocartella nella cartella sorgente
        shutil.rmtree(subfolder_path)

if __name__ == "__main__":
    source_folder = "/Users/iltempe/Desktop"
    destination_folder = "/Users/iltempe/Music/Produzioni/AI"

    try:
        organize_audio_files(source_folder, destination_folder)
        print("Organizzazione completata!")
    except FileNotFoundError as e:
        print(f"Errore: {e}")
