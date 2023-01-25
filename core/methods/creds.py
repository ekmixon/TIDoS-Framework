
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_____, ___
   '+ .;    
    , ;   
     .   
           
       .    
     .;.    
     .;  
      :  
      ,   
       

┌─[TIDoS]─[]
└──╼ VainlyStrain
"""


import core.variables as vars
from core.Core.colors import color, C, R, B

def creds(inp):
    if "add" in inp:
        correct = True
        user = input(" [§] username :> ")
        passwd = input(" [§] password :> ")
        url = inp.split("add")[1].strip()
        if user != "" and passwd != "" and "@" not in url:
            if "https" in url:
                domain = url.split("://")[1]
                url2 = f"https://{user}:{passwd}@{domain}"
            elif "http" in url:
                domain = url.split("://")[1]
                url2 = f"http://{user}:{passwd}@{domain}"
            else:
                print(
                    f"{R} [-] "
                    + "\033[0m"
                    + color.UNDERLINE
                    + "\033[1m"
                    + "Provide target formatted as in viclist"
                )
                correct = False
            if correct:
                found = False
                for i in range(len(vars.targets)):
                    if vars.targets[i].fullurl == url:
                        vars.targets[i].fullurl = url2
                        vars.targets[i].urluser = user
                        vars.targets[i].urlpasswd = passwd
                        found = True
                if found:
                    print(f" [+] {url} > {url2}")
        else:
            print(
                f"{R} [-] "
                + "\033[0m"
                + color.UNDERLINE
                + "\033[1m"
                + "An error occurred. Either, no credentials were provided or the URL already contains credentials."
            )
    elif "del" in inp:
        correct = True
        url = inp.split("del")[1].strip()
        if "https" in url:
            domain = url.split("@")[1]
            url2 = f"https://{domain}"
        elif "http" in url:
            domain = url.split("@")[1]
            url2 = f"http://{domain}"
        else:
            print(
                f"{R} [-] "
                + "\033[0m"
                + color.UNDERLINE
                + "\033[1m"
                + "Provide target formatted as in viclist"
            )
            correct = False
        if correct:
            found = False
            for i in range(len(vars.targets)):
                if vars.targets[i].fullurl == url:
                    vars.targets[i].fullurl = url2
                    vars.targets[i].urluser = ""
                    vars.targets[i].urlpasswd = ""
                    found = True
            if found:
                print(f" [+] {url} > {url2}")
    else:
        print(
            f"{R} [-] "
            + "\033[0m"
            + color.UNDERLINE
            + "\033[1m"
            + "Syntax: creds add|del target"
        )

def attackdrop(target):
    if "@" in target.fullurl:
        newtarget = target
        newtarget.fullurl = newtarget.name
        return newtarget
        #ssl = False
        #if "https" in target:
        #    ssl = True
        #splitar = target.split("@")[1]
        #if ssl:
        #    return "https://" + splitar
        #else:
        #    return "http://" + splitar
    else:
        print(
            f"{R} [-] "
            + "\033[0m"
            + color.UNDERLINE
            + "\033[1m"
            + "No credentials found."
        )
