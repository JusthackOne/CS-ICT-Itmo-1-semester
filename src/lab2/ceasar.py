def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    symbol_codes = [ord(symbol) for symbol in plaintext]
    symbol_codes_encrypt = list()
    for code in symbol_codes:
        encrypt_code = code + shift
        if ((encrypt_code > ord('Z')) and (code < ord('Z') + 1)):
            remainder = (encrypt_code % (ord('Z') + 1))
            encrypt_code = ord('A') + remainder
        elif ((encrypt_code > ord('z')) and (code < ord('z') + 1)):
            remainder = (encrypt_code % (ord('z') + 1))
            encrypt_code = ord('a') + remainder
        elif (code < ord('A')) or ((code > ord("Z")) and (code < ord('a'))) or (code > ord('z')):
            encrypt_code = code
        symbol_codes_encrypt.append(encrypt_code)

    symbols = [chr(code) for code in symbol_codes_encrypt]
    ciphertext += ciphertext.join(symbols)

    return ciphertext or ''

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    symbol_codes = [ord(symbol) for symbol in ciphertext]
    symbol_codes_decrypt = list()
    for code in symbol_codes:
        decrypt_code = code - shift
        if ((decrypt_code < ord('A')) and (code > ord('A') - 1)):
            remainder = ((ord('A') - 1) % decrypt_code)
            decrypt_code = ord('Z') - remainder
        elif ((decrypt_code < ord('a')) and (code > ord('a') - 1)):
            remainder = ((ord('a') - 1) % decrypt_code)
            decrypt_code = ord('z') - remainder
        elif (code < ord('A')) or ((code > ord("Z")) and (code < ord('a'))) or (code > ord('z')):
            decrypt_code = code
        symbol_codes_decrypt.append(decrypt_code)

    symbols = [chr(code) for code in symbol_codes_decrypt]
    plaintext += plaintext.join(symbols)
    return plaintext or ''


