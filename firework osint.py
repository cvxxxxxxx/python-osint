
import sys, os, time, socket, ssl, re, hashlib, ipaddress
import urllib.parse, subprocess, random, itertools
from datetime import datetime, timezone

for _pkg in ["colorama","requests","dnspython","python-whois"]:
    try: __import__(_pkg.replace("-","_"))
    except ImportError:
        subprocess.check_call([sys.executable,"-m","pip","install",_pkg,"-q"])

import requests, dns.resolver, whois
from colorama import init, Fore, Back, Style
init(autoreset=True)

GBR = Fore.GREEN  + Style.BRIGHT
YBR = Fore.YELLOW + Style.BRIGHT
RBR = Fore.RED    + Style.BRIGHT
CBR = Fore.CYAN
WBR = Fore.WHITE  + Style.BRIGHT
MBR = Fore.WHITE  + Style.BRIGHT
BBR = Fore.WHITE  + Style.BRIGHT
DIM = Style.DIM   + Fore.WHITE
RS  = Style.RESET_ALL

W   = 72

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

_MATRIX = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロ0123456789ABCDEF"
_GC     = list("!@#$%^&*<>?/|\\[]{}~`")
_HW     = ["0xDEAD","0xBEEF","0xCAFE","0xBABE","0xF00D","0xC0DE","0x1337","0xACE5"]

_G = GBR   # single accent colour used everywhere

def _grad(text, _pal=None):
    return _G + text + RS

def grad_line(text):   return _G + text + RS
def grad_fire(text):   return _G + text + RS
def grad_matrix(text): return DIM + text + RS
def grad_neon(text):   return CBR + text + RS
def grad_sunset(text): return _G + text + RS

def clear(): os.system("cls" if os.name=="nt" else "clear")

def matrix_rain(duration=2.0, width=78): time.sleep(0.1)


def static_burst(rows=4, delay=0.032): pass


def binary_rain(rows=2, width=70): pass


def hex_scroll(rows=4): pass


def ssh_sim(): pass


def glitch(text, iters=8, color=None):
    color=color or GBR
    sys.stdout.write(f"  {color}{text}{RS}\n"); sys.stdout.flush()

def typewrite(text, delay=0.020, color=None):
    color=color or GBR
    for ch in text:
        sys.stdout.write(color+ch); sys.stdout.flush()
        time.sleep(delay)
    print(RS)

def spin(msg, secs=1.6, style="bar"):
    pools={
        "bar":  ["[>      ]","[=>     ]","[==>    ]","[===>   ]","[====>  ]","[=====> ]","[======>]","[ ======]","[  =====]","[   ====]","[    ===]","[     ==]","[      =]","[       ]"],
        "hex":  _HW*2,
        "scan": [".   ",".   ","..  ","..  ","... ","... ","....","   .","  ..","  .."," ...","...."],
        "brute":["BRUTE [#      ]","BRUTE [##     ]","BRUTE [###    ]","BRUTE [####   ]","BRUTE [#####  ]","BRUTE [###### ]","BRUTE [#######]"],
        "crack":["CRACK...","CRACK....","CRACK.....","MATCH?  ","MATCH!  "],
        "ping": ["PING .   ","PING ..  ","PING ... ","PING ...."],
        "pulse":[">>>---","-->>>-","--->>>",">>>>--","->>>>-","-->>>>"],
        "cyber":list("/-\\|"),
    }
    frames=pools.get(style,pools["bar"])
    end=time.time()+secs; i=0
    while time.time()<end:
        col=GBR
        sys.stdout.write(f"\r  {col}{frames[i%len(frames)]}{RS} {DIM}{msg}...{RS}   ")
        sys.stdout.flush(); time.sleep(0.09); i+=1
    sys.stdout.write(f"\r  {GBR}[ OK ]{RS} {WBR}{msg}{RS}               \n")
    sys.stdout.flush()

def pbar(label, n=36):
    sys.stdout.write(f"\n  {DIM}[ {label} ]{RS}\n  {GBR}[{RS}")
    sys.stdout.flush()
    for i in range(n):
        sys.stdout.write(GBR+"="+RS)
        sys.stdout.flush(); time.sleep(0.018)
    sys.stdout.write(f"{GBR}]{RS} {GBR}100%{RS}\n\n"); sys.stdout.flush()

def _fw(col, cx=26, label=""):
    FH=12; FW=52
    cx=max(8,min(cx,FW-10))
    def render(px):
        for row in range(FH):
            line=""
            for c in range(FW):
                a,ch=px.get((row,c),(None,None))
                line+=(a+ch+RS) if a else " "
            sys.stdout.write("  "+line+"\n")
        sys.stdout.flush()
    def up(): sys.stdout.write(f"\033[{FH}A"); sys.stdout.flush()
    def put(px,r,c,a,ch):
        if 0<=r<FH and 0<=c<FW: px[(r,c)]=(a,ch)
    for _ in range(FH): sys.stdout.write("\n")
    sys.stdout.flush()
    trail={}
    for ry in range(FH-1,1,-1):
        px={}
        for ty,tch in trail.items(): put(px,ty,cx,Style.DIM+Fore.GREEN,tch)
        put(px,ry,cx,WBR,"^"); put(px,ry+1,cx,YBR,"|")
        trail[ry]=random.choice([".","`","'",","])
        up(); render(px); time.sleep(0.050)
    br=2
    for fc,fch in [(WBR,"*"),(col,"X"),(WBR,"*")]:
        px={}; put(px,br,cx,fc,fch); up(); render(px); time.sleep(0.048)
    gc=itertools.cycle(_GRAD_FULL)
    rings=[
        [(0,0,"o",WBR)],
        [(-1,0,"|",col),(1,0,"|",col),(0,-2,"-",col),(0,2,"-",col)],
        [(-1,0,"|",col),(1,0,"|",col),(0,-4,"-",col),(0,4,"-",col),
         (-1,-2,"\\",col),(-1,2,"/",col),(1,-2,"/",col),(1,2,"\\",col)],
        [(-2,0,"*",col),(2,0,"*",col),(0,-6,"*",col),(0,6,"*",col),
         (-1,-4,".",col),(-1,4,".",col),(1,-4,".",col),(1,4,".",col),
         (-2,-2,".",YBR),(-2,2,".",YBR),(2,-2,".",YBR),(2,2,".",YBR)],
        [(-3,0,".",col),(3,0,".",col),(0,-8,".",col),(0,8,".",col),
         (-2,-4,".",col),(-2,4,".",col),(2,-4,".",col),(2,4,".",col),
         (-1,-6,".",YBR),(-1,6,".",YBR),(1,-6,".",YBR),(1,6,".",YBR),
         (-3,-2,".",YBR),(-3,2,".",YBR),(3,-2,".",YBR),(3,2,".",YBR)],
        [(-4,0,".",Style.DIM+Fore.GREEN),(4,0,".",Style.DIM+Fore.GREEN),
         (0,-9,".",Style.DIM+Fore.GREEN),(0,9,".",Style.DIM+Fore.GREEN),
         (-3,-4,"`",Style.DIM+Fore.GREEN),(3,-4,"`",Style.DIM+Fore.GREEN),
         (-3,4,"`",Style.DIM+Fore.GREEN),(3,4,"`",Style.DIM+Fore.GREEN)],
        [(-4,-2,"`",DIM),(4,2,"`",DIM),(-2,-8,"`",DIM),(2,8,"`",DIM),(4,-2,"`",DIM),(-4,2,"`",DIM)],
    ]
    for frame in rings:
        px={}
        if label:
            lp=max(0,(FW-len(label))//2)
            for i,ch in enumerate(label): put(px,FH-1,lp+i,Style.DIM+Fore.GREEN,ch)
        rc=next(gc)
        for dr,dc,ch,a in frame: put(px,br+dr,cx+dc,rc if random.random()<0.3 else a,ch)
        up(); render(px); time.sleep(0.088)
    up()
    for _ in range(FH): sys.stdout.write("  "+" "*FW+"\n")
    sys.stdout.flush()

def fw(count=1):
    positions=[16,24,32,20,28]
    colors=[GBR,YBR,CBR,RBR,MBR]
    for i in random.sample(range(len(positions)),min(count,len(positions))):
        _fw(colors[i],cx=positions[i])
    print()

def multi_fw(n=3):
    labels=["","","WE ARE FSOCIETY"]
    cols=[GBR,YBR,CBR,RBR,MBR]
    for k in range(n):
        _fw(cols[k%5],cx=random.randint(10,38),label=labels[k] if k<len(labels) else "")

_FS_LOGO=[
    "",
    "  ╔══════════════════════════════════════════════════════════╗",
    "  ║   CVX WORK  --  OSINT Framework v6.0                    ║",
    "  ║   github.com/cvxxxxxxx                                   ║",
    "  ╚══════════════════════════════════════════════════════════╝",
]

def boot():
    clear()
    print()
    for msg in [
        "  [*] CVX Work OSINT v6.0",
        "  [*] Loading modules...",
        "  [+] 37 modules ready",
        "  [!] Authorized use only",
    ]:
        col = GBR if "[+]" in msg else YBR if "[!]" in msg else DIM
        typewrite(msg, delay=0.018, color=col)
        time.sleep(0.06)
    time.sleep(0.3)

def hacking_status(): pass

def card(title, rows, color=None):
    color=color or GBR
    iw=W
    valid=[(l,v) for l,v in rows if v is not None]
    max_l=max((len(l) for l,_ in valid),default=8)
    val_w=iw-max_l-5
    _copy_buf.clear()
    _copy_buf.append(f"\n{'='*iw}")
    _copy_buf.append(f"  {title}")
    _copy_buf.append(f"{'='*iw}")
    print()
    print(f"  {GBR}+{'─'*iw}+{RS}")
    tpad=(iw-len(title)-2)//2
    print(f"  {color}|{' '*tpad} {grad_neon(title)} {color}{' '*(iw-tpad-len(title)-2)}|{RS}")
    print(f"  {color}+{'='*iw}+{RS}")
    for label,value in rows:
        if value is None:
            print(f"  {color}+{'-'*iw}+{RS}")
            _copy_buf.append(f"  {'-'*40}")
            continue
        lc=_lc(label,color)
        val_str=str(value)
        chunks=[val_str[i:i+val_w] for i in range(0,max(1,len(val_str)),val_w)]
        for j,chunk in enumerate(chunks):
            if j==0:
                lbl=f"{lc}{label:<{max_l}}{RS}"
                print(f"  {color}|{RS}  {lbl}  {chunk}{color}{' '*(iw-max_l-len(chunk)-4)}|{RS}")
                _copy_buf.append(f"  {label:<{max_l}}  {chunk}")
            else:
                pad=" "*(max_l+4)
                print(f"  {color}|{RS}{pad}{DIM}{chunk}{color}{' '*(iw-max_l-len(chunk)-4)}|{RS}")
                _copy_buf.append(f"  {' '*(max_l+2)}{chunk}")
    print(f"  {color}+{grad_line('-'*iw)}+{RS}")
    _copy_buf.append(f"{'='*iw}\n")

_copy_buf=[]

def show_copy():
    if not _copy_buf: return
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"cvxwork_result_{ts}.txt"
    plain_lines = []
    for line in _copy_buf:
        plain_lines.append(line)
    try:
        with open(fname, "w", encoding="utf-8") as fh:
            fh.write("CVX WORK OSINT RESULT\n")
            fh.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            fh.write("="*72 + "\n\n")
            fh.write("\n".join(plain_lines))
        print(f"\n  {GBR}[SAVED]{RS} {WBR}Result saved to: {CBR}{fname}{RS}")
    except Exception as e:
        print(f"\n  {YBR}[!]{RS} {DIM}Could not save to file: {e}{RS}")
    print(f"\n  {grad_neon('─'*W)}")
    print(f"  {GBR}PLAIN-TEXT OUTPUT  (copy from below):{RS}")
    print(f"  {grad_neon('─'*W)}\n")
    for line in _copy_buf:
        print(f"  {WBR}{line}{RS}")
    print(f"\n  {grad_neon('─'*W)}")

def _lc(label,fallback):
    ul=label.upper()
    if any(k in ul for k in ("RISK","VULN","CVE","THREAT","WARN","PROXY","VPN","EXPOSED","CRITICAL","HIGH")): return RBR
    if any(k in ul for k in ("FLAG","MOBILE","HOSTING","NSFW","SCORE")): return YBR
    if any(k in ul for k in ("FOUND","VALID","CLEAN","OK","STATUS")): return GBR
    if any(k in ul for k in ("IP","ASN","HOST","DOMAIN","PORT","DNS","CERT")): return CBR
    if any(k in ul for k in ("USER","EMAIL","PHONE","NAME","DISCORD","SERVER","BADGE")): return MBR
    return fallback

def dhr(): print(f"  {GBR}{'═'*W}{RS}")
def hr():  print(f"  {DIM}{'─'*W}{RS}")

def section(title):
    fill="─"*max(0,W-8-len(title))
    print(f"\n  {GBR}┌─[ {WBR}{title} {GBR}]{fill}─┐{RS}")

def box(title):
    print()
    p=(W-len(title)-2)//2
    print("  "+grad_fire("╔"+"═"*W+"╗"))
    print(f"  {GBR}║{' '*p} {WBR}{title}{GBR}{' '*(W-p-len(title)-2)}║{RS}")
    print("  "+grad_fire("╚"+"═"*W+"╝"))

def ok(m):  print(f"  {GBR}[+]{RS} {WBR}{m}{RS}")
def warn(m):print(f"  {YBR}[!]{RS} {WBR}{m}{RS}")
def err(m): print(f"  {RBR}[-]{RS} {WBR}{m}{RS}")
def inf(m): print(f"  {CBR}[*]{RS} {DIM}{m}{RS}")

def ask(label):
    return input(f"\n  {GBR}[cvxwork]{RS}{DIM}[{label}]{GBR}>{RS} ").strip()

def wait():
    show_copy(); _copy_buf.clear()
    fw(1)
    input(f"  {DIM}[ press ENTER to continue ]{RS}")

_BANNER_RAW = [
    r"   ██████╗██╗   ██╗██╗  ██╗    ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗",
    r"  ██╔════╝██║   ██║╚██╗██╔╝    ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝",
    r"  ██║     ██║   ██║ ╚███╔╝     ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ",
    r"  ██║     ╚██╗ ██╔╝ ██╔██╗     ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ",
    r"  ╚██████╗ ╚████╔╝ ██╔╝ ██╗    ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗",
    r"   ╚═════╝  ╚═══╝  ╚═╝  ╚═╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝",
]

def banner():
    clear()
    for line in _BANNER_RAW:
        print(f"  {GBR}{line}{RS}")
        time.sleep(0.025)
    print()
    print(f"  {GBR}CVX WORK  --  OSINT Framework v6.0{RS}")
    print(f"  {DIM}{'─' * W}{RS}")
    print(f"  {DIM}No API keys required  |  Free public endpoints  |  github.com/cvxxxxxxx{RS}")
    print(f"  {RBR}[!]{RS} {DIM}Authorized use only. Misuse is a criminal offense.{RS}")
    print(f"  {DIM}{'─' * W}{RS}")
    print(f"  {DIM}Session: {RS}{GBR}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RS}  {GBR}[ONLINE]{RS}  {DIM}37 modules{RS}")
    print()

MENU=[
    ("NETWORK INTELLIGENCE",[
        ("01","IP Deep Recon",           "ip-api + ipinfo + hackertarget"),
        ("02","IP Threat Intel",         "Shodan InternetDB + abuse links"),
        ("03","WHOIS + RDAP",            "Full registration + RDAP enrichment"),
        ("04","DNS Full Recon",          "All types + AXFR zone transfer"),
        ("05","Subdomain Enumerator",    "DNS brute-force + crt.sh CT logs"),
        ("06","Port & Service Scanner",  "TCP connect sweep + banner grab"),
        ("07","BGP / ASN Recon",         "bgpview.io -- owner, prefixes, peers"),
        ("08","Reverse IP Lookup",       "hackertarget -- domains on same IP"),
    ]),
    ("HOST & WEB INTEL",[
        ("09","Website Fingerprint",     "Stack, WAF, headers, SSL"),
        ("10","SSL / TLS Audit",         "Chain, expiry, ciphers, SANs"),
        ("11","HTTP Header Probe",       "All headers, CORS, cookies"),
        ("12","URL Redirect Chaser",     "Full chain + final domain analysis"),
        ("13","Google Dork Builder",     "20 templates -- opens in browser"),
        ("14","Tech Stack Detector",     "CMS, framework, CDN, exposed files"),
    ]),
    ("IDENTITY & SOCIAL",[
        ("15","Username OSINT",          "Check 42 platforms simultaneously"),
        ("16","Email Investigator",      "MX, Gravatar, Hunter.io, breach links"),
        ("17","GitHub Recon",            "Profile, repos, orgs, starred"),
        ("18","Phone Recon",             "Country, carrier hints, lookup links"),
    ]),
    ("DISCORD INTELLIGENCE",[
        ("19","Snowflake Decoder",       "Any Discord ID -> exact timestamp"),
        ("20","Invite Probe",            "Server info, members, features"),
        ("21","User Lookup",             "Avatar, badges, age -- no key"),
        ("22","Server Hunt",             "Find public servers by keyword"),
        ("26","Server ID Lookup",        "Widget API + snowflake analysis"),
        ("27","Webhook Probe",           "Channel/server name from webhook URL"),
        ("28","Message Link Decoder",    "All snowflakes from message link"),
        ("29","Bot Lookup",              "Bot profile, top.gg data"),
        ("30","Vanity URL Resolver",     "Full server intel from custom URL"),
        ("31","Discord Status Check",    "Live Discord outage monitor"),
    ]),
    ("TRACKING & INVESTIGATION",[
        ("32","Wayback Machine",         "Archive snapshots + CDX history"),
        ("33","URLScan.io Analysis",     "Public scans, IPs, tech"),
        ("34","Email Header Analyzer",   "Hop extraction, geo, SPF/DKIM"),
        ("35","OSINT Aggregator",        "30+ tool links auto-tailored to target"),
        ("36","Domain History",          "WHOIS age, passive DNS, history links"),
        ("37","Breach Aggregator",       "LeakCheck API + 10 breach databases"),
    ]),
    ("THREAT & VULN RESEARCH",[
        ("23","CVE Search",              "NVD NIST live database"),
        ("24","Hash Identifier",         "Type detect + wordlist crack"),
        ("25","MAC Vendor Lookup",       "OUI to manufacturer"),
    ]),
]

def show_menu():
    print(f"  {GBR}┌{'─'*W}┐{RS}")
    t="CVX WORK  --  SELECT MODULE"
    p=(W-len(t)-2)//2
    print(f"  {GBR}│{' '*p} {GBR}{t}{' '*(W-p-len(t)-2)}│{RS}")
    print(f"  {GBR}├{'─'*W}┤{RS}")
    for cat,entries in MENU:
        catline=f"  -- {cat} --"
        print(f"  {GBR}│{RS} {DIM}{catline:<{W-2}}{GBR}│{RS}")
        print(f"  {GBR}│{RS}{DIM}{'─'*W}{RS}{GBR}│{RS}")
        for num,name,desc in entries:
            pad_r=max(0,W-2-4-1-len(name)-2-len(desc[:38])-2)
            print(f"  {GBR}│{RS}  {CBR}[{num}]{RS} {GBR}{name:<26}{RS}  {DIM}{desc[:38]}{RS}{' '*pad_r}{GBR}│{RS}")
        print(f"  {GBR}│{RS}{' '*W}{GBR}│{RS}")
    print(f"  {GBR}├{'─'*W}┤{RS}")
    print(f"  {GBR}│{RS}  {RBR}[00]{RS} {RBR}EXIT{RS}  {DIM}Terminate session{RS}{' '*(W-26)}{GBR}│{RS}")
    print(f"  {GBR}└{'─'*W}┘{RS}")

def m_ip():
    box("01  IP DEEP RECON")
    target=ask("Enter IP or domain")
    if not target: return
    try:
        ip=socket.gethostbyname(target)
        if ip!=target: inf(f"Resolved {target} -> {ip}")
    except: ip=target
    spin("Querying ip-api.com",1.4,"hex")
    try:
        r=requests.get(f"http://ip-api.com/json/{ip}?fields=66846719",timeout=8)
        d=r.json()
    except Exception as e: err(f"ip-api failed: {e}"); return
    spin("Querying ipinfo.io",1.0,"bar")
    ipinfo={}
    try:
        ri=requests.get(f"https://ipinfo.io/{ip}/json",timeout=6,headers=HEADERS)
        ipinfo=ri.json()
    except: pass
    pbar("IP-RECON",32)
    lat,lon=d.get("lat",""),d.get("lon","")
    rows=[
        ("IP ADDRESS",   d.get("query","--")),
        ("HOSTNAME",     d.get("reverse","--") or ipinfo.get("hostname","--")),
        ("ISP",          d.get("isp","--")),
        ("ORGANIZATION", d.get("org","--")),
        ("AS NUMBER",    d.get("as","--")),
        ("ASN NAME",     d.get("asname","--")),
        ("---",None),
        ("COUNTRY",      f"{d.get('country','--')} ({d.get('countryCode','--')})"),
        ("REGION",       d.get("regionName","--")),
        ("CITY",         d.get("city","--")),
        ("ZIP",          d.get("zip","--")),
        ("LATITUDE",     str(lat)),
        ("LONGITUDE",    str(lon)),
        ("TIMEZONE",     d.get("timezone","--")),
        ("---",None),
        ("MOBILE",       "YES -- MOBILE" if d.get("mobile") else "No"),
        ("PROXY/VPN",    "YES -- FLAGGED" if d.get("proxy") else "No"),
        ("HOSTING/DC",   "YES -- DATACENTER" if d.get("hosting") else "No"),
    ]
    if ipinfo.get("org"): rows.append(("IPINFO ORG", ipinfo["org"]))
    if ipinfo.get("abuse"):
        rows.append(("ABUSE EMAIL", ipinfo["abuse"].get("email","--")))
    if lat and lon:
        rows+=[
            ("---",None),
            ("OPENSTREETMAP",f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=13"),
            ("GOOGLE MAPS",  f"https://maps.google.com/?q={lat},{lon}"),
            ("ZOOM EARTH",   f"https://zoom.earth/#view={lat},{lon},12z"),
        ]
    spin("ipinfo.io enrichment",0.8,"scan")
    try:
        ri2=requests.get(f"https://ipinfo.io/{ip}/json",timeout=5,headers=HEADERS)
        id2=ri2.json()
        if id2.get("org"): rows.append(("IPINFO ORG", id2.get("org","--")))
        if id2.get("hostname"): rows.append(("IPINFO HOST", id2.get("hostname","--")))
        if id2.get("abuse",{}).get("email"): rows.append(("ABUSE EMAIL", id2["abuse"]["email"]))
    except: pass
    spin("HackerTarget host search",0.8,"ping")
    try:
        ht=requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}",timeout=8)
        if ht.status_code==200 and "error" not in ht.text.lower():
            co_hosts=[l.strip() for l in ht.text.strip().split("\n") if l.strip()]
            rows.append(("---",None))
            rows.append(("CO-HOSTED DOMAINS",f"{len(co_hosts)} domains share this IP"))
            for h in co_hosts[:4]: rows.append(("CO-HOST",h))
    except: pass
    card("IP INTELLIGENCE REPORT",rows,CBR)
    wait()

def m_threat():
    box("02  IP THREAT INTEL")
    ip=ask("Enter IP address")
    if not ip: return
    try: ipaddress.ip_address(ip)
    except: err("Not a valid IP"); return
    pbar("THREAT-SCAN",28)
    spin("Shodan InternetDB",1.4,"scan")
    try:
        sh=requests.get(f"https://internetdb.shodan.io/{ip}",timeout=8)
        if sh.status_code==200:
            sd=sh.json()
            ports=sd.get("ports",[]); vulns=sd.get("vulns",[])
            cpes=sd.get("cpes",[]); tags=sd.get("tags",[])
            hosts=sd.get("hostnames",[])
            rows=[
                ("OPEN PORTS",  ", ".join(str(p) for p in ports) or "--"),
                ("HOSTNAMES",   ", ".join(hosts[:6]) or "--"),
                ("CPEs",        ", ".join(cpes[:4]) or "--"),
                ("SHODAN TAGS", ", ".join(tags) or "--"),
                ("KNOWN CVEs",  str(len(vulns))+(" -- SEE BELOW" if vulns else " -- none")),
            ]
            if vulns:
                rows.append(("---",None))
                for v in vulns[:8]: rows.append(("VULN",v))
            card("SHODAN INTERNETDB",rows,RBR)
            if vulns: warn(f"{len(vulns)} known vulnerabilities!")
            else: ok("No known CVEs in Shodan InternetDB")
        elif sh.status_code==404: inf("Not indexed in Shodan InternetDB")
    except Exception as e: warn(f"Shodan error: {e}")
    links=[
        ("ABUSEIPDB",   f"https://www.abuseipdb.com/check/{ip}"),
        ("VIRUSTOTAL",  f"https://www.virustotal.com/gui/ip-address/{ip}"),
        ("SHODAN FULL", f"https://www.shodan.io/host/{ip}"),
        ("GREYNOISE",   f"https://viz.greynoise.io/ip/{ip}"),
        ("IPVOID",      f"https://www.ipvoid.com/ip-blacklist-check/?ip={ip}"),
        ("TALOS",       f"https://talosintelligence.com/reputation_center/lookup?search={ip}"),
        ("THREATFOX",   f"https://threatfox.abuse.ch/browse.php?search=ioc:{ip}"),
        ("CENSYS",      f"https://search.censys.io/hosts/{ip}"),
    ]
    card("MANUAL THREAT LOOKUP LINKS",links,YBR)
    wait()

def m_whois():
    box("03  WHOIS + RDAP LOOKUP")
    target=ask("Enter domain or IP")
    if not target: return
    spin("WHOIS query",2.0,"scan")
    try: w=whois.whois(target)
    except Exception as e: err(f"WHOIS failed: {e}"); wait(); return
    def fv(v):
        if v is None: return "--"
        return ", ".join(str(x) for x in v)[:72] if isinstance(v,list) else str(v)[:72]
    rows=[
        ("DOMAIN",      fv(w.domain_name)),
        ("REGISTRAR",   fv(w.registrar)),
        ("WHOIS SERVER",fv(w.whois_server)),
        ("---",None),
        ("CREATED",     fv(w.creation_date)),
        ("UPDATED",     fv(w.updated_date)),
        ("EXPIRES",     fv(w.expiration_date)),
        ("STATUS",      fv(w.status)),
        ("DNSSEC",      fv(w.dnssec)),
        ("---",None),
        ("NAME SERVERS",fv(w.name_servers)),
        ("ORG",         fv(w.org)),
        ("COUNTRY",     fv(w.country)),
        ("EMAILS",      fv(w.emails)),
    ]
    card("WHOIS DATA",rows,CBR)
    spin("RDAP query",1.2,"bar")
    try:
        rr=requests.get(f"https://rdap.org/domain/{target}",timeout=8,headers=HEADERS)
        if rr.status_code==200:
            rd=rr.json()
            rrows=[("STATUS",", ".join(rd.get("status",[])))]
            for ev in rd.get("events",[]):
                rrows.append((ev.get("eventAction","event").upper(),ev.get("eventDate","--")[:19]))
            card("RDAP ENRICHMENT",rrows,GBR)
    except: inf("RDAP not available for this domain")
    wait()

def m_dns():
    box("04  DNS FULL RECON")
    domain=ask("Enter domain")
    if not domain: return
    pbar("DNS-SWEEP",28)
    rows=[]
    for rtype in ["A","AAAA","MX","NS","TXT","CNAME","SOA","SRV","CAA","DNSKEY","DS"]:
        try:
            ans=dns.resolver.resolve(domain,rtype,lifetime=4)
            for a in ans: rows.append((rtype,str(a)))
        except dns.resolver.NoAnswer: rows.append((rtype,"no record"))
        except dns.resolver.NXDOMAIN: err("NXDOMAIN"); wait(); return
        except: rows.append((rtype,"timeout"))
    card(f"DNS RECORDS  {domain}",rows,CBR)
    spin("AXFR zone transfer attempt",1.2,"scan")
    try:
        ns_ans=dns.resolver.resolve(domain,"NS",lifetime=4)
        for ns in ns_ans:
            try:
                zone=dns.zone.from_xfr(dns.query.xfr(str(ns).rstrip("."),domain,timeout=3))
                warn(f"ZONE TRANSFER OPEN on {ns} -- MISCONFIGURATION")
                for n in zone.nodes: inf(f"  {n}.{domain}")
                break
            except: pass
        inf("Zone transfer blocked (secure)")
    except: pass
    wait()

_WL=[
    "www","mail","ftp","smtp","pop","imap","cpanel","webmail","admin","portal",
    "api","dev","test","staging","beta","demo","app","mobile","m","static",
    "cdn","assets","img","images","media","files","dl","download","blog","shop",
    "store","secure","vpn","remote","ssh","sftp","git","gitlab","jenkins","ci",
    "jira","confluence","wiki","docs","support","help","status","monitor",
    "nagios","grafana","kibana","elastic","search","db","database","mysql",
    "postgres","mongo","redis","cache","ns1","ns2","mx","mx1","mx2","relay",
    "backup","old","new","v2","v3","auth","login","sso","oauth","dashboard",
    "panel","internal","intranet","corp","api2","sandbox","uat","prod","live",
    "web","web1","web2","proxy","lb","waf","mail2","smtp2","forum","community",
    "news","analytics","crm","billing","payment","checkout","account","hooks",
]

def m_subdomain():
    box("05  SUBDOMAIN ENUMERATOR")
    domain=ask("Enter base domain (e.g. example.com)")
    if not domain: return
    found=[]
    pbar("DNS-BRUTE",20)
    for sub in _WL:
        fqdn=f"{sub}.{domain}"
        sys.stdout.write(f"\r  {DIM}probing {fqdn:<55}{RS}")
        sys.stdout.flush()
        try:
            ip=socket.gethostbyname(fqdn)
            found.append((fqdn,ip))
            sys.stdout.write(f"\r  {GBR}[HIT] {fqdn:<44} {CBR}{ip}{RS}\n")
            sys.stdout.flush()
        except: pass
    spin("crt.sh certificate transparency",1.8,"hex")
    ct=set()
    try:
        r=requests.get(f"https://crt.sh/?q=%.{domain}&output=json",timeout=14,headers=HEADERS)
        if r.status_code==200:
            for entry in r.json():
                for n in entry.get("name_value","").lower().split("\n"):
                    n=n.strip().lstrip("*."); 
                    if domain in n: ct.add(n)
    except: inf("crt.sh query failed")
    print(" "*65)
    if found: card("DNS BRUTE-FORCE HITS",[(f,ip) for f,ip in found],MBR)
    if ct:
        card(f"CERT TRANSPARENCY ({len(ct)} total)",[(n,"") for n in sorted(ct)[:30]],CBR)
        if len(ct)>30: inf(f"...and {len(ct)-30} more -- https://crt.sh/?q=%.{domain}")
    ok(f"Total unique: {len(set(f for f,_ in found)|ct)}")
    wait()

_PORTS={
    21:"FTP",22:"SSH",23:"TELNET",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",
    143:"IMAP",443:"HTTPS",445:"SMB",1433:"MSSQL",1521:"ORACLE",2049:"NFS",
    2375:"DOCKER",3306:"MYSQL",3389:"RDP",5432:"POSTGRESQL",5900:"VNC",
    5985:"WINRM",6379:"REDIS",8080:"HTTP-ALT",8443:"HTTPS-ALT",8888:"JUPYTER",
    9200:"ELASTICSEARCH",10250:"KUBELET",11211:"MEMCACHED",27017:"MONGODB",
}

def _grab(host,port):
    try:
        s=socket.socket(); s.settimeout(2.5)
        s.connect((host,port))
        try: b=s.recv(512).decode("utf-8","replace").strip().split("\n")[0]
        except: b=""
        s.close(); return b[:100]
    except: return None

def _scan(host,port):
    try:
        with socket.create_connection((host,port),timeout=1.2): return True
    except: return False

def m_ports():
    box("06  PORT & SERVICE SCANNER")
    warn("Only scan systems you own or have written permission to test.")
    host=ask("Enter host or IP")
    if not host: return
    try: ip=socket.gethostbyname(host); inf(f"Resolved: {ip}")
    except: err("Cannot resolve"); wait(); return
    custom=ask("Extra port range? (e.g. 8000-8100, leave blank to skip)")
    extra={}
    if custom and "-" in custom:
        try:
            lo,hi=[int(x) for x in custom.split("-")]
            for p in range(lo,min(hi+1,lo+300)): extra[p]="CUSTOM"
        except: pass
    targets={**_PORTS,**extra}
    open_ports=[]
    pbar("PORT-SCAN",28)
    for port,svc in targets.items():
        sys.stdout.write(f"\r  {DIM}[{port}] {svc:<18}{RS}"); sys.stdout.flush()
        if _scan(ip,port): open_ports.append((port,svc))
    print(" "*55)
    if open_ports:
        rows=[]
        for port,svc in sorted(open_ports):
            banner=_grab(ip,port)
            rows.append((f"PORT {port}",f"{svc}  |  {banner}" if banner else svc))
        card(f"OPEN PORTS ON {ip}",rows,GBR)
    else: warn("No open ports found")
    inf(f"Scanned: {len(targets)}  Open: {len(open_ports)}")
    wait()

def m_asn():
    box("07  BGP / ASN RECON")
    query=ask("Enter ASN (AS15169), IP, or domain")
    if not query: return
    if not query.upper().startswith("AS"):
        try:
            ip=socket.gethostbyname(query)
            r=requests.get(f"http://ip-api.com/json/{ip}?fields=as",timeout=5)
            raw=r.json().get("as","")
            if raw: query="AS"+raw.split(" ")[0].replace("AS","")
        except: pass
    asn=re.sub(r"[^0-9]","",query)
    if not asn: err("Could not determine ASN"); wait(); return
    spin("bgpview.io query",1.8,"hex")
    try:
        r=requests.get(f"https://api.bgpview.io/asn/{asn}",timeout=10,headers=HEADERS)
        if r.status_code!=200: err(f"BGPView returned {r.status_code}"); wait(); return
        d=r.json().get("data",{})
        rows=[
            ("ASN",        f"AS{d.get('asn','--')}"),
            ("NAME",       d.get("name","--")),
            ("DESCRIPTION",d.get("description_short","--")),
            ("COUNTRY",    d.get("country_code","--")),
            ("WEBSITE",    d.get("website","--")),
            ("EMAIL",      (d.get("email_contacts",["--"]) or ["--"])[0]),
            ("ABUSE EMAIL",(d.get("abuse_contacts",["--"]) or ["--"])[0]),
            ("RIR",        d.get("rir_allocation",{}).get("rir_name","--")),
        ]
        card("ASN IDENTITY",rows,CBR)
        pr=requests.get(f"https://api.bgpview.io/asn/{asn}/prefixes",timeout=8,headers=HEADERS)
        if pr.status_code==200:
            ipv4=pr.json().get("data",{}).get("ipv4_prefixes",[])
            prows=[(f"PREFIX",f"{p.get('prefix','--')}  ({p.get('name','--')})") for p in ipv4[:10]]
            if prows: card(f"IPv4 PREFIXES ({len(ipv4)} total)",prows,GBR)
    except Exception as e: err(f"BGPView error: {e}")
    wait()

def m_reverseip():
    box("08  REVERSE IP LOOKUP")
    target=ask("Enter IP or domain")
    if not target: return
    spin("hackertarget reverse IP",1.6,"scan")
    try:
        r=requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={target}",timeout=12)
        if r.status_code==200 and "error" not in r.text.lower():
            lines=[l for l in r.text.strip().split("\n") if l.strip()]
            rows=[(f"DOMAIN {i+1}",l) for i,l in enumerate(lines[:40])]
            card(f"REVERSE IP ({len(lines)} domains on this IP)",rows,CBR)
            if len(lines)>40: inf(f"...and {len(lines)-40} more")
        else: warn("No results or rate limited -- wait 1 min")
    except Exception as e: err(str(e))
    spin("hackertarget host search",1.2,"bar")
    try:
        r2=requests.get(f"https://api.hackertarget.com/hostsearch/?q={target}",timeout=12)
        if r2.status_code==200 and "error" not in r2.text.lower():
            lines2=[l for l in r2.text.strip().split("\n") if l.strip()]
            rows2=[]
            for l in lines2[:20]:
                parts=l.split(",")
                rows2.append(("HOST",f"{parts[0]}  ->  {parts[1] if len(parts)>1 else ''}"))
            if rows2: card("HOST SEARCH",rows2,GBR)
    except: pass
    wait()

_TECH={
    "WordPress":    ["wp-content","wp-includes","wp-json"],
    "Drupal":       ["drupal.js","/sites/default/"],
    "Joomla":       ["/components/com_","Joomla!"],
    "Shopify":      ["cdn.shopify.com","Shopify.theme"],
    "React":        ["__reactFiber","data-reactroot"],
    "Vue.js":       ["__vue__","data-v-"],
    "Angular":      ["ng-version","ng-app"],
    "Next.js":      ["_next/static","__NEXT_DATA__"],
    "Bootstrap":    ["bootstrap.min.css"],
    "jQuery":       ["jquery.min.js","jquery-"],
    "Cloudflare":   ["cf-ray","__cf_bm"],
    "AWS CloudFront":["x-amz-cf-id"],
    "Google Analytics":["gtag(","UA-"],
    "Laravel":      ["laravel_session"],
    "Django":       ["csrfmiddlewaretoken"],
    "Flask":        ["Werkzeug"],
    "PHP":          ["X-Powered-By: PHP"],
    "Node.js":      ["X-Powered-By: Express"],
    "ASP.NET":      ["X-AspNet-Version"],
    "Nginx":        ["nginx"],
    "Apache":       ["Apache"],
    "LiteSpeed":    ["LiteSpeed"],
}
_WAF={
    "Cloudflare":        ["cf-ray","cloudflare"],
    "AWS WAF":           ["x-amzn-requestid"],
    "Akamai":            ["akamai","x-akamai"],
    "Imperva/Incapsula": ["incap_ses","visid_incap"],
    "F5 BIG-IP":         ["BigIP","BIGipServer"],
    "Sucuri":            ["sucuri"],
    "ModSecurity":       ["Mod_Security"],
}
_SEC=["Strict-Transport-Security","Content-Security-Policy","X-Frame-Options",
      "X-Content-Type-Options","Referrer-Policy","Permissions-Policy"]

def _ssl(hostname):
    try:
        ctx=ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(),server_hostname=hostname) as s:
            s.settimeout(5); s.connect((hostname,443))
            cert=s.getpeercert(); proto=s.version(); cph=s.cipher()
        subj=dict(x[0] for x in cert.get("subject",[]))
        iss=dict(x[0] for x in cert.get("issuer",[]))
        sans=[v for t,v in cert.get("subjectAltName",[]) if t=="DNS"]
        days="--"
        try:
            exp=datetime.strptime(cert.get("notAfter",""),"%b %d %H:%M:%S %Y %Z")
            days=str((exp-datetime.utcnow()).days)
        except: pass
        return {
            "CN":         subj.get("commonName","--"),
            "ISSUER":     iss.get("organizationName","--"),
            "VALID FROM": cert.get("notBefore","--"),
            "VALID TO":   cert.get("notAfter","--"),
            "DAYS LEFT":  days,
            "PROTOCOL":   proto,
            "CIPHER":     cph[0] if cph else "--",
            "SANs":       ", ".join(sans[:6]),
        }
    except: return None

def m_website():
    box("09  WEBSITE FINGERPRINT")
    url=ask("Enter URL or domain")
    if not url: return
    if not url.startswith("http"): url="https://"+url
    hostname=urllib.parse.urlparse(url).netloc or url
    spin(f"Fetching {url}",2.0,"bar")
    try: r=requests.get(url,headers=HEADERS,timeout=12,allow_redirects=True)
    except Exception as e: err(f"Request failed: {e}"); wait(); return
    pbar("FINGERPRINT",26)
    body=r.text+str(dict(r.headers))
    tech=[t for t,sigs in _TECH.items() if any(re.search(s,body,re.I) for s in sigs)]
    waf=[w for w,sigs in _WAF.items() if any(re.search(s,body,re.I) for s in sigs)]
    rows=[
        ("FINAL URL",    r.url),
        ("STATUS",       str(r.status_code)),
        ("LATENCY",      f"{r.elapsed.total_seconds():.2f}s"),
        ("SERVER",       r.headers.get("Server","--")),
        ("X-POWERED-BY", r.headers.get("X-Powered-By","--")),
        ("---",None),
        ("TECH STACK",   ", ".join(tech) or "Unknown"),
        ("WAF DETECTED", ", ".join(waf) or "None"),
        ("---",None),
    ]
    for sh in _SEC:
        v=r.headers.get(sh)
        rows.append((sh.upper().replace("-","_"),v if v else "MISSING"))
    card("WEBSITE FINGERPRINT",rows,GBR)
    ssl_info=_ssl(hostname)
    if ssl_info: card("SSL CERTIFICATE",list(ssl_info.items()),CBR)
    try:
        resolved=socket.gethostbyname(hostname)
        inf(f"Resolved IP: {resolved}")
    except: pass
    wait()

def m_ssl():
    box("10  SSL / TLS DEEP AUDIT")
    host=ask("Enter hostname")
    if not host: return
    host=host.replace("https://","").replace("http://","").split("/")[0]
    spin("TLS handshake",1.8,"hex")
    try:
        ctx=ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(),server_hostname=host) as s:
            s.settimeout(8); s.connect((host,443))
            cert=s.getpeercert(); protocol=s.version(); cph=s.cipher()
    except Exception as e: err(f"TLS failed: {e}"); wait(); return
    subj=dict(x[0] for x in cert.get("subject",[]))
    iss=dict(x[0] for x in cert.get("issuer",[]))
    sans=[v for t,v in cert.get("subjectAltName",[]) if t=="DNS"]
    days="--"; expired=False
    try:
        exp=datetime.strptime(cert.get("notAfter",""),"%b %d %H:%M:%S %Y %Z")
        days=(exp-datetime.utcnow()).days; expired=days<0
    except: pass
    rows=[
        ("SUBJECT CN",  subj.get("commonName","--")),
        ("SUBJECT ORG", subj.get("organizationName","--")),
        ("ISSUER",      iss.get("organizationName","--")),
        ("ISSUER CN",   iss.get("commonName","--")),
        ("VALID FROM",  cert.get("notBefore","--")),
        ("VALID TO",    cert.get("notAfter","--")),
        ("DAYS LEFT",   str(days)+(" -- EXPIRED!" if expired else (" -- EXPIRING SOON" if isinstance(days,int) and days<14 else ""))),
        ("---",None),
        ("PROTOCOL",    protocol),
        ("CIPHER",      cph[0] if cph else "--"),
        ("KEY BITS",    str(cph[2]) if cph else "--"),
        ("---",None),
        ("SANs",        ", ".join(sans[:8])),
        ("TOTAL SANs",  str(len(sans))),
        ("---",None),
        ("SSLLABS",     f"https://www.ssllabs.com/ssltest/analyze.html?d={host}"),
        ("HARDENIZE",   f"https://www.hardenize.com/report/{host}"),
    ]
    card("TLS CERTIFICATE AUDIT",rows,CBR)
    if expired: warn("CERTIFICATE IS EXPIRED")
    elif isinstance(days,int) and days<14: warn(f"EXPIRES IN {days} DAYS")
    elif isinstance(days,int) and days<30: warn(f"Expires in {days} days")
    else: ok("Certificate valid")
    wait()

def m_headers():
    box("11  HTTP HEADER PROBE")
    url=ask("Enter URL")
    if not url: return
    if not url.startswith("http"): url="https://"+url
    spin("Fetching headers",1.4,"scan")
    try: r=requests.get(url,headers=HEADERS,timeout=10)
    except Exception as e: err(str(e)); wait(); return
    rows=[(k.upper(),v[:70]) for k,v in r.headers.items()]
    card("ALL RESPONSE HEADERS",rows,DIM)
    cors=r.headers.get("Access-Control-Allow-Origin","")
    if cors=="*": warn("CORS: * -- OPEN TO ALL ORIGINS")
    elif cors: ok(f"CORS Origin: {cors}")
    for h in ["Server","X-Powered-By","X-AspNet-Version","X-Generator"]:
        v=r.headers.get(h,"")
        if v: warn(f"Info disclosed via {h}: {v}")
    wait()

def m_url():
    box("12  URL REDIRECT CHASER")
    url=ask("Enter URL (short link, suspicious link, etc)")
    if not url: return
    if not url.startswith("http"): url="http://"+url
    spin("Chasing redirect chain",1.8,"bar")
    chain=[]; cur=url
    try:
        for _ in range(15):
            r=requests.head(cur,headers=HEADERS,timeout=6,allow_redirects=False)
            chain.append((r.status_code,cur))
            loc=r.headers.get("Location","")
            if r.status_code in (301,302,303,307,308) and loc:
                if not loc.startswith("http"):
                    p=urllib.parse.urlparse(cur)
                    loc=f"{p.scheme}://{p.netloc}{loc}"
                cur=loc
            else: break
    except Exception as e: warn(f"Chain broken: {e}")
    if chain:
        rows=[(f"HOP {i+1} [{code}]",u) for i,(code,u) in enumerate(chain)]
        fp=urllib.parse.urlparse(chain[-1][1])
        rows+=[("---",None),("FINAL DOMAIN",fp.netloc),("PROTOCOL",fp.scheme)]
        card("REDIRECT CHAIN",rows,CBR)
        if fp.scheme!="https": warn("Final URL is NOT HTTPS")
        else: ok("Final URL uses HTTPS")
        if len(chain)>3: warn(f"{len(chain)} hops -- possible tracking/cloaking")
    wait()

_DORKS={
    "01":("Login pages",         'site:{} intitle:"login" OR intitle:"sign in" OR inurl:login'),
    "02":("Admin panels",        'site:{} inurl:admin OR inurl:administrator OR inurl:wp-admin'),
    "03":("Config / env files",  'site:{} ext:env OR ext:config OR ext:yaml OR ext:ini'),
    "04":("SQL / DB dumps",      'site:{} ext:sql OR ext:db OR ext:sqlite OR ext:bak'),
    "05":("Open directories",    'site:{} intitle:"index of" "parent directory"'),
    "06":("Backup archives",     'site:{} ext:bak OR ext:backup OR ext:old OR ext:zip'),
    "07":("Log files",           'site:{} ext:log OR inurl:logs OR inurl:access.log'),
    "08":("Jenkins CI exposed",  'site:{} intitle:"Dashboard [Jenkins]"'),
    "09":("Exposed .git repo",   'site:{} inurl:"/.git/HEAD"'),
    "10":("API keys in source",  'site:{} intext:"api_key=" OR intext:"secret_key=" OR intext:"access_token="'),
    "11":("phpMyAdmin panels",   'site:{} inurl:phpmyadmin OR intitle:"phpMyAdmin"'),
    "12":("All subdomains",      'site:*.{} -www'),
    "13":("Email addresses",     'site:{} intext:"@{}"'),
    "14":("AWS S3 buckets",      'site:s3.amazonaws.com "{}"'),
    "15":("Firebase databases",  'site:firebaseio.com "{}"'),
    "16":("WordPress users",     'site:{} inurl:"/wp-json/wp/v2/users"'),
    "17":("XML-RPC exposed",     'site:{} inurl:xmlrpc.php'),
    "18":("PHP error messages",  'site:{} "PHP Parse error" OR "PHP Warning" OR "PHP Fatal error"'),
    "19":("Exposed passwords",   'site:{} inurl:password OR inurl:passwd ext:txt OR ext:log'),
    "20":("GraphQL endpoints",   'site:{} inurl:graphql OR inurl:/graphiql'),
}

def m_dork():
    box("13  GOOGLE DORK BUILDER")
    target=ask("Enter domain target (e.g. example.com)")
    if not target: return
    print(f"\n  {GBR}Available dork templates:{RS}\n")
    for k,(desc,_) in _DORKS.items():
        print(f"  {CBR}[{k}]{RS} {GBR}{desc}{RS}")
    choice=ask("Select number (1-20), 'all', or press Enter to cancel")
    if not choice: return
    results=[]
    if choice.lower()=="all":
        results=[(d,q.replace('{}',target)) for _,(d,q) in _DORKS.items()]
    elif choice.zfill(2) in _DORKS:
        d,q=_DORKS[choice.zfill(2)]
        results=[(d,q.replace('{}',target))]
    else: warn("Invalid choice"); wait(); return
    pbar("DORK-BUILD",16)
    print(f"\n  {grad_line('─'*W)}")
    print(f"  {GBR}GENERATED DORK QUERIES -- COPY SECTION BELOW{RS}")
    print(f"  {grad_line('─'*W)}\n")
    all_rows=[]
    for desc,query in results:
        enc=urllib.parse.quote(query)
        link=f"https://www.google.com/search?q={enc}"
        print(f"  {YBR}[DORK]{RS} {WBR}{desc}{RS}")
        print(f"  {GBR}Query:{RS} {query}")
        print(f"  {CBR}Link: {RS} {link}")
        print()
        all_rows+=[
            (f"DORK",desc),
            ("QUERY",query),
            ("LINK",link),
            ("---",None),
        ]
    card("ALL DORK QUERIES",all_rows,YBR)
    open_choice=ask("Open all links in browser? (y/n)")
    if open_choice.lower()=="y":
        import webbrowser
        for desc,query in results:
            enc=urllib.parse.quote(query)
            link=f"https://www.google.com/search?q={enc}"
            webbrowser.open(link)
            time.sleep(0.6)
            time.sleep(0.8)
        ok(f"Opened {len(results)} dork search(es) in browser")
    wait()

def m_tech():
    box("14  TECH STACK DETECTOR")
    url=ask("Enter URL or domain")
    if not url: return
    if not url.startswith("http"): url="https://"+url
    spin("Fetching & analyzing",2.0,"hex")
    try: r=requests.get(url,headers=HEADERS,timeout=12)
    except Exception as e: err(f"Failed: {e}"); wait(); return
    combined=r.text+str(dict(r.headers))
    tech=[t for t,sigs in _TECH.items() if any(re.search(s,combined,re.I) for s in sigs)]
    card("DETECTED TECHNOLOGIES",[(f"TECH {i+1}",t) for i,t in enumerate(tech)] or [("RESULT","None detected")],GBR)
    base=url.rstrip("/")
    probe_rows=[]
    for label,path in [
        ("robots.txt",       "/robots.txt"),
        ("sitemap.xml",      "/sitemap.xml"),
        ("security.txt",     "/.well-known/security.txt"),
        (".env file",        "/.env"),
        (".git/HEAD",        "/.git/HEAD"),
        ("readme",           "/README.md"),
        ("phpinfo",          "/phpinfo.php"),
        ("wp-config backup", "/wp-config.php.bak"),
    ]:
        try:
            pr=requests.get(base+path,headers=HEADERS,timeout=5)
            status=f"HTTP {pr.status_code}  ({len(pr.text)} bytes)"
            if pr.status_code==200 and path in ("/.env","/.git/HEAD","/phpinfo.php"):
                status=f"!!! EXPOSED !!!  {len(pr.text)} bytes"
            probe_rows.append((label.upper(),status))
        except: probe_rows.append((label.upper(),"unreachable"))
    card("SENSITIVE ENDPOINT PROBES",probe_rows,RBR)
    wait()

_PLAT={
    "GitHub":       "https://github.com/{}",
    "GitLab":       "https://gitlab.com/{}",
    "Twitter/X":    "https://twitter.com/{}",
    "Instagram":    "https://www.instagram.com/{}",
    "TikTok":       "https://www.tiktok.com/@{}",
    "Reddit":       "https://www.reddit.com/user/{}",
    "Pinterest":    "https://www.pinterest.com/{}",
    "Medium":       "https://medium.com/@{}",
    "Dev.to":       "https://dev.to/{}",
    "YouTube":      "https://www.youtube.com/@{}",
    "Twitch":       "https://www.twitch.tv/{}",
    "SoundCloud":   "https://soundcloud.com/{}",
    "Patreon":      "https://www.patreon.com/{}",
    "Behance":      "https://www.behance.net/{}",
    "Dribbble":     "https://dribbble.com/{}",
    "HackerNews":   "https://news.ycombinator.com/user?id={}",
    "Steam":        "https://steamcommunity.com/id/{}",
    "Keybase":      "https://keybase.io/{}",
    "Linktree":     "https://linktr.ee/{}",
    "Replit":       "https://replit.com/@{}",
    "HuggingFace":  "https://huggingface.co/{}",
    "Kaggle":       "https://www.kaggle.com/{}",
    "Codepen":      "https://codepen.io/{}",
    "npm":          "https://www.npmjs.com/~{}",
    "PyPI":         "https://pypi.org/user/{}",
    "DockerHub":    "https://hub.docker.com/u/{}",
    "Unsplash":     "https://unsplash.com/@{}",
    "Hashnode":     "https://hashnode.com/@{}",
    "Vimeo":        "https://vimeo.com/{}",
    "Flickr":       "https://www.flickr.com/people/{}",
    "500px":        "https://500px.com/p/{}",
    "Chess.com":    "https://www.chess.com/member/{}",
    "Lichess":      "https://lichess.org/@/{}",
    "Ko-fi":        "https://ko-fi.com/{}",
    "Wattpad":      "https://www.wattpad.com/user/{}",
    "About.me":     "https://about.me/{}",
    "ProductHunt":  "https://www.producthunt.com/@{}",
    "Spotify":      "https://open.spotify.com/user/{}",
    "GitBook":      "https://app.gitbook.com/@{}",
    "Imgur":        "https://imgur.com/user/{}",
    "Disqus":       "https://disqus.com/by/{}",
    "Mastodon":     "https://mastodon.social/@{}",
    "Bluesky":      "https://bsky.app/profile/{}",
}

def m_username():
    box("15  USERNAME OSINT")
    u=ask("Enter username")
    if not u: return
    print(f"\n  {CBR}[*]{RS} {WBR}Sweeping {len(_PLAT)} platforms for: {GBR}{u}{RS}\n")
    pbar("PLATFORM-SWEEP",22)
    found,nf=[],[]
    for plat,tmpl in _PLAT.items():
        url=tmpl.format(u)
        sys.stdout.write(f"\r  {DIM}checking {plat:<28}{RS}"); sys.stdout.flush()
        try:
            rr=requests.get(url,headers=HEADERS,timeout=5,allow_redirects=True)
            (found if rr.status_code==200 else nf).append((plat,url))
        except: nf.append((plat,""))
        time.sleep(0.035)
    print(" "*55)
    if found: card(f"'{u}' FOUND ON {len(found)} PLATFORMS",[(p.upper(),url) for p,url in found],GBR)
    else: warn(f"'{u}' not found on any checked platform")
    inf(f"Not found on {len(nf)}: {', '.join(p for p,_ in nf[:10])}{'...' if len(nf)>10 else ''}")
    wait()

_DISP={"mailinator.com","guerrillamail.com","temp-mail.org","10minutemail.com",
       "yopmail.com","trashmail.com","dispostable.com","spam4.me","throwam.com"}
_PROV={"gmail.com":"Google","yahoo.com":"Yahoo","outlook.com":"Microsoft",
       "hotmail.com":"Microsoft","protonmail.com":"ProtonMail","icloud.com":"Apple",
       "zoho.com":"Zoho","tutanota.com":"Tutanota","fastmail.com":"Fastmail"}

def m_email():
    box("16  EMAIL INVESTIGATOR")
    email=ask("Enter email address")
    if not email: return
    if not re.match(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$',email):
        err("Invalid email syntax"); wait(); return
    domain=email.split("@")[1].lower()
    spin("Investigating email",1.5,"scan")
    md5=hashlib.md5(email.strip().lower().encode()).hexdigest()
    gravatar="Unknown"
    try:
        gr=requests.get(f"https://www.gravatar.com/avatar/{md5}?d=404",timeout=5)
        gravatar="EXISTS" if gr.status_code==200 else "None"
    except: pass
    mx_str="--"
    try:
        mx=dns.resolver.resolve(domain,"MX",lifetime=4)
        mx_str=", ".join(str(r.exchange) for r in sorted(mx,key=lambda x: x.preference))
    except: pass
    hunter_result="--"
    try:
        hr=requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=0",timeout=5)
        if hr.status_code==200:
            hd=hr.json().get("data",{})
            hunter_result=f"{hd.get('status','--')} (score:{hd.get('score','--')})"
    except: pass
    enc=urllib.parse.quote(email)
    rows=[
        ("ADDRESS",          email),
        ("DOMAIN",           domain),
        ("PROVIDER",         _PROV.get(domain,"Unknown / Self-hosted")),
        ("DISPOSABLE",       "YES -- THROWAWAY" if domain in _DISP else "No"),
        ("---",None),
        ("MX SERVERS",       mx_str),
        ("GRAVATAR PROFILE", gravatar),
        ("GRAVATAR URL",     f"https://www.gravatar.com/{md5}" if gravatar=="EXISTS" else "--"),
        ("MD5 HASH",         md5),
        ("---",None),
        ("HAVEIBEENPWNED",   f"https://haveibeenpwned.com/account/{enc}"),
        ("DEHASHED",         f"https://www.dehashed.com/search?query={enc}"),
        ("LEAKCHECK",        f"https://leakcheck.io/api/public?check={enc}"),
        ("INTELX",           f"https://intelx.io/?s={enc}"),
        ("EMAILREP",         f"https://emailrep.io/{enc}"),
    ]
    card("EMAIL INTELLIGENCE",rows,MBR)
    wait()

def m_github():
    box("17  GITHUB RECON")
    username=ask("Enter GitHub username or organization")
    if not username: return
    spin("GitHub public API",1.5,"hex")
    try:
        u=requests.get(f"https://api.github.com/users/{username}",headers=HEADERS,timeout=8)
        if u.status_code==404: err("User not found"); wait(); return
        if u.status_code==403: warn("Rate limited -- try again in 1 min"); wait(); return
        d=u.json()
    except Exception as e: err(str(e)); wait(); return
    rows=[
        ("USERNAME",     d.get("login","--")),
        ("DISPLAY NAME", d.get("name","--")),
        ("BIO",          (d.get("bio") or "--")[:65]),
        ("COMPANY",      d.get("company","--")),
        ("LOCATION",     d.get("location","--")),
        ("EMAIL",        d.get("email","--")),
        ("BLOG",         d.get("blog","--")),
        ("ACCOUNT TYPE", d.get("type","--")),
        ("---",None),
        ("FOLLOWERS",    str(d.get("followers","--"))),
        ("FOLLOWING",    str(d.get("following","--"))),
        ("PUBLIC REPOS", str(d.get("public_repos","--"))),
        ("PUBLIC GISTS", str(d.get("public_gists","--"))),
        ("CREATED",      str(d.get("created_at","--"))[:10]),
        ("UPDATED",      str(d.get("updated_at","--"))[:10]),
        ("PROFILE URL",  f"https://github.com/{username}"),
    ]
    card("GITHUB PROFILE",rows,CBR)
    try:
        rv=requests.get(f"https://api.github.com/users/{username}/repos?per_page=10&sort=updated",headers=HEADERS,timeout=8)
        repos=[x for x in rv.json() if isinstance(x,dict)]
        if repos:
            repo_rows=[(r["name"],f"stars:{r.get('stargazers_count',0)}  lang:{r.get('language','--')}  {'[FORK]' if r.get('fork') else ''}") for r in repos[:10]]
            card("LATEST REPOS",repo_rows,GBR)
    except: pass
    try:
        og=requests.get(f"https://api.github.com/users/{username}/orgs",headers=HEADERS,timeout=8)
        orgs=[x for x in og.json() if isinstance(x,dict)]
        if orgs: card("ORGANIZATIONS",[(o.get("login","--"),o.get("description","--") or "--") for o in orgs[:6]],CBR)
    except: pass
    wait()

_CC={
    "+1":"US/Canada","+7":"Russia","+20":"Egypt","+27":"South Africa",
    "+33":"France","+34":"Spain","+39":"Italy","+44":"United Kingdom",
    "+49":"Germany","+55":"Brazil","+61":"Australia","+81":"Japan",
    "+82":"South Korea","+86":"China","+91":"India","+92":"Pakistan",
    "+971":"UAE","+966":"Saudi Arabia","+380":"Ukraine","+48":"Poland",
}

def m_phone():
    box("18  PHONE NUMBER RECON")
    phone=ask("Enter phone number with country code (+44 7700 900123)")
    if not phone: return
    cleaned=re.sub(r"[\s\-\(\)\.]+","",phone)
    country="--"; local="--"; code_found="--"
    for code,cname in sorted(_CC.items(),key=lambda x:-len(x[0])):
        if cleaned.startswith(code):
            country=cname; local=cleaned[len(code):]; code_found=code; break
    digits=len(re.sub(r"\D","",cleaned))
    rows=[
        ("CLEANED",       cleaned),
        ("COUNTRY CODE",  code_found),
        ("COUNTRY",       country),
        ("LOCAL NUMBER",  local),
        ("TOTAL DIGITS",  str(digits)),
        ("E.164 VALID",   "Yes" if 10<=digits<=15 else "No -- unusual length"),
        ("---",None),
        ("TRUECALLER",    f"https://www.truecaller.com/search/us/{cleaned.lstrip('+')}"),
        ("SYNC.ME",       f"https://sync.me/search/?number={urllib.parse.quote(cleaned)}"),
        ("NUMVERIFY",     f"https://numverify.com/"),
    ]
    card("PHONE INTELLIGENCE",rows,YBR)
    wait()

_DISC_EPOCH=1420070400000

def _sf_time(sf):
    ms=(sf>>22)+_DISC_EPOCH
    return datetime.fromtimestamp(ms/1000,tz=timezone.utc)

def _sf_age(sf):
    created=_sf_time(sf)
    d=(datetime.now(timezone.utc)-created).days
    return f"{d} days  ({d//365}y {(d%365)//30}m {d%30}d)"

_DISC_FLAGS={
    1<<0:"Discord Staff",1<<1:"Partnered Server Owner",
    1<<2:"HypeSquad Events",1<<3:"Bug Hunter Lv1",
    1<<6:"HypeSquad Bravery",1<<7:"HypeSquad Brilliance",
    1<<8:"HypeSquad Balance",1<<9:"Early Supporter",
    1<<14:"Bug Hunter Lv2",1<<16:"Verified Bot Developer",
    1<<22:"Active Developer",
}

_DH={"User-Agent":"Mozilla/5.0 (compatible; Discordbot/2.0)"}

def m_disc_snow():
    box("19  DISCORD SNOWFLAKE DECODER")
    sf_raw=ask("Enter Discord snowflake ID")
    if not sf_raw: return
    if not re.match(r"^\d{15,22}$",sf_raw.strip()): err("Not a valid snowflake"); wait(); return
    sf=int(sf_raw.strip())
    spin("Decoding snowflake",0.8,"hex")
    created=_sf_time(sf); age=_sf_age(sf)
    unix_ms=(sf>>22)+_DISC_EPOCH
    rows=[
        ("SNOWFLAKE ID",   str(sf)),
        ("CREATED (UTC)",  created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
        ("CREATED (LOCAL)",created.astimezone().strftime("%Y-%m-%d  %H:%M:%S  %Z")),
        ("ACCOUNT AGE",    age),
        ("UNIX TIMESTAMP", f"{unix_ms/1000:.3f}"),
        ("UNIX MS",        str(unix_ms)),
        ("---",None),
        ("INTERNAL WORKER",str((sf&0x3E0000)>>17)),
        ("INTERNAL PROC",  str((sf&0x1F000)>>12)),
        ("SEQUENCE INC",   str(sf&0xFFF)),
        ("---",None),
        ("AS USER LINK",   f"https://discord.com/users/{sf}"),
        ("AS SERVER LINK", f"https://discord.com/channels/{sf}"),
        ("LOOKUP PAGE",    f"https://discordlookup.mesalytic.moe/lookup/user/{sf}"),
    ]
    card("SNOWFLAKE ANALYSIS",rows,CBR)
    d=(datetime.now(timezone.utc)-created).days
    if d<7: warn(f"VERY NEW -- only {d} days old")
    elif d<30: warn(f"New -- {d} days old")
    elif d>2000: ok(f"Established -- over {d//365} years old")
    wait()

def m_disc_invite():
    box("20  DISCORD INVITE PROBE")
    raw=ask("Enter invite code or link (discord.gg/abc123)")
    if not raw: return
    code=re.sub(r"(https?://)?(www\.)?(discord\.(gg|com/invite))/","",raw).strip("/")
    if not code: err("Could not parse invite code"); wait(); return
    spin(f"Probing invite: {code}",1.5,"scan")
    try:
        r=requests.get(f"https://discord.com/api/v10/invites/{code}?with_counts=true&with_expiration=true",headers=_DH,timeout=8)
    except Exception as e: err(f"Request failed: {e}"); wait(); return
    if r.status_code==404: err("Invite not found or expired"); wait(); return
    if r.status_code!=200: err(f"Discord returned {r.status_code}"); wait(); return
    d=r.json(); g=d.get("guild",{}); ch=d.get("channel",{}); inv=d.get("inviter",{})
    gid=g.get("id","--"); feats=g.get("features",[])
    icon=g.get("icon","")
    icon_url=f"https://cdn.discordapp.com/icons/{gid}/{icon}.png?size=256" if icon else "--"
    guild_age="--"
    try:
        gc=_sf_time(int(gid)); gdays=(datetime.now(timezone.utc)-gc).days
        guild_age=f"{gc.strftime('%Y-%m-%d')}  ({gdays} days ago)"
    except: pass
    inviter_str="--"
    if inv: inviter_str=f"@{inv.get('username','--')}  (ID: {inv.get('id','--')})"
    vm={0:"None",1:"Low (email)",2:"Medium (5min)",3:"High (10min)",4:"Very High (phone)"}
    ct={0:"Text",2:"Voice",4:"Category",5:"Announcement",13:"Stage",15:"Forum"}
    rows=[
        ("SERVER NAME",    g.get("name","--")),
        ("SERVER ID",      gid),
        ("CREATED",        guild_age),
        ("DESCRIPTION",    g.get("description","None") or "None"),
        ("---",None),
        ("TOTAL MEMBERS",  str(d.get("approximate_member_count","--"))),
        ("ONLINE NOW",     str(d.get("approximate_presence_count","--"))),
        ("BOOST COUNT",    str(g.get("premium_subscription_count","--"))),
        ("NSFW",           "YES" if g.get("nsfw") else "No"),
        ("VERIFY LEVEL",   vm.get(g.get("verification_level",0),"Unknown")),
        ("---",None),
        ("INVITE CODE",    code),
        ("INVITE LINK",    f"https://discord.gg/{code}"),
        ("INVITE CHANNEL", f"#{ch.get('name','--')}  ({ct.get(ch.get('type',0),'?')})"),
        ("INVITED BY",     inviter_str),
        ("EXPIRES",        d.get("expires_at","Never") or "Never"),
        ("---",None),
        ("ICON URL",       icon_url),
        ("FEATURES",       (", ".join(feats[:6])+("..." if len(feats)>6 else "")) or "None"),
    ]
    card("DISCORD SERVER INTEL",rows,YBR)
    if "VERIFIED" in feats: ok("Discord VERIFIED server")
    if "PARTNERED" in feats: ok("Discord PARTNERED server")
    if g.get("nsfw"): warn("Server is marked NSFW")
    wait()

def m_disc_user():
    box("21  DISCORD USER LOOKUP")
    uid=ask("Enter Discord User ID").strip()
    if not uid: return
    if not re.match(r"^\d{17,20}$",uid): err("Invalid snowflake"); wait(); return
    sf=int(uid); created=_sf_time(sf); age=_sf_age(sf)
    age_days=(datetime.now(timezone.utc)-created).days
    spin("Querying public lookup API",1.5,"hex")
    rows=[
        ("USER ID",       uid),
        ("CREATED (UTC)", created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
        ("ACCOUNT AGE",   age),
        ("PROFILE LINK",  f"https://discord.com/users/{uid}"),
        ("LOOKUP PAGE",   f"https://discordlookup.mesalytic.moe/lookup/user/{uid}"),
    ]
    try:
        pl=requests.get(f"https://discordlookup.mesalytic.moe/v1/user/{uid}",timeout=6,headers=HEADERS)
        if pl.status_code==200:
            pd=pl.json()
            uname=pd.get("username","--"); display=pd.get("global_name") or uname
            flags=pd.get("public_flags",0); badge_list=pd.get("badge_list",[]) or []
            avatar=pd.get("avatar",{}); av_id=avatar.get("id","") if isinstance(avatar,dict) else ""
            av_url="--"
            if av_id:
                ext="gif" if av_id.startswith("a_") else "png"
                av_url=f"https://cdn.discordapp.com/avatars/{uid}/{av_id}.{ext}?size=512"
            elif isinstance(avatar,dict) and avatar.get("link"): av_url=avatar["link"]
            rows=[
                ("USERNAME",      f"@{uname}"),
                ("DISPLAY NAME",  display),
                ("USER ID",       uid),
                ("---",None),
                ("CREATED (UTC)", created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
                ("ACCOUNT AGE",   age),
                ("---",None),
                ("BADGES",        ", ".join(str(b) for b in badge_list) or "None"),
                ("PUBLIC FLAGS",  str(flags)),
                ("FLAGS DECODED", ", ".join(l for bit,l in _DISC_FLAGS.items() if flags&bit) or "None"),
                ("---",None),
                ("AVATAR URL",    av_url),
                ("PROFILE LINK",  f"https://discord.com/users/{uid}"),
                ("LOOKUP PAGE",   f"https://discordlookup.mesalytic.moe/lookup/user/{uid}"),
            ]
    except: inf("Public lookup API unavailable -- showing snowflake data only")
    card("DISCORD USER PROFILE",rows,MBR)
    if age_days<30: warn(f"New account -- only {age_days} days old")
    wait()

def m_disc_hunt():
    box("22  DISCORD SERVER HUNT")
    keyword=ask("Enter keyword (e.g. hacking, gaming, anime)")
    if not keyword: return
    enc=urllib.parse.quote(keyword)
    rows=[
        ("DISBOARD",         f"https://disboard.org/servers/tag/{enc}"),
        ("DISBOARD KEYWORD", f"https://disboard.org/search?keyword={enc}"),
        ("DISCORDSERVERS",   f"https://discordservers.com/search?q={enc}"),
        ("DISCORDME",        f"https://discord.me/servers/search?q={enc}"),
        ("DISCORD STREET",   f"https://discord.street/search?q={enc}"),
        ("FIND DISCORD",     f"https://finddiscord.com/?q={enc}"),
        ("DISCORD CENTER",   f"https://discord.center/search?q={enc}"),
        ("---",None),
        ("GOOGLE DORK",      f"https://www.google.com/search?q=site:discord.gg+{enc}"),
        ("GOOGLE DORK 2",    f"https://www.google.com/search?q=discord.gg+{enc}"),
    ]
    card(f"SERVER HUNT -- {keyword}",rows,CBR)
    wait()

def m_cve():
    box("23  CVE / VULNERABILITY SEARCH")
    kw=ask("Enter keyword, CVE ID, or product (e.g. apache log4j)")
    if not kw: return
    spin("Querying NVD NIST database",2.5,"hex")
    try:
        enc=urllib.parse.quote(kw)
        r=requests.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={enc}&resultsPerPage=8",timeout=15,headers={"User-Agent":"fsociety-osint/6.0"})
        data=r.json()
    except Exception as e: err(f"NVD API failed: {e}"); wait(); return
    vulns=data.get("vulnerabilities",[])
    if not vulns: warn("No CVEs found"); wait(); return
    pbar("CVE-RESULTS",22)
    inf(f"Total matching in NVD: {data.get('totalResults',0)} (showing {len(vulns)})")
    for item in vulns:
        cve_obj=item.get("cve",{})
        cve_id=cve_obj.get("id","--")
        desc=next((x["value"] for x in cve_obj.get("descriptions",[]) if x["lang"]=="en"),"No description")
        score="--"; sev="--"
        for key in ["cvssMetricV31","cvssMetricV30","cvssMetricV2"]:
            ml=cve_obj.get("metrics",{}).get(key,[])
            if ml:
                cd=ml[0].get("cvssData",{})
                score=str(cd.get("baseScore","--"))
                sev=cd.get("baseSeverity",ml[0].get("baseSeverity","--"))
                break
        col=RBR if sev in ("CRITICAL","HIGH") else YBR if sev=="MEDIUM" else GBR
        card(cve_id,[
            ("CVE ID",   cve_id),
            ("SCORE",    score),
            ("SEVERITY", sev),
            ("SUMMARY",  desc[:100]+("..." if len(desc)>100 else "")),
            ("NVD LINK", f"https://nvd.nist.gov/vuln/detail/{cve_id}"),
        ],col)
    wait()

_HTYPES={32:["MD5","NTLM","MD4"],40:["SHA-1","MySQL4.1+"],56:["SHA-224"],
         64:["SHA-256","Blake2s"],96:["SHA-384"],128:["SHA-512","Blake2b"]}
_WL_HASH=["password","123456","admin","letmein","qwerty","abc123","test","iloveyou",
          "monkey","dragon","welcome","shadow","master","hello","root","toor","secret",
          "changeme","default","1234","12345","password1","superman","batman","trustno1"]

def m_hash():
    box("24  HASH IDENTIFIER & CRACK")
    h=ask("Enter hash string").strip()
    if not h: return
    pbar("HASH-ANALYSIS",22)
    is_hex=bool(re.fullmatch(r"[0-9a-fA-F]+",h))
    htype="Unknown / custom"
    if h.startswith("$2a$") or h.startswith("$2b$"): htype="bcrypt"
    elif h.startswith("$6$"): htype="SHA-512crypt (Linux shadow)"
    elif h.startswith("$5$"): htype="SHA-256crypt (Linux shadow)"
    elif h.startswith("$1$"): htype="MD5crypt (Linux shadow)"
    elif is_hex and len(h) in _HTYPES: htype=" / ".join(_HTYPES[len(h)])
    spin("Wordlist crack attempt",1.4,"crack")
    cracked="--"
    for s in _WL_HASH:
        for fn,name in [(hashlib.md5,"MD5"),(hashlib.sha1,"SHA1"),(hashlib.sha256,"SHA256")]:
            if fn(s.encode()).hexdigest()==h.lower(): cracked=f"'{s}'  ({name})"; break
        if cracked!="--": break
    rows=[
        ("HASH",         h[:65]),
        ("LENGTH",       str(len(h))),
        ("HEX CHARSET",  "Yes" if is_hex else "No"),
        ("LIKELY TYPE",  htype),
        ("---",None),
        ("CRACK RESULT", cracked),
        ("---",None),
        ("CRACKSTATION",  "https://crackstation.net"),
        ("HASHES.COM",    "https://hashes.com/en/decrypt/hash"),
        ("HASHKILLER",    "https://hashkiller.io/listmanager"),
        ("MD5DECRYPT",    "https://md5decrypt.net"),
    ]
    card("HASH ANALYSIS",rows,RBR)
    if cracked!="--": warn(f"HASH CRACKED: {cracked}")
    wait()

def m_mac():
    box("25  MAC OUI VENDOR LOOKUP")
    mac=ask("Enter MAC address (00:1A:2B:3C:4D:5E)")
    if not mac: return
    clean=mac.replace(":","").replace("-","").replace(".","").upper()
    if len(clean)!=12: err("Invalid MAC -- must be 12 hex chars"); wait(); return
    fmt=":".join(clean[i:i+2] for i in range(0,12,2))
    spin("macvendors.com OUI lookup",1.4,"scan")
    vendor="--"
    try:
        r=requests.get(f"https://api.macvendors.com/{fmt}",timeout=6,headers=HEADERS)
        if r.status_code==200: vendor=r.text.strip()
        elif r.status_code==404: vendor="Not in OUI database"
    except: vendor="Lookup failed"
    first=int(clean[:2],16)
    rows=[
        ("MAC ADDRESS",    fmt),
        ("OUI",            fmt[:8]),
        ("VENDOR",         vendor),
        ("---",None),
        ("ASSIGNMENT",     "Locally administered (possible spoof)" if first&0x02 else "Globally unique"),
        ("ADDRESS TYPE",   "Multicast" if first&0x01 else "Unicast"),
        ("FIRST BYTE",     f"{first:08b}  (0x{first:02X})"),
        ("---",None),
        ("MACLOOKUP.APP",  f"https://maclookup.app/search/result?mac={fmt}"),
        ("WIRESHARK OUI",  f"https://www.wireshark.org/tools/oui-lookup.html"),
    ]
    card("MAC OUI LOOKUP",rows,CBR)
    wait()

def m_disc_server():
    box("26  DISCORD SERVER ID LOOKUP")
    gid_raw=ask("Enter Discord Server / Guild ID")
    if not gid_raw: return
    gid_raw=gid_raw.strip()
    if not re.match(r"^\d{15,22}$",gid_raw): err("Not a valid snowflake"); wait(); return
    sf=int(gid_raw); created=_sf_time(sf)
    age_days=(datetime.now(timezone.utc)-created).days
    age_str=_sf_age(sf)
    rows=[
        ("SERVER ID",      gid_raw),
        ("CREATED (UTC)",  created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
        ("SERVER AGE",     age_str),
        ("---",None),
        ("LOOKUP PAGE",    f"https://discordlookup.mesalytic.moe/lookup/guild/{gid_raw}"),
    ]
    spin("Probing widget API + public lookup",1.5,"scan")
    try:
        wr=requests.get(f"https://discord.com/api/v10/guilds/{gid_raw}/widget.json",headers=_DH,timeout=8)
        if wr.status_code==200:
            wd=wr.json()
            name=wd.get("name","--"); presence=wd.get("presence_count","--")
            invite=wd.get("instant_invite","--") or "--"
            channels=wd.get("channels",[]); members=wd.get("members",[])
            rows=[
                ("SERVER NAME",    name),
                ("SERVER ID",      gid_raw),
                ("CREATED (UTC)",  created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
                ("SERVER AGE",     age_str),
                ("---",None),
                ("ONLINE MEMBERS", str(presence)),
                ("INSTANT INVITE", invite),
                ("---",None),
            ]
            for ch in channels[:8]: rows.append(("CHANNEL",f"#{ch.get('name','--')}  (pos:{ch.get('position','--')})"))
            rows.append(("---",None))
            for mb in members[:6]: rows.append(("ONLINE USER",f"@{mb.get('username','--')}  [{mb.get('status','--')}]"))
            rows+=[("---",None),("WIDGET JSON",f"https://discord.com/api/guilds/{gid_raw}/widget.json"),("LOOKUP PAGE",f"https://discordlookup.mesalytic.moe/lookup/guild/{gid_raw}")]
            ok("Widget API data retrieved")
        elif wr.status_code==403: warn("Widget DISABLED on this server")
    except Exception as e: warn(f"Widget probe failed: {e}")
    try:
        pr=requests.get(f"https://discordlookup.mesalytic.moe/v1/guild/{gid_raw}",timeout=6,headers=HEADERS)
        if pr.status_code==200:
            pd=pr.json()
            if pd.get("name"):
                rows.insert(0,("SERVER NAME",pd.get("name","--")))
    except: pass
    card("DISCORD SERVER REPORT",rows,YBR)
    if age_days<7: warn(f"VERY NEW server -- only {age_days} days old")
    elif age_days>2000: ok(f"Established server -- over {age_days//365} years old")
    wait()

def m_disc_webhook():
    box("27  DISCORD WEBHOOK PROBE")
    warn("Only probe webhooks you own or have authorization to inspect.")
    wh_url=ask("Enter full Discord webhook URL")
    if not wh_url: return
    wh_match=re.search(r"https://discord(?:app)?\.com/api/webhooks/(\d+)/([\w\-]+)",wh_url)
    if not wh_match: err("Invalid webhook URL format"); wait(); return
    wh_id=wh_match.group(1); wh_token=wh_match.group(2)
    spin("Probing webhook",1.5,"bar")
    try:
        r=requests.get(wh_url,headers=_DH,timeout=8)
    except Exception as e: err(f"Request failed: {e}"); wait(); return
    if r.status_code==401: err("Webhook invalid or deleted"); wait(); return
    if r.status_code!=200: err(f"Discord returned {r.status_code}"); wait(); return
    d=r.json(); sf=int(wh_id); created=_sf_time(sf); age_str=_sf_age(sf)
    guild_id=d.get("guild_id","--"); channel_id=d.get("channel_id","--")
    guild_created="--"
    if guild_id and guild_id!="--":
        try:
            gc=_sf_time(int(guild_id)); gdays=(datetime.now(timezone.utc)-gc).days
            guild_created=f"{gc.strftime('%Y-%m-%d')}  ({gdays} days ago)"
        except: pass
    avatar=d.get("avatar","")
    avatar_url=f"https://cdn.discordapp.com/avatars/{wh_id}/{avatar}.png?size=256" if avatar else "--"
    rows=[
        ("WEBHOOK ID",     wh_id),
        ("WEBHOOK NAME",   d.get("name","--")),
        ("WEBHOOK TYPE",   {1:"Incoming",2:"Channel Follower",3:"Application"}.get(d.get("type",1),"Unknown")),
        ("CREATED (UTC)",  created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
        ("WEBHOOK AGE",    age_str),
        ("---",None),
        ("SERVER ID",      guild_id),
        ("SERVER CREATED", guild_created),
        ("CHANNEL ID",     channel_id),
        ("---",None),
        ("AVATAR URL",     avatar_url),
        ("TOKEN PREFIX",   wh_token[:8]+"..."+wh_token[-4:]),
    ]
    card("WEBHOOK INTELLIGENCE",rows,RBR)
    warn("Consider rotating this token if it was exposed publicly.")
    wait()

def m_disc_message():
    box("28  DISCORD MESSAGE LINK DECODER")
    link=ask("Enter Discord message link (discord.com/channels/...)")
    if not link: return
    m=re.search(r"discord(?:app)?\.com/channels/(\d+|@me)/(\d+)/(\d+)",link)
    if not m: err("Could not parse message link. Expected: discord.com/channels/GUILD/CHANNEL/MESSAGE"); wait(); return
    guild_id=m.group(1); channel_id=m.group(2); message_id=m.group(3)
    spin("Decoding all snowflakes",1.0,"hex")
    def sf_row(label,sid):
        if not sid.isdigit(): return [(label+" ID",sid)]
        sf=int(sid); c=_sf_time(sf); ag=(datetime.now(timezone.utc)-c).days
        return [
            (label+" ID",       sid),
            (label+" CREATED",  c.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
            (label+" AGE",      f"{ag} days  ({ag//365}y {(ag%365)//30}m)"),
        ]
    rows=[]
    rows+=sf_row("GUILD",guild_id); rows.append(("---",None))
    rows+=sf_row("CHANNEL",channel_id); rows.append(("---",None))
    rows+=sf_row("MESSAGE",message_id); rows.append(("---",None))
    rows.append(("DIRECT LINK",link))
    rows.append(("GUILD LOOKUP",f"https://discordlookup.mesalytic.moe/lookup/guild/{guild_id}"))
    card("MESSAGE LINK DECODER",rows,CBR)
    wait()

def m_disc_bot():
    box("29  DISCORD BOT LOOKUP")
    bot_id=ask("Enter Discord Bot User ID").strip()
    if not bot_id: return
    if not re.match(r"^\d{15,22}$",bot_id): err("Not a valid snowflake"); wait(); return
    sf=int(bot_id); created=_sf_time(sf); age_str=_sf_age(sf)
    spin("Querying public bot info",1.6,"hex")
    rows=[
        ("BOT ID",         bot_id),
        ("CREATED (UTC)",  created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
        ("BOT AGE",        age_str),
        ("---",None),
        ("BOT PAGE",       f"https://discord.com/users/{bot_id}"),
        ("LOOKUP PAGE",    f"https://discordlookup.mesalytic.moe/lookup/user/{bot_id}"),
        ("TOP.GG",         f"https://top.gg/bot/{bot_id}"),
        ("DISCORDBOTLIST", f"https://discordbotlist.com/bots/{bot_id}"),
    ]
    try:
        r=requests.get(f"https://discordlookup.mesalytic.moe/v1/user/{bot_id}",timeout=6,headers=HEADERS)
        if r.status_code==200:
            d=r.json(); uname=d.get("username","--"); display=d.get("global_name") or uname
            flags=d.get("public_flags",0); badge_list=d.get("badge_list",[]) or []
            avatar=d.get("avatar",{}); av_id=avatar.get("id","") if isinstance(avatar,dict) else ""
            av_url="--"
            if av_id:
                ext="gif" if av_id.startswith("a_") else "png"
                av_url=f"https://cdn.discordapp.com/avatars/{bot_id}/{av_id}.{ext}?size=512"
            rows=[
                ("BOT USERNAME",   f"@{uname}"),
                ("DISPLAY NAME",   display),
                ("BOT ID",         bot_id),
                ("---",None),
                ("CREATED (UTC)",  created.strftime("%Y-%m-%d  %H:%M:%S  UTC")),
                ("BOT AGE",        age_str),
                ("---",None),
                ("PUBLIC FLAGS",   str(flags)),
                ("FLAGS DECODED",  ", ".join(l for bit,l in _DISC_FLAGS.items() if flags&bit) or "None"),
                ("BADGES",         ", ".join(str(b) for b in badge_list) or "None"),
                ("---",None),
                ("AVATAR URL",     av_url),
                ("---",None),
                ("BOT PAGE",       f"https://discord.com/users/{bot_id}"),
                ("TOP.GG",         f"https://top.gg/bot/{bot_id}"),
            ]
    except: inf("Public lookup unavailable -- showing snowflake data only")
    card("DISCORD BOT INTEL",rows,MBR)
    wait()

def m_disc_vanity():
    box("30  DISCORD VANITY URL RESOLVER")
    vanity=ask("Enter vanity code or URL (discord.gg/minecraft OR minecraft)")
    if not vanity: return
    code=re.sub(r"(https?://)?(www\.)?(discord\.(gg|com/invite))/","",vanity).strip("/")
    if not code: err("Could not parse vanity code"); wait(); return
    spin(f"Resolving vanity: {code}",1.5,"scan")
    try:
        r=requests.get(f"https://discord.com/api/v10/invites/{code}?with_counts=true&with_expiration=true",headers=_DH,timeout=8)
    except Exception as e: err(f"Request failed: {e}"); wait(); return
    if r.status_code==404: err("Vanity URL not found"); wait(); return
    if r.status_code!=200: err(f"Discord returned {r.status_code}"); wait(); return
    d=r.json(); g=d.get("guild",{}); ch=d.get("channel",{})
    gid=g.get("id","--"); feats=g.get("features",[])
    icon=g.get("icon",""); banner=g.get("banner","")
    icon_url=f"https://cdn.discordapp.com/icons/{gid}/{icon}.png?size=256" if icon else "--"
    banner_url=f"https://cdn.discordapp.com/banners/{gid}/{banner}.png?size=1024" if banner else "--"
    guild_age="--"
    try:
        gc=_sf_time(int(gid)); gdays=(datetime.now(timezone.utc)-gc).days
        guild_age=f"{gc.strftime('%Y-%m-%d')}  ({gdays} days ago)"
    except: pass
    vm={0:"None",1:"Low",2:"Medium",3:"High",4:"Very High (phone)"}
    ct={0:"Text",2:"Voice",4:"Category",5:"Announcement",13:"Stage",15:"Forum"}
    rows=[
        ("VANITY CODE",    code),
        ("INVITE URL",     f"https://discord.gg/{code}"),
        ("---",None),
        ("SERVER NAME",    g.get("name","--")),
        ("SERVER ID",      gid),
        ("DESCRIPTION",    g.get("description","None") or "None"),
        ("CREATED",        guild_age),
        ("---",None),
        ("TOTAL MEMBERS",  str(d.get("approximate_member_count","--"))),
        ("ONLINE NOW",     str(d.get("approximate_presence_count","--"))),
        ("BOOST COUNT",    str(g.get("premium_subscription_count","--"))),
        ("BOOST TIER",     str(g.get("premium_tier","--"))),
        ("---",None),
        ("VERIFIED",       "Yes" if "VERIFIED" in feats else "No"),
        ("PARTNERED",      "Yes" if "PARTNERED" in feats else "No"),
        ("NSFW",           "YES" if g.get("nsfw") else "No"),
        ("VERIFY LEVEL",   vm.get(g.get("verification_level",0),"Unknown")),
        ("---",None),
        ("INVITE CHANNEL", f"#{ch.get('name','--')}  ({ct.get(ch.get('type',0),'?')})"),
        ("---",None),
        ("ICON URL",       icon_url),
        ("BANNER URL",     banner_url),
        ("FEATURES",       (", ".join(feats[:8])+("..." if len(feats)>8 else "")) or "None"),
        ("SERVER LOOKUP",  f"https://discordlookup.mesalytic.moe/lookup/guild/{gid}"),
    ]
    card("VANITY URL INTEL",rows,GBR)
    if "PARTNERED" in feats: ok("Discord PARTNERED server")
    if "VERIFIED"  in feats: ok("Discord VERIFIED server")
    wait()

def m_disc_status():
    box("31  DISCORD LIVE STATUS CHECK")
    spin("Fetching Discord status",1.5,"bar")
    try:
        sr=requests.get("https://discordstatus.com/api/v2/status.json",timeout=8,headers=HEADERS)
        sd=sr.json(); status=sd.get("status",{}); ind=status.get("indicator","none")
        desc=status.get("description","Unknown"); updated=sd.get("page",{}).get("updated_at","--")[:19]
        ind_col={"none":GBR,"minor":YBR,"major":RBR,"critical":RBR}.get(ind,WBR)
        card("DISCORD PLATFORM STATUS",[
            ("OVERALL STATUS",desc),
            ("INDICATOR",ind.upper()),
            ("LAST UPDATED",updated),
            ("STATUS PAGE","https://discordstatus.com"),
        ],ind_col)
    except Exception as e: err(f"Status API failed: {e}")
    try:
        cr=requests.get("https://discordstatus.com/api/v2/summary.json",timeout=8,headers=HEADERS)
        cd=cr.json(); components=cd.get("components",[])
        sym_map={"operational":"[OK]","degraded_performance":"[SLOW]","partial_outage":"[PARTIAL]","major_outage":"[OUTAGE]","under_maintenance":"[MAINT]"}
        comp_rows=[(c.get("name","--").upper(),sym_map.get(c.get("status","--"),c.get("status","--").upper())) for c in components]
        if comp_rows: card("COMPONENT STATUS",comp_rows,CBR)
    except Exception as e: warn(f"Summary API failed: {e}")
    try:
        ir=requests.get("https://discordstatus.com/api/v2/incidents/unresolved.json",timeout=8,headers=HEADERS)
        id_=ir.json(); incidents=id_.get("incidents",[])
        if incidents:
            for inc in incidents[:3]:
                updates=inc.get("incident_updates",[])
                i_rows=[("NAME",inc.get("name","--")),("IMPACT",inc.get("impact","--").upper()),("STATUS",inc.get("status","--").upper()),("LINK",inc.get("shortlink","--"))]
                if updates:
                    latest=updates[0]
                    i_rows+=[("---",None),("LATEST UPDATE",latest.get("body","--")[:80]),("UPDATE TIME",latest.get("created_at","--")[:19])]
                card("ACTIVE INCIDENT",i_rows,RBR)
        else: ok("No active incidents reported")
    except Exception as e: warn(f"Incidents API failed: {e}")
    wait()

def m_wayback():
    box("32  WAYBACK MACHINE LOOKUP")
    target=ask("Enter URL or domain")
    if not target: return
    if not target.startswith("http"): target="https://"+target
    spin("Wayback availability API",1.5,"scan")
    try:
        r=requests.get(f"https://archive.org/wayback/available?url={urllib.parse.quote(target)}",timeout=10,headers=HEADERS)
        d=r.json(); snap=d.get("archived_snapshots",{}).get("closest",{})
    except Exception as e: err(f"Wayback API failed: {e}"); wait(); return
    rows=[]
    if snap and snap.get("available"):
        ts_raw=snap.get("timestamp",""); ts_fmt="--"
        if len(ts_raw)>=14:
            try: ts_fmt=datetime.strptime(ts_raw,"%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
            except: ts_fmt=ts_raw
        rows=[
            ("TARGET URL",    target),
            ("AVAILABLE",     "Yes"),
            ("SNAPSHOT TIME", ts_fmt),
            ("STATUS CODE",   snap.get("status","--")),
            ("SNAPSHOT URL",  snap.get("url","--")),
            ("---",None),
        ]
    else: rows=[("TARGET URL",target),("AVAILABLE","No snapshot found"),("---",None)]
    domain=urllib.parse.urlparse(target).netloc or target.replace("https://","").replace("http://","")
    rows+=[
        ("FULL CALENDAR",  f"https://web.archive.org/web/*/{target}"),
        ("CDX SEARCH",     f"https://web.archive.org/cdx/search/cdx?url={domain}&output=text&limit=10&fl=timestamp,statuscode"),
    ]
    spin("CDX snapshot count",1.6,"bar")
    try:
        cdx_r=requests.get(f"https://web.archive.org/cdx/search/cdx?url={urllib.parse.quote(domain)}&output=json&limit=5&fl=timestamp,statuscode",timeout=10,headers=HEADERS)
        if cdx_r.status_code==200:
            snaps=cdx_r.json()
            if len(snaps)>1:
                rows.append(("---",None)); rows.append(("RECENT SNAPSHOTS",f"{len(snaps)-1} returned (limited to 5)"))
                for s in snaps[1:]:
                    try: ts=datetime.strptime(s[0],"%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M"); rows.append(("SNAPSHOT",f"{ts}  status:{s[1]}"))
                    except: rows.append(("SNAPSHOT",str(s)))
    except: pass
    card("WAYBACK MACHINE REPORT",rows,CBR)
    wait()

def m_urlscan():
    box("33  URLSCAN.IO ANALYSIS")
    target=ask("Enter domain or URL")
    if not target: return
    domain=urllib.parse.urlparse(target).netloc or target.replace("https://","").replace("http://","").split("/")[0]
    domain=domain.lstrip("www.")
    spin("Searching urlscan.io",1.8,"bar")
    rows=[("TARGET DOMAIN",domain),("---",None)]
    try:
        r=requests.get(f"https://urlscan.io/api/v1/search/?q=domain:{domain}&size=5",timeout=10,headers=HEADERS)
        if r.status_code==200:
            results=r.json().get("results",[])
            rows.append(("SCAN COUNT FOUND",str(len(results))))
            for i,res in enumerate(results[:5]):
                task=res.get("task",{}); page=res.get("page",{})
                rows+=[
                    ("---",None),
                    (f"SCAN {i+1} DATE",   task.get("time","--")[:16]),
                    (f"SCAN {i+1} URL",    task.get("url","--")[:65]),
                    (f"SCAN {i+1} IP",     page.get("ip","--")),
                    (f"SCAN {i+1} COUNTRY",page.get("country","--")),
                    (f"SCAN {i+1} SERVER", page.get("server","--")),
                    (f"SCAN {i+1} TITLE",  (page.get("title","--") or "--")[:50]),
                    (f"SCAN {i+1} LINK",   f"https://urlscan.io/result/{res.get('_id','')}/"),
                ]
        elif r.status_code==429: warn("Rate limited by urlscan.io")
    except Exception as e: rows.append(("ERROR",str(e)))
    rows+=[("---",None),("SEARCH PAGE",f"https://urlscan.io/search/#domain:{domain}")]
    card("URLSCAN.IO REPORT",rows,YBR)
    wait()

def m_email_headers():
    box("34  EMAIL HEADER ANALYZER")
    print(f"\n  {CBR}[*]{RS} {DIM}Paste raw email headers below. Enter a blank line when done.{RS}\n")
    lines=[]
    while True:
        try: ln=input("  ")
        except EOFError: break
        if ln.strip()=="": break
        lines.append(ln)
    if not lines: warn("No headers provided"); wait(); return
    raw="\n".join(lines)
    spin("Analyzing headers",1.2,"scan")
    rows=[]
    received=re.findall(r"Received:\s+(.+?)(?=\nReceived:|\nFrom:|\nTo:|\Z)",raw,re.S|re.I)
    hops=[]
    for i,hop in enumerate(received):
        hop_clean=" ".join(hop.split())
        ips_in_hop=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",hop_clean)
        ip=ips_in_hop[0] if ips_in_hop else "--"
        ts_match=re.search(r";\s*(.{20,35})$",hop_clean)
        ts=ts_match.group(1).strip() if ts_match else "--"
        hops.append((i+1,ip,ts))
    if hops:
        rows.append(("HOP COUNT",str(len(hops)))); rows.append(("---",None))
        for num,ip,ts in hops:
            rows.append((f"HOP {num} IP",ip)); rows.append((f"HOP {num} TIME",ts))
        rows.append(("---",None))
    for label,pattern in [
        ("FROM",        r"^From:\s*(.+)$"),
        ("TO",          r"^To:\s*(.+)$"),
        ("SUBJECT",     r"^Subject:\s*(.+)$"),
        ("DATE",        r"^Date:\s*(.+)$"),
        ("MESSAGE-ID",  r"^Message-ID:\s*(.+)$"),
        ("REPLY-TO",    r"^Reply-To:\s*(.+)$"),
        ("RETURN-PATH", r"^Return-Path:\s*(.+)$"),
        ("X-ORIG-IP",   r"^X-Originating-IP:\s*(.+)$"),
        ("X-MAILER",    r"^X-Mailer:\s*(.+)$"),
        ("SPF",         r"Received-SPF:\s*(.+)$"),
        ("DKIM",        r"DKIM-Signature:.*d=([^;]+)"),
        ("ARC-AUTH",    r"^ARC-Authentication-Results:\s*(.+)$"),
    ]:
        m2=re.search(pattern,raw,re.M|re.I)
        if m2: rows.append((label,m2.group(1).strip()[:70]))
    all_ips=list(dict.fromkeys(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",raw)))
    try:
        public_ips=[ip for ip in all_ips if not ipaddress.ip_address(ip).is_private and not ipaddress.ip_address(ip).is_loopback]
    except: public_ips=[]
    if public_ips:
        rows+=[("---",None),("PUBLIC IPs FOUND",", ".join(public_ips[:8])),("LOOKUP FIRST IP",f"https://www.abuseipdb.com/check/{public_ips[0]}")]
    card("EMAIL HEADER ANALYSIS",rows,MBR)
    if public_ips:
        spin(f"Geolocating {public_ips[0]}",1.2,"hex")
        try:
            gr=requests.get(f"http://ip-api.com/json/{public_ips[0]}?fields=status,country,city,isp,org,proxy",timeout=6)
            gd=gr.json()
            if gd.get("status")=="success":
                card("ORIGINATING IP GEO",[
                    ("IP",      public_ips[0]),
                    ("COUNTRY", gd.get("country","--")),
                    ("CITY",    gd.get("city","--")),
                    ("ISP",     gd.get("isp","--")),
                    ("ORG",     gd.get("org","--")),
                    ("PROXY",   "YES" if gd.get("proxy") else "No"),
                ],RBR)
        except: pass
    wait()

def m_aggregator():
    box("35  OSINT AGGREGATOR")
    target=ask("Enter target (IP, domain, email, username, hash)")
    if not target: return
    enc=urllib.parse.quote(target)
    spin("Building OSINT link set",1.2,"bar")
    is_ip    =bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",target))
    is_email =bool(re.match(r"^[^@]+@[^@]+\.[^@]+$",target))
    is_domain=bool(re.match(r"^[a-zA-Z0-9][a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}$",target)) and not is_ip
    is_hash  =bool(re.match(r"^[0-9a-fA-F]{32,128}$",target))
    type_str="IP" if is_ip else "Email" if is_email else "Domain" if is_domain else "Hash" if is_hash else "Username"
    rows=[("TARGET",target),("TYPE",type_str),("---",None)]
    rows+=[("GOOGLE",f"https://www.google.com/search?q={enc}"),("BING",f"https://www.bing.com/search?q={enc}"),("DUCKDUCKGO",f"https://duckduckgo.com/?q={enc}"),("INTELX",f"https://intelx.io/?s={enc}"),("DEHASHED",f"https://www.dehashed.com/search?query={enc}"),("---",None)]
    if is_ip:
        rows+=[("SHODAN",f"https://www.shodan.io/host/{target}"),("CENSYS",f"https://search.censys.io/hosts/{target}"),("VIRUSTOTAL",f"https://www.virustotal.com/gui/ip-address/{target}"),("ABUSEIPDB",f"https://www.abuseipdb.com/check/{target}"),("GREYNOISE",f"https://viz.greynoise.io/ip/{target}"),("IPINFO",f"https://ipinfo.io/{target}"),("IPVOID",f"https://www.ipvoid.com/ip-blacklist-check/?ip={target}"),("TALOS",f"https://talosintelligence.com/reputation_center/lookup?search={target}"),("THREATFOX",f"https://threatfox.abuse.ch/browse.php?search=ioc:{target}"),("URLSCAN",f"https://urlscan.io/search/#ip:{target}")]
    elif is_domain:
        rows+=[("VIRUSTOTAL",f"https://www.virustotal.com/gui/domain/{target}"),("SHODAN",f"https://www.shodan.io/search?query={target}"),("URLSCAN",f"https://urlscan.io/search/#domain:{target}"),("SECURITYTRAILS",f"https://securitytrails.com/domain/{target}/dns"),("CRTSH",f"https://crt.sh/?q={enc}"),("WAYBACK",f"https://web.archive.org/web/*/{target}"),("WHOIS",f"https://who.is/whois/{target}"),("BUILTWITH",f"https://builtwith.com/{target}"),("DNSLYTICS",f"https://dnslytics.com/domain/{target}"),("SPYONWEB",f"https://spyonweb.com/{target}")]
    elif is_email:
        rows+=[("HAVEIBEENPWNED",f"https://haveibeenpwned.com/account/{enc}"),("LEAKCHECK",f"https://leakcheck.io/api/public?check={enc}"),("EMAILREP",f"https://emailrep.io/{enc}"),("HUNTER",f"https://hunter.io/email-verifier/{enc}"),("GRAVATAR",f"https://www.gravatar.com/{hashlib.md5(target.lower().encode()).hexdigest()}")]
    elif is_hash:
        rows+=[("VIRUSTOTAL",f"https://www.virustotal.com/gui/file/{target}"),("MALWAREBAZAAR",f"https://bazaar.abuse.ch/browse.php?search=sha256hash:{target}"),("THREATFOX",f"https://threatfox.abuse.ch/browse.php?search=ioc:{target}"),("CRACKSTATION","https://crackstation.net/"),("HASHES.COM","https://hashes.com/en/decrypt/hash")]
    else:
        rows+=[("GITHUB",f"https://github.com/{target}"),("TWITTER",f"https://twitter.com/{target}"),("INSTAGRAM",f"https://instagram.com/{target}"),("REDDIT",f"https://reddit.com/user/{target}"),("YOUTUBE",f"https://youtube.com/@{target}"),("TIKTOK",f"https://tiktok.com/@{target}")]
    card(f"OSINT AGGREGATOR -- {target[:40]}",rows,GBR)
    wait()

def m_domain_history():
    box("36  DOMAIN HISTORY TRACKER")
    domain=ask("Enter domain")
    if not domain: return
    domain=domain.replace("https://","").replace("http://","").split("/")[0]
    spin("WHOIS + history sources",2.0,"hex")
    rows=[("DOMAIN",domain),("---",None)]
    try:
        w=whois.whois(domain)
        def fv(v):
            if v is None: return "--"
            return ", ".join(str(x)[:24] for x in v)[:70] if isinstance(v,list) else str(v)[:70]
        rows+=[("REGISTRAR",fv(w.registrar)),("CREATED",fv(w.creation_date)),("UPDATED",fv(w.updated_date)),("EXPIRES",fv(w.expiration_date)),("NAME SERVERS",fv(w.name_servers)),("STATUS",fv(w.status))]
    except Exception as e: rows.append(("WHOIS ERROR",str(e)[:60]))
    try:
        w2=whois.whois(domain); created=w2.creation_date
        if isinstance(created,list): created=created[0]
        if created:
            age=(datetime.now()-created).days
            rows.append(("DOMAIN AGE",f"{age} days  ({age//365}y {(age%365)//30}m)"))
    except: pass
    rows+=[("---",None),("WHOIS HISTORY",f"https://whoishistory.com/domain/{domain}"),("DOMAINTOOLS",f"https://whois.domaintools.com/{domain}"),("SECURITYTRAILS DNS",f"https://securitytrails.com/domain/{domain}/history/dns"),("SECURITYTRAILS IP",f"https://securitytrails.com/domain/{domain}/history/a"),("WHOXY",f"https://www.whoxy.com/{domain}"),("VIEWDNS WHOIS",f"https://viewdns.info/whois/?domain={domain}"),("WAYBACK",f"https://web.archive.org/web/*/{domain}"),("URLSCAN HISTORY",f"https://urlscan.io/search/#domain:{domain}")]
    spin("HackerTarget passive DNS",1.5,"scan")
    try:
        ht=requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}",timeout=10)
        if ht.status_code==200 and "error" not in ht.text.lower():
            lines=[l for l in ht.text.strip().split("\n") if l.strip()]
            rows+=[("---",None),("PASSIVE DNS HITS",str(len(lines)))]
            for l in lines[:8]:
                parts=l.split(",")
                rows.append(("HOST -> IP",f"{parts[0]}  ->  {parts[1] if len(parts)>1 else '?'}"))
    except: pass
    card("DOMAIN HISTORY REPORT",rows,CBR)
    wait()

def m_breach():
    box("37  BREACH AGGREGATOR")
    target=ask("Enter email address or username")
    if not target: return
    enc=urllib.parse.quote(target); is_email="@" in target
    rows=[("TARGET",target),("---",None)]
    spin("LeakCheck public API",1.5,"hex")
    try:
        lc_r=requests.get(f"https://leakcheck.io/api/public?check={enc}",timeout=8,headers=HEADERS)
        if lc_r.status_code==200:
            lc_d=lc_r.json(); found=lc_d.get("found",0); fields=lc_d.get("fields",[]); sources=lc_d.get("sources",[])
            rows+=[("LEAKCHECK STATUS","FOUND IN BREACHES" if found else "Not found"),("BREACH COUNT",str(found)),("EXPOSED FIELDS",", ".join(fields) if fields else "--")]
            if sources:
                rows.append(("---",None))
                for src in sources[:6]:
                    name=src.get("name","--") if isinstance(src,dict) else str(src)
                    rows.append(("BREACH SOURCE",name))
        elif lc_r.status_code==429: rows.append(("LEAKCHECK","Rate limited"))
    except Exception as e: rows.append(("LEAKCHECK ERROR",str(e)[:50]))
    rows+=[("---",None),("HAVEIBEENPWNED",f"https://haveibeenpwned.com/account/{enc}"),("LEAKCHECK",f"https://leakcheck.io/api/public?check={enc}"),("DEHASHED",f"https://www.dehashed.com/search?query={enc}"),("INTELX",f"https://intelx.io/?s={enc}"),("SNUSBASE","https://snusbase.com/"),("BREACHDIRECTORY","https://breachdirectory.org/"),("SPYCLOUD","https://spycloud.com/check-your-exposure/"),("PASTEBIN DORK",f"https://www.google.com/search?q=site:pastebin.com+{enc}"),("GIST DORK",f"https://www.google.com/search?q=site:gist.github.com+{enc}")]
    if is_email:
        rows+=[("EMAILREP",f"https://emailrep.io/{enc}"),("HUNTER VERIFY",f"https://hunter.io/email-verifier/{enc}")]
        md5=hashlib.md5(target.strip().lower().encode()).hexdigest()
        spin("Gravatar check",0.8,"scan")
        try:
            gr=requests.get(f"https://www.gravatar.com/avatar/{md5}?d=404",timeout=5)
            rows+=[("---",None),("GRAVATAR","EXISTS" if gr.status_code==200 else "None")]
            if gr.status_code==200: rows.append(("GRAVATAR URL",f"https://www.gravatar.com/{md5}"))
        except: pass
    card("BREACH AGGREGATOR REPORT",rows,RBR)
    wait()

_MODS={
    "01":m_ip,        "02":m_threat,     "03":m_whois,
    "04":m_dns,       "05":m_subdomain,  "06":m_ports,
    "07":m_asn,       "08":m_reverseip,  "09":m_website,
    "10":m_ssl,       "11":m_headers,    "12":m_url,
    "13":m_dork,      "14":m_tech,       "15":m_username,
    "16":m_email,     "17":m_github,     "18":m_phone,
    "19":m_disc_snow, "20":m_disc_invite,"21":m_disc_user,
    "22":m_disc_hunt, "23":m_cve,        "24":m_hash,
    "25":m_mac,
    "26":m_disc_server,"27":m_disc_webhook,"28":m_disc_message,
    "29":m_disc_bot,  "30":m_disc_vanity,"31":m_disc_status,
    "32":m_wayback,   "33":m_urlscan,    "34":m_email_headers,
    "35":m_aggregator,"36":m_domain_history,"37":m_breach,
}

def main():
    boot()
    while True:
        banner(); show_menu()
        choice=ask("SELECT MODULE")
        if choice=="00":
            clear()
            print(f"\n  {GBR}[+]{RS} {DIM}Session closed.{RS}\n")
            multi_fw(3)
            print(f"\n  {DIM}github.com/cvxxxxxxx  |  Stay legal.{RS}\n")
            sys.exit(0)
        key=choice.zfill(2)
        if key in _MODS: _MODS[key]()
        else:
            print(f"\n  {RBR}[!]{RS} {WBR}Invalid selection '{choice}'.  Enter 01-37 or 00.{RS}")
            time.sleep(1.2)

if __name__=="__main__":
    try: main()
    except KeyboardInterrupt:
        print(f"\n\n  {DIM}Interrupted.{RS}\n")
        sys.exit(0)
