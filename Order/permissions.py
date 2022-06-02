from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Only for view - GET
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only author can change - PUT
        return obj.author == request.user
