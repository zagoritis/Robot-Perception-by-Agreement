from autobahn.twisted.component import Component, run
from non_verbal_cues import perform_non_verbal_cue
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from Topics import TOPICS
import random

@inlineCallbacks
def ask_with_clarification(session, question, retries=2):
    """
    Ask the user a question and clarify if the response is unclear.
    Retries are limited to avoid infinite loops.
    """
    attempts = 0
    while attempts <= retries:
        # Get user response
        user_response = yield session.call(
            "rie.dialogue.ask",
            question=question,
            answers={"yes": ["yes", "yeah", "yep", "of course", "sure", "absolutely", "finally"],
                     "no": ["no", "nope", "not really", "nah", "never"]}
        )
        print("Answer heard...")
        z = input()
        if z == "y":
            return "yes"
        # Check if the response is clear
        elif z == "n":
            return "no"
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

    user_response = yield ask_with_clarification(session, topic["question"])

    response_data = topic["responses"].get("neutral", topic["responses"]["neutral"])

    yield session.call("rie.dialogue.say_animated", text=response_data["text"])
    return user_response


# Main interaction function
@inlineCallbacks
def main(session, details):
    yield session.call("rom.actuator.audio.volume", volume=60)
    print("Starting interaction...")
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")

    print("Looking for a face...")
    yield session.call("rie.vision.face.find")

    # Step 1: Greet the user
    yield session.call("rom.optional.behavior.play", name="BlocklyWaveRightArm")
    yield session.call("rie.dialogue.say",
                       text="Hello! Nice to meet you! My name is Nao, but you can call me little fella, I am a conversational agent. I will ask you some questions")
    yield sleep(2)
    # Step 2: Select and handle topics
    chosen_topics = random.sample(TOPICS, 3)
    i = 0
    for topic in chosen_topics:
        yield handle_topic(session, topic)
        random_subtopic = random.choice(["subtopics_Yes", "subtopics_No"])

        yield sleep(1.5)
        for subtopic in topic[random_subtopic]:
            yield handle_topic(session, subtopic)
        yield sleep(1.5)
        if i == 0:
            yield session.call("rie.dialogue.say", text="Let's go with another question.")
            yield sleep(2)
        if i == 1:
            yield session.call("rie.dialogue.say", text="No we are heading for the final question.")
            yield sleep(2)
        i += 1

    yield session.call("rie.dialogue.say", text="Thank you for chatting with me! Goodbye!")
    yield session.call("rom.optional.behavior.play", name="BlocklyCrouch")
    session.leave()


# Set up WAMP connection
wamp = Component(
    transports=[{
        "url": "ws://wamp.robotsindeklas.nl",
        "serializers": ["msgpack"]
    }],
    realm="rie.6751703401e236295c512e0b"
)
wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])

