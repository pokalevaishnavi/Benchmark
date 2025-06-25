import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core import exceptions

#path to downloaded JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"


project_id = 'demoagent-wgo9'  


def update_default_fallback_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    # Get existing Default Fallback Intent
    intents = client.list_intents(request={"parent": parent})
    for intent in intents:
        if intent.display_name == 'Default Fallback Intent':
            intent.messages[0].text.text[0] = "Sorry, I didn’t get that. Can you rephrase?"
            response = client.update_intent(intent=intent, language_code="en")
            print("Default Fallback Intent updated.")
            return

update_default_fallback_intent()
