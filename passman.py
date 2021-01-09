import hashlib
import random
import enquiries
import json
import subprocess
import scrypt, os, binascii
import base64
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    encoded_message = password.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_password(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

def load_passwords():
    try:
        with open('passwords.txt') as j:
            pass_dict = json.load(j)
        return pass_dict
    except json.decoder.JSONDecodeError:
        pass_dict = {}
        return pass_dict

def add_password(pass_dict):
    #user = Site.create(site_name="facebook", password="hashed password")
    print("enter a site name")
    new_site = str(input())
    print("enter the password")
    new_pass = str(input())
    hashed_pass = encrypt_password(new_pass)
    pass_dict.update({new_site : hashed_pass.decode('utf-8')})
    return pass_dict


def auth():
    print("enter master password...")
    input_pass = str(input())
    if get_master_password() == input_pass:
        return True

def save_new_passwords(pass_dict):
    with open("passwords.txt", 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(pass_dict))
        f.close()

def get_password(pass_dict):
    #all = Site.query().filter(Site.site_name == "facebook").all()
    #print(all[1].password)
    print("enter a site name")
    site_name = str(input())
    if auth() == True:
        try:
            password = decrypt_password(pass_dict[site_name].encode('utf-8'))
            return password.decode('utf-8')
        except KeyError:
            print("There is no {} site in your passman!".format(site_name))
    else:
        print("unsuccessful auth")

def get_password_menu(pass_dict):
    print("enter a site name")
    options = pass_dict.keys()
    choice = enquiries.choose('Choose one of these options: ', options)
    print("you chose:", choice)
    if auth() == True:
        try:
            password = decrypt_password(pass_dict[choice].encode('utf-8'))
            return password.decode('utf-8')
        except KeyError:
            print("There is no {} site in your passman!".format(site_name))
    else:
        print("unsuccessful auth")

def create_master_password():
    if os.stat('.master_pass').st_size==0:
        print("avaiable")
        master_pass = encrypt_password(str(input()))
        print(master_pass)
        with open('.master_pass', 'wb') as f:
            f.write(master_pass)
            f.close()
    else:
        print("you have already set a master password")

def get_master_password():
    with open('.master_pass', 'r') as f:
        master_pass = f.read().replace('\n', '')
        f.close()
    master_pass = decrypt_password(master_pass.encode('utf-8'))

    return master_pass.decode('utf-8')
