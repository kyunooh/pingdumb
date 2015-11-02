import datetime
import sys
import time

from main_module import form_msg, get_status, set_config, \
    smtp_login, smtp_login_test, configure_to_tuple, checker
from smtp_module import send_email, smtp_login_test, smtp_login, form_msg
from conf import write_config, set_config, configure_to_tuple

if __name__ == "__main__":

    if len(sys.argv) == 1:
        conf = set_config()
        s_pw = conf["smtpPw"]
        write_config(conf)
    else:
        s_pw = sys.argv[1]
    """if exist argv, set password and execute with default configure"""
    url_for_test, s_server, s_user, recv_mail = configure_to_tuple()
    smtp_login_test(s_server, s_user, s_pw)
    conf["smtpPW"] = s_pw
    checker(url_for_test, conf)
