from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


class CustomResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):

        if hasattr(response, 'data'):
            data = {
                "success": response.status_code < 400,
                "status_code": response.status_code,
                "data": response.data if response.status_code < 400 else None,
                "error": response.data if response.status_code >= 400 else None,
            }
            return JsonResponse(data, status=response.status_code)
        else:
            return response