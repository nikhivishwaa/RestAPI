# This app has implementation of Viewset class in which following method we have to define following methods

### list - handle `get` method to list all

### create - handle `post` method

### Retrieve - handle `get` method

### Update - handle `put` method

### partial_update - handle `patch` method

### destroy - handle `delete` method



## DefaultRouter class handel all the urls according to request

```
router = DefaulRouter()
routewr.register("student", views.StudentViewSet, basname="student")
```


### After this we have include router in url_patterns like this:

```
url_patterns = [
    path("", include(router.urls), name="studentapi"),
]
```