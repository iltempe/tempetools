#scarica un video da youtube e lo converte in mp3
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def download_audio(link, output_folder='downloads'):
    # Crea la cartella di output se non esiste
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Impostazioni di yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file_path = ydl.prepare_filename(info_dict)
            base, ext = os.path.splitext(audio_file_path)
            mp3_file_path = f"{base}.mp3"
            
            # Rinomina il file scaricato in MP3
            if not audio_file_path.endswith('.mp3'):
                audio = AudioSegment.from_file(audio_file_path)
                audio.export(mp3_file_path, format="mp3")
                os.remove(audio_file_path)
            
            print(f"Audio salvato come MP3: {mp3_file_path}")
    except Exception as e:
        print(f"Errore durante il download o la conversione: {e}")

# Esempio di utilizzo
download_audio('https://youtube.com/watch?v=jizMMBKCP3U')