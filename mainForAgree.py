from autobahn.twisted.component import Component, run
from non_verbal_cues import perform_non_verbal_cue
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from Topics import TOPICS
from db_management import save_response
import random

study = False
user_name = None

def interpret_response(response):
    """
    Categorize the user's response into 'yes', 'no', or 'neutral'.
    """
    positive = ["yes", "yeah", "yep", "of course", "sure", "absolutely", "finally"]
    negative = ["no", "nope", "not really", "nah", "never"]

    if any(word in response.lower() for word in positive):
        return "yes"
    elif any(word in response.lower() for word in negative):
        return "no"
    else:
        return "neutral"


@inlineCallbacks
def ask_with_clarification(session, question, current_topic, current_subtopic=None, retries=2):
    """
    Ask the user a question and clarify if the response is unclear.
    Retries are limited to avoid infinite loops.
    """
    
    attempts = 0
    while attempts <= retries:
        speech_config = {"silence_timeout": 2.0}
        yield session.call("rie.dialogue.start_listening", speech_config)
        
        yield session.call("rie.dialogue.say", text=question)
        
        raw_response = yield session.call("rie.dialogue.stop_listening")
        user_response = interpret_response(raw_response)
        
        if user_response in ["yes", "no"]:
            
            save_response(
                    id=None,
                    user_id=user_name,
                    topic=current_topic["question"],
                    subtopic=current_subtopic["question"],
                    response=raw_response,
                    interpreted_response=user_response
                )
            
            return user_response
        else:
            attempts += 1
            yield session.call("rie.dialogue.say", text="I didn't quite catch that. Could you say it again?")
        
        yield session.call("rie.dialogue.say", text="Let's move on for now.")
        save_response(
                    id=None,
                    user_id=user_name,
                    topic=current_topic["question"],
                    subtopic=current_subtopic["question"],
                    response="Unclear",
                    interpreted_response="neutral"
                )
        return "neutral"

@inlineCallbacks
def handle_topic(session, topic, current_topic, current_subtopic=None):
    """
    Handle a single topic, including asking the main question and subtopics.
    """

    # Ask the main question
    user_response = yield ask_with_clarification(session, topic["question"], current_topic, current_subtopic)
        
    # Respond and perform gestures based on the response
    response_data = topic["responses"].get(user_response, topic["responses"]["neutral"])
    yield session.call("rie.dialogue.say", text=response_data["text"])
    if response_data.get("action"):
        yield perform_non_verbal_cue(session, response_data["action"])


# Main interaction function
@inlineCallbacks
def main(session, details):
    print("Starting interaction...")
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")

    print("Looking for a face...")
    yield session.call("rie.vision.face.find")

    perform_non_verbal_cue(session, "smile")

    # Step 1: Greet the user
    yield session.call("rom.optional.behavior.play", name="BlocklyWaveRightArm")
    yield session.call("rie.dialogue.say",
                       text="Hello! Nice to meet you! My name is little fella, I am a conversational agent. I will ask you some questions")
    yield sleep(5)
    # Step 2: Select and handle topics
    chosen_topics = random.sample(TOPICS, 3)
    for topic in chosen_topics:
        current_topic = topic
        
        x=yield handle_topic(session, topic, topic, None)
        # Handle subtopics

        if x == "yes":
            subtopic_response = "subtopics_Yes"
        elif x == "no":
            subtopic_response = "subtopics_No"

        for subtopic in topic[subtopic_response]:
            
            yield handle_topic(session, subtopic, topic, subtopic)
        

    # Step 3: Conclude the interaction
    yield session.call("rie.dialogue.say", text="Thank you for chatting with me! Goodbye!")
    yield session.call("rom.optional.behavior.play", name="BlocklyCrouch")
    session.leave()


# Set up WAMP connection
wamp = Component(
    transports=[{
        "url": "ws://wamp.robotsindeklas.nl",
        "serializers": ["msgpack"]
    }],
    realm="rie.6745a2ffbafa928f1e3a79d2"
)
wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
