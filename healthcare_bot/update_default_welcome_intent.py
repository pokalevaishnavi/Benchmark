from google.cloud import dialogflow_v2 as dialogflow
import os
from google.api_core import exceptions
from google.protobuf.struct_pb2 import Struct

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"

project_id = 'demoagent-wgo9'

def update_default_welcome_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    intents = client.list_intents(request={"parent": parent})

    for intent in intents:
        if intent.display_name == 'Default Welcome Intent':
            intent.messages.clear()

            text = dialogflow.Intent.Message.Text(text=["Hi there! Welcome to our Healthcare Bot. How can I assist you today?"])
            text_message = dialogflow.Intent.Message(text=text)

            payload_struct = Struct()
            payload_struct.update({
                "richContent": [
                    [
                        {
                            "type": "chips",
                            "options": [
                                {"text": "Hello!"},
                                {"text": "View Services"},
                                {"text": "Help"}
                            ]
                        }
                    ]
                ]
            })
            payload_message = dialogflow.Intent.Message(payload=payload_struct)

            intent.messages.extend([text_message, payload_message])

            training_phrases = [
                "hello", "hi", "good morning", "good evening", "hey",
                "what's up", "howdy", "greetings"
            ]
            intent.training_phrases.clear()
            for phrase in training_phrases:
                part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
                training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
                intent.training_phrases.append(training_phrase)

            output_context = dialogflow.Context(
                name=f"projects/{project_id}/agent/sessions/-/contexts/awaiting-service",
                lifespan_count=5
            )
            intent.output_contexts.clear()
            intent.output_contexts.append(output_context)

            client.update_intent(request={'intent': intent, 'language_code': "en"})
            print("Default Welcome Intent updated successfully.")
            return

update_default_welcome_intent()
