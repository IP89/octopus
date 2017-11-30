import hashlib, uuid
import base64


salt = 'd8b189241f8940f4ad17b4625359bf8d'

def generate_id(word):
    #salt = uuid.uuid4().hex
    return hashlib.sha512(word + salt).hexdigest()

def encrypt_word(word):
    return base64.b64encode(bytes(word))

def decrypt_word(word):
    return base64.b64decode(word)
