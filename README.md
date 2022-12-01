# TOTP Management

![Demo Validation](https://github.com/karisti/totp-management/blob/main/demo1.png?raw=true)

## Description
This project is about creating a server-side program that can create a TOTP service for a given user. To do this, it will create a URI for the user using a random personal secret, and represent it as a QR code. User can scan this QR code on his favorite TOTP app and he will get the valid codes. This program also allows to check if those codes are valid.

![Demo QR](https://github.com/karisti/totp-management/blob/main/demo2.png?raw=true)

## Prerequisites
- TOTP app that can scan QR codes

## Usage
1. Run `python ./totp.py`
2. Scan QR code on a TOTP app
3. Verify codes

## Lessons
- TOTP usage
- TOTP creation
- TOTP verification

## Resources
- [How HOTP and TOTP work](https://www.youtube.com/watch?v=46AKWNOJ3-Y "How HOTP and TOTP work")
- [Time-Based One-Time Password (TOTP)](https://www.youtube.com/watch?v=VOYxF12K1vE "Time-Based One-Time Password (TOTP)")
- [PyOTP - Python One-Time Password Library](https://pyauth.github.io/pyotp/ "PyOTP - Python One-Time Password Library")
- [Generate QR Code](https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/ "Generate QR Code")
- [Python PIL](https://www.geeksforgeeks.org/python-pil-image-open-method/ "Python PIL")
