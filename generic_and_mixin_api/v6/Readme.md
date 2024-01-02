# This app has implementation of ReadOnlyModelViewset class in which following method we have:

### list - handle `get` method to list all

### Retrieve - handle `get` method



## DefaultRouter class handle all the urls according to request

```
router = DefaulRouter()
routewr.register("student", views.StudentReadOnlyModelViewSet, basname="student")
```


### After this we have include router in url_patterns like this:

```
url_patterns = [
    path("", include(router.urls), name="studentapi"),
]
```