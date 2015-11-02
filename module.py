import datetime
import getpass
import json
import smtplib
import time
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
    if "://" not in url:
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
        f = open(f_path, 'r+b')
        conf = json.loads(f.read())
        f.close()
        return conf


def write_config(conf):
    if 'smtpPw' in conf:
        del conf['smtpPw']
    f_path = "." + sep + "pingdumb.json"
    f = open(f_path, 'w')
    f.truncate()
    f.write(json.dumps(conf))
    f.close()


def input_conf(message, default):
    value = raw_input(message)
    if not value:
        return default
    return value


def set_config():
    configure = read_config()
    url_for_test = input_conf(
        "URL to test? (" + configure["url"] + ")", configure["url"]
    )
    url_for_test = url_type(url_for_test)

    recv_mail = input_conf(
        "Receive mail? (" + configure["toEmail"] + ")",
        configure["toEmail"]
    )

    s_server = input_conf(
        "SMTP server? (" + configure["smtpServer"] + ")",
        configure["smtpServer"]
    )
    s_user = input_conf(
        "SMTP Server username? (" + configure["smtpUser"] + ")",
        configure["smtpUser"]
    )
    s_pw = getpass.getpass("SMTP Server password?", "")

    configure["url"] = url_for_test
    configure["toEmail"] = recv_mail

    configure["smtpServer"] = s_server
    configure["smtpUser"] = s_user
    configure["smtpPw"] = s_pw
    return configure


def configure_to_tuple():
    configure = read_config()

    return configure["url"], configure["smtpServer"], \
        configure["smtpUser"], configure["toEmail"]


def print_status(status, st):
    print(st + " | Status is " + status)


def checker(url_for_test, conf):
    while(True):
        status = get_status(url_for_test)
        st = get_strftime()
        print_status(status, st)
        if status != 200:
            msg = form_msg(st + "\nHttp status is " + status, conf["toEmail"])
            send_status_mail(conf, msg)
        time.sleep(300)

def get_strftime():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts). \
        strftime('%Y-%m-%d %H:%M:%S')

def smtp_login_with_conf(conf):
    s = smtp_login(conf["smtpServer"], conf["smtpUser"], conf["smtpPw"])


def send_status_mail(conf, msg):
    s = smtp_login_with_conf(conf)
    send_email(s, msg)
    s.quit()
