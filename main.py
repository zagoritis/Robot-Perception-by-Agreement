from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
import random
from Topics import TOPICS
from non_verbal_cues import perform_non_verbal_cue

def interpret_response(response):
    """
    Categorize the user's response into 'yes', 'no', or 'neutral'.
    """
    positive = ["yes", "yeah", "yep", "of course", "sure", "absolutely"]
    negative = ["no", "nope", "not really", "nah", "never"]
    
    if any(word in response.lower() for word in positive):
        return "yes"
    elif any(word in response.lower() for word in negative):
        return "no"
    else:
        return "neutral"

@inlineCallbacks
def ask_with_clarification(session, question, retries=2):
    """
    Ask the user a question and clarify if the response is unclear.
    Retries are limited to avoid infinite loops.
    """
    attempts = 0
    while attempts <= retries:
        # Get user response
        raw_response = yield session.call(
            "rie.dialogue.ask",
            question=question,
            answers={"yes": ["yes", "yeah"], "no": ["no", "nope"]}
        )
        
        # Interpret the response
        user_response = interpret_response(raw_response)
        
        # Check if the response is clear
        if user_response in ["yes", "no"]:
            return user_response
        else:
            attempts += 1
            yield session.call("rie.dialogue.say", text="I didn't quite catch that. Could you say it again?")
    
    # If still unclear after retries, return neutral
    yield session.call("rie.dialogue.say", text="Let's move on for now.")
    return "neutral"

@inlineCallbacks
def handle_topic(session, topic):
    """
    Handle a single topic, including asking the main question and subtopics.
    """
    yield session.call("rie.dialogue.say", text=topic["question"])
    
    # Ask the main question
    user_response = yield ask_with_clarification(session, topic["question"])
    
    # Respond and perform gestures based on the response
    response_data = topic["responses"].get(user_response, topic["responses"]["neutral"])
    yield session.call("rie.dialogue.say", text=response_data["text"])
    if response_data.get("action"):
        yield perform_non_verbal_cue(session, response_data["action"])
    
    # Handle subtopics
    for subtopic in topic.get("subtopics", []):
        yield session.call("rie.dialogue.say", text=subtopic["question"])
        sub_response = yield ask_with_clarification(session, subtopic["question"])
        
        sub_response_data = subtopic["responses"].get(sub_response, subtopic["responses"]["neutral"])
        yield session.call("rie.dialogue.say", text=sub_response_data["text"])
        if sub_response_data.get("action"):
            yield perform_non_verbal_cue(session, sub_response_data["action"])


# Main interaction function
@inlineCallbacks
def main(session, details):
    
    print("Starting interaction...")
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")
    
    # Step 1: Greet the user
    yield session.call("rie.dialogue.say", text="Hello! Nice to meet you!")
    yield session.call("rom.optional.behavior.play", name="BlocklyWaveRightArm")
    
    # Step 2: Select and handle topics
    chosen_topics = random.sample(TOPICS, 3)
    for topic in chosen_topics:
        yield handle_topic(session, topic)
    
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
    