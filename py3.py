#Caesar's cypher
#Introduce ROT-X (de)coder
#>>> encode('Hello python!')
#'Hryyb clguba!'
#>>> decode('Hryyb clguba!')
#'Hello python!'
#Bonus: dynamic rotation


def encode(text):      
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    key = int(raw_input('Enter rotation key (1 - 26): '))
    if key == 0 or key > 26:
        print('Invalid key!')
        key = int(raw_input('Enter rotation key (1 - 26): '))


    before_key = alphabet[:key]
    after_key = alphabet[key:]
    shifted_alphabet = after_key + before_key



    caesar_text = []

    for i in text:

        if i == ' ':

            caesar_text += [' ']

        else:

            letter_position = int(alphabet.index(i))

            caesar_letter = shifted_alphabet[letter_position]

            caesar_text += caesar_letter

    print(''.join(caesar_text))

    return 

            

    



def decode(caesar_text):     

    alphabet = ('abcdefghijklmnopqrstuvwxyz')

    key = int(raw_input('Enter rotation key (1 - 26): '))

    if key > 26 or key == 0:

        print('Invalid key!')

        key = int(raw_input('Enter rotation key (1 - 26): '))

    before_key = alphabet[:key]

    after_key = alphabet[key:]

    shifted_alphabet = after_key + before_key



    text = []

    for i in caesar_text:

        if i == ' ':

            text += [' ']

        else:

            caesar_letter_position = int(shifted_alphabet.index(i))

            letter = alphabet[caesar_letter_position]

            text += letter

    print(''.join(text)) 

    return 
