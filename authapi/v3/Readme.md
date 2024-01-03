## CustomPermission class inherit from 

```
from rest_framework.permissions import BasePermission
```

###### Define either one or both method (return True to grant access)
```
has_permission(self, request, view)
```

```
has_object_permission(self, request, view, obj)
```