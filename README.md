# EOL Zoom XBlock

![https://github.com/eol-uchile/eol-zoom-xblock/actions](https://github.com/eol-uchile/eol-zoom-xblock/workflows/Python%20application/badge.svg) ![Coverage Status](https://github.com/eol-uchile/eol-zoom-xblock/blob/master/coverage-badge.svg)

XBlock and API to integrate zoom with the Open edX LMS. Editable within Open edx Studio.

# Install

    docker-compose exec cms pip install -e /openedx/requirements/eolzoom
    docker-compose exec lms pip install -e /openedx/requirements/eolzoom
    docker-compose exec lms python manage.py lms --settings=prod.production makemigrations
    docker-compose exec lms python manage.py lms --settings=prod.production migrate

# Configuration Zoom

To enable [Zoom API](https://marketplace.zoom.us/docs/guides) Edit *production.py* in *lms and cms settings* and add your own keys and domain url.

    import base64
    EOLZOOM_CLIENT_ID = AUTH_TOKENS.get('EOLZOOM_CLIENT_ID', '')
    EOLZOOM_CLIENT_SECRET = AUTH_TOKENS.get('EOLZOOM_CLIENT_SECRET', '')
    EOLZOOM_AUTHORIZATION = base64.b64encode('{}:{}'.format(EOLZOOM_CLIENT_ID, EOLZOOM_CLIENT_SECRET).encode("utf-8")).decode("utf-8")
    EOLZOOM_DOMAIN = AUTH_TOKENS.get('EOLZOOM_DOMAIN', '')

# Configuration Zoom Event

To enable [Zoom Event API](https://marketplace.zoom.us/docs/guides/build/webhook-only-app) Edit *production.py* in *lms and cms settings* and add your own token authorization.

    EOLZOOM_EVENT_AUTHORIZATION = AUTH_TOKENS.get('EOLZOOM_EVENT_AUTHORIZATION', '')

# Configuration Youtube

To enable [Youtube API](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps) Edit *production.py* in *lms and cms settings* and add your own credentials and timezone.

    GOOGLE_CLIENT_ID = AUTH_TOKENS.get('GOOGLE_CLIENT_ID', '')
    GOOGLE_PROJECT_ID = AUTH_TOKENS.get('GOOGLE_PROJECT_ID', '')
    GOOGLE_CLIENT_SECRET = AUTH_TOKENS.get('GOOGLE_CLIENT_SECRET', '')
    GOOGLE_REDIRECT_URIS = AUTH_TOKENS.get('GOOGLE_REDIRECT_URIS', [])
    GOOGLE_JAVASCRIPT_ORIGINS = AUTH_TOKENS.get('GOOGLE_JAVASCRIPT_ORIGINS', [])
    EOLZOOM_YOUTUBE_TIMEZONE = AUTH_TOKENS.get('EOLZOOM_YOUTUBE_TIMEZONE', '')

## TESTS
**Prepare tests:**

- Install **act** following the instructions in [https://nektosact.com/installation/index.html](https://nektosact.com/installation/index.html)

**Run tests:**
- In a terminal at the root of the project
    ```
    act -W .github/workflows/pythonapp.yml
    ```
# Screenshots
*Last Update 26/03/2020*

## CMS - Studio Edit
<p align="center">
<img width="600" src="examples/studio_edit_01.png">
</p>
<p align="center">
<img width="600" src="examples/studio_edit_02.png">
</p>

## CMS - Author View
<p align="center">
<img width="600" src="examples/author_view_01.png">
</p>

## LMS - Staff View
<p align="center">
<img width="400" src="examples/staff_view_lms_01.png">
</p>

## LMS - Student View
<p align="center">
<img width="400" src="examples/student_view_lms_01.png">
</p>
