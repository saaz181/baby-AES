# baby-Rijndael
**NOTE:** No third-party library needed

To run test the algorithm for avalanche, strict avalanche and completeness test run:
```bash
python test.py
```
or if you are on linux/Mac:
```bash
python3 test.py
```
Next step is to run the **Randomness Tests** which in this project are:
- Autocorrelation Test
- Binary Derivation Test

To run each do as below:
```bash
python randomness_test/autocorrelation_test.py
python randomness_test/binary_derivation_test.py
```
or if you are on Linux/Mac:
```bash
python3 randomness_test/autocorrelation_test.py
python3 randomness_test/binary_derivation_test.py
```
---

## Algorithm (Simplified Version of Rijndael):

### Key Components:

1. **S-box Operations (`S_operation` and `Si_operation`):**
   - `S_operation`: Substitution operation using a fixed S-box. It replaces each nibble (4 bits) with its corresponding value in the S-box.
   - `Si_operation`: Inverse substitution operation using a different fixed S-box.

2. **Signature Hat Operation (`sig_hat_operation`):**
   - A simple operation that swaps the second and fourth elements of a 4-element array.

3. **Matrix Multiplication (`mult_m`):**
   - Performs matrix multiplication of a binary matrix `t` (used for encryption) or `ti` (used for decryption) with a 4-element array `x`.

4. **Bitwise XOR Operation (`XOR_m`):**
   - Performs bitwise XOR operation on two arrays `x` and `y` of the same size.

5. **Key Expansion (`get_key_m`):**
   - Generates round keys for encryption and decryption based on the input key. It uses a combination of S-box operations, XOR operations, and bitwise shifts.

6. **Printing Function (`print_b`):**
   - Converts a 4-element array to its hexadecimal representation.

### Encryption (`babyr_enc`):

The encryption process is organized into rounds (5 rounds in total), where each round consists of the following steps:
   1. **Initial Round:**
      - XOR the state with the round key.
   2. **Intermediate Rounds (1 to 3):**
      - Apply the following operations sequentially:
         - Substitute each nibble using the S-box (`S_operation`).
         - Apply the Signature Hat operation (`sig_hat_operation`).
         - Multiply the state matrix with the fixed matrix `t` using `mult_m`.
         - XOR the result with the round key.
   3. **Final Round:**
      - Apply the inverse substitution operation (`Si_operation`).
      - Apply the Signature Hat operation.
      - XOR the result with the final round key.

### Decryption (`babyr_dec`):

The decryption process is similar to encryption but in reverse order. It also involves multiple rounds, each consisting of substitution, matrix multiplication, XOR, and inverse substitution operations.

### Note:
- The algorithm operates on 16-bit blocks.
- The key expansion process generates round keys for encryption and decryption.
- The S-boxes and matrices used for substitution and multiplication are fixed.
- The algorithm employs bitwise XOR and various logical operations to perform encryption and decryption.

### Additional Comments:
- The choice of S-boxes and matrices significantly influences the security of the algorithm. In real-world scenarios, these elements are carefully designed and optimized.
- The algorithm is a simplified version for educational purposes and may not provide the same level of security as more advanced encryption algorithms like AES.
---

Dataset Generation:

There are 9 dataset:
- Random
- Avalanche Key
- Avalanche Plaintext
- CBC mode
- High-Density with Plaintext
- High-Density with Key
- Low-Density with Plaintext
- Low-Density with Key
- Plaintext-Ciphertext Correlation


### 1. Avalanche Plaintext Dataset

**Purpose:** This dataset is designed to measure the avalanche effect in the encryption algorithm concerning changes in the plaintext.

**Generation Process:**
1. Generate a random 16-bit plaintext.
2. Encrypt the original plaintext with a random key to obtain the original ciphertext.
3. Generate a slightly modified plaintext (e.g., flip one bit).
4. Encrypt the modified plaintext with the same key to obtain the modified ciphertext.
5. Record the sample in the dataset, including the original and modified plaintexts, as well as the original and modified ciphertexts.

---

### 2. Avalanche Key Dataset

**Purpose:** This dataset aims to assess the avalanche effect in the encryption algorithm concerning changes in the encryption key.

**Generation Process:**
1. Generate a random 16-bit plaintext.
2. Generate two slightly different keys.
3. Encrypt the plaintext with the original key to obtain the original ciphertext.
4. Encrypt the plaintext with the modified key to obtain the modified ciphertext.
5. Record the sample in the dataset, including the plaintext, original and modified keys, as well as the original and modified ciphertexts.

---

### 3. Plaintext-Ciphertext Correlation Dataset

**Purpose:** This dataset is intended to explore the correlation between plaintext and ciphertext.

**Generation Process:**
1. Generate a random 16-bit plaintext.
2. Generate a random 16-bit key.
3. Encrypt the plaintext with the key to obtain the ciphertext.
4. Record the sample in the dataset, including the plaintext, key, and ciphertext.

---

### 4. CBC Mode Dataset

**Purpose:** This dataset is created to assess the Cipher Block Chaining (CBC) mode of operation.

**Generation Process:**
1. Generate a random 16-bit plaintext and key.
2. Generate a random 16-bit Initialization Vector (IV).
3. Encrypt the plaintext using CBC mode.
4. Record the sample in the dataset, including the ciphertext and key.

---

### 5. Low-Density with Plaintext Dataset

**Purpose:** This dataset explores the encryption algorithm's behavior with low-density plaintext.

**Generation Process:**
1. Generate a random 16-bit plaintext with low density (few bits set to 1).
2. Generate a random 16-bit key.
3. Encrypt the low-density plaintext with the key.
4. Record the sample in the dataset, including the original plaintext, key, and ciphertext.

---

### 6. Low-Density with Key Dataset

**Purpose:** This dataset investigates the encryption algorithm's behavior with low-density keys.

**Generation Process:**
1. Generate a random 16-bit plaintext.
2. Generate a random 16-bit key with low density (few bits set to 1).
3. Encrypt the plaintext with the low-density key.
4. Record the sample in the dataset, including the plaintext, original key, and ciphertext.

---

### 7. High-Density with Plaintext Dataset

**Purpose:** This dataset examines the encryption algorithm's behavior with high-density plaintext.

**Generation Process:**
1. Generate a random 16-bit plaintext with high density (many bits set to 1).
2. Generate a random 16-bit key.
3. Encrypt the high-density plaintext with the key.
4. Record the sample in the dataset, including the original plaintext, key, and ciphertext.

---

### 8. High-Density with Key Dataset

**Purpose:** This dataset explores the encryption algorithm's behavior with high-density keys.

**Generation Process:**
1. Generate a random 16-bit plaintext.
2. Generate a random 16-bit key with high density (many bits set to 1).
3. Encrypt the plaintext with the high-density key.
4. Record the sample in the dataset, including the plaintext, original key, and ciphertext.

---

### 9. Random Dataset

**Purpose:** This dataset serves as a general test, using completely random plaintexts and keys.

**Generation Process:**
1. Generate a random 16-bit block and a random 16-bit key.
2. Record the sample in the dataset, including the block, key, encrypted block, and decrypted block.

---


## Randomness Tests
- **Binary Derivation Test**
    ### Key Concepts in the Code:

    1. **Bit Position Iteration:**
    - The code iterates over each bit position (from 0 to 15) in the plaintext, key, or ciphertext.
    - For example: `for bit_position in range(16):`

    2. **Bit Extraction:**
    - It extracts individual bits from numbers (plaintext, key, ciphertext) using bit manipulation.
    - Example:
        ```python
        original_bit = (original_ciphertext >> bit_position) & 1
        modified_bit = (modified_ciphertext >> bit_position) & 1
        ```

    3. **Hamming Distance Check:**
    - The Hamming distance between two binary strings of equal length is the number of positions at which the corresponding bits are different.
    - The code compares the bits at the same position in the original and modified values.
    - Example:
        ```python
        if original_bit != modified_bit:
            print(f"Avalanche Plaintext Test Failed: Bit position {bit_position}")
        ```

    4. **Test Categories:**
    - The code performs different tests based on the type of dataset:
        - Avalanche Plaintext Test
        - Avalanche Key Test
        - Plaintext-Ciphertext Correlation Test
        - CBC Mode Test
        - Low-Density with Plaintext Test
        - Low-Density with Key Test
        - High-Density with Plaintext Test
        - High-Density with Key Test
        - Random Test

    ### High-Level Explanation:

    1. **Avalanche Tests:**
    - These tests (Avalanche Plaintext and Avalanche Key) check how changes in the plaintext or key affect the resulting ciphertext. The goal is to observe a significant change in the ciphertext for small changes in the plaintext or key.

    2. **Plaintext-Ciphertext Correlation Test:**
    - This test checks the correlation between the plaintext and ciphertext bits.

    3. **CBC Mode Test:**
    - In CBC mode, it checks how changing individual bits in the ciphertext affects the corresponding bits in the decrypted block.

    4. **Low-Density and High-Density Tests:**
    - These tests involve changing individual bits in either the plaintext or the key and observing the impact on the resulting ciphertext.

    5. **Random Test:**
    - This test involves random changes to the plaintext and key to assess the overall behavior of the encryption algorithm.

- **Auto Correlation test**

    ### Autocorrelation Test:
    In this context, the autocorrelation test aims to evaluate how changing a specific bit in the plaintext, key, or ciphertext affects the corresponding bit in the resulting ciphertext. The test checks whether changing a bit in the input results in a significant change in the corresponding output.

    ### Explanation of the Code:

    1. **Bit Position Iteration:**
    - The code iterates over each bit position (from 0 to 15) in the plaintext, key, or ciphertext.
    - Example:
        ```python
        for bit_position in range(16):
        ```

    2. **Bit Extraction:**
    - It extracts individual bits from numbers (plaintext, key, ciphertext) using bit manipulation.
    - Example:
        ```python
        original_bit = (original_ciphertext >> bit_position) & 1
        modified_bit = (modified_ciphertext >> bit_position) & 1
        ```

    3. **Autocorrelation Check:**
    - The code checks whether the original bit and the corresponding modified bit are equal. If they are equal, the autocorrelation test fails.
    - Example:
        ```python
        if original_bit == modified_bit:
            print(f"Avalanche Plaintext Autocorrelation Test Failed: Bit position {bit_position}")
        ```

    4. **Test Categories:**
    - Similar to the binary derivation tests, the autocorrelation tests are categorized based on the type of dataset:
        - Avalanche Plaintext Autocorrelation Test
        - Avalanche Key Autocorrelation Test
        - Plaintext-Ciphertext Correlation Autocorrelation Test
        - CBC Mode Autocorrelation Test
        - Low-Density with Plaintext Autocorrelation Test
        - Low-Density with Key Autocorrelation Test
        - High-Density with Plaintext Autocorrelation Test
        - High-Density with Key Autocorrelation Test
        - Random Autocorrelation Test

    ### Note:
    - The specific behavior of the `babyr_enc` and `babyr_dec` functions is essential in understanding how changing individual bits affects the autocorrelation in the resulting ciphertext.
    - The tests aim to identify any unexpected or undesired behavior in the encryption algorithm, especially concerning autocorrelation properties.