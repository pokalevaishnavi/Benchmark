import os
from google.cloud import dialogflow_v2 as dialogflow
from google.protobuf.struct_pb2 import Struct
from google.api_core import exceptions
from google.cloud.dialogflow_v2.types import Intent

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"
project_id = 'demoagent-wgo9'

def create_confirm_location_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    phrases = ["Pune", "Mumbai", "Ratnagiri", "Kolhapur"]
    training_phrases = [Intent.TrainingPhrase(parts=[Intent.TrainingPhrase.Part(text=phrase)]) for phrase in phrases]

    input_context = f"{parent}/sessions/-/contexts/awaiting-location-confirmation"

    output_context = {
        "name": f"{parent}/sessions/-/contexts/awaiting-date",
        "lifespan_count": 5
    }

    
    intent = Intent(
        display_name='Confirm Location',
        training_phrases=training_phrases,
        messages=[],
        input_context_names=[input_context],
        output_contexts=[output_context]
    )

    response = client.create_intent(request={'parent': parent, 'intent': intent})
    print("Confirm Location Intent created successfully.")


    

create_confirm_location_intent()
