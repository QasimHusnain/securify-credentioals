# simple login system

data_base : list[tuple[str,int]] = [("qasim", "12345"),
                                ("aqib", "54321"),
                                ("ali", "12354"),
                                ("hussan", "2145"),
                                ("zain", "12098"),
                                ("zia", "98760")
                                ]
input_user_name : str = input('Enter user name')
input_user_password : str = input('Enter user password')

for newdata_base in data_base:  
    username, password = newdata_base
    if input_user_name.lower() == username.lower() and input_user_password == password: 
        print("Valid User")
        break                
else:
    print("Not found or Invalid user")
