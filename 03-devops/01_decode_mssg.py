import base64

encoded_message = "UHl0aG9uIGlzIGFuIGF3ZXNvbWUgbGFuZ3VhZ2Uu"

decoded_message = base64.b64decode(encoded_message).decode('utf-8')

print(decoded_message)
