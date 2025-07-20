import os
import shutil

path = os.getcwd()

print(f"'{os.path.basename(path)}' klasörü düzenleniyor...")

try:
    files = os.listdir(path)
except OSError as e:
    print(f"Hata: Klasör okunurken bir sorun oluştu. {e}")
    exit()

file_extensions = {
    "Resimler": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videolar": [".mp4", ".mov", "avi", ".mkv", ".wmv"],
    "Müzikler": [".mp3", ".wav", ".ogg", ".flac"],
    "Belgeler": [".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".txt", ".rtf"],
    "Arşivler": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Kodlar": [".py", ".cs", ".js", ".html", ".css", ".cpp", ".java", ".php"],
    "Uygulamalar": [".exe", ".msi"],
}

def move_file(file, extension_map):
    file_extension = os.path.splitext(file)[1].lower()
    
    destination_folder = "Diğer Dosyalar"
    for folder, extensions in extension_map.items():
        if file_extension in extensions:
            destination_folder = folder
            break
            
    destination_path = os.path.join(path, destination_folder)
    
    if not os.path.exists(destination_path):
        try:
            os.makedirs(destination_path)
            print(f"Klasör oluşturuldu: {destination_folder}")
        except OSError as e:
            print(f"Hata: '{destination_folder}' klasörü oluşturulamadı. {e}")
            return

    try:
        shutil.move(os.path.join(path, file), os.path.join(destination_path, file))
        print(f"'{file}' dosyası '{destination_folder}' klasörüne taşındı.")
    except (shutil.Error, OSError) as e:
        print(f"Hata: '{file}' dosyası taşınamadı. {e}")

for file in files:
    if os.path.isfile(os.path.join(path, file)) and file != os.path.basename(__file__):
        move_file(file, file_extensions)

print("\nDüzenleme tamamlandı!")

input("\nKapatmak için Enter tuşuna basın...")

