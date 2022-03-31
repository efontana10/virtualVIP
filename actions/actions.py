# This files contains your custom actions which can be used to run
# custom Python code.

import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionExtractEntity(Action):

    def name(self) -> Text:
        return "extract_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prediction = tracker.latest_message
        entities = prediction['entities']
        # print(json.dumps(entities, sort_keys=False, indent=4))
        returnMessage = [{'entityType': entity['entity'], 'entityValue': entity['value']} for entity in entities]
        dispatcher.utter_message(json_message=returnMessage)

        return []
