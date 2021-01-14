# pip install PySocks
# pip intall bs4

#!/usr/bin/env python
# -.- coding: utf-8 -.-
import socket, socks, requests, sys, os, optparse, time, httplib
import datetime, hashlib, urllib2, ssl
from termcolor import colored
from bs4 import BeautifulSoup
from time import sleep
reload(sys)
sys.setdefaultencoding('utf-8')

sock = None
ipcheck_url = 'http://checkip.amazonaws.com/'



def create_connection(address, timeout=None, source_address=None):
    global sock
    sock = socks.socksocket()
    sock.connect(address)
    return sock



# Checking Tor Service Status
def verifyTor():
    global urllib2
    global publicIP
    global ipcheck_url


    # Get Public IP(Original IP) from AWS
    publicIP = requests.get(ipcheck_url).text.replace('\n','')
    print "[!] Original Public IP : " + str(publicIP)


    # Change Socket Connection to Tor Service Port(9050)
    # (Tor is running with 9050 port)
    # Then, Public ip will be change to one of the tor ip
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection


    # Get Changed Tor IP
    tor_ip = urllib2.urlopen(ipcheck_url).read().replace('\n','') # Tor IP
    print "[!] Changed Tor IP : " + str(tor_ip)


    # Checking Original Public IP with Changed Tor IP
    if publicIP == tor_ip:
        print "[-] Unsuccessful Tor Connection\n[-] System Exit\n"
       	raise SystemExit
    else:
        print "[+] Tor Running Normally"
        



def checkOnion(onion): # Check Onion Status
    global ipcheck_url
    responseCode = None
    responseInfo = None
    responseRead = None

    try:
        print "\n\n[!] Onion : " + str(onion)
        check_ip = urllib2.urlopen(ipcheck_url).read().replace('\n','')

        if check_ip != publicIP:
            try:
                # Disable SSL Certification Error : [SSL: CERTIFICATE_VERIFY_FAILED]
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE

                request_headers = {
                    "Accept-Language": "en-US,en;q=0.5",
                    "User-Agent": "Mozilla/5.0(Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Connection": "keep-alive"
                }

                request = urllib2.Request(onion, headers=request_headers)
                response = urllib2.urlopen(request, timeout=30, context=ctx)

                responseCode = response.getcode()
                responseInfo = response.info()
                responseRead = response.read()
            except Exception as e:
                #print "ErrorLine:{0}: {1}".format(sys.exc_info()[-1].tb_lineno, str(e))
                pass


            if responseCode == 200:
                soup = BeautifulSoup(responseRead, 'html.parser')
                responseOnionTitle = soup.title.string

                # View HTML Contents
                if soup.prettify() is not None:
                    soupContents = str(soup.prettify()).encode('utf8')
                else:
                    soupContents = ""

                print "[+] Onion Is ACTIVE"
                print "[+] Onion Title : " + str(responseOnionTitle)
                print "[*] Response Code : " + str(responseCode)
                print "[*] Response Info : " + str(responseInfo)
                print "[*] Response Contents : " + str(soupContents)


                # Write Log File
                onionNametwo = onion.replace("http://", "")
		onionName = onionNametwo.replace("onion/", "onion_")
                with open(str(onionName)+ "_logs.txt", "a+") as f:
                    f.write("[!] Onion : " + str(onion))
                    f.write("\n[+] Onion Is ACTIVE")
                    f.write("\n[+] Onion Title : " + str(responseOnionTitle))
                    f.write("\n[*] Response Code : " + str(responseCode))
                    f.write("\n[*] Response Info : " + str(responseInfo))
                    f.write("\n[*] Response Contents : " + str(soupContents))

            else:
                print "[+] Onion Is Down"
                pass

        else:
            print "[-] Connection Anonymity Lost"
            print "[-] System Exit\n"

    except Exception as e:
        print "ErrorLine:{0}: {1}".format(sys.exc_info()[-1].tb_lineno, str(e))
        pass



# Read Onion Addres From File
def readFile(file):
    try:
        with open(file, 'r') as myFile:
            onions = myFile.readlines()
            for onion in onions:
                onion = onion.replace('\n', '')
                if not onion.startswith('http') and not onion.startswith('https'):
                    pass
                else:
                    checkOnion(onion)
    except Exception as e:
        print "ErrorLine:{0}: {1}".format(sys.exc_info()[-1].tb_lineno, str(e))
        pass





def main():
    try:
        if len(sys.argv[1:]) > 0:
            # Chcking Tor Service Status
            try:
                verifyTor()
            except Exception as e:
                print "\n[-] Tor Offline --> Tor Is Not Running\n[-] System Exit"
                print "ErrorLine:{0}: {1}".format(sys.exc_info()[-1].tb_lineno, str(e))
                raise SystemExit


            # Checking Http and Https protocol(Single Onion Check Mode)
            for onion in argv:
                if not onion.startswith('http') and not onion.startswith('https'):
                    print "[-] No Onion URL Found --> Please Enter A Valid URL\n[-] System Exit"
                    raise SystemExit
                else:
                    # Start On/Off Check with Crawling
                    checkOnion(onion)


            # Checking Http and Https protocol(Multiple Onion Check Mode with file)
            if options.file != None:
                file = options.file
                try:
                    # get onion from file
                    readFile(file)
                except Exception as e:
                    print "ErrorLine:{0}: {1}".format(sys.exc_info()[-1].tb_lineno, str(e))
                    raise SystemExit


            print "[!] Onion Inspection Successfully Complete"
        else:
            print "[!] Use '-h' Or '--help' For Usage Options"
    except Exception as e:
        print "ErrorLine:{0}: {1}".format(sys.exc_info()[-1].tb_lineno, str(e))
        pass




if __name__ == '__main__':

    #
    # python onoffcheck_crawler_v2.0.py -f onion_list.txt
    #

    try:
        os.system("clear")
        optparse.OptionParser.format_epilog = lambda self, formatter: self.epilog
        examples = ('\nExamples:\n' +
                    '  python onoffcheck_crawler.py http://xmh57jrzrnw6insl.onion/\n' +
                    '  python onoffcheck_crawler.py -f onion_list.txt\n')

        parser = optparse.OptionParser(epilog=examples, usage='python %prog {onion} [options]', prog='onioffcheck_crawler.py')
        parser.add_option('-f', '--file', action='store', dest='file', help='onion filename')
        (options, argv) = parser.parse_args()

        main()
    except Exception as e:
        print 'ErrorLine:{0}: {1}'.format(sys.exc_info()[-1].tb_lineno, str(e))
        pass
