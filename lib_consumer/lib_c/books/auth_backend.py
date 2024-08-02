from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.conf import settings


class MasterPasswordBackend(ModelBackend):
    # def authenticate(self, request, username, password, **kwargs):
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return None
    #     if user.check_password(password) and self.user_can_authenticate(user):
    #         return user

    #     return None
        
    def user_can_authenticate(self, user):
        return user.username.startswith('hillel_')
    
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
