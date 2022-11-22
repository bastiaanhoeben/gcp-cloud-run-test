import functions_framework

# Register an HTTP function with the Functions Framework
@functions_framework.http
def my_http_function(request):

    print("hello world")
    # Return an HTTP response
    return 'OK'
