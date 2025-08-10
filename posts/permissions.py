from rest_framework import permissions

# Create a custom class which extends BasePermission.
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #has_permission的作用不止是必须登陆，还可以添加全局的与对象无关的逻辑
        #比如必须邮箱已经验证才能访问，只能在工作日访问
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
            return True
        return obj.author == request.user