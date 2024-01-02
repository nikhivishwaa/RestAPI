## This App implements BasicAuthentication for Secure API's

#### Username and Password required to Authenticate

```
from rest_framework.authentications import BasicAuthentication
```

#### With IsAuthenticated Permission class
```
from rest_framework.permissions import IsAuthenticated
```



#### Setup Global Authentication and Permission Class

###### Put this snippet inside your settings.py
```
REST_FRAMEWORK = {
    PERMISSION_CLASSES = [
        rest_framework.permissions.IsAuthenticated
    ],
    AUTHENTICATION_CLASSES = [
        rest_framework.authentication.BasicAuthentication
    ]
}
```