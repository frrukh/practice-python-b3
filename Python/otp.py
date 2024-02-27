import random, smtplib

otp = ''.join([str(random.randint(0,9)) for i in range(4)])
print(otp)
print(type(otp))

server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
server.starttls()
server.login('mhmdfrrukh13@gmail.com','ferv gkfh edns dqql')

msg = 'helo'+otp

server.sendmail('mhmdfrrukh13@gmail.com', 'farrukhmaqsood1122@gmail.com', msg)
server.quit()
