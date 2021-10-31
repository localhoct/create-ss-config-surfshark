from os.path import exists as file_exists
import socket
import os
import base64
import flag

print(''' 
Url Are beging ip and ss config will created with IP of url

please wait...
''')

PORT = '48597'
CONFIGS_PASSWORD = 'eazhT9GXDtuwZMDVHnF2wk8G'
ENCRYPTION_METHOD = 'aes-256-gcm'

# ------ 
BASE = ENCRYPTION_METHOD + ":" + CONFIGS_PASSWORD
sample_string_bytes = BASE.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
# ------

with open('list-of-url.txt', 'r', encoding="utf-8") as urls:
    if file_exists('SS-Config.txt'):
            os.remove('SS-Config.txt')
    for url in urls:
        Name = url.strip().split('.')[0]
        IP_addres = socket.gethostbyname(url.strip())
        Flag = flag.flag(Name.split('-')[0])
        with open('SS-Config.txt', 'a', encoding="utf-8") as ssconf:
            SS = f"ss://{base64_string}@{IP_addres}:{PORT}#{Name}{Flag}\n"
            ssconf.write(SS)


print('--------')
print('Finisehd')