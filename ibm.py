import json
from dotenv import load_dotenv
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions

load_dotenv()

authenticator = IAMAuthenticator(os.getenv('IBM'))
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(os.getenv('IBMURL'))

txt = input("Analyse: ")
targets = [input("Enter a target to measure emotions of: ")]
while True:
    t = input("Enter another target or enter to cancel: ")
    if t == "":
        break
    else:
        targets.append(t)

response = natural_language_understanding.analyze(
    text=txt,
    features=Features(emotion=EmotionOptions(targets=targets)),
    language="en",
).get_result()

print(json.dumps(response, indent=2))
