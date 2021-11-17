import os
import sys
import json
import signal
import urllib3
import logging
import random
import argparse
import requests
import threading
from datetime import datetime
sys.path.append(os.getcwd()+"/.lib/")
from headers import user_agents
from colors import red,green,yellow,white,reset


def thorndyke(site,username=None):
   global found_sites
   global username_results

   if not site['valid']:
       if args.debug:
           print(f"🚫 {white}{site['name']}: {yellow}Skipped - Marked as invalid{reset}")
   	    
   if not site['known_accounts'][0]:
   	if args.debug:
   		print(f"🚫 {white}{site['name']}: {yellow}Skipped - No valid user names to test{reset}")
   		
   if username:
   	username = username
   else:
       username = site['known_accounts'][0]
   	    
   url =  site['check_uri'].format(username)
   print(f"🔎 {white}{site['name']}: {green}{url}{reset}")
   try:
      header = {"User-Agent": random.choice(user_agents)}
      response = requests.get(url, headers=header, timeout=60, verify=False, allow_redirects=False)
      code_match = response.status_code == int(site['account_existence_code'])
      string_match = response.text.find(site['account_existence_string']) >= 0
      if username:
          if code_match and string_match:
              username_results.append(f"{white}{site['name']}\n├─ username: @{green}{username}{white}\n├─ status: {green}Found{white}\n├─ url: {green}{site['check_uri'].format(username)}{reset}\n")
              found_sites.append(url)
              return
          else:
           	pass
   	        	
   except requests.exceptions.ReadTimeout:
       if args.debug:
       	print(f"〽️ {white}{site['name']}: {yellow}Request Timed Out{reset}")
       
   #except requests.exceptions.HTTPError as err:
   #	print(f"{white}[{red}!{white}] {err}Connection Reset By Peer{reset}")    
   	    
   except Exception as e:
   	if args.debug:
   		print(f"‼️  {white}{site['name']}: {red}{e}{reset}")
   	
   	
   	
def signal_handler(*_):
    exit(f"\n⭕ {white}[{red}Thorndyke{white}] interrupted with {red}Ctrl{white}+{red}C{reset}")
    sys.exit(130)

signal.signal(signal.SIGINT, signal_handler)
# Disabling HTTPS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


username_results = []
found_sites = []
parser = argparse.ArgumentParser(description=f"{white}Thorndyke: 👥username {green}enumeration{white} tool that 🔎checks the availability of a specified username on over {green}300{white} 🌐websites. | {green}https://github.com/{white}rlyonheart{reset}")
parser.add_argument("-u", "--username", dest="username", metavar=f"{white}[USERNAME]{reset}", help=f"{white}If username is specified, Thorndyke will perform the lookups against the given username instead of running checks against the {green}JSON{white} file{reset}")
parser.add_argument("-f", "--file", dest="file", metavar=f"{white}[FILENAME]{reset}", help=f"{white}perform lookup from a specified site list{reset}")
parser.add_argument("-o", "--output", dest="output", metavar=f"{white}[FILENAME]{reset}", help=f"{white}write output to a specified {green}file{reset}")
parser.add_argument("-S", "--shell", dest="shell", help=f"{white}initiate the {green}BASH{white} alternative of thorndyke{reset}", action="store_true")
parser.add_argument("-d", "--debug", dest="debug", help=f"{white}run thorndyke in {green}debug{white} mode ({green}shows all network logs and errors{white}){reset}", action="store_true")
args = parser.parse_args()

if args.debug:
	logging.basicConfig(level=logging.DEBUG, format=f"🌐 {white}%(message)s{reset}")
