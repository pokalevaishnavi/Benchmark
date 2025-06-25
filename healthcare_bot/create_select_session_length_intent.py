import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core import exceptions
from google.protobuf.struct_pb2 import Struct
from google.cloud.dialogflow_v2.types import Intent, Context

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"

project_id = 'demoagent-wgo9'  

def create_select_session_length_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    
    phrases = ["Monday","Tuesday","Friday","Wednesday","Thursday","Sunday","Saturday","30 minutes", "Book for one hour", "I want a 45 minute session", "2 hours session"]
    
    training_phrases = [Intent.TrainingPhrase(parts=[Intent.TrainingPhrase.Part(text=phrase)]) for phrase in phrases]

    
    input_context = f"projects/{project_id}/agent/sessions/-/contexts/awaiting-duration"
    
    output_context = {
        "name": f"{parent}/sessions/-/contexts/awaiting-slot",
        "lifespan_count": 5
    }

    text = dialogflow.Intent.Message.Text(text=["Please select the session duration from the options below:"])
    text_message = dialogflow.Intent.Message(text=text)

    payload_struct = Struct()
    payload_struct.update({
        "richContent": [
            [
                {
                    "type": "chips",
                    "options": [
                        {"text": "30 minutes"},
                        {"text": "45 minutes"},
                        {"text": "1 hour"},
                        {"text": "2 hours"}
                    ]
                }
            ]
        ]
    })

    payload_message = Intent.Message(payload=payload_struct)

    intent = dialogflow.Intent(
        display_name='Select Session Length',
        training_phrases=training_phrases,
        messages=[text_message, payload_message],
        input_context_names=[input_context],
        output_contexts=[output_context]
    )

    try:
        response = client.create_intent(request={'parent': parent, 'intent': intent})
        print("Select Session Length Intent created successfully.")
    except exceptions.AlreadyExists:
        print("Intent with this name already exists.")
    except exceptions.InvalidArgument as e:
        print("Invalid Argument Error:", e)
    except exceptions.PermissionDenied as e:
        print("Permission Denied Error:", e)
    except Exception as e:
        print("Some other error occurred:", e)

create_select_session_length_intent()
