import smtplib
from email.mime.text import MIMEText


def send_email(s, msg):
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()


def smtp_login_test(server, username, password):
    s = smtplib.SMTP(server)
    s.starttls()
    s.login(username, password)
    s.quit()
    print("SMTP Login Success!!")
    pass


def smtp_login_with_conf_test(conf):
    smtp_login_test(conf["smtpServer"], conf["smtpUser"], conf["smtpPw"])
    pass
    

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


def smtp_login_with_conf(conf):
    s = smtp_login(conf["smtpServer"], conf["smtpUser"], conf["smtpPw"])
    return s


def send_status_mail(conf, msg):
    s = smtp_login_with_conf(conf)
    send_email(s, msg)
    s.quit()
    pass

