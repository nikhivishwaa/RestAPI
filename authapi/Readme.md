## This Project includes the Secure API's


### Authentication Classes in `rest_framework.authentication`

###### BasicAuthentication

###### SessionAuthentication

###### TokenAuthentication

###### RemoteUserAuthentication

###### CustomAuthentication


### Permission Classes in `rest_framework.permissions`

###### AllowAny    - any one can access API

###### IsAuthenticated    - only authenticated user can access

###### IsAdminUser    - only staff member can access the API (isstaff is True)

###### IsAuthenticatedOrReadOnly    - if user is unauthenticated so it have read only permissions and after authentication user can be write 

###### DjangoModelPermissions     - django.contrib.auth permission default is read permission from mgiving more permission we have to give change permission to upadate, delete permission fer delete and add permission for create

###### DjangoModelPermissionsOrAnonReadOnly    - same as DjangoModelPermissions but have read only access to unauthenticated user

###### DjangoObjectPermissions     - objeact level permission for different models

###### Custom Permissions    - create own permission class as per the need

#