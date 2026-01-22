import sys

def count_characters(text):
    count = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters (alphabets, numbers, symbols)
            count += 0.5
        else:  # Non-ASCII characters (full-width characters, etc.)
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                input_text = f.read()
            length = count_characters(input_text)
            print(length)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("Usage: python custom_character_counter.py <file_path>")
