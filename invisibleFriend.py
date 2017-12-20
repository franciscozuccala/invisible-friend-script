#!/usr/bin/env python
import smtplib
import random
import getpass
from jinja2 import Template
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "InvisibleFriendByZuccala@gmail.com"
password = ""

class Person:

	def __init__(self, name="", email=""):
		self.name = name
		self.email = email
		self.invisible_friend = ""
		
 
def send_email(toaddr, name, invisible_friend_name):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "AMIGO INVISIBLE"
	
	body = Template(open('template/mail.html','r').read()).render(invisible_friend=invisible_friend_name, person=name)
	
	msg.attach(MIMEText(body, 'html'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "MyInvisibleFriend")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()



def main():
	persons = []
	invisible_friends_selected = []

	while True:
		name = raw_input("Please enter name of person, (for start generate process press \"Q\" and then enter): ")
		if(name is "Q"):
			print("Started invisible person game")
			break
		email = raw_input("Please enter email of person: ")
		actualPerson = Person(name, email)
		persons.append(actualPerson)

	print("Generating invisible friends please wait ...")

	for person in persons:
		selected_friend = False
		attempts = 0
		while not selected_friend:
			possible_invisible_friend = random.choice(persons)
			attempts = attempts + 1
			if (possible_invisible_friend not in invisible_friends_selected) and (possible_invisible_friend != person):
				person.invisible_friend = possible_invisible_friend
				invisible_friends_selected.append(possible_invisible_friend)
				selected_friend = True
			if attempts >= 1000:
				return False


	print("Done generating invisible friends")

	want_send_email = raw_input("Do you want to send the emails? (Y for yes N for no) ")
	if(want_send_email is "Y"):
		global password 
		password = getpass.getpass("Insert password: ")

		print("Sending emails ...")

		for person in persons:
			send_email(person.email, person.name , person.invisible_friend.name)

		print("Done sending emails")

	return True


while (not main()):
	print("Something go wrong, tryng again")
print("Thanks for playing.")