from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django REST Framework.
    """

    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "success": False,
            "status": response.status_code,
            "message": (
                response.data.get("detail")
                if isinstance(response.data, dict) and "detail" in response.data
                else "Validation failed"
            ),
            "errors": (
                response.data
                if isinstance(response.data, dict) and "detail" not in response.data
                else None
            ),
        }

    return response