import getpass
import json
import getopt
from genericpath import isfile
from os.path import sep

from pingdumb.main_module import url_type


def read_config():
    f_path = "." + sep + "pingdumb.json"
    if not isfile(f_path):
        f = open(f_path, 'w')
        conf = {
            "url": "jellyms.kr",
            "smtpServer": "smtp.gmail.com:587",
            "smtpUser": "",
            "toEmail": "",
            "interval": 300,
        }
        f.write(json.dumps(conf))
        f.close()
        return conf
    else:
        f = open(f_path, 'r+b')
        conf = json.loads(f.read().decode('utf-8'))
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
    value = input(message)
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

    interval = input_conf(
        "interval of seconds? (" + str(configure["interval"]) + ")",
        configure["interval"]
    )
    interval = int(interval)
    
    configure["url"] = url_for_test
    configure["toEmail"] = recv_mail

    configure["smtpServer"] = s_server
    configure["smtpUser"] = s_user
    configure["smtpPw"] = s_pw
    configure["interval"] = interval

    return configure


def configure_to_tuple():
    configure = read_config()

    return configure["url"], configure["smtpServer"], \
        configure["smtpUser"], configure["toEmail"], configure["interval"]

        
def extract_password_with_argv(argv):
    opts, args = getopt.getopt(argv, 'p')
    for o, a in opts:
            if o == "-p":
                return getpass.getpass("SMTP Server password", "")
           

    
