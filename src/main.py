import os
from dotenv import load_dotenv

from clashstudio import Clash_Studio

load_dotenv()


def main():
    COC_API_TOKEN = os.getenv("COC_API_TOKEN")

    cs = Clash_Studio(COC_API_TOKEN)





if __name__ == "__main__":
    main()