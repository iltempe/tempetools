import os
from pydub import AudioSegment

def cut_mp3(input_file, start_time, end_time, output_file):
    try:
        # Carica il file audio
        audio = AudioSegment.from_file(input_file)
        
        # Taglia l'audio
        cut_audio = audio[start_time:end_time]
        
        # Salva il file tagliato
        cut_audio.export(output_file, format="mp3")
        print(f"Parte tagliata salvata come: {output_file}")
    except Exception as e:
        print(f"Errore: {e}")

# Esempio di utilizzo
if __name__ == "__main__":
    input_file = input("Inserisci il percorso del file MP3 di input: ")
    
    # Crea la cartella di output se non esiste
    output_folder = os.path.join(os.path.dirname(input_file), 'output')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_file_name = input("Inserisci il nome del file MP3 di output (es. output.mp3): ")
    output_file = os.path.join(output_folder, output_file_name)
    
    start_time = int(input("Inserisci il tempo di inizio in millisecondi (es. 30000 per 30 secondi): "))
    end_time = int(input("Inserisci il tempo di fine in millisecondi (es. 60000 per 60 secondi): "))
    
    cut_mp3(input_file, start_time, end_time, output_file)