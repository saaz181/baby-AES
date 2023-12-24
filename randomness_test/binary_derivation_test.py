import sys
import os
import random
sys.path.append(os.getcwd())


from Dataset.plaintext_avalanche import dataset
from Dataset.avalanche_key import dataset_avalanche_key
from Dataset.plaintext_ciphertext_correlation import dataset_correlation
from Dataset.CBC import cbc_dataset
from Dataset._random_ import random_dataset
from Dataset.high_density_with_plaintext import high_density_plaintext_dataset
from Dataset.high_density_with_key import high_density_key_dataset
from Dataset.low_density_with_plaintext import low_density_dataset
from Dataset.low_density_with_key import low_density_key_dataset
from cipher_algorithm.baby_rijndael import babyr_dec, babyr_enc


def convert_list_of_bytes_to_hex(list_of_bytes: list) -> int:
    hex_representation = ''.join([hex(x)[2:].zfill(2) for x in list_of_bytes])

    # Convert the concatenated hexadecimal string to an integer
    return int(hex_representation, 16)




def binary_derivation_test_avalanche_plaintext(dataset):
    for sample in dataset:
        original_ciphertext = sample['original_ciphertext']
        modified_ciphertext = sample['modified_ciphertext']

        # Check Hamming distance for each bit
        for bit_position in range(16):
            original_bit = (original_ciphertext >> bit_position) & 1
            modified_bit = (modified_ciphertext >> bit_position) & 1

            if original_bit != modified_bit:
                print(f"Avalanche Plaintext Test Failed: Bit position {bit_position}")


def binary_derivation_test_avalanche_key(dataset):
    for sample in dataset:
        original_ciphertext = sample['original_ciphertext']
        modified_ciphertext = sample['modified_ciphertext']

        # Check Hamming distance for each bit
        for bit_position in range(16):
            original_bit = (original_ciphertext >> bit_position) & 1
            modified_bit = (modified_ciphertext >> bit_position) & 1

            if original_bit != modified_bit:
                print(f"Avalanche Key Test Failed: Bit position {bit_position}")


def binary_derivation_test_plaintext_ciphertext_correlation(dataset):
    for sample in dataset:
        plaintext = sample['plaintext']
        ciphertext = sample['ciphertext']

        # Check Hamming distance for each bit
        for bit_position in range(16):
            plaintext_bit = (plaintext >> bit_position) & 1
            ciphertext_bit = (ciphertext >> bit_position) & 1

            if plaintext_bit != ciphertext_bit:
                print(f"Plaintext-Ciphertext Correlation Test Failed: Bit position {bit_position}")


def binary_derivation_test_cbc(dataset):
    print(dataset)
    for ciphertext, key in dataset:
        original_block = convert_list_of_bytes_to_hex(babyr_dec(ciphertext, key))

        # Check Hamming distance for each bit
        for bit_position in range(16):
            original_bit = (original_block >> bit_position) & 1
            modified_ciphertext = ciphertext ^ (1 << bit_position)
            modified_block = convert_list_of_bytes_to_hex(babyr_dec(modified_ciphertext, key))
            modified_bit = (modified_block >> bit_position) & 1

            if original_bit != modified_bit:
                print(f"CBC Mode Test Failed: Bit position {bit_position}")


def binary_derivation_test_low_density_plaintext(dataset):
    for plaintext, key in dataset:
        encrypted_block = convert_list_of_bytes_to_hex(babyr_enc(plaintext, key))

        # Check Hamming distance for each bit
        for bit_position in range(16):
            plaintext_bit = (plaintext >> bit_position) & 1
            encrypted_bit = (encrypted_block >> bit_position) & 1

            if plaintext_bit != encrypted_bit:
                print(f"Low-Density with Plaintext Test Failed: Bit position {bit_position}")


def binary_derivation_test_low_density_key(dataset):
    for plaintext, key in dataset:
        encrypted_block = convert_list_of_bytes_to_hex(babyr_enc(plaintext, key))

        # Check Hamming distance for each bit
        for bit_position in range(16):
            key_bit = (key >> bit_position) & 1
            encrypted_bit = (encrypted_block >> bit_position) & 1

            if key_bit != encrypted_bit:
                print(f"Low-Density with Key Test Failed: Bit position {bit_position}")


def binary_derivation_test_high_density_plaintext(dataset):
    for plaintext, key in dataset:
        encrypted_block = convert_list_of_bytes_to_hex(babyr_enc(plaintext, key))

        # Check Hamming distance for each bit
        for bit_position in range(16):
            plaintext_bit = (plaintext >> bit_position) & 1
            encrypted_bit = (encrypted_block >> bit_position) & 1

            if plaintext_bit != encrypted_bit:
                print(f"High-Density with Plaintext Test Failed: Bit position {bit_position}")


def binary_derivation_test_high_density_key(dataset):
    for plaintext, key in dataset:
        encrypted_block = convert_list_of_bytes_to_hex(babyr_enc(plaintext, key))

        # Check Hamming distance for each bit
        for bit_position in range(16):
            key_bit = (key >> bit_position) & 1
            encrypted_bit = (encrypted_block >> bit_position) & 1

            if key_bit != encrypted_bit:
                print(f"High-Density with Key Test Failed: Bit position {bit_position}")


def binary_derivation_test_random(dataset):
    for block, key in dataset:
        encrypted_block = convert_list_of_bytes_to_hex(babyr_enc(block, key))

        # Check Hamming distance for each bit
        for bit_position in range(16):
            block_bit = (block >> bit_position) & 1
            encrypted_bit = (encrypted_block >> bit_position) & 1

            if block_bit != encrypted_bit:
                print(f"Random Test Failed: Bit position {bit_position}")


# Call binary derivation tests for each dataset
binary_derivation_test_avalanche_plaintext(dataset)
binary_derivation_test_avalanche_key(dataset_avalanche_key)
binary_derivation_test_plaintext_ciphertext_correlation(dataset_correlation)
binary_derivation_test_cbc(cbc_dataset)
binary_derivation_test_low_density_plaintext(low_density_dataset)
binary_derivation_test_low_density_key(low_density_key_dataset)
binary_derivation_test_high_density_plaintext(high_density_plaintext_dataset)
binary_derivation_test_high_density_key(high_density_key_dataset)
binary_derivation_test_random(random_dataset)
