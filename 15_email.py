import smtplib

conn= smtplib.SMTP('smtp.gmail.com', 587)
print(conn.ehlo())
print()

print(conn.starttls())
print()

print(conn.login('email@gmail.com', 'app-specific-password'))
print()

conn.sendmail('email@gmail.com', 'email2@gmail.com', 'Subject: Sent from python code\n\nDear Shubhanan,\n You are a coder')
conn.quit()

#####################################################################################

import imapclient
conn= imapclient.IMAPClient('imap.gmail.com', ssl=True)

conn.login('email@gmail.com', 'app-specific-password')

conn.select_folder('INBOX', readonly=True)

UIDs= conn.search(['SINCE 1-Jan-2024'])
print(UIDs)

rawMessage= conn.fetch([47474], ['BODY[]', 'FLAGS'])


conn.select_folder('INBOX', readonly=False)
UIDs= conn.search(['ON 26-Jan-2024'])
conn.delete_messages(UIDs)

#####################################################################################

import pyzmail

message= pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])

message.get_subject()
message.get_addresses('from')
message.get_addresses('to')

message.text_part.get_payload().decode('UTF-8')
conn.logout()