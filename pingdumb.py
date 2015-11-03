import sys

from smtp_module import smtp_login_test
from conf import write_config, set_config, configure_to_tuple
from main_module import checker
if __name__ == "__main__":

    if len(sys.argv) == 1:
        conf = set_config()
        s_pw = conf["smtpPw"]
        write_config(conf)
    else:
        s_pw = sys.argv[1]
    """if exist argv, set password and execute with default configure"""

    smtp_login_test(conf)
    conf["smtpPW"] = s_pw
    
    checker(url_for_test, conf)
