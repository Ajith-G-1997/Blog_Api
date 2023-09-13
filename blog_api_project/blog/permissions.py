# from django.contrib.auth.models import User, Permission
# from django.contrib.contenttypes.models import ContentType
# from .models import Blog


# # class accesspermissions():
# #     
# from rest_framework import permissions

# class CanCreateBlogPermission(permissions.BasePermission):
#     message = "You do not have permission to create a blog."

#     def has_permission(self, request, view):
#         user = User.objects.get(username="ajith")


#         content_type = ContentType.objects.get_for_model(Blog)


#         permission_create = Permission.objects.get(codename="can_create_blog", content_type=content_type)
#         user.user_permissions.add(permission_create)

#     # Assign the "can_view_blog" permission to another user
        



from rest_framework import permissions

class CanViewBlogPermission(permissions.BasePermission):
    message = "You do not have permission to create a blog."

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user is "ajith"
            if request.user.username == "ajith":
                # "ajith" is not allowed to create blogs
                return request.method == "GET"  
            
            # For other authenticated users, they can view blogs
            return True
        
        return False  # User is not authenticated, so they do not have permission to create or view blogs
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user is "ajith"
            if request.user.username == "amal":
                # "ajith" is not allowed to create blogs
                return request.method == "GET" 
            # Allow only GET requests (viewing)
            
            # For other authenticated users, they can view blogs
            return True
        
        return False 
  

   

    
class CreateBlogPermission(permissions.BasePermission):
    message = "You do not have permission to View The   blog."

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user is "ajith"
            if request.user.username == "admin":
                # "ajith" is not allowed to create blogs
                return request.method == "POST"
            

            
            # For other authenticated users, they can view blogs
            return True
        return False
        

class AllpermissionsGranted(permissions.BasePermission):
    message = "You do not have permission to View The   blog."
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.username == "SuperUser":
                return request.method == "GET"
            
            return True
        return False
     
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.username == "SuperUser": 
                return request.method == "POST"
         
            return True
        return False

    
class CanUpdateBlogPermission(permissions.BasePermission):
    message = "You do not have permission to update this blog."

    def has_object_permission(self, request, view, obj):
        # Check if the user is "ajith" and the blog's author is the same as the user
        return request.user.username == "ajith" and obj.author == request.user.username