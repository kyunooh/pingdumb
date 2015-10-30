import datetime
import getpass
import sys
import time

from module import form_msg, get_status, input_conf, read_config, send_email, \
    smtp_login, smtp_login_test, url_type, write_config


if __name__ == "__main__":

    configured = read_config()
    if len(sys.argv) == 1:
        url_for_test = input_conf(
            "URL to test? (" + configured["url"] + ")", configured["url"]
        )
        url_for_test = url_type(url_for_test)

        recv_mail = input_conf(
            "Receive mail? (" + configured["toEmail"] + ")",
            configured["toEmail"]
        )

        s_server = input_conf(
            "SMTP server? (" + configured["smtpServer"] + ")",
            configured["smtpServer"]
        )
        s_user = input_conf(
            "SMTP Server username? (" + configured["smtpUser"] + ")",
            configured["smtpUser"]
        )
        s_pw = getpass.getpass("SMTP Server password?", "")

        configured["url"] = url_for_test
        configured["toEmail"] = recv_mail

        configured["smtpServer"] = s_server
        configured["smtpUser"] = s_user

    else:
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
