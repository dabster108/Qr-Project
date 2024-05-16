import validators

def is_valid_url(url):
    return validators.url(url)

url = input("Enter the URL you would like to make it for making QR code: ")
if is_valid_url(url):
    pass
else:
    print("The URL is not valid.")
