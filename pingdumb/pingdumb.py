import sys

from conf import read_config, set_config, \
    write_config, extract_password_with_argv
from main_module import checker
from smtp_module import smtp_login_with_conf_test


def main(argv):
    
    if len(sys.argv) == 1:
        conf = set_config()
        s_pw = conf["smtpPw"]
        write_config(conf)
    else:
        """if exist argv, set password and execute with default configure"""
        s_pw = extract_password_with_argv(argv)
        conf = read_config()
        
    conf["smtpPw"] = s_pw
    smtp_login_with_conf_test(conf)

    checker(conf)

if __name__ == "__main__":
    main(sys.argv[1:])
