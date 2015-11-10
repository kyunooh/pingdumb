import getpass
import json
from builtins import input
from genericpath import isfile
from os.path import sep

from main_module import url_type


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

    recv_mail = raw_input(
        "Receive mail? (" + configure["toEmail"] + ")",
        configure["toEmail"]
    )

    s_server = raw_input(
        "SMTP server? (" + configure["smtpServer"] + ")",
        configure["smtpServer"]
    )
    s_user = raw_input(
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


