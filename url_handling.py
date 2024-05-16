def is_valid_url(url):
    if url.startswith(("http://", "https://", "ftp://")):
        return True
    else:
        return False

url = input("Enter the URL you would like to make it for making QR code: ")
if is_valid_url(url):
    pass
else:
    print("The URL is not valid.")
