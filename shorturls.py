import random
import pyshorteners as ps


def shortener():
    link = input("Enter the link you wanna shorten: ")
    try:
        if link.startswith('https://') or link.startswith('http://'):
            services = ["bitly", 'cuttly',  'tinyurl', 'dagd', 'isgd' , 'chilpit']
            service = random.choice(services)
            if service == 'bitly':
                url = ps.Shortener(api_key='46f5c8eff800e1d3277e8bb35bbe283776d97d9a')
                shorturl = url.bitly.short(link)
                print(shorturl)
            if service == 'cuttly':
                url = ps.Shortener(api_key='f2dabc59748765cb87ce73a3ca556fb337253')
                shorturl = url.cuttly.short(link)
                print(shorturl)
            elif service == 'tinyurl':
                url = ps.Shortener()
                shorturl = url.tinyurl.short(link)
                print(shorturl)
            elif service == 'dagd':
                url = ps.Shortener()
                shorturl = url.dagd.short(link)
                print(shorturl)
            elif service == 'isgd':
                url = ps.Shortener()
                shorturl = url.isgd.short(link)
                print(shorturl)
            elif service == 'chilpit':
                url = ps.Shortener()
                shorturl = url.chilpit.short(link)
                print(shorturl)
            else:
                print("Oops...") #Unnecessary line, but looks good!
        else:
            print("Invalid Link! Make sure the link starts with https:// or http://")
            shortener()
    except ps.exceptions.ShorteningErrorException:
        print("Error Occured! Most likely invalid URL format or server-side error, please try again.")
        shortener()
    except ps.exceptions.BadURLException:
        print("Invalid URL Format!")
        shortener()
    except ps.exceptions.BadAPIResponseException:
        try:
            url = ps.Shortener(api_key='46f5c8eff800e1d3277e8bb35bbe283776d97d9a')
            shorturl = url.bitly.short(link)
            print(shorturl)
        except ps.exceptions.BadAPIResponseException:
            print("Server-error! Please retry")
            shortener()
    

shortener()
