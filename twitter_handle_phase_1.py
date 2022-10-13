print("USER HANDLER")
def sp_char(password):
    sp_character=['!','@','#','$','%','^','&','*','/','-',',','.','?','{','}','[',']','<','>','\\']
    for val in password:
        if val in sp_character:
            print("password should consists of only'_'")
            input_password()
        else:
            is_alpha(password)
            break
        break
def is_alpha(password):
    if password[0].isalpha():
        length(password)
    else:
        print("password should start with alphabet")
        input_password()
def length(password):
    if (len(password)<8):
        print("password should contain minimum of 8 characters")
        input_password()
    else:
        print("WELCOME TO KWITTER")
        
        
        
            
def input_password():
    password=input("Enter password:")
    sp_char(password)
twitter_handlers=set()

def user_handle():
    first_name=input("Enter first name:")
    second_name=input("Enter second name:")
    first=first_name.capitalize()
    second=second_name.capitalize()
    twitter_handle="@"+first+second
    if twitter_handle in twitter_handlers:
        print("TRY SOME OTHER USER HANDLE!")
        user_handle()
    else:
        twitter_handlers.add(twitter_handle)
        print(twitter_handle)
        input_password()
        
while(True):
    print("Enter your choice:")
    print("1.Create user handle")
    print("2.Exit")
    choice=int(input())
    if choice==1:
        user_handle()
    elif choice==2:
        break
    

