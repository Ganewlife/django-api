from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from core.user.serializers import UserSerializer
from core.abstract.viewsets import AbstractViewSet
from core.user.models import User
from rest_framework.permissions import IsAuthenticated


# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(AbstractViewSet):
    http_method_names = ('patch', 'get') # methode GET and PUT
    # permission_classes = (AllowAny,) # toutes permission accordée for anybody
    permission_classes = (IsAuthenticated,) # toutes permission accordée for anybody
    serializer_class = UserSerializer
    def get_queryset(self): # a list of all the users. This method will be called when /user/ is hit with a GET request
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self): # to get one user. This method is called when GET or PUT request is made on the /user/id/ endpoint, with id representing the ID of the user
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj