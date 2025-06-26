import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core import exceptions
from google.cloud.dialogflow_v2.types import Intent, Context
from google.protobuf.struct_pb2 import Struct
from db_logger import log_conversation

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"

project_id = 'demoagent-wgo9'

def create_book_slot_by_duration_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    phrases = [
        "30 minutes",
        "45 minutes",
        "1 hour",
        "2 hours"
    ]
    training_phrases = [Intent.TrainingPhrase(parts=[Intent.TrainingPhrase.Part(text=phrase)]) for phrase in phrases]

    
    input_context = f"projects/{project_id}/agent/sessions/-/contexts/awaiting-duration"
    
    output_context=Context(
    name=f"projects/{project_id}/agent/sessions/-/contexts/awaiting-confirmation",
    lifespan_count=5
)

    text = dialogflow.Intent.Message.Text(text=["Please select a time slot from the options below:"])
    text_message = dialogflow.Intent.Message(text=text)

    payload_struct = Struct()
    payload_struct.update({
        "richContent": [
            [
                {
                    "type": "chips",
                    "options": [
                        {"text": "10:00 AM"},
                        {"text": "11:30 AM"},
                        {"text": "3:00 PM"},
                        {"text": "4:30 PM"}
                    ]
                }
            ]
        ]
    })

    payload_message = Intent.Message(payload=payload_struct)

    intent = dialogflow.Intent(
        display_name='Book Slot by Duration',
        training_phrases=training_phrases,
        messages=[text_message, payload_message],
        input_context_names=[input_context],
        output_contexts=[output_context]
    )

    try:
        response = client.create_intent(request={'parent': parent, 'intent': intent})
        print("Book Slot by Duration Intent created successfully.")
    except exceptions.AlreadyExists:
        print("Intent with this name already exists.")
    except exceptions.InvalidArgument as e:
        print("Invalid Argument Error:", e)
    except exceptions.PermissionDenied as e:
        print("Permission Denied Error:", e)
    except Exception as e:
        print("Some other error occurred:", e)

create_book_slot_by_duration_intent()
