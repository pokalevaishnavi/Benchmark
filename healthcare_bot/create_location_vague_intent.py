import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core import exceptions
from google.protobuf.struct_pb2 import Struct

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"

project_id = 'demoagent-wgo9'

def create_location_vague_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    training_phrases = []
    phrases = ["Massage","Spa Service","Doctor Consultation","Physiotherapy","Somewhere nearby", "Any location is fine", "Anywhere", "No preference"]
    for phrase in phrases:
        part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
        training_phrases.append(dialogflow.Intent.TrainingPhrase(parts=[part]))

    input_context = dialogflow.Context(
        name=f"projects/{project_id}/agent/sessions/-/contexts/awaiting-location",
        lifespan_count=5
    )

    output_context = dialogflow.Context(
        name=f"projects/{project_id}/agent/sessions/-/contexts/awaiting-location",
        lifespan_count=5
    )

    text = dialogflow.Intent.Message.Text(text=["Could you please specify the location you prefer?"])
    text_message = dialogflow.Intent.Message(text=text)

    payload_struct = Struct()
    payload_struct.update({
        "richContent": [
            [
                {
                    "type": "chips",
                    "options": [
                        {"text": "Pune"},
                        {"text": "Mumbai"},
                        {"text": "Ratnagiri"},
                        {"text": "Kolhapur"}
                    ]
                }
            ]
        ]
    })

    payload_message = dialogflow.Intent.Message(payload=payload_struct)

    intent = dialogflow.Intent(
        display_name='Location - Vague',
        training_phrases=training_phrases,
        messages=[text_message, payload_message],
        input_context_names=[input_context.name],
        output_contexts=[output_context]
    )

    try:
        response = client.create_intent(request={'parent': parent, 'intent': intent})
        print("Location - Vague Intent created successfully.")
    except exceptions.AlreadyExists:
        print("Intent with this name already exists.")
    except exceptions.InvalidArgument as e:
        print("Invalid Argument Error:", e)
    except exceptions.PermissionDenied as e:
        print("Permission Denied Error:", e)
    except Exception as e:
        print("Some other error occurred:", e)

create_location_vague_intent()
