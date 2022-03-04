#!/usr/bin/env python3

import os
import sys
import time
import urllib3
import random
import argparse
import requests
from tqdm import tqdm
from datetime import datetime
sys.path.append(f'{os.getcwd()}/.lib')
import banner,colors, headers, sites, found, not_found, default_lookup


def Thorndyke():
    start_time = datetime.now()
    parser = argparse.ArgumentParser(description=f'{colors.white}Lightweight username enumeration tool',epilog=f'{colors.white}Thorndyke checks the availability of a specified username on over 200 popular websites{colors.white}. Developed by Richard Mwewa | https://github.com/{colors.green}rly0nheart{colors.reset}')
    parser.add_argument('username', help=f'{colors.green}target username{colors.reset}')
    parser.add_argument('--found', dest='found', help=f'{colors.green}return found results only{colors.reset}', action='store_true')
    parser.add_argument('--not-found', dest='notfound', help=f'{colors.green}return not found results only{colors.reset}', action='store_true')
    parser.add_argument('--output', dest='output', metavar=f'{colors.green}FILENAME{colors.reset}', help=argparse.SUPPRESS)
    parser.add_argument('--version',version=f'{colors.white}2022.1.2.1 Released on 5th March 2022{colors.reset}',action='version')
    args = parser.parse_args()
    print(banner.banner)
    
    
    print(f'{colors.white}[{colors.green}~{colors.white}] Enumerating @{colors.green}{args.username}{colors.white} on:{colors.reset}')
    for site_name, site_url in tqdm(sites.database.items()):
        try:
            # Suppressing HTTPS warnings
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            user_agent = {'User-Agent': f'{random.choice(headers.user_agents)}'}
            response = requests.get(site_url.format(args.username), headers=user_agent, verify=False, allow_redirects=False)
            if args.found:
            	found.found(args,response,site_name,site_url)
            elif args.notfound:
            	not_found.not_found(args,response,site_name,site_url)
            else:
            	default_lookup.default(args,response,site_url,site_name)
            	
        except KeyboardInterrupt:
            exit(f'\n{colors.white}[{colors.red}x{colors.white}] Process interrupted with {colors.red}Ctrl{colors.white}+{colors.red}C{colors.reset}')
            
        except requests.exceptions.ReadTimeout:
            print(f'{colors.white}[{colors.yellow}!{colors.white}] {site_name}: {colors.yellow}Request Timed Out{colors.reset}')
            
        except Exception as e:
            print(f'{colors.white}[{colors.red}!{colors.white}] {site_name}: {colors.red}{e}{colors.reset}')
            
    print(f'{colors.white}[{colors.green}-{colors.white}] Finished in {colors.green}{datetime.now()-start_time}{colors.white} seconds.{colors.reset}')
