# config_insecure.py
# Intentionally INSECURE configuration for demo purposes ONLY.
# Do NOT use values like this in any real application.

DEBUG = True  # ❌ In production, debug mode should be disabled.

# ❌ Hardcoded secrets – bad practice:
DATABASE_USERNAME = "admin"
DATABASE_PASSWORD = "SuperSecretPassword123!"  # hardcoded credential
DATABASE_HOST = "localhost"
DATABASE_NAME = "demo_app"

# ❌ Insecure, hardcoded secret key:
SECRET_KEY = "this-is-a-very-weak-and-hardcoded-secret-key"

# ❌ Overly permissive CORS setting:
ALLOWED_ORIGINS = ["*"]  # any origin can access the app

# Example of how these might be used in an application:
def get_database_connection_string():
    """
    Build a database connection string using the insecure, hardcoded values.
    Security tools should flag the use of hardcoded credentials and secrets.
    """
    return (
        f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}"
        f"@{DATABASE_HOST}/{DATABASE_NAME}"
    )


def is_debug_mode():
    """
    Return whether the app is running in debug mode.
    In a production setting, DEBUG should be False.
    """
    return DEBUG


if __name__ == "__main__":
    print("Debug mode:", is_debug_mode())
    print("Database connection string:", get_database_connection_string())
    print("Allowed origins:", ALLOWED_ORIGINS)
