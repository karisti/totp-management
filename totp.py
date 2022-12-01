'''
	@Author: Kepa Aristi
	@Date: 30/11/2022
	@Links: https://github.com/karisti
'''

import pyotp, qrcode
from PIL import Image



APP_NAME = "YOUR APP NAME"
USER_NAME = 'user@domain.com'



class User:
	def __init__(self, username):
		self.__username = username
		self.__totp_secret = ''
		self.__totp_uri = ''
		self.__totp_qr = ''
	
	def __generate_totp_secret(self):
		totp_secret = pyotp.random_base32()
		self.__totp_secret = totp_secret

	def __generate_topt_uri(self):
		self.__totp_uri = pyotp.totp.TOTP(self.__totp_secret).provisioning_uri(name=self.__username, issuer_name=APP_NAME)
	
	def __generate_totp_qr(self):
		self.__totp_qr = 'myotp.png'
		img = qrcode.make(self.__totp_uri)
		img.save(self.__totp_qr)

	def generate_topt(self):
		self.__generate_totp_secret()
		self.__generate_topt_uri()
		self.__generate_totp_qr()

		im = Image.open(self.__totp_qr)
		im.show()
	
	def verify_totp(self, code):
		totp = pyotp.TOTP(self.__totp_secret)
		result = totp.verify(code)

		if result == True:
			print("✅ Valid code, welcome!")
		else:
			print("❌ Opss! You're not good enough :)")

		return result



def main():
	user = User(USER_NAME)
	user.generate_topt()

	while True:
		print("\n\nThis account is very secure! Give me your TOTP code :)")
		print("Code: ", end="")

		totp_code = str(input())
		user.verify_totp(totp_code)



if __name__ == "__main__":
	main()
