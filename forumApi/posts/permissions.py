from rest_framework import permissions


class IsPostAuthor(permissions.BasePermission):

    message = 'Not an author'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.creator


class IsUserProfileOwner(permissions.BasePermission):

    message = "You can't change other users profiles!"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.user