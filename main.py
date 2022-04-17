from random import randint
from string import ascii_uppercase as alphabet
from os.path import exists
from sys import exit as quit
from pickle import load, dump


class CaesarCipher():
    def __init__(self):
        self.__secret_key = 0

    def generate_key(self):
        self.__secret_key = randint(1, 25)
        print("New key: ", self.__secret_key)

    def __algorithm__(self, infile, outfile, reverse=False):
        key = self.__secret_key
        if reverse:
            key *= -1
        input_file = open(infile, 'r')
        output_file = open(outfile, 'w')
        for line in input_file.readlines():
            new_line = ""
            for letter in line:
                if letter.upper() in alphabet:
                    number = alphabet.find(letter.upper())
                    number = (number + key) % 26
                    if letter.isupper():
                        new_line += alphabet[number]
                    else:
                        new_line += alphabet[number].lower()
                else:
                    new_line += letter
            output_file.write(new_line)
        output_file.close()
        input_file.close()

    def encrypt(self, infile, outfile):
        self.__algorithm__(infile, outfile)

    def decrypt(self, infile, outfile):
        self.__algorithm__(infile, outfile, reverse=True)

    def print_key(self):
        print(f"Key: {self.__secret_key}")

    def export_data(self, outfile):
        try:
            file = open(outfile, 'wb')
            dump(self, file)
            file.close()
            print("Key written to file " + outfile)
        except:
            print("There was an error.\nCould not export the key.")


def import_cipher(infile):
    file = open(infile, 'rb')
    output = load(file)
    file.close()
    return output


def menu():
    cipher = CaesarCipher()
    while True:
        print("Enter your choice: ")
        print("1) Generate secret key.")
        print("2) Encrypt a file.")
        print("3) Decrypt a file.")
        print("4) Export cipher state.")
        print("5) Import cipher state.")
        print("6) Quit.")
        choice = input("> ")
        if choice == '1':
            cipher.generate_key()
            print("New key generated!\n")
        elif choice == '2':
            input_file = input("input file:\n> ")
            if not exists(input_file):
                print("Input file does not exist!\n")
                break
            else:
                output_file = input("output file:\n> ")
                cipher.encrypt(input_file, output_file)
        elif choice == '3':
            input_file = input("input file:\n> ")
            if not exists(input_file):
                print("Input file does not exist!\n")
                break
            else:
                output_file = input("output file:\n> ")
                cipher.decrypt(input_file, output_file)
        elif choice == '4':
            file = input("Export key filename: ")
            cipher.print_key()
            cipher.export_data(file)
        elif choice == '5':
            file = input("File: ")
            try:
                if exists(file):
                    cipher = import_cipher(file)
                    cipher.print_key()
                else:
                    print("File not found.")
            except:
                print("Invalid file.")
        elif choice == '6':
            print("Thanks for using!")
            quit()
        else:
            print("Invalid option!\n")


if __name__ == '__main__':
    menu()
