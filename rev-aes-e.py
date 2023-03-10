from Crypto.Cipher import AES
import sys

print("usage python3 rev-aes-e.py filein fileout")
# define the encryption key and block size
key = b'your_key_here'
block_size = 16

# read the contents of the original file
with open(sys.argv[1], 'rb') as f:
    data = f.read()

# pad the data to a multiple of the block size
padding = block_size - len(data) % block_size
data += bytes([padding] * padding)

# create a new AES cipher object with the key and mode of operation
cipher = AES.new(key, AES.MODE_ECB)

# encrypt the data using the cipher
encrypted_data = cipher.encrypt(data)

# reverse the encrypted data
reversed_encrypted_data = encrypted_data[::-1]

# write the reversed encrypted data to a new file
with open(sys.argv[2], 'wb') as f:
    f.write(reversed_encrypted_data)
