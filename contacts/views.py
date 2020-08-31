from django.shortcuts import render
import requests
from bs4 import *
import re
from django.http import HttpResponse
from .models import *

# Create your views here.

def contacts(request):
    try:
        all_urls = ["https://www.andplus.com/", "https://isadoradigitalagency.com/", "https://upqode.com/", "https://www.xfive.co/", "https://www.strv.com/", \
                        "https://uruit.com/", "https://dockyard.com/", "https://polcode.com/", "https://www.miquido.com/", "https://www.3mediaweb.com/", \
                        "https://willowtreeapps.com/", "https://hedgehoglab.com/", "https://www.eteam.io/", "https://brainhub.eu/", "https://www.rolemodelsoftware.com/"]

        for url in all_urls:
            # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
            # headers = {
            #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            #     "Accept-Encoding": "gzip, deflate",
            #     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            #     "Dnt": "1",
            #     "Host": "httpbin.org",
            #     "Upgrade-Insecure-Requests": "1",
            #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            # }

            # web_data = requests.get(url, headers=headers)
            web_data = requests.get(url)
            soup = BeautifulSoup(web_data.content, "html.parser")

            name = "NanoTech" # Unable to get regex for names for each website that why using constant name for a time being

            phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", soup.text)

            # Convert to set so as to get distinct values
            phone_data = list(dict.fromkeys(phone))

            if phone_data == []:
                phone = "Phone number Not Available"
            else:
                phone = ','.join(str(s) for s in phone_data)

            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", soup.text)
            emails_data = list(dict.fromkeys(emails))

            if emails_data == []:
                emails = "Email is not available"
            else:
                emails = ','.join(str(s) for s in emails_data)

            # Storing in database
            contact = Contact(name=name, email=emails, phone=phone)
            contact.save()

        return HttpResponse('<h1>Success</h1>')

    except Exception as exe:
        print('Unexpected error:' + str(exe))
        # return HttpResponse('<h1>Some Error Occured</h1>')







