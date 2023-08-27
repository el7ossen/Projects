def urlmail():
    while True:
        url = str(input("What site is this password for? "))
        if url == "":
            print("Please input a url\n")
            continue
        else:
            break

    while True:
        email = str(input("What E-mail are you using? "))
        if email == "":
            print("Please input an email\n")
            continue
        else:
            break

    urlmail.url = url
    urlmail.email = email
urlmail()