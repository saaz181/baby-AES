import random
from baby_rijndael import babyr_enc, babyr_dec

def CBC_enc(plaintext, key):
    ciphertext = ''
    iv = [random.randint(0, 0xFF) for _ in range(4)]  # Initialization Vector

    for i_block in plaintext:
        if len(i_block) < 4:
            i_block = i_block + [0] * (4 - len(i_block))

        # XOR the block with the IV
        i_block_xor = [a ^ b for a, b in zip(i_block, iv)]

        # Encrypt the XOR result using babyr_enc
        c_block = babyr_enc(i_block_xor, key)

        # Update IV for the next iteration
        iv = c_block

        # Convert the ciphertext block to a hexadecimal string
        ciphertext += ''.join(format(x, '02x') for x in c_block)

    return ciphertext

def CBC_dec(ciphertext, key):
    plaintext = ''
    iv = [0] * 4  # Initialization Vector

    for i in range(0, len(ciphertext), 8):
        c_block = [int(ciphertext[i:i+2], 16), int(ciphertext[i+2:i+4], 16),
                   int(ciphertext[i+4:i+6], 16), int(ciphertext[i+6:i+8], 16)]

        # Decrypt the ciphertext block using babyr_dec
        i_block_xor = babyr_dec(c_block, key)

        # XOR the decrypted block with the IV
        plaintext_block = [a ^ b for a, b in zip(i_block_xor, iv)]

        # Update IV for the next iteration
        iv = c_block

        # Convert the plaintext block to a hexadecimal string
        plaintext += ''.join(format(x, '02x') for x in plaintext_block)

    return plaintext

