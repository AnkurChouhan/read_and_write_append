def read_file(filename="sample.txt"):
    try:
        with open(filename, "r") as file:
            print("File content:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

if __name__ == "__main__":
    read_file()
