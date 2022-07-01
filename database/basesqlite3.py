from libs.libslist import *
base = sqlite3.connect('data.db')
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS users(name VARCHAR(256),userid VARCHAR(300),follows VARCHAR(30),statususer VARCHAR(500),timejoin VARCHAR(3000))')
base.execute('CREATE TABLE IF NOT EXISTS commudity(name VARCHAR(1000),price VARCHAR(50000),information VARCHAR(50000),discount VARCHAR(500),link VARCHAR(3000),welcomemessage VARCHAR(1000000))')
base.execute('CREATE TABLE IF NOT EXISTS formessage(welcomemessage VARCHAR(1000000))')
base.commit()