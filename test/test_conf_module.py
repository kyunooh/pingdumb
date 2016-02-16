import unittest

import mock

from pingdumb.conf import input_conf, read_config, set_config, write_config


class ConfTest(unittest.TestCase):
    def test_read_config(self):
        self.assertEquals("smtp.gmail.com:587", read_config()["smtpServer"])

    def test_write_config(self):
        conf = {
            "url": "jellyms.kr",
            "smtpServer": "smtp.gmail.com:587",
            "smtpUser": "jelly",
            "toEmail": "chm073@naver.com"
        }
        write_config(conf)
        self.assertEquals(conf, read_config())

    def test_input_conf(self):
        conf = {
            "url": "jellyms.kr",
            "smtpServer": "smtp.gmail.com:587",
            "smtpUser": "jelly",
            "toEmail": "chm073@naver.com"
        }

        write_config(conf)

        with mock.patch("__builtin__.raw_input", return_value=""):
            self.assertEquals(conf["url"], input_conf(
                "Please just enter", conf["url"]))
        with mock.patch("__builtin__.raw_input", return_value="test"):
            self.assertEquals("test", input_conf(
                "Please write 'test'", conf["url"]))

    def test_set_config(self):
        expected_conf = {
            "url": "http://abc",
            "smtpServer": "abc",
            "smtpUser": "abc",
            "toEmail": "abc",
            "smtpPw": "Password",
        }

        with mock.patch("__builtin__.raw_input", return_value="abc"):
            with mock.patch("getpass.getpass", return_value="Password"):
                self.assertEquals(expected_conf["url"], set_config()["url"])
                self.assertEquals(
                    expected_conf["smtpServer"], set_config()["smtpServer"])
                self.assertEquals(
                    expected_conf["smtpUser"], set_config()["smtpUser"])
                self.assertEquals(
                    expected_conf["toEmail"], set_config()["toEmail"])
                self.assertEquals(
                    expected_conf["smtpPw"], set_config()["smtpPw"])
