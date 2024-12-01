def read_file_to_list(file_path):
    result = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Zeile trimmen und in Wörter aufteilen
                result.append(line.strip())
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    return result

