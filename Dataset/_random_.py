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