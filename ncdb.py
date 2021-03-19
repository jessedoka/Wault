from werkzeug.security import generate_password_hash
from main.vault import Metavault as MV


net = MV('TESTDB', 'data.json')
connection = net.connnection()
if connection:
    print('Created')

def save_user(username:  str, email: str, password: str):
    password_hash = generate_password_hash(password)
    net.insert_object({
        '_id': username,
        'email': email,
        'password': password_hash
    })

if __name__ == '__main__':
    save_user('jesse', 'non@gmail.com', 'Droiw142')
    save_user('jack', 'two@gmail.com', 'Jaxlol123')
