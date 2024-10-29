
class SimpleClassMiddleware:


    def __init__(self, get_response):
        print("init middleware")
        self.get_response = get_response

    def __call__(self, request):
        print("call middleware")
        response = self.get_response(request)
        print("after middleware")
        return response