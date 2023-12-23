import random
import sys
import os
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc, print_b


# Function to generate a "Low-Density with plaintext" dataset
def generate_low_density_dataset(size, density=0.2):
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext with low density
        plaintext = 0
        for _ in range(16):
            if random.random() < density:
                plaintext |= 1 << random.randint(0, 15)
        key = random.randint(0, 0xFFFF)  # Generating a random 16-bit key
        dataset.append((plaintext, key))
    return dataset

# Example: Generate a dataset with 10 random pairs of low-density plaintexts and keys
low_density_dataset = generate_low_density_dataset(10, density=0.2)

# Example of how to use your encryption function
for plaintext, key in low_density_dataset:
    encrypted_block = babyr_enc(plaintext, key)
    
    print(f"Original Plaintext: {plaintext}")
    print(f"Encrypted Block: {print_b(encrypted_block)}")
    print("=" * 20)
