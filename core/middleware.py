from .models import VisitorCounter

class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # On incrémente le compteur pour chaque requête GET
        if request.method == 'GET':
            # On utilise une session pour ne compter qu'une fois par visiteur
            if not request.session.get('visited', False):
                request.session['visited'] = True
                VisitorCounter.increment()
        response = self.get_response(request)
        return response