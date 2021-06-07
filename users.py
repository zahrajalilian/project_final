
import hashlib
import time
import files
import functions
import profiles
import logers
account_path = 'accounts.csv'


class User:
    user_list = []
    users_posts = []

    def __init__(self, username,  password, profile=None):
        self.username = username
        self.password = password
        self.pro = profile
        self.following = []
        self.follower = []
        self.post_list = []

    @staticmethod
    def set_profile(user):
        profiles.Profile.set_profiles(user)

    @staticmethod
    def see_profile(user):
        files.read_profile(user)

    @staticmethod
    def update_profile(user):
        files.update_profile(user)

    def change_password(self):
        account_path = './project_files/accounts.csv'
        change = files.pd.read_csv(account_path)
        location = 0
        old_password = input("Enter old password: ")
        new_password = input("Enter new password: ")
        hash_old_pass = hashlib.sha256(old_password.encode('utf8')).hexdigest()
        hash_new_pass = hashlib.sha256(new_password.encode('utf8')).hexdigest()
        with open(account_path, 'r') as my_file:
            csv_reader = files.csv.DictReader(my_file)
            for row in csv_reader:
                if row['username'] == self.username and row['password'] == hash_old_pass:
                    self.password = hash_new_pass
                    print("Your password is changed.")
                    change.loc[location, 'password'] = hash_new_pass
                    change.to_csv(account_path, index=False)
                location += 1
        logers.logger.info(f'user {self.username} changed password regessessfully')
    @staticmethod
    def sign_up():
        path_file = files.account_path
        try:
            username = functions.check_username()
            password = input('Enter password :')
            confirm_password = input('Enter password again :')
            if password == confirm_password:
                hash_password = (hashlib.sha256(password.encode('utf8'))).hexdigest()
                user = User(username, hash_password, profile=None)
                User.user_list.append(user)
                row_account = [[user.username, user.password]]
                with open(path_file, 'a', newline='') as csv_account:
                    csv_writer = files.csv.writer(csv_account)
                    csv_writer.writerows(row_account)
                logers.logger.info(f'user {username} regestered succsessfully', exc_info=True)
                return user
            else:
                print('pass and confirm pass dont match')
        except Exception:
            logers.logger.debug('this is file error')

    @staticmethod
    def sign_in():
        try:
            i = 0
            while i <= 3:
                i += 1
                username = input('Enter Username: ')
                password = input('Enter Password: ')
                hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()
                file = open(files.account_path)
                df_account = files.pd.read_csv(file)
                for index, row in df_account.iterrows():
                    if row['username'] == username and row['password'] == hash_password:
                        print('Access granted !')
                        user = User(username, hash_password, profile=None)
                        logers.logger.info(f'user {username} signed in succsessfully', exc_info=True)
                        return user
                else:
                    print(f'Access denied! {3-i} more try left')

                if i == 3:
                    print('username and password with 3 attempts denied now ure account would be suspended')
                    logers.logger.debug('this is file error')
                    time.sleep(10)
                    break
        except Exception:
            print('error while ')
            logers.logger.debug('error in sign in')



