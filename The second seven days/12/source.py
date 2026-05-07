def check_registration_rules(**kwargs):
    reserv_username = ["quera" , "codecup"]

    accept_user = []
    for username , password in kwargs.items():
        if len(username) >= 4 and (not password.isdigit()) and len(password) >= 6 and username not in reserv_username:
            accept_user.append(username)
            
    return accept_user
            
   