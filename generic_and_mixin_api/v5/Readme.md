# This app has implementation of ModelViewset class in which following method we have

### list - handle `get` method to list all

### create - handle `post` method

### Retrieve - handle `get` method

### Update - handle `put` method

### partial_update - handle `patch` method

### destroy - handle `delete` method


##### No need to define above methods they are already defined



## DefaultRouter class handel all the urls according to request

```
router = DefaulRouter()
routewr.register("student", views.StudentModelViewSet, basname="student")
```


### After this we have include router in url_patterns like this:

```
url_patterns = [
    path("", include(router.urls), name="studentapi"),
]
```