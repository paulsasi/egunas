from django.contrib.auth.models import User
from django.contrib.auth import authenticate

print('Creating user')

# Create user
#user = User.objects.create_user('josebva', 'lennon@thebeatles.com', '1234567')
#user.save()

print('User created')

# Authenticate user
user = authenticate(username='josebva', password='1234567')

if user is not None:
    print('User authenticated')

else:
    print('Wrong user name or password')


