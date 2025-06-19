from django.shortcuts import render

# Create your views here.
class LoginView():
    def get(self, request):
        # Render the login template
        return render(request, 'loginout/login.html')

    def post(self, request):
        # Handle the login logic here
        # For simplicity, we will just redirect to the blog page
        return render(request, 'blog/post_list.html')

class LogoutView():
    def get(self, request):
        # Handle the logout logic here
        # For simplicity, we will just redirect to the blog page
        return render(request, 'blog/post_list.html')
    def post(self, request):
        # Handle the logout logic here
        # For simplicity, we will just redirect to the blog page
        return render(request, 'blog/post_list.html')