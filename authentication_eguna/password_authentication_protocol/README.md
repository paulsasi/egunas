# PAP in Django

**User** objects are the core of authentication system in Django. A User represents the people itneracting with the system. Only one class of user exists in Django's authentication framework. Superusers or admin users are just regultar users with special attribute set, not different classes of user objects. The primary attributes of the default user are: username, password, email, first_name, last_name. 

Users are created with tue **create_user()** function:

```python
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'j@gmail.com', 'password')
user.last_name = 'Lennon'
user.save()
```


Django does not store raw (clear text) password on the user model, but only a hash. Django uses PBKDF2 by default. The password attribute of a User object is a strign of this format:

```
<algorithm>$<iterations>$<salt>$<hash>
```
