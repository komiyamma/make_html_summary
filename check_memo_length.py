
import sys
import os

# docsフォルダにあるcharacter_counter.pyをインポートするためにパスを追加
sys.path.append(os.path.dirname(__file__))
from custom_character_counter import count_characters

def check_length(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        length = count_characters(content)
        print(f"Calculated length: {length}")
        if 65 <= length < 80:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_to_check = sys.argv[1]
        if check_length(file_to_check):
            print(f"Validation OK: {file_to_check}")
            sys.exit(0)
        else:
            print(f"Validation NG: {file_to_check}")
            sys.exit(1)
    else:
        print("Usage: python check_memo_length.py <file_path>")
        sys.exit(1)
