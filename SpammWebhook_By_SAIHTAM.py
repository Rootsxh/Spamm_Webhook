import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import *

colorama.init()

print(f'''{Fore.BLUE} 









 ______     __     ______     ______     ______    
/\  ___\   /\ \   /\  ___\   /\  ___\   /\  == \   
\ \  __\   \ \ \  \ \ \__ \  \ \  __\   \ \  __<   
 \ \_____\  \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/   \/_____/   \/_____/   \/_/ /_/ 
                                                   
                           
                                                                                                            


                                                                                                                       
                        By SAIHTAM

          
                        Faite ENTER pour arreter le Spamm ! {Style.RESET_ALL}
''')

def sbammah():
    webhook = input(Fore.YELLOW + "[>] Entrer le webhook: ")
    message = input(Fore.BLUE + "[>] Entrer le message : ")    
    delay = float(input(Fore.RED + "[>] entrer le delai (EX: 0.1): "))
    print(Fore.BLUE + 'Début de l’envoi d’un messages')

    while True:

        print(Fore.CYAN + "Sending -> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent -> " + message) 
        except:
            print("Quelque chose s’est passé! | Webhook probablement cassé -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    sbammah()
