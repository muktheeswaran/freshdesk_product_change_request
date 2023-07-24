import time

import requests
from pathlib import Path
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import pprint

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

mukapi = os.environ["MUKAPI"]
ticket_url = os.environ["TICKET_URL"]

payload = {}

mukthy = []
bala = []
gaetan = []
manoj = []
tejashri = []
sajan = []
rosheen = []
nagz = []
nestor = []
no_agent = []

mukthy_id = os.environ["MUKTHY_ID"]
bala_id = os.environ["BALA_ID"]
gaetan_id = os.environ["GAETAN_ID"]
manoj_id = os.environ["MANOJ_ID"]
tejashri_id = os.environ["TEJASHRI_ID"]
sajan_id = os.environ["SAJAN_ID"]
rosheen_id = os.environ["ROSHEEN_ID"]
nagz_id = os.environ["NAGZ_ID"]
leandro_id = os.environ["LEANDRO_ID"]
thriveni_id = os.environ["THRIVENI_ID"]
nestor_id = os.environ["NESTOR_ID"]

slack_webhook_url = os.environ["SLACK_WEBHOOK_URL"]


def get_detail(ticket_list):
    headers = {
        'Content-Type': 'application/json',
    }

    for ticketID in ticket_list:

        # agent_ids = [mukthy_id, bala_id, gaetan_id, manoj_id, tejashri_id, sajan_id, rosheen_id] # not needed for now atleast.
        print(f"Ticket ID: {ticketID}")
        ticketUrl = f"{ticket_url}{ticketID}/?include=conversations"
        conversations = requests.request("GET", url=ticketUrl, auth=(mukapi, 'X'), headers=headers)
        conversations = conversations.text
        conversations = json.loads(conversations)

        if len(conversations["conversations"]) > 0:

            # if conversations["conversations"][-1]["user_id"] == int(mukthy_id) or conversations["conversations"][-1]["user_id"] == int(bala_id) or conversations["conversations"][-1]["user_id"] == int(gaetan_id) or conversations["conversations"][-1]["user_id"] == int(manoj_id) or conversations["conversations"][-1]["user_id"] == int(tejashri_id) or conversations["conversations"][-1]["user_id"] == int(sajan_id) or conversations["conversations"][-1]["user_id"] == int(rosheen_id) or conversations["conversations"][-1]["user_id"] == int(nagz_id):
            #     user_id = conversations["conversations"][-1]["user_id"]
            #     updated_at = conversations["conversations"][-1]["updated_at"]
            #     print("user id: ", user_id)
            #     print("From -1 updated at: ", updated_at)
            #

            # below part is to check the last agent who updated the ticket, instead of taking the updated time from
            # ticket.

            for i in range(len(conversations["conversations"]) - 1, -1, -1):
                user_id = conversations["conversations"][i]["user_id"]
                if user_id == int(mukthy_id) or user_id == int(bala_id) or user_id == int(gaetan_id) or user_id == int(
                        manoj_id) or user_id == int(tejashri_id) or user_id == int(sajan_id) or user_id == int(
                    rosheen_id) or user_id == int(nagz_id) or user_id == int(leandro_id) or user_id == int(thriveni_id) or user_id == int(nestor_id):
                    # pprint.pprint(conversations["conversations"][i])
                    user_id = user_id
                    updated_at = conversations["conversations"][i]["updated_at"]
                    break

        else:
            user_id = "Not Found"
            updated_at = conversations["updated_at"]

        print("last update: ", updated_at)

        current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        current_time = datetime.strptime(f'{current_time}', "%Y-%m-%dT%H:%M:%SZ")
        print("current time: ", current_time)
        if 'Z' not in str(updated_at):
            updated_at = str(updated_at)
            updated_at = updated_at.split(' ')
            updated_at = f'{updated_at[0]}T{updated_at[1]}Z'
        else:
            updated_at = updated_at
        print("updated at: ", updated_at)
        updated_at = datetime.strptime(f'{updated_at}', "%Y-%m-%dT%H:%M:%SZ")
        # try:
        #     updated_at = datetime.strptime(f'{updated_at}', "%Y-%m-%dT%H:%M:%SZ")
        # except ValueError:
        #     print(type(updated_at))
        #     updated_at = int(str(updated_at))
        #     updated_at = updated_at.split(" ")
        #     updated_at = updated_at[0] + "T" + updated_at[1] + "Z"
        #     updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ")
        #     print(updated_at)

        if updated_at > current_time:
            time_diff = updated_at - current_time
            print("time diff: ", time_diff.days)
            time_diff = int(time_diff.total_seconds() / 60 / 60 / 24)
            print("time diff: ", time_diff)

        else:
            time_diff = current_time - updated_at
            time_diff = int(time_diff.total_seconds() / 60 / 60 / 24)
            print("time diff: ", time_diff)

        if user_id == int(mukthy_id) and int(str(time_diff)) >= 5:
            print("ticket id for Mukthy: ", ticketID)
            mukthy.append(ticketID)
        elif user_id == int(bala_id) and int(str(time_diff)) >= 5:
            print("ticket id for Bala: ", ticketID)
            bala.append(ticketID)
        elif user_id == int(gaetan_id) and int(str(time_diff)) >= 5:
            print("ticket id for Gaetan: ", ticketID)
            gaetan.append(ticketID)
        elif user_id == int(manoj_id) and int(str(time_diff)) >= 5:
            print("ticket id for Manoj: ", ticketID)
            manoj.append(ticketID)
        elif user_id == int(tejashri_id) and int(str(time_diff)) >= 5:
            print("ticket id for Tejashri: ", ticketID)
            tejashri.append(ticketID)
        elif user_id == int(sajan_id) and int(str(time_diff)) >= 5:
            print("ticket id for Sajan: ", ticketID)
            sajan.append(ticketID)
        elif user_id == int(rosheen_id) and int(str(time_diff)) >= 5:
            print("ticket id for Rosheen: ", ticketID)
            rosheen.append(ticketID)
        elif user_id == int(nagz_id) and int(str(time_diff)) >= 5:
            print("ticket id for Nagz: ", ticketID)
            nagz.append(ticketID)
        elif user_id == int(nestor_id) and int(str(time_diff)) >= 5:
            print("ticket id for Nestor: ", ticketID)
            nagz.append(ticketID)
        elif int(str(time_diff)) >= 5:
            print("ticket id with No Agent: ", ticketID)
            no_agent.append(ticketID)

        print("sleeping for 2 seconds, to avoid rate limit")
        time.sleep(2)

    dict_of_lists = {
        "mukthy": list(set(mukthy)),
        "bala": list(set(bala)),
        "gaetan": list(set(gaetan)),
        "manoj": list(set(manoj)),
        "tejashri": list(set(tejashri)),
        "sajan": list(set(sajan)),
        "rosheen": list(set(rosheen)),
        "nagz": list(set(nagz)),
        "nestor": list(set(nestor)),
        "no_agent": list(set(no_agent))
    }

    for key, value in dict_of_lists.items():
        ticket_url_list = []
        if len(value) > 0:

            for i in value:
                final_ticket_url = f"https://support.zyte.com/a/tickets/{i}/"
                ticket_url_list.append(final_ticket_url)

            print(f"Post Slack Notification to {key}: ", json.dumps(value, indent=4))

            if key == "mukthy":
                slack_id = "muktheeswaran.mariapp"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "bala":
                slack_id = "bala.ravichandran"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "gaetan":
                slack_id = "gaetan.belsack"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "manoj":
                slack_id = "manoj.kamal"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "tejashri":
                slack_id = "tejashri"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "sajan":
                slack_id = "sajan.shetty"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "rosheen":
                slack_id = "Rosheen"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "nagz":
                slack_id = "nagharajan.rathina"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            elif key == "nestor":
                slack_id = "nestor"

                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n @{slack_id} has below tickets in Product Change Requests.\n\n *{results_list}*"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

            else:
                headers = {
                    "Content-type": "application/json",
                }

                results_list = json.dumps(ticket_url_list, indent=4)
                print(results_list)

                payload = {
                    "text": "Product Change Requests Weekly Report",
                    "blocks": [
                        {
                            "type": "section",
                            "block_id": "section567",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\n here We are not able to track who created these below tickets via API in Product Change Requests. So Please check and update them.\n{results_list}\n"
                            },
                        },
                    ],
                }

                response = requests.post(url=slack_webhook_url, headers=headers, data=json.dumps(payload, indent=4))
                print(response)

        else:
            print(f"{key} with No Tickets in Product Change Requests: ", json.dumps(value, indent=4))

    return "all checks done"
