#
#   In order to be able to send messages, you must first import the module smtplib

import smtplib

#   To connect to an SMTP server, you need to know the domain name as well as the port to use. Usually the name of the
#   SMTP server will be the name of the email provide plus smtp in front:
#       Gmail       smtp.gmail.com
#       Yahoo       smtp.mail.yahoo.com
#       Comcast     smtp.comcast.net

#   Port is almost always 587 but double check

#   Once you have the domain name and port information for your email provider, create an SMTP object by calling
#   smptlib.SMTP(), passing the domain name and the port

smtpObject = smtplib.SMTP('smtp.mail.yahoo.com', 587)

#   If the smtlib.smtp call is not successful, your smtp server might not support TLS on port 587. In this case, you
#   will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead

#   Once you have the SMTP object, call its ehlo method to "say hello" to the server. Like a tcp syn packet
smtpObject.ehlo()

#   If you're using port 587 on the SMTP server, you'll need to call the starttls() method next; if using 465 then
#   skip this step

smtpObject.starttls()

#   Once this is set up, you can log in with your username and email password by calling the login() method.

smtpObject.login('msalem_deeap0810@yahoo.com', 'Wggs8m42=')

'''
Gmail has an additional security feature for Google accounts called applicationspecific passwords .
If you receive an Application-specific password required error message when your program tries to log in, you will have
to set up one of these passwords for your Python script . Check out the resources at http:// nostarch.com/automatestuff/
 for detailed directions on how to set up an application-specific password for your Google account .
'''

#   Once logged in, you can call the sendmail to actually send the email.

smtpObject.sendmail('msalem_deeap0810@yahoo.com', 'mariano.salem@frogslayer.com', 'Subject: So long.\n Dear Alice, '
                                                                                  'so long and thanks for all the '
                                                                                  'fish. Sincerely, bob')

#   Be sure to call the quit() method when you are done sending emails.

smtpObject.quit()

