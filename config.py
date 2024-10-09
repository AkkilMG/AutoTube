import os
from dotenv import load_dotenv

load_dotenv()

# Mail
mail = os.getenv("mail")
password = os.getenv("password")