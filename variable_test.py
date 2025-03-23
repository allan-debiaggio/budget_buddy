import os
from dotenv import load_dotenv

def get_env_variable(var_name):
    """Get a variable from the .env file"""
    load_dotenv()
    var = os.getenv(var_name)
    if not var:
        raise ValueError(f"{var_name} is not set in the .env file")
    return var