import posts
import files
import datetime


class Comment(posts.Post):

    def __init__(self, date, comment_text, post_id=None, username=None):
        super().__init__(date, post_id, username=None, text=None)
        self.comment_text = comment_text
        self.post_id = post_id
        self.username = username

    @staticmethod
    def leave_comment(post_id, user):
        date = datetime.datetime.now()
        post_id = post_id
        comment_text = input('enter ure comment here:')
        username = user.username
        comment = Comment(date, post_id, comment_text, username)
        row_comments = [[date, post_id, comment_text, username]]
        files.write_comments(row_comments)
        return comment

