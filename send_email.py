import smtplib,ssl

host = "smtp.gmail.com"
port=465

username = "sreejishajpisharody@gmail.com"
password = "yuwj wydb wtkb qhva"

receiver = "sreejishajpisharody@gmail.com"
context = ssl.create_default_context()

message = """\
subject: Hi! 
How are you?
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)