from Crypto.Cipher import AES
import sys
print("usage python3 rev-aes-d.py filein fileout")

# define the encryption key and block size (must match the ones used for encryption)
key = b'your_key_here'
block_size = 16

# read the contents of the reversed encrypted file
with open(sys.argv[1], 'rb') as f:
    reversed_encrypted_data = f.read()

# reverse the encrypted data to restore the original order
encrypted_data = reversed_encrypted_data[::-1]

# create a new AES cipher object with the key and mode of operation
cipher = AES.new(key, AES.MODE_ECB)

# decrypt the data using the cipher
decrypted_data = cipher.decrypt(encrypted_data)

# remove the padding from the decrypted data
padding = decrypted_data[-1]
decrypted_data = decrypted_data[:-padding]

# write the decrypted data to a new file
with open(sys.argv[2], 'wb') as f:
    f.write(decrypted_data)
