import sys
import os
import random
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc, babyr_dec, print_b


def convert_list_of_bytes_to_hex(list_of_bytes: list) -> int:
    hex_representation = ''.join([hex(x)[2:].zfill(2) for x in list_of_bytes])

    # Convert the concatenated hexadecimal string to an integer
    return int(hex_representation, 16)



def generate_cbc_dataset(size):
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext and key
        plaintext = random.randint(0, 0xFFFF)
        key = random.randint(0, 0xFFFF)

        # Generate a random 16-bit Initialization Vector (IV)
        iv = random.randint(0, 0xFFFF)

        # Encrypt the plaintext using CBC mode
        ciphertext = iv  # Initialization Vector for the first block
        for i in range(16):
            # XOR the plaintext with the previous ciphertext (or IV for the first block)
            plaintext ^= ciphertext
            # Encrypt the XORed result
            ciphertext = convert_list_of_bytes_to_hex(babyr_enc(plaintext, key))

            # Append the encrypted block to the dataset
            dataset.append((ciphertext, key))

    return dataset

# Example: Generate a dataset with 10 random pairs of ciphertexts and keys in CBC mode
cbc_dataset = generate_cbc_dataset(10)

print(cbc_dataset)
# # Example of how to use your decryption function for CBC mode
# for ciphertext, key in cbc_dataset:
#     decrypted_block = babyr_dec(ciphertext, key)
    
#     print(f"Original Ciphertext: {hex(ciphertext)}")
#     print(f"Decrypted Block: {print_b(decrypted_block)}")
#     print("=" * 20)