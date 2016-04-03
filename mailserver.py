# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


def send(mail_title,smtpadr,efrom,epass,eto,items):
    if items.__len__() == 0:
        return
    content = ""
    table = unicode("<meta charset=\"utf-8\"><table border=\"1\"><tbody>{}</table></tbody>","utf-8")
    for item in items:

        template = unicode("<tr><td>{img}</td><td><a href=\"{link}\">{title}</a></td></tr>","utf-8")
        link = item.get("link")
        img = item.get("img")
        title = item.get("title")
        template = template.format(link=link,img=img,title=title)
        content += template

    table = table.format(content)
    print table
    msg = MIMEText(table,'html',_charset='utf-8')
    msg['Subject'] = mail_title
    msg['From'] = efrom
    msg['To'] = eto
    smtp = smtplib.SMTP(smtpadr)
    smtp.login(efrom,epass)
    smtp.sendmail(efrom,eto,msg.as_string())
    smtp.quit()
