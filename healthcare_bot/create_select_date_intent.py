import os
from google.cloud import dialogflow_v2 as dialogflow
from google.cloud.dialogflow_v2.types import Intent, Context
from google.protobuf.struct_pb2 import Struct

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"
project_id = 'demoagent-wgo9'

def create_select_date_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    phrases = ["Monday", "Tuesday", "Wednesday", "Thursday"]
    training_phrases = [Intent.TrainingPhrase(parts=[Intent.TrainingPhrase.Part(text=phrase)]) for phrase in phrases]

    input_context = f"{parent}/sessions/-/contexts/awaiting-date"

    output_context = {
        "name": f"{parent}/sessions/-/contexts/awaiting-duration",
        "lifespan_count": 5
    }

    
    intent = Intent(
        display_name='Select Date',
        training_phrases=training_phrases,
        messages=[],
        input_context_names=[input_context],
        output_contexts=[output_context]
    )

    
    response = client.create_intent(request={'parent': parent, 'intent': intent})
    print("Select Date Intent created successfully.")

create_select_date_intent()
