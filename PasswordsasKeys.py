from Crypto.Cipher import AES
import hashlib
import requests

# collect the words list from the given github link
keys=requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words").text.split("\n")

# collect ciphertext from ecncrypt_flag route
ciphertext = bytes.fromhex(requests.get(
    "https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/").json()['ciphertext'])


for key in keys:    
    key=hashlib.md5(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)

    if b'crypto' in decrypted:
        print(decrypted.decode())
        break