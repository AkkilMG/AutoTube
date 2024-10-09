import os
from dotenv import load_dotenv

load_dotenv()

# Mail
email = os.getenv("email")
password = os.getenv("password")