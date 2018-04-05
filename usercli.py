users = []
moderateUser = []
adminUsers = []
comments = []


class User:
    """Common class for users"""

    def __init__(self):
        self.user_information = {}
        self.users = users
        self.comments = comments

    def register(self, user_name, password, password_confirmation):
        self.user_information['username'] = user_name
        self.user_information['password'] = password
        self.user_information['password_confirmation'] = password_confirmation

        if user_name in [None, ""]:
            return "Please enter a valid username."
        elif len(password) < 8:
            return "Password should have a minimum of 8 characters"
        elif password_confirmation != password:
            return "Password does not match"
        elif user_name in [user.user_name for user in users]:
            return "The username exist."
        else:
            users.append(self.user_information)
            return "Successfully registered."

    def login(self, user_name, password):
        """
        Enables login of users by submitting the following correctly
        :param user_name:
        :param password:
        :return: success/failure on login
        """
        for user in users:
            if user['username'] == user_name and user['password'] == password:
                return "successfully logged in"
            else:
                return "Invalid password or User name"

    def add_comment(self):
        comment = input("Please type to add your comment")
        print (">>> {}".format(comment))
        comments.append(comment)


class ModerateUser(User):
    def __init__(self):
        self.moderateUser_information = {}
        self.moderateUser = moderateUser

    def edit_comment(self):
        pass


class AdminUser(ModerateUser):
    def __init__(self):
        self.adminuser_information = {}
        self.adminusers = adminUsers

    def delete_comment(self):
        pass


print("Welcome to Thee A Team CLI APP")
name = input('Please input your name: ')
print("\nWhat do you wish to do?")
choice = input("For register '1'")
choice = int(choice)
if choice is 1:
    name = User()
    username = input("input your username: ")
    password = input("Input your password: ")
    confirm_pass = input("Confirm your password: ")

    print(name.register(username, password, confirm_pass))
    username = input("input your username to log in: ")
    password = input("Input your password: ")
    print(name.login(username, password))
else:
    print("Nice having you here and always welcome back")
