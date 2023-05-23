from rest_framework import viewsets, generics
from rest_framework.response import Response
from . import models
from . import serializers
from . import permissions


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostsViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsPostAuthor]
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        query_set = super().get_queryset()
        category = str(self.request.query_params.get('category')).lower()
        if category not in ['', 'null', 'false', None]:
            try:
                return query_set.filter(category__pk=category)
            except:
                return query_set

        return query_set

    # def update(self, request, *args, **kwargs):
    #     data_to_change = {}
    #     data_to_change['content'] = request.data.get("content")
    #     data_to_change['image'] = request.data.get("image")
    #     serializer = self.serializer_class(request.user, data=data_to_change, partial=True)
    #     if serializer.is_valid():
    #         self.perform_update(serializer)
    #
    #     return Response(serializer.data)


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

    def get_queryset(self):
        query_set = super().get_queryset()
        user = str(self.request.query_params.get('user')).lower()
        if user not in ['', 'null', 'false', None]:
            try:
                return query_set.filter(user__pk=user)
            except:
                return query_set

        return query_set



