##### Install simple jwt package

```
pip install djangorestframework-simplejwt
```

###### import simplejwt views

```
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 
```

```
urlpatterns = [
    path("gettoken/", TokenObtainPairView.as_view(), name='generate_token'),
    path("refreshtoken/", TokenObtainPairView.as_view(), name='refresh_token'),
    path("verifytoken/", TokenObtainPairView.as_view(), name='verify_token')
]
```

###### Generate Token

```
http POST http://127.0.0.1:5600/gettoken/ username=<USERNAME> password=<PASSWORD>
```

###### Apply authentication to api

```
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class XYZViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
```

###### Access JWT Protected Api

```
http GET http://127.0.0.1:5600/api/students/ 'Authorization:Bearer <JWT_TOKEN>'
```