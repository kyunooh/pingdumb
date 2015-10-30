import json
import smtplib
from email.mime.text import MIMEText
from os.path import isfile, sep
from urllib2 import urlopen


def get_status(url):
    try:
        f = urlopen(url)
    except IOError:
        return "IOError: can't connect"
    return f.getcode()


def send_email(s, msg):
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()


def smtp_login_test(server, username, password):
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username, password)
    s.quit()
    print("SMTP Login Success!!")


def smtp_login(server, username, password):
    s = smtplib.SMTP(server)
    s.starttls()
    s.login(username, password)
    return s


def form_msg(text, to):
    our_application = "pingdumb"
    msg = MIMEText(text, _subtype="plain", _charset="utf-8")
    msg['Subject'] = 'The contents of %s' % text
    msg['From'] = our_application
    msg['To'] = to
    return msg


def url_type(url):
    if not "://" in url:
        return "http://" + url
    else:
        return url


def read_config():
    f_path = "." + sep + "pingdumb.json"
    if not isfile(f_path):
        f = open(f_path, 'w')
        conf = {
            "url": "jellyms.kr",
            "smtpServer": "smtp.gmail.com:587",
            "smtpUser": "",
            "toEmail": ""
        }
        f.write(json.dumps(conf))
        f.close()
        return conf
    else:
        f = open(f_path, 'r')
        conf = json.loads(f.read())
        f.close()
        return conf


def write_config(conf):
    f_path = "." + sep + "pingdumb.json"
    f = open(f_path, 'w')
    f.truncate()
    f.write(json.dumps(conf))


def input_conf(message, default):
    value = raw_input(message)
    if not value:
        return default
    return value
