import db_operations


def check_create_acc_data(login, password, c_password, db):
    msg = None
    if not (password == c_password):
        msg = "Passwords are not the same"
        return False, msg

    if not (5 <= len(login) <= 32):
        msg = "Login must be between 5 and 32"
        return False, msg

    if not (5 <= len(password) <= 32):
        msg = "Password must be between 5 and 32"
        return False, msg

    if not (not password.isupper() and not password.islower()):
        msg = "Password must contain upper and lower cases"
        return False, msg

    if not (any(char.isdigit() for char in password)):
        msg = "Password must contain a digit"
        return False, msg

    logins = db.get_all_names()
    print(logins)
    if login in logins:
        msg = f"{login} is already taken"
        return False, msg

    msg = "Account created succesfully"
    return True, msg