import os

# BASIC AUTH SETTINGS
ALFRED_PASSWORD_SALT = os.environ.get("ALFRED_PASSWORD_SALT")

# JWT_AUTH_SETTINGS
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
JWT_EXP_DELTA_SECONDS = int(os.environ.get("JWT_EXP_DELTA_SECONDS", "604800"))
JWT_SECRET = os.environ.get("JWT_SECRET")
FERNET_CRYPT_KEY = os.environ.get("FERNET_CRYPT_KEY")


# CACHE SETTINGS
ALFRED_REDIS_HOST = os.environ.get("ALFRED_REDIS_HOST", "")

# SENTRY SETTINGS
SENTRY_DSN = os.environ.get("SENTRY_DSN", "")
