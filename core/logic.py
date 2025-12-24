import re
import qrcode
import os

def clean_filename(text: str) -> str:
    """Очистка текста для создания безопасного имени файла."""
    text = text.replace("https://", "").replace("http://", "").replace("www.", "")
    slug = re.sub(r'[^a-zA-Z0-9а-яА-Я]', '_', text)
    return slug[:40]

def read_links_from_file(file_path: str) -> list:
    """Читает файл links.txt и возвращает список строк."""
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        # Убираем пробелы и пустые строки
        return [line.strip() for line in f if line.strip()]

# --- ФУНКЦИЯ 3: Генерация QR-кода (Ядро) ---
def generate_qr(data: str, folder: str, filename: str):
    """Создает и сохраняет QR-код."""
    os.makedirs(folder, exist_ok=True)
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    full_path = os.path.join(folder, filename)
    img.save(full_path)
    return full_path