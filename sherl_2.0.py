# -*- coding: utf-8 -*-
import requests, os, urllib.request, json, random, time
os.system("clear")

text = """  
 [1] - [ПОИСК ПО НОМЕРУ МАШИНЫ]   [3] - [ПОИСК ПО НИКУ]  
 [2] - [ИНФА ПО НОМЕРУ ТЕЛЕФОНА]                         
 """
print(text)
while True:
    numb = input("{]-> ")
    if numb == "1":
        car_num = input("|  [ВВЕДИТЕ НОМЕР МАШИНЫ](ПРИМЕР:B777OP)-> ")
        try:
            car_nums = car_num.upper()
            nc = car_num.lower()
            numb_car = nc[:6] + '.' + nc[6:]
            a_h=requests.get("https://авто-история.рф/num/"+car_nums+"/")
            km=requests.get("https://www.230km.ru/"+numb_car+".nomer")
            an=requests.get("http://avto-nomer.ru/ru/gallery.php?fastsearch="+nc)
            if a_h:
                print("|    |_")
                print("|      |https://авто-история.рф/num/"+car_nums+"/")
                print("|      |")
                if km:
                    print("|      |-https://www.230km.ru/"+numb_car+".nomer")
                    print("|      |")
                else:
                    print("|    |")
                    print("|    |-[НЕТ РЕЗУЛЬТАТОВ]")
            else:
                print("|    |")
                print("|    |-[НЕТ РЕЗУЛЬТАТОВ]")
                print("|    |")
            if len(nc)<8:
                print("|    |-[НЕТ РЕЗУЛЬТАТОВ]")
                print("|    |")
            else:
                print("|    |-http://avto-nomer.ru/ru/gallery.php?fastsearch="+nc)
                print("|    |")


        except:
                print("[НЕТ РЕЗУЛЬТАТОВ]")
    elif numb == "2":
        while True:
            try:
                phone = input("|  |-[ВВЕДИТЕ НОМЕР]-> ")
                break
            except:
                print("|  |")
                print("|  |-[если вы видите это сообщение, это означает, что нет результатов
                print("|  |")

        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
        try:
            infoPhones = urllib.request.urlopen( getInfo )
        except:
            print("|  |")
            print("|  |-[НЕТ РЕЗУЛЬТАТОВ]")
            print("|  |")

        infoPhone = json.load( infoPhones )
        try:
            print( u"|  |")
            print( u"|    |-[СТРАНА]--->", infoPhone["country"]["name"] )
            print( u"|    |-[РЕГИОН]---->", infoPhone["region"]["name"] )
            print( u"|    |-[ОПЕРАТОР]-->", infoPhone["0"]["oper"] )
            print( u"|    |-[ГОРОД]------> ", infoPhone["0"]["name"] )
        except:
            print("|  |")
            print("|  |-[НЕТ РЕЗУЛЬТАТОВ]")
            print("|  |")
    

   
    elif numb == '3':
        nick = input("|  |-[ВВЕДИТЕ НИКНЕЙМ]-> ")
        urls_site = ["https://vk.com/",
        "https://my.mail.ru/mail/",
        "https://www.drive2.ru/users/",
        "https://twitter.com/",
        "https://github.com/",
        "https://instagram.com/",
        "http://forum.3dnews.ru/member.php?username=",
        "https://4pda.ru/forum/index.php?act=search&source=pst&noform=1&username=",
        "https://forums.adobe.com/people/",
        "https://ask.fm/",
        "https://badoo.com/profile/",
        "https://www.bandcamp.com/",
        "https://bitcoinforum.com/profile/",
        "blogspot.com",
        "https://dev.to/",
        "https://www.ebay.com/usr/",
        "https://www.gamespot.com/profile/",
        "https://ok.ru/",
        "https://play.google.com/store/apps/developer?id=",
        "https://pokemonshowdown.com/users/",
        "https://www.reddit.com/user/",
        "https://steamcommunity.com/id/",
        "https://steamcommunity.com/groups/",
        "https://tamtam.chat/",
        "https://t.me/",
        "https://www.tiktok.com/@",
        "https://www.twitch.tv/",
        "https://data.typeracer.com/pit/profile?user=",
        "https://www.wikipedia.org/wiki/User:",
        "https://yandex.ru/collections/user/",
        "https://www.youtube.com/",
        "https://www.baby.ru/u/",
        "https://www.babyblog.ru/user/info/",
        "https://www.geocaching.com/profile/?u=",
        "https://habr.com/ru/users/",
        "https://pikabu.ru/@",
        "https://spletnik.ru/user/",
        "https://www.facebook.com/",
        "hhttps://zen.yandex.ru/",
        "https://ggscore.com/ru/dota-2/player?t=",
        "https://www.facebook.com/public/",
        "www.roblox.com/search/users?keyword=",
        "https://www.roblox.com/search/groups?keyword=",
        "https://vk.com/groups/"]
        set_i = 0
        print("|   |_")
        while True:
            try:
                if set_i==13:
                    scan_s = requests.get("https://"+nick+"."+urls_site[set_i])
                else:
                    scan_s = requests.get(urls_site[set_i]+""+nick)

                if scan_s:
                    if set_i==13:
                        print("|     |- https://"+nick+"."+urls_site[set_i])
                    else:
                        print("|     |- "+urls_site[set_i]+""+nick)
                else:
                    print("|     |-[НЕТ РЕЗУЛЬТАТОВ]")
            except:
                print("|     |-[НЕТ РЕЗУЛЬТАТОВ]")
            if set_i+1 == len(urls_site):break

            set_i += 1
