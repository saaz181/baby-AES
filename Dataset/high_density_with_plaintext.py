import random
import sys
import os
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc, print_b


def generate_high_density_plaintext_dataset(size, plaintext_density=0.8, key_density=0.8):
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext with high density
        plaintext = 0
        for i in range(16):
            if random.random() < plaintext_density:
                plaintext |= 1 << i
        
        # Generate a random 16-bit key with high density
        key = 0
        for i in range(16):
            if random.random() < key_density:
                key |= 1 << i
        
        dataset.append((plaintext, key))
    return dataset

#  Generate a dataset with 10 random pairs of high-density plaintexts and keys
high_density_plaintext_dataset = generate_high_density_plaintext_dataset(10, plaintext_density=0.8, key_density=0.8)
