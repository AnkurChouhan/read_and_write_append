def write_to_file(filename="output.txt"):
    user_input = input("Enter some data to write to the file: ")
    with open(filename, "w") as file:
        file.write(user_input + "\n")

def append_to_file(filename="output.txt"):
    additional_input = input("Enter additional data to append to the file: ")
    with open(filename, "a") as file:
        file.write(additional_input + "\n")

def read_file(filename="output.txt"):
    print("\nFinal content of the file:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    write_to_file()
    append_to_file()
    read_file()
