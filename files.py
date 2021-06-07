"""import section:
csv
pandas as pd
import datetime
"""

import csv
import pandas as pd
import datetime
import re
########################################################################################################################
########################################################################################################################
"""
paths:
account_path 
profile_path  
posts_path 
comments_path
"""
account_path = './project_files/accounts.csv'
profile_path = './project_files/profile.csv'
posts_path = './project_files/posts.csv'
comments_path = './project_files/comments.csv'
friends_path = './project_files/friends.csv'
#######################################################################################################################
#######################################################################################################################
"""
profile functions
profile_path = 'profile.csv'
1-write profiles
2-read profiles
3-update profiles
4-delete profiles
"""
"""
1
"""


def write_profile(row_profile):
    with open(profile_path, 'a', newline='') as profile_csv:
        profile_writer = csv.writer(profile_csv)
        profile_writer.writerows(row_profile)


"""
2
"""


def read_profile(item):
    file = open(profile_path)
    df_profile = pd.read_csv(file)
    for index, row in df_profile.iterrows():
        if row['username'] == item.username:
            print(f"FullName : {row['full_name']} \n"
                  f"username : {row['username']} \n"
                  f"Email : {row['email']} \n"
                  f"PhoneNumber : {row['phone_number']} \n"
                  f"Bio : {row['bio']} \n")


"""
3
"""


def update_profile(user):
    update_profiles = pd.read_csv(profile_path)
    location = 0
    with open(profile_path, 'r') as my_profile:

        csv_reader = csv.DictReader(my_profile)
        for row in csv_reader:
            if row['username'] == user.username:
                while True:
                    profile_menu = input('please set ure profile :\n'
                                         '1-set Fullname\n'
                                         '2-set Email\n'
                                         '3-set phoneNumber\n'
                                         '4-set Bio\n'
                                         '5-return to profile menu\n'
                                         'Enter here :').strip()
                    if profile_menu == '1':
                        fullname = input('Enter FullName:')
                        row['full_name'] = fullname
                        print('ure FullName changed')
                        update_profiles.loc[location, 'full_name'] = fullname
                        update_profiles.to_csv(profile_path, index=False)

                    elif profile_menu == '2':
                        email_format = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                        while True:
                            print('please Enter a  valid email address')
                            email = input('phoneNumber:')
                            if not re.search(email_format, email):
                                print('the phone number pattern incorrect Enter again')
                            else:
                                row['email'] = email
                                print('ure Email changed')
                                update_profiles.loc[location, 'email'] = email
                                update_profiles.to_csv(profile_path, index=False)
                                break
                    elif profile_menu == '3':
                        phone_number_format = '^09[\d]{9}$'
                        while True:
                            print('please Enter a 11 digit number that start with  09')
                            phone_number = input('phoneNumber:')
                            if not re.search(phone_number_format, phone_number):
                                print('the phone number pattern incorrect Enter again')
                            else:
                                row['phone_number'] = phone_number
                                print('ure phone_number changed')
                                update_profiles.loc[location, 'phone_number'] = phone_number
                                update_profiles.to_csv(profile_path, index=False)
                                break
                    elif profile_menu == '4':
                        bio = input('Enter Bio:')
                        row['bio'] = bio
                        print('ure Bio changed')
                        update_profiles.loc[location, 'bio'] = bio
                        update_profiles.to_csv(profile_path, index=False)
                    elif profile_menu == '5':
                        break
                    else:
                        print('chose between 1-5')
            location += 1


#######################################################################################################################
#######################################################################################################################

"""
posts functions
posts_path = 'posts.csv'
1-write posts
2-read posts
3-update posts
4-delete posts
"""
"""1"""


def write_post(row_post):
    with open(posts_path, 'a', newline='') as post_csv:
        post_writer = csv.writer(post_csv)
        post_writer.writerows(row_post)


"""2"""


def read_posts(item):

    file_ = open(posts_path)
    df_posts = pd.read_csv(file_)
    for index, row in df_posts.iterrows():
        if row['username'] == item.username:
            print(f"in : {row['date']} \n"
                  f"username : {row['username']} \n"
                  f"posted : {row['text']} \n"
                  f"with ID : {row['post_id']} \n")


"""
3
"""


def update_posts(user):
    update_post = pd.read_csv(posts_path)
    location = 0
    post_id = input('Enter the post id here:')
    with open(posts_path, 'r') as my_posts:
        csv_reader = csv.DictReader(my_posts)
        for row in csv_reader:
            if row['username'] == user.username and row['post_id'] == post_id:
                text = input('Enter text:')
                row['text'] = text
                print(f' you changed ure post text in {datetime.datetime.now()}')
                update_post.loc[location, 'text'] = text
                update_post.to_csv(posts_path, index=False)

            location += 1

#######################################################################################################################
#######################################################################################################################


"""
show all the posts from all users
"""


def show_all_users_posts():
    file_ = open(posts_path)
    df_posts = pd.read_csv(file_)
    for index, row in df_posts.iterrows():
        print(f"in : {row['date']} \n"
              f"username : {row['username']} \n"
              f"posted : {row['text']} \n"
              f"with ID : {row['post_id']} \n")

#######################################################################################################################
#######################################################################################################################


"""
comments functions
posts_path = 'comments.csv'
1-write comments
2-read comments
3-update comments
4-delete comments
"""

"""
1
"""


def write_comments(row_comment):
    with open(comments_path, 'a', newline='') as comment_csv:
        comment_writer = csv.writer(comment_csv)
        comment_writer.writerows(row_comment)


"""
2
"""
"""
read comments of a specific post
"""

def read_comments(item):
    file_ = open(comments_path)
    df_comments = csv.DictReader(file_)
    for row in df_comments:
        if row['post_id'] == item:
            print(f"in : {row['date']} \n"
                  f"username : {row['username']} \n"
                  f"commented : {row['comment_text']} \n"
                  f"with ID : {row['post_id']} \n")



