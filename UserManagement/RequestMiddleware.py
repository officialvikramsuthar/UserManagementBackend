# middleware.py
import datetime
from django.utils import timezone
from User.models import RequestLog

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Log request details to NoSQL database
        self.log_request(request, response)

        return response

    def log_request(self, request, response):
        timestamp = timezone.now()
        endpoint = request.path
        ip_address = self.get_client_ip(request)
        status = response.status_code


        RequestLog.objects.using("mongo").create(
            timestamp=timestamp,
            endpoint=endpoint,
            ip_address=ip_address,
            status=status,
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
