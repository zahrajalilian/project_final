"""
import section
"""

import files
# import csv

#####################################################################################################################
######################################################################################################################

"""
here we chose a post we like 
"""


def chose_post_to(item):
    path_file = files.posts_path
    file_post_to_commit = open(path_file)
    df_post_ = files.pd.read_csv(file_post_to_commit)
    for index, row in df_post_.iterrows():
        if row['username'] == item:
            print(f"in : {row['date']} \n"
                  f"username : {row['username']} \n"
                  f"posted : {row['text']} \n"
                  f"with ID : {row['post_id']} \n")
    list_id_posts = list(df_post_['post_id'])
    while True:
        chose_post = int(input('chose the ID of the post  :'))
        if chose_post in list_id_posts:
            return chose_post
        else:
            print('some thing went wrong enter again')

# path_file = files.posts_path
# df_id_posts = files.pd.read_csv(path_file)
# list_id_posts = list(df_id_posts['post_id'])
# print(list_id_posts)
# while True:
#     id_post = int(input('enter here:'))
#     if id_post in list_id_posts:
#         print('the post id already exist')
#     else:
#         return id_post
#######################################################################################################################
########################################################################################################################


"""
for all users menu
"""


def chose_post_to_comment(item):
    path_file = files.posts_path
    file_post_to_commit = open(path_file)
    df_post_ = files.pd.read_csv(file_post_to_commit)
    for index, row in df_post_.iterrows():
        if row['username'] == item.username:
            print(f"in : {row['date']} \n"
                  f"username : {row['username']} \n"
                  f"posted : {row['text']} \n"
                  f"with ID : {row['post_id']} \n")
    chose_post_t_c = input('chose the ID from IDs  :')
    with open(path_file) as my_posts:
        csv_reader = files.csv.DictReader(my_posts)
        for row in csv_reader:
            if row['post_id'] == chose_post_t_c:
                print(f'you chose {chose_post_t_c}')
                return chose_post_t_c

########################################################################################################################
########################################################################################################################
########################################################################################################################
#
# def chose_post_to_comment(item):
#     path_file = files.posts_path
#     file_post_to_commit = open(path_file)
#     df_post_ = files.pd.read_csv(file_post_to_commit)
#     for index, row in df_post_.iterrows():
#         if row['username'] == item.username:
#             print(f"in : {row['date']} \n"
#                   f"username : {row['username']} \n"
#                   f"posted : {row['text']} \n"
#                   f"with ID : {row['post_id']} \n")
#     # chose_post_t_c = input('chose the ID from IDs  :')
#     list_id_posts = list(df_post_['post_id'])
#     while True:
#         chose_post = int(input('chose the ID of the post  :'))
#         if chose_post in list_id_posts:
#             return chose_post
#         else:
#             print('some thing went wrong enter again')
#

######################################################################################################################


"""
here we chose a post we like to comment on from public menu
"""


def comment_from_public_menu():
    path_posts = files.posts_path
    file_post_to_commit = open(path_posts)
    df_posts = files.pd.read_csv(file_post_to_commit)
    for index, row in df_posts.iterrows():
        print(f"in : {row['date']} \n"
              f"username : {row['username']} \n"
              f"posted : {row['text']} \n"
              f"with ID : {row['post_id']} \n")
    chose_posts = input('chose the ID from IDs   :')
    with open(path_posts) as my_posts:
        csv_reader = files.csv.DictReader(my_posts)
        for row in csv_reader:
            if row['post_id'] == chose_posts:
                print(f'you chose {chose_posts}')
                return chose_posts


"""
this function shows all comments for all posts
"""

"""
works
"""


def see_all_comments():
    comments_path = files.comments_path
    file_ = open(comments_path)
    df_comments = files.pd.read_csv(file_)
    for index, row in df_comments.iterrows():
        print(f"in : {row['date']} \n"
              f"username : {row['username']} \n"
              f"commented : {row['comment_text']} \n"
              f"for post with ID : {row['post_id']}")


########################################################################################################################
########################################################################################################################


"""
see comment for a specific post by post id
"""
"""
problem maker
"""


def see_comments(item):
    comments_path = files.comments_path
    file_ = open(comments_path)
    df_comments = files.csv.DictReader(file_)
    for row in df_comments:
        if row['post_id'] == item:
            print(f"in : {row['date']} \n"
                  f"username : {row['username']} \n"
                  f"commented : {row['comment_text']} \n"
                  f"for post with ID : {row['post_id']}")
        else:
            print('some thing wrong')
########################################################################################################################
########################################################################################################################


"""
show all the posts from all users
"""


def show_all_users_posts():
    file_ = open(files.posts_path)
    df_posts = files.pd.read_csv(file_)
    print(df_posts)


###########################################################################################################
###########################################################################################################

"""
 chosen user to work with
"""

"""
here we chose a user from all users to work with
"""


def chose_users(user):
    df_post = files.pd.read_csv(files.account_path)
    list_username = list(df_post['username'])
    print(list_username)
    chose_user = input('chose the user')
    with open(files.account_path) as my_accounts:
        csv_reader = files.csv.DictReader(my_accounts)
        for row in csv_reader:
            if row['username'] == chose_user and row['username'] != user.username:
                print(f'you chose {chose_user}')
                return chose_user
        else:
            print('chose another username')


"""
here we can see the profile of the user we chose
"""


def read_profile_users(item):
    file = open(files.profile_path)
    df_profile = files.pd.read_csv(file)
    for index, row in df_profile.iterrows():
        if row['username'] == item:
            print(f"FullName : {row['full_name']} \n"
                  f"username : {row['username']} \n"
                  f"Email : {row['email']} \n"
                  f"Bio : {row['bio']} \n")


"""
here we can see the  posts of the user we chose
"""


def read_posts_users(item):

    file_ = open(files.posts_path)
    df_posts = files.pd.read_csv(file_)
    for index, row in df_posts.iterrows():
        if row['username'] == item:
            print(f"in : {row['date']} \n"
                  f"username : {row['username']} \n"
                  f"posted : {row['text']} \n"
                  f"with ID : {row['post_id']} \n")
##################################################################################################################


def check_post_id():
    path_file = files.posts_path
    df_id_posts = files.pd.read_csv(path_file)
    list_id_posts = list(df_id_posts['post_id'])
    print(list_id_posts)
    while True:
        id_post = int(input('enter here:'))
        if id_post in list_id_posts:
            print('the post id already exist')
        else:
            return id_post


"""
check username
"""


def check_username():
    path_file = files.account_path
    df_usernames = files.pd.read_csv(path_file)
    list_usernames = list(df_usernames['username'])
    while True:
        username = input('enter username here:')
        if username in list_usernames:
            print('the username already exist')
        elif username == '':
            print('please make sure to enter ure username')
        else:
            return username

#####################################################################################################################
###########################

def follow(user):
    path = files.account_path
    df_users = files.pd.read_csv(path)
    list_usernames = list(df_users['username'])
    print(list_usernames)
    while True:
        following = input('enter username here:')
        if following in list_usernames and following != user.username:
            with open(files.friends_path, 'a', newline='') as friend_csv:
                profile_writer = files.csv.writer(friend_csv)
                row = [[following, user.username]]
                profile_writer.writerows(row)
                break
        elif following == '':
            print('please make sure to enter the username')
        else:
            print('something went wrong')

#######################################

def follower_list(user):
    path = files.friends_path
    df_users = files.pd.read_csv(path)
    for index, row in df_users.iterrows():
        if row['following'] == user.username:
            print(f" follower : {row['follower']} \n")

###########################

def following_list(user):
    path = files.friends_path
    df_users = files.pd.read_csv(path)
    for index, row in df_users.iterrows():
        if row['follower'] == user.username:
            print(f" following : {row['following']} \n")
##########################################################################################
def delete_post(post_to_delete):
    lines = list()
    with open(files.posts_path, 'r') as readFile:
        reader = files.csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == post_to_delete:
                    lines.remove(row)
    with open(files.posts_path, 'w') as writeFile:
        writer = files.csv.writer(writeFile)
        writer.writerows(lines)
############################################################################################
# def unfollow(user):
#     path = files.account_path
#     df_users = files.pd.read_csv(path)
#     user_to_unfollow = list(df_users['username'])
#     print(user_to_unfollow)
#     lines = list()
#     with open(files.posts_path, 'r') as readFile:
#         reader = files.csv.reader(readFile)
#         for row in reader:
#             lines.append(row)
#             for following, follower in row:
#                 if following == user_to_unfollow and follower == user.username:
#                     lines.remove(row)
#     with open(files.posts_path, 'w') as writeFile:
#         writer = files.csv.writer(writeFile)
#         writer.writerows(lines)