import random

# Permutasi awal (Initial Permutation) dan akhir
INITIAL_PERMUTATION = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERMUTATION = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
                     38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                     36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
                     34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# P-Box Permutation untuk fungsi f
P_BOX_PERMUTATION = [16, 7, 20, 21, 29, 12, 28, 17,
                     1, 15, 23, 26, 5, 18, 31, 10,
                     2, 8, 24, 14, 32, 27, 3, 9,
                     19, 13, 30, 6, 22, 11, 4, 25]

# Generate key 64-bit (8 bit parity tidak digunakan)
def generate_key():
    key = random.getrandbits(64)
    return key

# Apply permutasi awal pada blok 64-bit
def initial_permutation(block):
    return ''.join([block[i-1] for i in INITIAL_PERMUTATION])

# Apply permutasi akhir
def final_permutation(block):
    return ''.join([block[i-1] for i in FINAL_PERMUTATION])

# Fungsi sederhana untuk mengonversi integer menjadi bit string
def to_bit_string(value, length):
    return bin(value)[2:].zfill(length)

# XOR dua blok
def xor(block1, block2):
    return ''.join([str(int(a) ^ int(b)) for a, b in zip(block1, block2)])

# Contoh fungsi enkripsi blok 64-bit
def des_encrypt(plaintext, key):
    # Apply initial permutation
    permuted_block = initial_permutation(plaintext)
    # Pisah jadi dua bagian, kiri (L) dan kanan (R)
    L, R = permuted_block[:32], permuted_block[32:]
    for i in range(16):  # Lakukan 16 putaran (sederhanakan untuk contoh)
        new_L = R
        new_R = xor(L, R)  # Fungsi f sederhana (xor saja)
        L, R = new_L, new_R
    # Gabungkan L dan R
    combined = L + R
    # Apply final permutation
    cipher_text = final_permutation(combined)
    return cipher_text

# Contoh dekripsi blok 64-bit (proses yang sama tapi urutan putaran terbalik)
def des_decrypt(ciphertext, key):
    # Apply initial permutation
    permuted_block = initial_permutation(ciphertext)
    L, R = permuted_block[:32], permuted_block[32:]
    for i in range(16):  # Urutan putaran terbalik
        new_R = L
        new_L = xor(R, L)
        L, R = new_L, new_R
    combined = L + R
    plain_text = final_permutation(combined)
    return plain_text

if __name__ == "__main__":
    key = generate_key()  # Hasilkan kunci 64-bit
    plaintext = to_bit_string(0x123456789ABCDEF, 64)  # Contoh data 64-bit
    ciphertext = des_encrypt(plaintext, key)
    decrypted_text = des_decrypt(ciphertext, key)
    
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted_text}")
