import datetime
import sys
import time

from module import form_msg, get_status, read_config, send_email, set_config, \
    smtp_login, smtp_login_test, write_config


if __name__ == "__main__":

    configured = read_config()
    if len(sys.argv) == 1:
        set_config()

    else:
        """if exist argv, set password and execute with default configure"""
        url_for_test = configured["url"]
        recv_mail = configured["toEmail"]
        s_server = configured["smtpServer"]
        s_user = configured["smtpUser"]
        s_pw = sys.argv[1]

    smtp_login_test(s_server, s_user, s_pw)

    write_config(configured)

    while(True):
        status = get_status(url_for_test)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if status != 200:
            print(st + " | Status is " + status)
            s = smtp_login(s_server, s_user, s_pw)
            msg = form_msg(st + "\nHttp status is " + status)
            send_email(s, msg)
        else:
            print(st + " | Is OK")
        time.sleep(300)
