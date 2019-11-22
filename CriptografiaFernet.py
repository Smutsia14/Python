from cryptography.fernet import Fernet

chave = Fernet.generate_key()
suite_cifrada = Fernet(chave)
texto = input("Digite o texto para ser criptografado: ")
Bitagem = bytes(texto, 'utf-8')
texto_cifrado = suite_cifrada.encrypt(Bitagem)
texto_decifrado = suite_cifrada.decrypt(texto_cifrado)

print(texto_decifrado)
print(texto_cifrado)


