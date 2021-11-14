#!/bin/bash

# This is a BASH version of Thorndyke
sites_list=.rsc/sites.txt
printf "\n@\e[32m%s\e[0m\n" $1
for url in $(cat $sites_list);
do
    link=$(echo $url | sed "s/username/$1/")
    response=$(curl -I $link 2>/dev/null | head -n 1 | cut -d$' ' -f2)
    if [[ $response =~ "200" ]]; then
	printf "├ \e[32mFound\n\e[0m├─ url: \e[32m%s\e[0m\n" $link
    else
	printf "├ \e[31mNot Found\n\e[0m├─ url: \e[31m%s\e[0m\n" $link
    fi
done

printf "└╼ Thorndyke completed\n"
