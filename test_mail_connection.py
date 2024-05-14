from imaplib import IMAP4, IMAP4_SSL
from poplib import POP3, POP3_SSL
from smtplib import SMTP, SMTP_SSL


def smtp(host, user, password):
    tests = [SMTP(host), SMTP_SSL(host)]
    for test in tests:
        test.set_debuglevel(1)
        test.login(user, password)


def pop3(host, user, password):
    tests = [POP3(host), POP3_SSL(host)]
    for test in tests:
        test.set_debuglevel(1)
        test.user(user)
        test.pass_(password)
        test.quit()


def imap4(host, user, password):
    tests = [IMAP4(host), IMAP4_SSL(host)]
    for test in tests:
        test.debug = 3
        test.login(user, password)
        test.noop()
        test.logout()


def main():
    print("Starting tests")
    host = "smtp.example.com"
    username = "user@example.com"
    password = "password"

    tests = [smtp,pop3,imap4]
    for test in tests:
        try:
            test(host, username, password)
        except Exception as e:
            print(f"Failed {test.__name__}, reason {e}")


if __name__ == "__main__":
    main()