import sys
import os
import random
sys.path.append(os.getcwd())

from cipher_algorithm.baby_rijndael import babyr_enc


def convert_list_of_bytes_to_hex(list_of_bytes: list) -> int:
    hex_representation = ''.join([hex(x)[2:].zfill(2) for x in list_of_bytes])

    # Convert the concatenated hexadecimal string to an integer
    return int(hex_representation, 16)



def encrypt(plaintext, key):
    # Replace this function with the actual encryption function
    return babyr_enc(plaintext, key)

def plaintext_avalanche_dataset(encryption_func, num_samples=1000, block_size=16):
    dataset = []

    for _ in range(num_samples):
        # Generate a random plaintext
        plaintext = random.randint(0, 2**block_size - 1)

        # Encrypt the original plaintext
        original_ciphertext = convert_list_of_bytes_to_hex(encrypt(plaintext, random_key()))

        # Generate a slightly modified plaintext (e.g., flip one bit)
        modified_plaintext = plaintext ^ (1 << random.randint(0, block_size - 1))

        # Encrypt the modified plaintext
        modified_ciphertext = convert_list_of_bytes_to_hex(encrypt(modified_plaintext, random_key()))

        # Record the sample in the dataset
        dataset.append({
            'plaintext': plaintext,
            'modified_plaintext': modified_plaintext,
            'original_ciphertext': original_ciphertext,
            'modified_ciphertext': modified_ciphertext,
        })

    return dataset

def random_key():
    # Replace this function with a secure random key generator
    return random.randint(0, 2**16 - 1)


random.seed(42)  # For reproducibility
dataset = plaintext_avalanche_dataset(babyr_enc, num_samples=1000)




# # Print the first few samples
# for sample in dataset[:10]:
#     print(f"Plaintext: {sample['plaintext']}, Modified Plaintext: {sample['modified_plaintext']}, Original Ciphertext: {sample['original_ciphertext']}, Modified Ciphertext: {sample['modified_ciphertext']}")
