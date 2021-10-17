
from profiles_api.models import profileFieldItem
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
     """Check user is trying to edit their own profile"""

     def has_object_permission(self, request, view, object):
         """Check user is trying to edit their own profile"""
         if request.method in permissions.SAFE_METHODS:
            return True

         return object.id == request.user.id

class UpdateFeedClass(permissions.BasePermission):
       """Allow users to update their own status"""

       def has_object_permission(seld,request, view, obj):
              """Check if users is trying to update their own status"""
              if request.method in permissions.SAFE_METHODS:
                     return True
               
              return obj.user_profile.id == request.user.id
       

        