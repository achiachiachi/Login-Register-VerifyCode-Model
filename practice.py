from werkzeug.security import generate_password_hash, check_password_hash

word =  generate_password_hash('password')
print(word)
var = check_password_hash(word, 'password')
print(var)