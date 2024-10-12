sbox = [
        [10, 6, 4, 15, 13, 2, 11, 8, 5, 14, 0, 3, 9, 12, 1, 7,
        3, 14, 10, 5, 2, 8, 1, 12, 0, 9, 7, 15, 11, 6, 4, 13,
        15, 5, 1, 13, 6, 2, 0, 10, 4, 8, 3, 12, 7, 11, 14, 9,
        2, 11, 12, 4, 5, 3, 8, 15, 1, 10, 0, 9, 14, 13, 6, 7],

        [9, 7, 2, 1, 10, 8, 15, 14, 5, 3, 0, 4, 12, 13, 6, 11,
        0, 5, 3, 9, 15, 2, 1, 6, 10, 11, 4, 12, 13, 8, 7, 14,
        4, 6, 12, 0, 11, 14, 10, 1, 3, 5, 9, 8, 2, 7, 13, 15,
        15, 4, 1, 7, 6, 13, 10, 2, 12, 9, 14, 5, 8, 3, 11, 0],

        [6, 0, 2, 4, 7, 10, 9, 15, 8, 14, 3, 11, 5, 1, 12, 13,
        14, 12, 10, 9, 3, 7, 4, 0, 5, 2, 8, 1, 6, 11, 15, 13,
        7, 1, 5, 6, 2, 12, 4, 10, 15, 14, 13, 0, 8, 3, 9, 11,
        10, 9, 15, 1, 4, 6, 11, 12, 14, 8, 2, 3, 0, 5, 13, 7],

        [8, 15, 1, 4, 3, 10, 12, 9, 0, 6, 5, 11, 7, 2, 14, 13,
        12, 10, 15, 8, 2, 6, 9, 4, 5, 3, 1, 11, 0, 14, 13, 7,
        4, 2, 6, 11, 15, 7, 0, 9, 10, 1, 14, 3, 5, 12, 13, 8,
        11, 1, 9, 5, 10, 4, 12, 0, 8, 7, 3, 6, 2, 14, 15, 13],

        [1, 6, 11, 4, 3, 9, 14, 12, 5, 10, 15, 8, 0, 7, 2, 13,
        15, 3, 12, 6, 11, 0, 8, 9, 1, 10, 2, 14, 5, 4, 7, 13,
        13, 7, 1, 5, 0, 8, 14, 3, 2, 10, 9, 12, 6, 15, 4, 11,
        10, 2, 7, 8, 12, 3, 14, 1, 4, 5, 11, 9, 0, 6, 15, 13],

        [3, 8, 12, 7, 4, 11, 2, 10, 1, 9, 0, 6, 15, 14, 5, 13,
        0, 5, 10, 3, 8, 12, 7, 9, 2, 11, 14, 4, 15, 1, 6, 13,
        2, 3, 14, 6, 4, 8, 1, 0, 7, 12, 11, 10, 9, 13, 5, 15,
        1, 15, 3, 2, 0, 10, 8, 14, 12, 6, 11, 5, 13, 9, 4, 7],

        [5, 9, 15, 12, 11, 0, 3, 8, 14, 7, 1, 10, 4, 6, 2, 13,
        7, 4, 8, 10, 12, 2, 11, 5, 9, 6, 15, 1, 0, 3, 14, 13,
        10, 2, 8, 6, 12, 1, 4, 14, 0, 7, 9, 5, 3, 11, 15, 13,
        9, 15, 11, 0, 2, 8, 3, 4, 14, 1, 7, 6, 5, 10, 13, 12],

        [14, 1, 3, 2, 12, 10, 8, 11, 6, 15, 5, 4, 0, 7, 9, 13,
        10, 6, 3, 11, 12, 8, 1, 0, 4, 7, 9, 5, 15, 2, 13, 14,
        1, 4, 10, 11, 3, 9, 0, 2, 8, 5, 12, 7, 15, 14, 6, 13,
        5, 8, 1, 14, 0, 4, 6, 3, 2, 9, 12, 10, 11, 15, 7, 13],
    ]
pbox = [
            10,  15, 26, 4, 27, 18, 3,  6,
            14,  2, 12, 28, 20, 5, 25, 29,
            8,   11, 21, 0, 9,  17, 19, 13,
            30,  7,  1, 24, 22, 23, 31, 16
        ]
IP =    [       
                57, 49, 41, 33, 25, 17, 9,  1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7,
                56, 48, 40, 32, 24, 16, 8,  0,
                58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6
    ]
FP =    [
                39,  7, 47, 15, 55, 23, 63, 31,
                38,  6, 46, 14, 54, 22, 62, 30,
                37,  5, 45, 13, 53, 21, 61, 29,
                36,  4, 44, 12, 52, 20, 60, 28,
                35,  3, 43, 11, 51, 19, 59, 27,
                34,  2, 42, 10, 50, 18, 58, 26,
                33,  1, 41,  9, 49, 17, 57, 25,
                32,  0, 40,  8, 48, 16, 56, 24
    ]
C =     [
            9,  1, 51, 50, 42, 34, 26,
            56, 48, 40, 32, 24, 41,  8,
            0, 57, 49, 16, 33, 25, 17,
            18, 10,  2, 59, 58, 43, 35
        ]
D =     [
            27, 54, 46, 38, 30, 22, 13,
            20, 36,  4, 62, 19, 11,  3,
            6, 61, 53, 45, 37, 12, 21,
            14,  5, 60, 52, 44, 29, 28
        ]
exponensial_permutation =  [
                31,  0,  1,  2,  3,  4,
                3,  4,  5,  6,  7,  8,
                7,  8,  9, 10, 11, 12,
                11, 12, 13, 14, 15, 16,
                15, 16, 17, 18, 19, 20,
                19, 20, 21, 22, 23, 24,
                23, 24, 25, 26, 27, 28,
                27, 28, 29, 30, 31,  0
            ]
compression_permutation = [
                13, 16, 10, 23,  0,  4,
                2, 27, 14,  5, 20,  9,
                22, 18, 11,  3, 25,  7,
                15,  6, 26, 19, 12,  1,
                40, 51, 30, 36, 46, 54,
                29, 39, 50, 44, 32, 47,
                43, 48, 38, 55, 33, 52,
                45, 41, 49, 35, 28, 31
            ]
binary_to_hex = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3', 
    '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
    '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', 
    '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'
}

hex_to_binary = {v:k for k, v in binary_to_hex.items()}
row_mapping = {'00': 0, '01': 1, '10': 2, '11': 3}
column_mapping = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8, '1001': 9, '1010': 10, '1011': 11, '1100': 12, '1101': 13, '1110': 14, '1111': 15}
to_binary = []
text_bits = []
key = []
keys = []
CD = []
block = []
left_block = []
right_block = []
binary_to_text = {}

def precompute():
    global to_binary, binary_to_text
    for n in range(128):
        b = [0,0,0,0,0,0,0,0]
        for i in range(0, 8):
            if(n%2):
                b[7-i]=1
            n=n//2
        to_binary.append(b)

    k = 0
    binary_to_text = {}
    for i in to_binary:
        string = ''
        for j in i:
            string += str(j)
        binary_to_text[string] = chr(k)
        k += 1
    
    return



def plain_to_binary(plaintext):
    global to_binary
    global text_bits
    for i in plaintext:
        text_bits.extend(to_binary[ord(i)])
    return


def apply_Initial_Permutation():
    global FP, block
    dummy = []
    dummy.extend(block)
    for i in range(0, 64):
        dummy[i] = block[(IP[i])]
    block = []
    block.extend(dummy)
    return


def apply_Final_Permutation():
    global FP, block
    dummy = []
    dummy.extend(block)
    for i in range(0, 64):
        dummy[i] = block[(FP[i])]
    block = []
    block.extend(dummy)
    return


def expansion_permutation():
    global right_block, exponensial_permutation
    dummy = []
    for i in range(48):
        dummy.append(right_block[exponensial_permutation[i]])
    right_block = []
    for i in range(0, 48, 6):
        j = i+6
        right_block.append(dummy[i:j])
    return


def sbox_function():
    global sbox, right_block, to_binary, row_mapping, column_mapping

    for i in range(0, 8):
        row = str(right_block[i][0])+str(right_block[i][-1])
        column = ''
        for j in range(1, 5):
            column = column+str(right_block[i][j])
        a = 16 * row_mapping[row]
        a += column_mapping[column]
        right_block.pop(i)
        right_block.insert(i, to_binary[ord(chr(sbox[i][a]))])
    dummy = []
    for i in right_block:
        dummy.extend(i[4:8])
    right_block = []
    right_block.extend(dummy)
    return


def pbox_function():
    global right_block, pbox
    dummy = []
    dummy.extend(right_block)
    for i in range(32):
        dummy[i] = right_block[pbox[i]]
    right_block = []
    right_block.extend(dummy)
    return
    
def xor_rounds():
    global right_block, left_block, keys
    for j in range(0, 16):
        d9 = []
        d9.extend(right_block)
        expansion_permutation()
        for i in range(0, 8):
            di = i*6
            # xor process
            for k in range(0, 6):
                right_block[i][k] ^= keys[j][di+k]
        sbox_function()
        pbox_function()
        for i in range(0, 32):
            right_block[i] ^= left_block[i]

        left_block = []
        left_block.extend(d9)
    return

def left_shift(times):
    global C, D
    for i in range(times):
        C.append(C.pop(0))
        D.append(D.pop(0))
    return


def key_permutation():
    global CD, compression_permutation, keys
    dummy = []
    for i in range(48):
        dummy.append(CD[compression_permutation[i]])
    keys.append(dummy)
    return


def subkey_generate():
    global CD
    for i in range(28):
        C[i] = key[C[i]]
    for i in range(28):
        D[i] = key[D[i]]
    for i in range(0, 16):
        if(i==0 or i==1 or i==8 or i==15):
            left_shift(1)
        else:
            left_shift(2)
        CD = []
        CD.extend(C)
        CD.extend(D)
        key_permutation()
    return

def apply_pads():
    global text_bits
    no_of_pads = len(text_bits) % 64
    if(no_of_pads):
        for i in range(64-no_of_pads):
            text_bits.append(0)
    return

def encryption(start, end):
    global block, left_block, right_block, text_bits
    block = []
    for i in range(start, end):
        block.append(text_bits[i])
    
    apply_Initial_Permutation()
    
    left_block = []
    right_block = []
    left_block.extend(block[0:32])
    right_block.extend(block[32:64])
    
    xor_rounds()

    block = []
    block.extend(right_block)
    block.extend(left_block)

    apply_Final_Permutation()

    cipher_block = ''
    for i in block:
        cipher_block += str(i)
    return cipher_block

def decryption(start, end):
    global block, left_block, right_block, text_bits
    block = []
    for i in range(start, end):
        block.append(text_bits[i])
    
    apply_Initial_Permutation()
    
    left_block = []
    right_block = []
    left_block.extend(block[0:32])
    right_block.extend(block[32:64])
    
    xor_rounds()

    block = []
    block.extend(right_block)
    block.extend(left_block)

    apply_Final_Permutation()

    plain_block = ''
    for i in block:
        plain_block += str(i)
    return plain_block

def main():
    global text_bits, key, to_binary, binary_to_text, binary_to_hex
    precompute()

    print('1. ENCRYPTION')
    print('2. DECRYPTION')
    choice = int(input())

    print('Masukkan key')
    keytext = str(input())
    for i in keytext:
        key.extend(to_binary[ord(i)])
    subkey_generate()

    if(choice == 1):
        print('Masukkan Teks')
        plaintext = str(input())
        plain_to_binary(plaintext)
        apply_pads()
        
        final_cipher = ''
        for i in range(0, len(text_bits), 64):
            final_cipher += encryption(i, (i+64))
        
        hex_cipher = ''
        i = 0
        while i < len(final_cipher):
            hex_cipher += binary_to_hex[final_cipher[i:i+4]]
            i = i+4
        
        print('Hasil Enkripsi')
        print(hex_cipher)
        
    else:
        print('Masukkan Teks')
        cipher = str(input())
        text_bits = []
        ciphertext = ''
        for i in cipher:
            ciphertext += hex_to_binary[i]        
        for i in ciphertext:
            text_bits.append(int(i))
        apply_pads()
            
        keys.reverse()
        bin_mess = ''
        for i in range(0, len(text_bits), 64):
            bin_mess += decryption(i, (i+64))

        i = 0
        text_mess = ''
        while i < len(bin_mess):
            text_mess += binary_to_text[bin_mess[i:i+8]]
            i = i+8
        
        print('Hasil Dekripsi')
        print(text_mess)
        
    
    return

main()
