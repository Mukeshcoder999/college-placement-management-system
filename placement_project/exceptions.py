from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        return response

    message = "Something went wrong."

    if isinstance(response.data, dict):
        if "detail" in response.data:
            message = response.data["detail"]
        else:
            message = "Validation failed."

    response.data = {
        "success": False,
        "status": response.status_code,
        "message": message,
        "errors": response.data,
    }

    return response