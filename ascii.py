def decrypt(message: [int]) -> str:
    decrypted_message = []
    for x in message:
        decrypted_message.append(chr(x))
    return ''.join(decrypted_message)