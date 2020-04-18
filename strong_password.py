import re
pswd = re.compile('''(
    ^(?=.*[A-Z].*[A-Z])                 #2 capital letters
    (?=.*[!@#$%&*])                     #1 special character
    (?=.*[0-9].*[0-9])                  #2 numbers
    (?=.*[a-z].*[a-z].*[a-z])           #3 lower case letters
    .{10,}                              # atleast 10 total digits
    $
)''', re.VERBOSE)


def pswdCheck():
    password = input("Enter a password: ")
    p = pswd.search(password)

    if(not p):
        print("Password too weak")
        return False
    else:
        print("Strong Password")
        return True


pswdCheck()
