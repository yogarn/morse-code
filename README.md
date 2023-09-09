# morse-code
turn string input to morse code

##How does this work?
this program is working by splitting each words into character and then turn that each character into morse code.
```
letters = [*words.lower()]
    for letter in letters:
        code.append(morse(letter))
    print("Morse : ", *code)
```
the code above is the most important part in this code. it's change the words to lower case and split each character to array. after that, the program will do a loop and turn each character to morse by calling ```morse()``` function. that function hold morse code data for each character.

to run the program, simply get in to the program directory and run ```python main.py```
