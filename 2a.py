def attack_text_plain(plaintext1, ciphertext1, plaintext2, ciphertext2):
   #caucalute the difference in the pairs
    diff_plain = [(ord(plaintext2[i]) - ord(plaintext1[i])) % 26 for i in range(len(plaintext1))]
    diff_cipher = [(ord(ciphertext2[i]) - ord(ciphertext1[i])) % 26 for i in range(len(ciphertext1))]

    #caculate the key be using the difference
    key = [(diff_cipher[i] - diff_plain[i]) % 26 for i in range(len(diff_plain))]

    #return key
    return key


#example for 2 massage recived
plaintext1 = "2C"
ciphertext1 = "2M"


plaintext2 = "1M"
ciphertext2 = "1C"

#find the key
key = attack_text_plain(plaintext1, ciphertext1, plaintext2, ciphertext2)
print("המפתח המצוי:", key)
