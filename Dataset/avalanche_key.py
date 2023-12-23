import sys
import os
import secrets
import random

sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc


def encrypt(plaintext, key):
    # Replace this function with the actual encryption function
    return babyr_enc(plaintext, key)


def generate_random_key(block_size=16):
    # Use secrets module for secure random key generation
    return secrets.randbits(block_size)


def avalanche_key_dataset(encryption_func, num_samples=1000, block_size=16):
    dataset = []

    for _ in range(num_samples):
        # Generate a random plaintext
        plaintext = random.randint(0, 2**block_size - 1)

        # Generate two slightly different keys
        original_key = generate_random_key(block_size)
        modified_key = original_key ^ (1 << random.randint(0, block_size - 1))

        # Encrypt with the original key
        original_ciphertext = encrypt(plaintext, original_key)

        # Encrypt with the modified key
        modified_ciphertext = encrypt(plaintext, modified_key)

        # Record the sample in the dataset
        dataset.append({
            'plaintext': plaintext,
            'original_key': original_key,
            'modified_key': modified_key,
            'original_ciphertext': original_ciphertext,
            'modified_ciphertext': modified_ciphertext,
        })

    return dataset

random.seed(42)  # For reproducibility
dataset = avalanche_key_dataset(babyr_enc, num_samples=1000)

# Print the first few samples
for sample in dataset[:5]:
    print(f"Plaintext: {sample['plaintext']}, Original Key: {sample['original_key']}, Modified Key: {sample['modified_key']}, Original Ciphertext: {sample['original_ciphertext']}, Modified Ciphertext: {sample['modified_ciphertext']}")
