"""
you are:
- a designer, engineer, programmer at the same time!
- hired in big corporation: good code, good algorithmic time expected

task:
- create a knock-off version of facebook in 45 minutes (no pressure)
    - via a menu, users can log in, sign up (not same username twice)
      with password
    - via  a submenu, they can post a status, view all posted statuses,
      edit a status, remove a status
"""
# LISTS + DICTIONARIES
noList = ["n", "N", "no", "No", "NO", "nah", "Nah", "NAH", "nope", "Nope", "NOPE"]
yesList = ["eyes", "y", "Y", "yes", "Yes", "YES", "yeah", "Yeah", "YEAH", "yea", "Yea", "YEA", "yep", "Yep", "YEP", "sure", "Sure",
           "SURE"]

accounts = {"username":"password"}

statuses = ["this is a status please change it"]


# TITLE
print("W E L C O M E   T O   H E A D N O V E L ™\nthe facebook you never needed")


# END
def end():
    print("\nwhen we suffer, you suffer with us :)")


# BACK TO MENU
def backMenu():
    menu = input("\nwould you like to go back to the main menu?\n> ")
    if menu in yesList:
        stuff()
    else:
        end()


# LOGIN / SIGN UP
def account():
    global loggedInUser
    first = input("\nlogin or sign up? (type 1 to quit)\n> ")
    if first == "sign up" or first == "signup":
        newUser = input("\nusername: ")
        while newUser in accounts:
            print("\nthis username already exists :(")
            newUser = input("please enter a new username: ")
        newPassword = input("password (at least 8 characters): ")

        print("\nYOU HAVE SIGNED IN :)")
        accounts[newUser] = newPassword

        account()

    elif first == "login" or first == "log in":
        username = input("\nusername: ")
        while username not in accounts:
            print("\nthis username doesnt exist :(\nplease check for spelling errors")
            username = input("\nusername:")
        password = input("password: ")

        while password != accounts[username]:
            print("\nincorrect password")
            password = input("\npassword: ")

        print("\nYOU HAVE LOGGED IN :)")
        loggedInUser = username

        stuff()

    elif first == "1":
        end()

    else:
        print("\ni'm sorry, i could not understand that")

        account()


# STUFF
def stuff():
    global i
    theStuff = input(f"\nHELLO {loggedInUser.upper()}:\n1. add a status\n2. edit a status\n3. remove a status\n4. view statuses\n5. log out\n> ")
    if theStuff == "1" or theStuff == "add a status" or theStuff == "add":
        addStatus = input("\nnew status: ")
        statuses.append(addStatus)

        backMenu()

    elif theStuff == "2" or theStuff == "edit a status" or theStuff == "edit":
        print("\ncurrent statuses:")
        for i in range(len(statuses)):
            print(f"{i+1}. {statuses[i]}")
        pickStatus = input("\nwhich status would you like to edit?\n> ")
        while (int(pickStatus)-1) not in range(len(statuses)):
            pickStatus = input("\nwhich status would you like to edit?\n> ")
        edit = input(f"\nEDIT '{statuses[int(pickStatus)-1]}': ")
        statuses[int(pickStatus)-1] = edit
        print("\nSTATUS EDITED :)")

        backMenu()

    elif theStuff == "3" or theStuff == "remove a status" or theStuff == "remove":
        print("\ncurrent statuses:")
        for i in range(len(statuses)):
            print(f"{i + 1}. {statuses[i]}")
        pickStatus = input("\nwhich status would you like to remove\n> ")
        while (int(pickStatus) - 1) not in range(len(statuses)):
            pickStatus = input("\nwhich status would you like to edit?\n> ")

        del statuses[int(pickStatus) - 1]
        print("\nSTATUS REMOVED :) it will be missed")

        backMenu()

    elif theStuff == "4" or theStuff == "view statuses" or theStuff == "view":
        print("\nyour statuses:")
        for i in range(len(statuses)):
            print(f"{i + 1}. {statuses[i]}")

        backMenu()

    elif theStuff == "5" or theStuff == "logout":
        print("\nYOU HAVE LOGGED OUT")

        account()

    else:
        print("\nim sorry, i couldn't understand that")

        stuff()

account()
