# I am providing an example_config.py file for reference.
# Please ensure you create a "config.py" file in the "Dogspot" folder to avoid errors, and kindly add your "EMAIL" and "PASSWORD" variable strings as shown below.

EMAIL = ''
PASSWORD = ''

"""
Note: We are using a Gmail app password, so the configuration is as follows:-
Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = PASSWORD
"""
