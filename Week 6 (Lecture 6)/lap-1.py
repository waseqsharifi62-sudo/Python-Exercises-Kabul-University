class DocumentReadError(Exception):
    pass

def read_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except UnicodeDecodeError:
        print("Error: Encoding error.")
    except Exception as e:
        raise DocumentReadError(f"Failed to read document: {e}")

read_file()