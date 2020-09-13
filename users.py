from flask import Flask
import bcrypt
def register(username, password):
    pwhash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(password)
    print(pwhash)
    print(bcrypt.checkpw("perkeleh".encode('utf-8'), pwhash))
