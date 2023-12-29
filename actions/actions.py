from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class GetWeather(Action):

    def name(self) -> Text:
        return "get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        weather = ['sunny', 'rainy', 'fog']
        dispatcher.utter_message(
            text=f"{random.choice(weather)}"
        )
        return []