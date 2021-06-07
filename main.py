import users
import posts
import comments
import files
import functions
import profiles
import logers

"""
import section
import users
import posts
import comments
import files
import functions
"""

########################################################################################################
#########################################################################################################

"""
user profile menu
"""
"""
profile part
set profile
see ure profile
"""


def profile_management(user):
    while True:
        chose = input('profile management \n'
                      '1-set profile\n'
                      '2-see profile\n'
                      '3-return to main menu\n'
                      'enter here :').strip()
        if chose == '1':
            users.User.update_profile(user)
        elif chose == '2':
            users.User.see_profile(user)
        elif chose == '3':
            break
        else:
            print('chose between 1-3')


########################################################################################################
########################################################################################################


"""
user post menu
"""
"""
post part
options:
add post
see ure posts
edit ure posts
comment
see comments
see all the posts from all users here
go to main menu

"""


def post_manage(user):
    while True:
        post_management = input('enter ure choice \n'
                                '1-add post\n'
                                '2-see ure posts\n'
                                '3-edit ure posts\n'
                                '4-delete post\n'
                                '5-comment\n'
                                '6-see comments\n'
                                '7-go to main menu\n'
                                'enter here :')
        if post_management == '1':
            try:
                posts.Post.add_post(user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong IN ADDING POST')
        elif post_management == '2':
            try:
                posts.Post.show_posts(user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong in showing posts')
        elif post_management == '3':
            try:
                posts.Post.show_posts(user)
                posts.Post.change_post(user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong in editing post')
        elif post_management == '4':
            try:
                post_delete = functions.chose_post_to_comment(user)
                functions.delete_post(post_delete)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong in deleting post')
        elif post_management == '5':
            try:
                post_comment = functions.chose_post_to_comment(user)
                comments.Comment.leave_comment(post_comment, user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong in leaving comment post')
        elif post_management == '6':
            try:
                item = functions.chose_post_to_comment(user)
                functions.see_comments(item)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong in reading comment post')
        elif post_management == '7':
            break
        else:
            print('chose between 1-7')


#####################################################################################################
#####################################################################################################


"""
connection menu
"""
""" 
follower list
following list
follow
unfollow
block

"""


def user_follow_managements(user):
    while True:
        chose_relation = input('enter ure choice \n'
                               '1-follower list\n'
                               '2-following list\n'
                               '3-follow\n'
                               '4-return to main menu :\n'
                               'enter here :').strip()
        if chose_relation == '1':
            functions.follower_list(user)
        elif chose_relation == '2':
            functions.following_list(user)
        elif chose_relation == '3':
            functions.follow(user)
        elif chose_relation == '4':
            break
        else:
            print('chose between 1-4')


######################################################################################################
#####################################################################################################

def others(user):
    chose_user = functions.chose_users(user)
    while chose_user:
        chose = input('please chose:\n'
                      '1-see user profile\n'
                      '2-see user posts\n'
                      '3-leave comment\n'
                      '4-return to main menu\n'
                      'Enter here:')

        if chose == '1':
            try:
                functions.read_profile_users(chose_user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong ')
        elif chose == '2':
            functions.read_posts_users(chose_user)
        elif chose == '3':
            try:
                chose_post_to_commit = functions.chose_post_to(chose_user)
                comments.Comment.leave_comment(chose_post_to_commit, user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong ')
        elif chose == '4':
            break
        else:
            print('please chose between 1-4')


########################################################################################################################
########################################################################################################################


"""
public section
"""
"""
options:
see posts from all the other users
leave comment for posts
see comments of posts
see all the comments from all posts
"""


def all_users(user):
    while True:
        chose = input('Enter\n'
                      '1-see posts\n'
                      '2-leave comment for posts\n'
                      '3-see comments of posts\n'
                      '4-see all the comments from all posts\n'
                      '5-return to main menu\n'
                      'Enter here:')
        if chose == '1':
            files.show_all_users_posts()
        elif chose == '2':
            try:
                chose_post_commit = functions.comment_from_public_menu()
                comments.Comment.leave_comment(chose_post_commit, user)
            except Exception:
                print('sth went wrong')
                logers.logger.debug('something went wrong in seeing posts')
        elif chose == '3':
            try:
                chose_to_see_comments = functions.comment_from_public_menu()
                files.read_comments(chose_to_see_comments)
            except Exception :
                print('sth went wrong')
                logers.logger.debug('something went wrong in leaving comment post')
        elif chose == '4':
            functions.see_all_comments()
        elif chose == '5':
            break
        else:
            print('chose between 1-5')


########################################################################################################################
########################################################################################################################
"""
main menu for users
options:
sign up
sign in

"""
"""
user main menu
options:
profile
post
connections
others
all users
change password
log out 
"""


def register():
    try:
        user = users.User.sign_up()
        profiles.Profile.set_profiles(user)
    except Exception:
        print('something went wrong try again')
        logers.logger.debug('something went wrong in sign up')

def enter():
    while True:
        enter_account = input('chose\n'
                              '1-sign up\n'
                              '2-sign in\n'
                              'Enter here:').strip()
        if enter_account == '1':
            register()

        elif enter_account == '2':
            user = users.User.sign_in()
            while user:
                options = input('menu:\n'
                                '1-profile\n'
                                '2-post\n'
                                '3-connections\n'
                                '4-others\n'
                                '5-public\n'
                                '6-change password\n'
                                '7-log out \n'
                                'please enter the number here:').strip()

                if options == '1':
                    profile_management(user)
                elif options == '2':
                    post_manage(user)
                elif options == '3':
                    user_follow_managements(user)
                elif options == '4':
                    others(user)
                elif options == '5':
                    all_users(user)
                elif options == '6':
                    users.User.change_password(user)
                elif options == '7':
                    break
                else:
                    print('please chose between 1-7!!!!!!!!!!!!')


print('Welcome  would you like to Enter :')

enter()
