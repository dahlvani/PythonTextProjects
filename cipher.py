Max_Key = 26

def getMode():
    while True:
        print('encrypt or decrypt?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('What is your message?/n')
    return input()

def getKey():
    key = 0
    while True:
        print('What is your key number? (1-%s)' % (Max_Key))
        key = int(input())
        if (key >= 1 and key <= Max_Key):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Your message translated reads')

print(getTranslatedMessage(mode, message, key))
