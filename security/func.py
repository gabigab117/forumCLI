class AuthError(Exception):
    pass

def is_authenticate(auth: bool):
    if not auth:
        raise AuthError("Veuillez vous authentifier")