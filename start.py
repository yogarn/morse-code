def morse(letter):
    match(letter):
        #alphabet
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
        #number
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
        #special case
        case " ":
            return("/")
def main():
    code = []
    #waiting input
    words = input("Enter Word(s) : ")
    #divide word to letters
    letters = [*words.lower()]
    #turn letter into code
    for letter in letters:
        code.append(morse(letter))
    #print final code
    print("Morse : ", *code)
main()