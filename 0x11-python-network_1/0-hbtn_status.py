#!/usr/bin/python3
# this module gets data from htbn website

from urllib.request import urlopen

def main():
    """ this function will be executed when code is
    not imported.
    """

    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as response:
        body = response.read()

    utf = body.decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf-8 content: {utf}")

if __name__ == "__main__":
    main()
