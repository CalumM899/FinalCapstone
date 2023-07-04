def encrypt():

    user_word = input("Input words to encode\n> ")
    user_word = user_word.upper()
   
    encoded_message = ""
    
    for i in user_word:
        
        if ord(i) < 65 or ord(i) > 90:
            encoded_message = encoded_message + i
            continue

        if (ord(i) + 15) > 90:
            difference = ord(i) + 15 - 90
            encoded_message = encoded_message + chr(64 + difference)
            continue

        else:
            encoded_message = encoded_message + chr(ord(i) + 15)
            continue
    
    print(encoded_message)


encrypt()
