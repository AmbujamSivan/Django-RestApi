from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their own profile"""
    """ Object-level permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        #""" Check if it is their own profile"""
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allows the user to update thair own status"""

    def has_object_permission(self,request,view,obj):
        #check if the action is safe 
        if request.method in permissions.SAFE_METHODS:
            return True
        #""" Check if it is their own profile"""
        return obj.id == request.user.id
