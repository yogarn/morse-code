#define morse code for each letter
def morse(letter):
    match(letter):
        #morse code for alphabet
        case "a":
            return(".-")
        case "b":
            return("-...")
        case "c":
            return("-.-.")
        case "d":
            return("-..")
        case "e":
            return(".")
        case "f":
            return("..-.")
        case "g":
            return("--.")
        case "h":
            return("....")
        case "i":
            return("..")
        case "j":
            return(".---")
        case "k":
            return("-.-")
        case "l":
            return(".-..")
        case "m":
            return("--")
        case "n":
            return("-.")
        case "o":
            return("---")
        case "p":
            return(".--.")
        case "q":
            return("--.-")
        case "r":
            return(".-.")
        case "s":
            return("...")
        case "t":
            return("-")
        case "u":
            return("..-")
        case "v":
            return("...-")
        case "w":
            return(".--")
        case "x":
            return("-..-")
        case "y":
            return("-.--")
        case "z":
            return("--..")
        #morse code for number
        case "1":
            return(".----")
        case "2":
            return("..---")
        case "3":
            return("...--")
        case "4":
            return("....-")
        case "5":
            return(".....")
        case "6":
            return("-....")
        case "7":
            return("--...")
        case "8":
            return("---..")
        case "9":
            return("----.")
        case "0":
            return("-----")
def main():
    code = []
    #get input from user
    words = input("Enter Word(s) : ")
    #turn string to lower case and divide word to character
    letters = [*words.lower()]
    #turn each character into morse code and add it to the list
    for letter in letters:
        code.append(morse(letter))
    #print the entire morse code
    print("Morse : ", *code)
main()
