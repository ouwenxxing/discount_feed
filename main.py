import sys
import ConfigParser
import webview
import mailserver

config = ConfigParser.RawConfigParser()

configpath = sys.argv[1]
config.read(configpath)

for section in config.sections():
    sectionObj = dict(config.items(section))
    keywords = sectionObj.get("keywords")
    link = sectionObj.get("link")
    efrom = sectionObj.get("email_from")
    eauth = sectionObj.get("email_auth")
    epass = sectionObj.get("email_pass")
    eto = sectionObj.get("email_to")
    eserver = sectionObj.get("smtp")
    for keyword in keywords.split(","):
        items = webview.crawl(keyword, link)
        if(eauth):
            mailserver.send('{}-{}'.format(section,keyword),eserver,efrom,epass,eto,items)
