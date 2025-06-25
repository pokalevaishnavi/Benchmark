import os
from google.cloud import dialogflow_v2 as dialogflow

#path to downloaded JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"


project_id = 'demoagent-wgo9'  

def create_service_selection_intent():
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"


    # Training phrases (what user might say)
    training_phrases = []
    phrases = [
        "I want a massage",
        "Book a doctor appointment",
        "Need physiotherapy session",
        "Get me a session for yoga therapy",
        "I'm looking for a nutrition consultation",
        "Book an eye check-up",
        "I'd like to see a skin specialist",
        "Can I get an appointment for a chiropractor?"
    ]
    
    for phrase in phrases:
        part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    # What bot replies
    text = dialogflow.Intent.Message.Text(text=["Great! Which location do you prefer?"])
    message = dialogflow.Intent.Message(text=text)

    # Intent details
    intent = dialogflow.Intent(
        display_name='Service Selection',
        training_phrases=training_phrases,
        messages=[message]
    )

    # Create intent in Dialogflow agent
    response = client.create_intent(request={'parent': parent, 'intent': intent})

    print('✅ Intent created successfully: {}'.format(response.name))

create_service_selection_intent()
