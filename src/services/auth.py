from models.user import User

def find_account_by_username(username: str) -> User:
    #if the owner exist this will return a User 
    user = User.objects(username=username).first()
    return user
def find_account_by_password(password: str) -> User:
    user = User.objects(password=password).first()
    return user