def check_password_correct(login, password, sql_row_object):
    try:
        if len(sql_row_object) == 1 and sql_row_object[0]["login"] == login and sql_row_object[0]["password"] == password:
            return True
        else:
            return False
    except:
        return False


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


    if login in [row["login"] for row in logins]:
        msg = f"Name {login} is already taken"
        return False, msg

    msg = "Account created succesfully"
    return True, msg