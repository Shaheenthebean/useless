import sys

if __name__ == "__main__":
    print("enter/paste your text to uselessify. Ctrl-D when done.")
    contents = ''
    while True:
        try:
            contents += input()+"\n"
        except EOFError:
            break

    qwerty = 'qwertyuiopasdfghjklzxcvbnm'
    newstring = ''

    for letter in contents:
        if letter.lower() in qwerty:
            upper = letter.isupper()
            letter = letter.lower()
            if len(sys.argv) > 1 and sys.argv[1] == "reverse":
                letter = qwerty[(qwerty.index(letter)-1) % len(qwerty)]
            else:
                letter = qwerty[(qwerty.index(letter)+1) % len(qwerty)]
            if upper:
                letter = letter.upper()
        newstring += letter
    print("we am now become useless:")
    print(newstring)
