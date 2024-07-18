#!/usr/bin/env python3
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS contains a tuple that contains GET, OPTIONS and HEAD
            return True
        return obj.author == request.user
