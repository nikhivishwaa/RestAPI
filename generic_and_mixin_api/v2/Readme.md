# This app has implementation of GenericAPIView class and Mixin classes such as

### ListModelMixin - have list method
```
list(request, *args, **kwargs)
```

### RetrieveModelMixin - have retrieve method
```
retrieve(request, *args, **kwargs)
```

### CreateModelMixin - have create method
```
create(request, *args, **kwargs)
```

### UpdateModelMixin- have update and update_partial method
```
update(request, *args, **kwargs)
```

###### above method can handle partial update if `partial = True` in kwargs
```
partial_update(request, *args, **kwargs)
```

### DestroyModelMixin - have destroy method
```
destroy(request, *args, **kwargs)
```

