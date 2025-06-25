import os
from google.cloud import dialogflow_v2 as dialogflow
from google.protobuf.struct_pb2 import Struct
from google.api_core import exceptions
from google.cloud.dialogflow_v2.types import Intent

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"
project_id = 'demoagent-wgo9'

def create_confirm_booking_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    phrases = [
        "10:00 AM",
        "11:30 AM",
        "3:00 PM",
        "4:30 PM"
    ]

    training_phrases = [
        Intent.TrainingPhrase(parts=[
            Intent.TrainingPhrase.Part(text=phrase, entity_type="@time_slot", alias="time")
        ]) for phrase in phrases
    ]

    text_message = dialogflow.Intent.Message(
        text=dialogflow.Intent.Message.Text(text=["Your session has been booked!"])
    )
    
    input_context = "awaiting-confirmation"

    intent = dialogflow.Intent(
        display_name='Confirm Booking',
        training_phrases=training_phrases,
        messages=[text_message],
        input_context_names=[input_context]
    )

    try:
        response = client.create_intent(request={'parent': parent, 'intent': intent})
        print("Confirm Booking Intent created successfully.")
    except exceptions.AlreadyExists:
        print("Intent with this name already exists.")
    except exceptions.InvalidArgument as e:
        print("Invalid Argument Error:", e)
    except exceptions.PermissionDenied as e:
        print("Permission Denied Error:", e)
    except Exception as e:
        print("Some other error occurred:", e)

create_confirm_booking_intent()
