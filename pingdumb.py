import getopt
import getpass
import sys

from conf import read_config, set_config, write_config
from main_module import checker
from smtp_module import smtp_login_with_conf_test


def main(argv):
    
    if len(sys.argv) == 1:
        conf = set_config()
        s_pw = conf["smtpPw"]
        write_config(conf)
    else:
        """if exist argv, set password and execute with default configure"""
        opts, args = getopt.getopt(argv, 'p')
        for o, a in opts:
            if o == "-p":
                if a == "":
                    s_pw = getpass.getpass("SMTP Server password", "")
                else:
                    s_pw = a

        conf = read_config()
        
    conf["smtpPw"] = s_pw
    smtp_login_with_conf_test(conf)

    checker(conf)

if __name__ == "__main__":
    main(sys.argv[1:])
