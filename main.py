from active_alchemy import ActiveAlchemy
import config
import hashlib
import random
import enquiries
import json
import os
import subprocess
import passman

#db = ActiveAlchemy("mysql+pymysql://{}:{}@{}:{}/{}".format(config.db_username, config.db_password, config.db_endpoint, config.dc_port, config.db_name))

#class Site(db.Model):
#    site_name = db.Column(db.String(25))
#    password = db.Column(db.String(25))


#db.create_all()
#user = Site.create(site_name="facebook", password="hashed password")
#all = Site.query().filter(Site.site_name == "facebook").all()
#print(all[1].password)

#for site in Site.query():
#    print(site.site_name)
#    print(site.password)
os.system('clear')

while True:
    options = [ 'get a password', 'add a new password', 'get a password with menu', 'settings', 'exit']
    settings_options = ['set the machine_id(requires password)', 'create master password', 'exit']
    choice = enquiries.choose('Choose one of these options: ', options)
    print("you chose:", choice)

    if choice == options[0]:
        print("getting your password...")
        print("your password is: ", passman.get_password())
    elif choice == options[1]:
        print("adding a new password...")
        passman.add_password()
        #passman.save_new_passwords(pass_dict)
    elif choice == options[2]:
        print("getting password...")
        print("your password is: ", passman.get_password_menu(pass_dict))
    elif choice == options[3]:
        print("entering setting menu...")
        settings_choice = enquiries.choose('Choose one of these options: ', settings_options)
        if settings_choice == settings_options[0]:
            print("setting machine_id...")
            #passman.set_machine_id()
        elif settings_choice == settings_options[1]:
            print("creating master password...")
            passman.create_master_password()
            #passman.generate_key()
        elif settings_choice == settings_options[2]:
            print("exiting...")
            quit()
    elif choice == options[4]:
        print("exiting...")
        quit()

    if enquiries.confirm('yes to continue using passman, no to exit'):
        os.system('clear')
    else:
        quit()
