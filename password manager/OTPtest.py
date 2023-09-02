import pyotp, qrcode, time

secret_key = "NWKAL3UJOGZD7CG454DH5G7ROSWJXRDZ"

totp_auth = pyotp.totp.TOTP(secret_key).provisioning_uri(name='el7ossen', issuer_name='OPM')

totp = pyotp.TOTP(secret_key)
  
while True:
    print(totp.verify(input(("Enter the Code : "))))