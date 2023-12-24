import random
import sys
import os
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc, print_b


def generate_high_density_key_dataset(size, key_density=0.8):
    dataset = []
    for _ in range(size):
        plaintext = random.randint(0, 0xFFFF)  # Generating a random 16-bit plaintext
        
        # Generate a random 16-bit key with high density
        key = 0
        for i in range(16):
            if random.random() < key_density:
                key |= 1 << i
        
        dataset.append((plaintext, key))
    return dataset

# Example: Generate a dataset with 10 random pairs of random plaintexts and high-density keys
high_density_key_dataset = generate_high_density_key_dataset(10, key_density=0.8)

# # Example of how to use your encryption function
# for plaintext, key in high_density_key_dataset:
#     encrypted_block = babyr_enc(plaintext, key)
    
#     print(f"Original Plaintext: {plaintext}")
#     print(f"Original Key: {key}")
#     print(f"Encrypted Block: {print_b(encrypted_block)}")
#     print("=" * 20)