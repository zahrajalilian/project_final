import files


class Profile:
    def __init__(self, username=None, full_name=None, email=None,
                 phone_number=None, bio=None):

        self.username = username
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.bio = bio

    @staticmethod
    def set_profiles(user):

        username = user.username
        full_name = ''
        email = ''
        phone_number = ''
        bio = ''
        profile = Profile(username, full_name=None, email=None, phone_number=None, bio=None)
        row_profile = [[username, full_name, email, phone_number, bio]]
        files.write_profile(row_profile)
        return profile

#