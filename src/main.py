import os
from dotenv import load_dotenv

from clashstudio import Clash_Studio

load_dotenv()

def main():
    COC_API_TOKEN = os.getenv("COC_API_TOKEN")
    main_acc_tag = os.getenv("MAIN_ACCOUNT_TAG")
    second_acc_tag = os.getenv("SECOND_ACCOUNT_TAG")
    donation_acc_tag = os.getenv("DONATION_ACCOUNT_TAG")

    cs = Clash_Studio(COC_API_TOKEN)

    cs.get_player_data(main_acc_tag)

if __name__ == "__main__":
    main()