import pprint
import time

import requests
from pathlib import Path
from dotenv import load_dotenv
import os
import json

from models.ticket_details import get_detail

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

mukapi = os.environ["MUKAPI"]
getlist_url = os.environ["GETLIST_URL"]
ticket_url = os.environ["TICKET_URL"]
reply_url = os.environ["REPLY_URL"]
company_url = os.environ["COMPANY_URL"]

payload = {}
headers = {
    'Content-Type': 'application/json',
}

mukthy_id = os.environ["MUKTHY_ID"]
bala_id = os.environ["BALA_ID"]
gaetan_id = os.environ["GAETAN_ID"]
manoj_id = os.environ["MANOJ_ID"]
tejashri_id = os.environ["TEJASHRI_ID"]
sajan_id = os.environ["SAJAN_ID"]
rosheen_id = os.environ["ROSHEEN_ID"]
nagz_id = os.environ["NAGZ_ID"]

def get_tickets():
    total_tickets = requests.request("GET", url=f"{getlist_url}", auth=(mukapi, "x"), headers=headers,
                                     data=payload)
    total = json.loads(total_tickets.text)
    # pprint.pprint(total)

    total_tickets = total['total']
    print(f"Total tickets: {total_tickets}")

    total_pages = int(total_tickets / 30)
    print(f"Total pages: {total_pages}")
    #
    # for ticketId in range(ticketlen):
    #     print(f"Ticket ID: {ticketList['results'][ticketId]['id']}")
    #     print(f"Ticket Last Updated: {ticketList['results'][ticketId]['updated_at']}")

    ticket_list = []

    for page in range(1, 3):  # total_pages + 1): this is for total pages, removed as it creates too many tickets to track.
        print(f"Page: {page}")
        pagination_url = getlist_url + f"&page={page}"

        ticketList = requests.request("GET", url=f"{pagination_url}", auth=(mukapi, "x"), headers=headers,
                                      data=payload)
        tickets = json.loads(ticketList.text)
        ticketLen = len(tickets['results'])

        for ticketId in range(ticketLen):
            # print(f"Ticket ID: {ticketList['results'][ticketId]['id']}")
            # print(f"Ticket Last Updated: {ticketList['results'][ticketId]['updated_at']}")

            ticket_list.append(tickets['results'][ticketId]['id'])

    print(f"Ticket List: {ticket_list}")
    print(f"Ticket List Length: {len(ticket_list)}")

    return ticket_list


def main():
    # get_tickets()
    ticket_list = get_tickets()

    checks = get_detail(ticket_list)


if __name__ == "__main__":
    main()
