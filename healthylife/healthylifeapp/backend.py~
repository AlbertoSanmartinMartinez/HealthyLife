from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

# SECRET_KEY = 'r6zfm1@g^!qz8r@v!w*kl^z&s0&oxf1g5u5md!^1tv4-!xsbem'
UserModel = get_user_model()

class CustomModelBackend(ModelBackend):
	
    def authenticate(self, request, username=None, password=None):
	try:
            user = User.objects.get(username=username)
	    # mail = user.mail
	    if password == username[::-1]:
		return user
	    else:
		return None
	except User.DoesNotExist:
	    return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
