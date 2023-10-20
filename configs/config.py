import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    URL_JSPLACEHOLDER = os.getenv("URL_JSPLACEHOLDER")


config = Config()
