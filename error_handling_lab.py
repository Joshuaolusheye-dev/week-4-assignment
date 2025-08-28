# Error Handling Lab
# This program asks the user for a filename and handles errors if it does not exist.

def read_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_file()
