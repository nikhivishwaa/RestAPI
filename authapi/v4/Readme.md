## TokenAuthentication


###### In `setting.py` add following app into installed apps

```
'rest_framework.authtoken'
```

###### To test the Token Authenticaton we need CLI tools such as curl, httpie

###### httpie request format
```
http flag METHOD URL [list[list]]
```

```
http http://127.0.0.1:8000/api/v6/students/ 'Authorization:Token YOUR_TOKEN_HERE'
```


##### Methods to Generate Token

###### 1. Generate from Admin Panel

###### 2. Generate from DRF CLI

```
python manage.py drf_create_token USERNAME
```

###### Same Command is used to view existing token


###### 3. By exposing an API endpoint

```
from rest_framework.authtoken.views import obtain_auth_token
```

```
urlpatterns = [
    path('register/', obtain_auth_token),
]
```

###### Get httpie package 
```
pip install httpie
```


###### Use httpie to Create or retrieve token

```
http POST http://127.0.0.1:8000/api/v4/register/ username="user" password="xyz@123."
```