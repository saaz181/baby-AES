from cipher_algorithm.baby_rijndael import babyr_enc, babyr_dec

def strict_avalanche_test(enc_func):
    block = 0x5b69
    key = 0x87b2

    original_output = enc_func(block, key)

    for i in range(16):
        modified_block = block ^ (1 << i)
        modified_output = enc_func(modified_block, key)

        print(f"Bit {i + 1}: {'Pass' if modified_output != original_output else 'Fail'}")

# Run strict avalanche test on encryption
print("\nStrict Avalanche Test: ")
strict_avalanche_test(babyr_enc)
print("########################\n")


def avalanche_test(enc_func):
    block = 0x5b69
    key = 0x87b2

    original_output = enc_func(block, key)

    for i in range(16):
        modified_block = block ^ (1 << i)
        modified_output = enc_func(modified_block, key)

        print(f"Bits {i + 1}: {'Pass' if modified_output != original_output else 'Fail'}")

# Run avalanche test on encryption
print("\nAvalanche Test: ")
avalanche_test(babyr_enc)
print("########################\n")


def completeness_test(enc_func):
    for i in range(16):
        block = 0x5b69
        key = 0x87b2

        original_output = enc_func(block, key)

        modified_block = block ^ (1 << i)
        modified_output = enc_func(modified_block, key)

        print(f"Bit {i + 1}: {'Pass' if modified_output != original_output else 'Fail'}")

# Run completeness test on encryption
print("\nCompleteness Test: ")
completeness_test(babyr_enc)
print("########################\n")
