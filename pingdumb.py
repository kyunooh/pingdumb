import datetime
import sys
import time

from module import form_msg, get_status, send_email, set_config, \
    smtp_login, smtp_login_test, write_config, configure_to_tuple


if __name__ == "__main__":

    if len(sys.argv) == 1:
        configured = set_config()
        s_pw = configured["smtpPw"]
        write_config(configured)
    else:
        s_pw = sys.argv[1]
    """if exist argv, set password and execute with default configure"""
    url_for_test, s_server, s_user, recv_mail = configure_to_tuple()
    smtp_login_test(s_server, s_user, s_pw)

    while(True):
        status = get_status(url_for_test)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if status != 200:
            print(st + " | Status is " + status)
            s = smtp_login(s_server, s_user, s_pw)
            msg = form_msg(st + "\nHttp status is " + status, recv_mail)
            send_email(s, msg)
        else:
            print(st + " | Is OK")
        time.sleep(300)

