import multiprocessing
import requests
from smtplib import SMTP
from email.mime.text import MIMEText
import poplib, imaplib


def send_alert_email(from_addr, to_addr, subject, message):
    mesg = MIMEText(message)
    mesg['From'] = from_addr
    mesg['To'] = to_addr
    mesg['Subject'] = subject

    smtp = SMTP('mailout.data.ie.intuit.net')  # smtp-qy.intuit.com
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(queue):
    try:
        url = queue.get()
        p_name = multiprocessing.current_process().name
        response = requests.get(url)
        print('{}: {}: {}'.format(p_name, url, response.content[:128]))
    except requests.exceptions.ConnectionError as err:
        subject = 'faild http request {}: {}'.format(p_name, url)
        send_alert_email('ravi@localhost', 'training@localhost', subject, str(err))


def main():
    q = multiprocessing.Queue()
    urls = ['http://linux.org', 'http://kernel.org', 'http://python.org', 'http://perllang.org']

    for url in urls:
        p = multiprocessing.Process(target=web_crawler, args=(q,))
        p.start()

    for url in urls:
        q.put(url)

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
