import os
import sys

# Добавляем путь к корню проекта, чтобы импорты работали корректно
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.logic import read_links_from_file, clean_filename, generate_qr

def main():
    INPUT_FILE = "links.txt"
    OUTPUT_DIR = os.path.join("output", "QR_Results")

    print("--- Запуск Batch QR Generator ---")

    # 1. Загрузка данных
    links = read_links_from_file(INPUT_FILE)
    
    if not links:
        print(f"Ошибка: файл {INPUT_FILE} не найден или пуст.")
        return

    print(f"Найдено ссылок для обработки: {len(links)}")

    # 2. Цикл генерации
    for i, link in enumerate(links):
        try:
            name = f"{i+1:03d}_{clean_filename(link)}.png"
            generate_qr(link, OUTPUT_DIR, name)
            print(f"[+] Успешно: {name}")
        except Exception as e:
            print(f"[!] Ошибка на строке {link}: {e}")

    print(f"\nГотово! Файлы сохранены в папке: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()