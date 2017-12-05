import datetime
import time
from urllib.request import urlopen


from pingdumb.smtp_module import form_msg, send_status_mail


def get_status(url):
    try:
        f = urlopen(url)
    except IOError:
        return "IOError: can't connect"
    return f.getcode()


def url_type(url):
    if "://" not in url:
        return "http://" + url
    else:
        return url


def print_status(status, st):
    print(st + " | Status is " + str(status))


def checker(conf):
    while(True):
        status = get_status(conf["url"])
        st = get_strftime()
        print_status(status, st)
        if status != 200:
            msg = form_msg(st + "\nHttp status is " + status, conf["toEmail"])
            send_status_mail(conf, msg)
        time.sleep(conf['interval'])


def get_strftime():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts). \
        strftime('%Y-%m-%d %H:%M:%S')

