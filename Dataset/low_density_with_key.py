import random
import sys
import os
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc, print_b



def generate_low_density_key_dataset(size, plaintext_density=0.2, key_density=0.2):
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext with low density
        plaintext = 0
        for _ in range(16):
            if random.random() < plaintext_density:
                plaintext |= 1 << random.randint(0, 15)
        
        # Generate a random 16-bit key with low density
        key = 0
        for _ in range(16):
            if random.random() < key_density:
                key |= 1 << random.randint(0, 15)
        
        dataset.append((plaintext, key))
    return dataset

# Example: Generate a dataset with 10 random pairs of low-density plaintexts and keys
low_density_key_dataset = generate_low_density_key_dataset(10, plaintext_density=0.2, key_density=0.2)

# Example of how to use your encryption function
for plaintext, key in low_density_key_dataset:
    encrypted_block = babyr_enc(plaintext, key)
    
    print(f"Original Plaintext: {plaintext}")
    print(f"Original Key: {key}")
    print(f"Encrypted Block: {print_b(encrypted_block)}")
    print("=" * 20)