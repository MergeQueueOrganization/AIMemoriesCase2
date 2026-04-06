from rest_framework.decorators import api_view
import bleach  # third-party library

@api_view(["GET", "POST"])
def snippet_list(request):
    tainted = request.GET.get("query", "")

    # Clean the input (basic sanitization)
    cleaned = bleach.clean(tainted)

    eval(cleaned)
