def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    plaintext_length = len(plaintext)
    keyword_length = len(keyword)
    length_difference = plaintext_length / keyword_length
    if length_difference > 1:
        keyword = keyword*int((length_difference+1))

    symbol_codes = [ord(symbol) for symbol in plaintext]
    keyword_codes = [ord(symbol) for symbol in keyword]

    for i in range(len(keyword_codes)):
        if ord('A') <= keyword_codes[i] <= ord('Z'):
            keyword_codes[i] -= ord('A')
        else:
            keyword_codes[i] -= ord('a')

    symbol_codes_encrypt = list()
    count_key = 0
    for i in range(len(symbol_codes)):
        code = symbol_codes[i]
        code_keyword = keyword_codes[count_key]
        encrypt_code = code + code_keyword

        if ((encrypt_code > ord('Z')) and (code < ord('Z') + 1)):
            remainder = (encrypt_code % (ord('Z') + 1))
            encrypt_code = ord('A') + remainder
        elif ((encrypt_code > ord('z')) and (code < ord('z') + 1)):
            remainder = (encrypt_code % (ord('z') + 1))
            encrypt_code = ord('a') + remainder
        elif (code < ord('A')) or ((code > ord("Z")) and (code < ord('a'))) or (code > ord('z')):
            encrypt_code = code
            count_key -= 1

        count_key += 1
        symbol_codes_encrypt.append(encrypt_code)

    symbols = [chr(code) for code in symbol_codes_encrypt]
    ciphertext += ciphertext.join(symbols)

    return ciphertext or ''

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    ciphertext_length = len(ciphertext)
    keyword_length = len(keyword)
    length_difference = ciphertext_length / keyword_length
    if length_difference > 1:
        keyword = keyword*int((length_difference+1))

    symbol_codes = [ord(symbol) for symbol in ciphertext]
    keyword_codes = [ord(symbol) for symbol in keyword]

    for i in range(len(keyword_codes)):
        if ord('A') <= keyword_codes[i] <= ord('Z'):
            keyword_codes[i] -= ord('A')
        else:
            keyword_codes[i] -= ord('a')

    symbol_codes_decrypt = list()
    count_key = 0
    for i in range(len(symbol_codes)):
        code = symbol_codes[i]
        code_keyword = keyword_codes[count_key]
        decrypt_code = code - code_keyword

        if ((decrypt_code < ord('A')) and (code > ord('A') - 1)):
            remainder = ((ord('A') - 1) % decrypt_code)
            decrypt_code = ord('Z') - remainder
        elif ((decrypt_code < ord('a')) and (code > ord('a') - 1)):
            remainder = ((ord('a') - 1) % decrypt_code)
            decrypt_code = ord('z') - remainder
        elif (code < ord('A')) or ((code > ord("Z")) and (code < ord('a'))) or (code > ord('z')):
            decrypt_code = code
            count_key -= 1

        count_key += 1
        symbol_codes_decrypt.append(decrypt_code)

    symbols = [chr(code) for code in symbol_codes_decrypt]
    plaintext += plaintext.join(symbols)

    return plaintext or ''