from django.shortcuts import render

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, 'nothing.html')
        elif 500 <= response.status_code < 600:
            return render(request, 'error.html',{ "info":"500 Internal Server Error"}) 
        return response

    def process_exception(self, request, exception):
        error_message = str(exception)
        response_data = {'error': error_message}
        print(f"Exception caught >>>> : {error_message}")