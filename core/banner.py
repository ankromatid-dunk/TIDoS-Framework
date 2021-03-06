# coding: utf-8
#!/usr/bin/env python

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework 

import os
from random import randint
from colors import *

def banner():

    header = """
\033[1;31m
    T H E

        ▄▀▀▀█▀▀▄  ▄▀▀█▀▄    ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄ \033[1;37m
       █    █  ▐ █   █  █  █ ▄▀   █ █      █  ██   ▐ 
       ▐   █     ▐   █  ▐  ▐ █    █ █      █    ▀▄   
          █          █       █    █ ▀▄    ▄▀ ▀▄   █  \033[1;31m
        ▄▀        ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀   
       █         █       █ █     ▐            ▐      
       ▐         ▐       ▐ ▐               
				        F R A M E W O R K

"""


    oblique = C + """
\033[1;36m
   T H E

         ███      ▄█  ████████▄   ▄██████▄     ▄████████ 
     ▀█████████▄ ███  ███   ▀███ ███    ███   ███    ███ \033[1;37m
        ▀███▀▀██ ███▌ ███    ███ ███    ███   ███    █▀  
         ███   ▀ ███▌ ███    ███ ███    ███   ███        
         ███     ███▌ ███    ███ ███    ███ ▀███████████ 
         ███     ███  ███    ███ ███    ███          ███ \033[1;36m
         ███     ███  ███   ▄███ ███    ███    ▄█    ███ 
        ▄████▀   █▀   ████████▀   ▀██████▀   ▄████████▀  

                                                 F R A M E W O R K
"""

    modular = O + """
\033[1;33m
              ___________________________
             |\_________________________/|＼ 
             ||                         || ＼
             ||    \033[1;36mThe                  \033[1;33m||  |
             ||    \033[1;36m   TIDoS             \033[1;33m||  |
             ||    \033[1;36m        Framework    \033[1;33m||  |
             ||      	                \033[1;33m||  |
             ||  \033[1;34mWeb Application Audit  \033[1;33m||  |
             ||  \033[1;34m      Framework        \033[1;33m||  |
             ||                         \033[1;33m||  |
             ||    \033[1;37mFrom: CodeSploit     \033[1;33m||  /
             ||_________________________|| /
             |/_________________________\|/
                __\_________________/__/|
               |_______________________|/
             ________________________
            /\033[0m\033[37moooo  oooo  oooo  oooo \033[1;33m/|
           /\033[0m\033[37mooooooooooooooooooooooo\033[1;33m/ /
          /\033[0m\033[37mooooooooooooooooooooooo\033[1;33m/ /
         /C=_____________________/_/
"""

    speed = G + """

   T H E

	 ████████╗██╗██████╗  ██████╗ ███████╗\033[1;33m
	 ╚══██╔══╝██║██╔══██╗██╔═══██╗██╔════╝
	    ██║   ██║██║  ██║██║   ██║███████╗
            ██║   ██║██║  ██║██║   ██║╚════██║\033[1;32m
	    ██║   ██║██████╔╝╚██████╔╝███████║
            ╚═╝   ╚═╝╚═════╝  ╚═════╝ ╚══════╝

                                         F R A M E W O R K
"""



    fb = C + """
\033[1;36m
     ,------,-------------------------------------,------.
     |      |                                     |      |
     |      |          \033[1;37mThe TIDoS Framework        |      |
     |      |             \033[1;34m< CodeSploit > \033[1;36m         |      |
     |      |                                     |      |
     |      |-------------------------------------|      |
     |      ||...................................||      |
     |      ||                                   ||      |
     |      ||        \033[1;33mHack Facebook? (y/n)       \033[1;36m||      |
     |      ||       \033[1;34m----------------------      \033[1;36m||      |
     |      ||_______    \033[1;33m$ > (Input)      \033[1;36m_______||      |
     |      || \033[1;32m$$$$$ \033[1;36m|                   | \033[1;32m$$$$$\033[1;36m ||      |
     |      ||-------'-------------------'-------||      |
     `------'|___________________________________|`------'  
             
"""
    codesploit = GR + """

                     MMMMMNMNMMMM$%&.
                 .DMMM            lM$%.
               .MMN                  \M$%,.
               MN                     \M%$..
             .M.    \033[1;36mXXXXXXXXXXXXX      \033[1;37m\M%$M
            .M     \033[1;36m XXXXXXXXXXXXX       \033[1;37m\l$%M.
            M      \033[1;36m XXX                  \033[1;37m\M$%M:.
           M      \033[1;36m XXX                    \033[1;37m\$MMM:
          M        \033[1;36m XXX   \033[1;34mXXXXXXX          \033[1;37m:$%MM:
         :M         \033[1;36m XXX   \033[1;34mXX            \033[1;37m :$%MMM:
          M        \033[1;36m XXX   \033[1;34mXXXXXXX       \033[1;37m  M%$MM:
          :M:      \033[1;36m XXX   \033[1;34m     XX       \033[1;37m M$%M:'
            NM     \033[1;36m XXXXXX\033[1;34mXXXXXXX\033[1;36mm    \033[1;37m .M$%MM:
             IMM.  \033[1;36m XXXXXXXXXXXXX\033[1;36mm    \033[1;37m.MD%4M'
              :MM .                  .MM$%M'
                $MM                .MMM$%"'
                 MMMM.            MMMMMM"
                   MMMMMMMMMMMMMMMMMM:*"
\033[1;33m
               ╔═════════════════════════╗
               █   \033[1;31mC O D E S P L O I T\033[1;33m   █
               ╚═════════════════════════╝
"""
    swan = """
\033[1;33m
                      ...,ooooooooo......
                 .o8888888888888888888888888o.
             .o888888888888888888888888888888888o.
           o8888888888A88"V888888888888888888888888o
         o88888887"8"  V   V888  88888888888888888888o
       o88888888            VV0   888888888888888888888
      o888888888             !/    88888888888888888888o
     .88888888888                  88888V"  "V8888888888.
     o88888888888v   \033[1;37mT H E    \033[1;33m     8888"  v8  8888888888o
     88888888888v                  8888v  v88 88888888888
     888888888888     \033[1;37mT I D O S\033[1;33m    88888v  "8888888888888
      88888888888V                  ""M888   "888P8888888
      88888888888v     \033[1;37mF R A M E W O R K \033[1;33m     88P8888888
\033[1;36m ______\033[1;33m8888888888888v.........................VF8888888\033[1;36m_______
 :::::::::::::::::::'                         ::::::::::::::::
 :::::::::::::::::              .:::::::    .:::::::::::::::::\033[1;34m
 :::::::::::::::    \033[1;36mFrom:\033[1;34m        :::::::  .:::::::::::::::::::
 :::::::::::::::      \033[1;37mCodeSploit\033[1;34m  ::::::  ::: ::::::::::::::::
 :::::::::::::::.                 ::::::. :: .::::::::::::::::\033[1;36m
 ::::::::::::::::                 :::::::.  .:::::::::::::::::
 :::::::::::::::.           .     ::::::::::::::::::::::::::::
"""
    headers = [header, oblique, modular, speed, codesploit, fb, swan]
    os.system('clear')
    print headers[randint(0,6)]

