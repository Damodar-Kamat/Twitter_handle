from datetime import date
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
        print("WELCOME",user_handle.twitter_handle)
        
        
        
            
def input_password():
    password=input("Enter password: ")
    sp_char(password)
    
twitter_handlers=set()

def user_handle():
    first_name=input("Enter first name: ")
    second_name=input("Enter second name: ")
    first=first_name.capitalize()
    second=second_name.capitalize()
    user_handle.twitter_handle="@"+first+second
    if user_handle.twitter_handle in twitter_handlers:
        print("TRY SOME OTHER USER HANDLE!")
        user_handle()
    else:
        twitter_handlers.add(user_handle.twitter_handle)
        print(user_handle.twitter_handle)
        input_password()
        
follower1=set()


def follower_1():
    follower_1.user1=input("Enter your user handle : ")
    if follower_1.user1 not in twitter_handlers:
        print("INVALID USER HANDLE")
        follower_1()
    else:
        user_1()
def user_1():
    follower=input("Enter the user handle you want to follow : ")
    if follower==follower_1.user1:
        print("YOU CANNOT FOLLOW YOURSELF")
        user_1()
    elif follower not in twitter_handlers:
        print("INVALID USER HANDLE")
        user_1()
    elif follower in follower1:
        print("ALREADY YOUR ARE FOLLOWING",follower)
        follower_2()
    else:
        follower1.add(follower)
        print(follower_1.user1,"IS NOW FOLLOWING",follower)
        str=input("DO YOU WANT TO FOLLOW OTHER USER HANDLE(Y/N) : ")
        if str=="Y" or str=="y":
            user_1()
        elif str=="N" or str=="n":
            str1=input("DO YOU WANT TO FOLLOW HANDLE USING OTHER USER HANDLE(Y/N) :")
            follower_2()
        else:
            print("INVALID INPUT")
        
follower2=set()
def follower_2():
    follower_2.user2=input("Enter the user handle : ")
    if follower_2.user2 not in twitter_handlers:
        print("INVALID USER HANDLE")
        follower_2()
    else:
        user_2()
def user_2():
    follower=input("Enter the user handle you want to follow : ")
    if follower==follower_2.user2:
        print("YOU CANNOT FOLLOW YOURSELF")
        user_2()
    elif follower not in twitter_handlers:
        print("INVALID USER HANDLE")
        user_2()
    if follower in follower2:
        print("ALREADY YOUR ARE FOLLOWING",follower)
        follower_2()
    else:
        follower2.add(follower)
        print(follower_2.user2,"IS NOW FOLLOWING",follower)
        str=input("DO YOU WANT TO FOLLOW OTHER USER HANDLE(Y/N) : ")
        if str=="Y" or str=="y":
            user_2()
        else:
            pass
        
        
def display():
    display1=input("Enter the user handle for which follower list must be displayed : ")
    if display1 in twitter_handlers and display1==follower_1.user1:
        print(follower1)
    elif display1 in twitter_handlers and display1==follower_2.user2:
        print(follower2)
    else:
        print("INVALID USER HANDLE")
        display()
    
def mutual():
    user1=input("Enter the user handle 1 : ")
    user2=input("Enter the user handle 2 : ")
    if user1 in twitter_handlers and user2 in twitter_handlers and user1==follower_1.user1 and user2==follower_2.user2:
        print("MUTUAL FRIENDS OF",user1,"AND",user2,(follower1).intersection(follower2))
    else:
        print("INVALID USER HANDLE")
    
def count():
    count1=input("Enter the user handle : ")
    if count1 in twitter_handlers and count1==follower_1.user1:
        print("the count of the followers of",count1)
        print(len(follower1))
        if len(follower1)>10:
            print("The user handle",count1,"has more than 10 followers")
    elif count1 in twitter_handlers and count1==follower_2.user2:
        print("the count of the followers of",count1)
        print(len(follower2))
        if len(follower2)>10:
            print("The user handle",count1,"has more than 10 followers")
    else:
        print("INVALID USER HANDLE")
        display()

post1=[]
post2=[]
post3=[]
tag1 = []
tag2 = []
tag3 = []
def post():
    user=input("enter your user_handle :")
    if user in twitter_handlers and user==follower_1.user1:
        today = date.today()
        print("Post for Today's date:", today)
        post = input("Enter your post :")
        post1.append(post)
        t = post.split( )
        x=input("enter the user_handle which you want to tag :")
        if x in follower1:
            tag1.append(x)
                                
                    
        any(x in post1 for x in post2)              #reposting
        any(x in post1 for x in post3)

                                
        print("Your taged handel are :-",tag1)
        print("Your total post is :" , len(post1))
        print("Post are :")
        print(', '.join(post1))
        print(', '.join(post2))
        print(', '.join(post3))
    elif user in twitter_handlers and user==follower_2.user2:
        today = date.today()
        print(" Post for Today's date:", today)
        post = input(" Enter your post : ")
        post2.append(post)
        t = post.split( )
        x=input("enter the user_handle which you want to tag :")
        if x in follower2:
            tag2.append(x)
                    
        any(x in post2 for x in post1)             #reposting
        any(x in post2 for x in post3)
                            
                
        print("Your taged handel are :-",tag2)
        print("Your total post is :" , len(post2))
        print("Post are :")
        print(', '.join(post1))
        print(', '.join(post2))
        print(', '.join(post3))
                    
                   
                
    else:
        print(" \ninvalid user_handle!!")                   

def taged():
        user=input("enter user_handle :")
        if user in twitter_handlers and user==follower_1.user1:
            print("Your taged handel are :-",tag1)
            print("Your total post is :" , len(post1))
            print("Post are :")
            print(', '.join(post1))
            print(', '.join(post2))
            print(', '.join(post3))
        elif user in twitter_handlers and user==follower_2.user2:
            print("Your taged handel are :-",tag2)
            print("Your total post is :" , len(post2))
            print("Post are :")
            print(', '.join(post1))
            print(', '.join(post2))
            print(', '.join(post3))
        else:
            print("invalid user_handle!!")
        
                            
while(True):
    print("Enter your choice: ")
    print("1.Create user handle")
    print("2.To follow other twitter_handle")
    print("3.Display the followers")
    print("4.Display mutual followers")
    print("5.number of followers for specific twitter_handle")
    print("6.post something or repost something")
    print("7.user_handles  taged")
    print("10.Exit")
    choice=int(input())
    if choice==1:
        user_handle()
    elif choice==2:
        follower_1()
    elif choice==3:
        display()
    elif choice==4:
        mutual()
    elif choice==5:
        count()
    elif choice==6:
        post()
    elif choice==7:
        taged()
    elif choice==10:
        break







