import sys
import os
import random
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc, babyr_dec, print_b


def generate_random_dataset(size):
    dataset = []
    for _ in range(size):
        block = random.randint(0, 0xFFFF)  # Generating a random 16-bit block
        key = random.randint(0, 0xFFFF)    # Generating a random 16-bit key
        dataset.append((block, key))
    return dataset

# Example: Generate a dataset with 10 random pairs of blocks and keys
random_dataset = generate_random_dataset(10)

# Example of how to use your encryption and decryption functions
for block, key in random_dataset:
    encrypted_block = babyr_enc(block, key)
    hex_string = ''.join([hex(b)[2:].zfill(2) for b in encrypted_block])

    decrypted_block = babyr_dec(int(hex_string, 16), key)
    
    # print(f"Original Block: {print_b(block)}")
    print(f"Encrypted Block: {print_b(encrypted_block)}")
    print(f"Decrypted Block: {print_b(decrypted_block)}")
    print("=" * 20)