if not user.has_logged_in or not user.is_from_chrome:
    return "our service is only open for chrome logged in user"

if not (user.has_logged_in and user.is_from_chrome):
    return "our service is only open for chrome logged in user"
