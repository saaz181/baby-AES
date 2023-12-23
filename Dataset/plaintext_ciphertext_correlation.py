import sys
import os
import random

sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc


def encrypt(plaintext, key):
    # Replace this function with the actual encryption function
    return babyr_enc(plaintext, key)

def plaintext_ciphertext_correlation_dataset(encryption_func, num_samples=1000, block_size=16):
    dataset = []

    for _ in range(num_samples):
        # Generate a random plaintext
        plaintext = random.randint(0, 2**block_size - 1)

        # Generate a random key
        key = random.randint(0, 2**block_size - 1)

        # Encrypt the plaintext with the key
        ciphertext = encrypt(plaintext, key)

        # Record the sample in the dataset
        dataset.append({
            'plaintext': plaintext,
            'key': key,
            'ciphertext': ciphertext,
        })

    return dataset

# Example usage
random.seed(42)  # For reproducibility
dataset = plaintext_ciphertext_correlation_dataset(babyr_enc, num_samples=1000)

# Print the first few samples
for sample in dataset[:5]:
    print(f"Plaintext: {sample['plaintext']}, Key: {sample['key']}, Ciphertext: {sample['ciphertext']}")
