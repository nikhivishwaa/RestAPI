#### Generate Token through Signals


###### When the user is registered generate its token

```
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

###### GET request by httpie
```
http http://127.0.0.1:8000/api/v6/students/ 'Authorization:Token YOUR_AUTH_TOKEN'
```

###### POST request by httpie
```
http -f POST http://127.0.0.1:8000/api/v6/students/ name=Jay roll=114 city=Sehore 'Authorization:Token YOUR_AUTH_TOKEN'
```

###### PUT request by httpie
```
http PUT http://127.0.0.1:8000/api/v6/students/8/ name='Jay Singh' roll=114 city=Sehore 'Authorization:Token YOUR_AUTH_TOKEN'
```

###### PATCH request by httpie
```
http PATCH http://127.0.0.1:8000/api/v6/students/8/ roll=115 'Authorization:Token YOUR_AUTH_TOKEN'
```

###### DELETE request by httpie
```
http DELETE http://127.0.0.1:8000/api/v6/students/8/ 'Authorization:Token YOUR_AUTH_TOKEN'
```