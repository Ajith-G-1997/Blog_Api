class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("hai am ajith")
        
        # Perform middleware logic here
        response = self.get_response(request)
        return response
