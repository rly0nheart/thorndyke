import os
import sys
import json
import signal
import urllib3
import argparse
import requests
import threading
from tqdm import tqdm
from datetime import datetime
sys.path.append(os.getcwd()+"/.lib/")
from colors import red,green,yellow,white,reset


def thorndyke(site,username=None):
   global found_sites
   global username_results
   # Examine the current validity of the entry
   if not site['valid']:
       if args.verbose:
           return print(f"{white}[{yellow}-{white}] {site['name']} Skipped - {yellow}Marked as invalid{reset}")
       return
   	    
   if not site['known_accounts'][0]:
   	if args.verbose:
   		return print(f"{white}[{yellow}-{white}] {site['name']} Skipped - {yellow}No valid user names to test{reset}")
   	return
   		
   if username:
   	username = username
   else:
       username = site['known_accounts'][0]
   	    
   url =  site['check_uri'].format(username)
   print(f"{white}[{green}-{white}] {site['name']}: {green}{url}{reset}")
   try:
      response = requests.get(url, timeout=60, verify=False, allow_redirects=False)
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
       if args.verbose:
       	print(f"{white}[{yellow}!{white}] {site['name']}: {yellow}Read Timeout{reset}")
       
   #except requests.exceptions.HTTPError as err:
   #	print(f"{white}[{red}!{white}] {err}Connection Reset By Peer{reset}")    
   	    
   except Exception as e:
   	if args.verbose:
   		print(f"{white}[{red}!{white}] {site['name']}: {red}{e}{reset}")
   	
   	
   	
def signal_handler(*_):
    """
    If user pressed Ctrl+C close all connections and exit
    """
    if args.verbose:
    	exit(f"\n{white}[{red}x{white}] Process interrupted with {red}Ctrl{white}+{red}C{reset}")
    	sys.exit(130)
    sys.exit(130)

signal.signal(signal.SIGINT, signal_handler)
# Suppress HTTPS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


username_results = []
found_sites = []
parser = argparse.ArgumentParser(description=f"{white}Thorndyke: {green}username enumeration{white} tool that checks the availability of a specified username on over {green}300{white} websites. | {green}https://github.com/{white}rlyonheart{reset}")
parser.add_argument("-v", "--verbose", help=f"{white}run Thorndyke in {green}verbose{white} mode ({green}show all network logs and errors{white}){reset}", action="store_true")
parser.add_argument("-sh","--shell", help=f"{white}run the {green}BASH{white} alternative of Thorndyke{reset}", action="store_true")
parser.add_argument("-d", "--dictionary", dest="dictionary", metavar=f"{white}[FILENAME]{reset}", help=f"{white}perform lookup from a specified site list{reset}")
parser.add_argument("-u", "--username", dest="username", metavar=f"{white}[USERNAME]{reset}", help=f"{white}If username is specified, Thorndyke will perform the lookups against the given username instead of running checks against the {green}JSON{white} file{reset}")
args = parser.parse_args()
