
import users
import files
import functions


class Post(users.User):

    def __init__(self, date, post_id, text=None, username=None):
        """

        :param date: datetime
        :param post_id: post id
        :param text: text of the post
        :param username: username of the person who posted
        """
        super().__init__(username, password=None, profile=None)
        self.text = text
        self.post_id = post_id
        self.date = date
        self.username = username
        self.comments_count = 0
        self.comments_list = []


    """
    a static method to show posts
    """
    @staticmethod
    def show_posts(user):
        files.read_posts(user)

    """
    a method to update posts ==>text of the posts
    """
    @staticmethod
    def change_post(user):
        files.update_posts(user)

    """
    a method to add posts
    """
    @staticmethod
    def add_post(user):
        post_id = functions.check_post_id()
        date = files.datetime.datetime.now()
        text = input('enter text :')
        username = user.username
        post = Post(date, text, username)
        users.User.users_posts.append(post)
        user.post_list.append(post)
        row_post = [[date, post_id, text, username]]
        files.write_post(row_post)
        return post

