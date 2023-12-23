
import requests

def decrypt(ciphertext):
	url = "https://aes.cryptohack.org/block_cipher_starter/decrypt/" + ciphertext + "/"
	response = requests.get(url)
	return response.json()['plaintext']

def get_enc_flag():
	url = "https://aes.cryptohack.org/block_cipher_starter/encrypt_flag/"
	response = requests.get(url)
	return response.json()['ciphertext']

enc_flag = get_enc_flag()
print(f"Enc. Flag (hex): {enc_flag}")
dec_flag = decrypt(enc_flag)
print(f"Dec. Flag (hex): {dec_flag}")
print(f"Dec. Flag (bytes): {bytes.fromhex(dec_flag).decode()}")