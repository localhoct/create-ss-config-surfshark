from os.path import exists as file_exists
import socket
import os
import base64
import flag

# -------- {Create ss configs} --------- #

PORT = '48597'
CONFIGS_PASSWORD = 'eazhT9GXDtuwZMDVHnF2wk8G'
ENCRYPTION_METHOD = 'aes-256-gcm'

BASE = ENCRYPTION_METHOD + ":" + CONFIGS_PASSWORD

sample_string_bytes = BASE.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

with open('list-of-url.txt', 'r', encoding="utf-8") as urls:
    if file_exists('SS-Config.txt'):
            os.remove('SS-Config.txt')
    for url in urls:
        Name = url.strip().split('.')[0]
        IP_addres = socket.gethostbyname(url.strip())
        Flag = flag.flag(Name.split('-')[0])
        with open('SS-Config.txt', 'a', encoding="utf-8") as ssconf:
            SS = f"ss://{base64_string}@{IP_addres}:{PORT}#{Flag}%20{Name}\n"
            ssconf.write(SS)

# -------- {Create Base64 for server configs} --------- #

from time import gmtime, strftime

text = open('SS-Config.txt','r')
sample_string_bytes = text.read().encode("utf-8")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("utf-8")
with open('SS','w') as f:
    f.write(base64_string)

# -------- {PUSH to Main Branch} --------- #

os.system(f'git commit -am \"Latest Update: {strftime("%Y-%m-%d %H%M%S %z", gmtime())}\"')
os.system('git push origin main')