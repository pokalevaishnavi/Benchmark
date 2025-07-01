import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core import exceptions
from google.protobuf.struct_pb2 import Struct
from google.cloud.dialogflow_v2.types import Intent, Context 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"

project_id = 'demoagent-wgo9'

def create_select_service_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    training_phrases = []
    phrases = ["I want a massage", "Book a spa service", "I need physiotherapy", "Doctor consultation",
               "View Services", "Show me services", "What services do you have?", "I want to book a service"]
    for phrase in phrases:
        part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
        training_phrases.append(dialogflow.Intent.TrainingPhrase(parts=[part]))

    input_context = dialogflow.Context(
        name=f"projects/{project_id}/agent/sessions/-/contexts/awaiting-service",
        lifespan_count=5
    )

    output_context = Context(
        name=f"{parent}/sessions/-/contexts/awaiting-location",
        lifespan_count=5
    )

    
    intent = dialogflow.Intent(
        display_name='Select Service',
        training_phrases=training_phrases,
        messages=[],
        input_context_names=[input_context.name],
        output_contexts=[output_context]
    )

    try:
        response = client.create_intent(request={'parent': parent, 'intent': intent})
        print("Select Service Intent created successfully.")
    except exceptions.AlreadyExists:
        print("Intent with this name already exists.")
    except exceptions.InvalidArgument as e:
        print("Invalid Argument Error:", e)
    except exceptions.PermissionDenied as e:
        print("Permission Denied Error:", e)
    except Exception as e:
        print("Some other error occurred:", e)

create_select_service_intent()