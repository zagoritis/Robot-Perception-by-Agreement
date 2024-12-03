from autobahn.twisted.component import Component, run
from non_verbal_cues import perform_non_verbal_cue
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from Topics import TOPICS
import random

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
    yield session.call("rie.dialogue.say_animated",
                       text="Hello! This is a test conversation to show you how the interaction should look like. For every question you have to give a firm answer YES or NO. Then you can elaborate more on this. This is the test question:")

    yield sleep(2)
    # Step 2: Select and handle topics
    # Yes, I like this pizza because It is tasty
    yield session.call(
        "rie.dialogue.ask",
        question="Do you like to eat salami pizza?",
        answers={"yes": ["yes", "yeah", "yep", "of course", "sure", "absolutely", "finally"],
                 "no": ["no", "nope", "not really", "nah", "never"]}
    )
    print("Answer heard...")
    yield sleep(4)
    yield session.call("rie.dialogue.say_animated", text="Here I would answer. And after that I would ask you more questions.")
    yield session.call("rie.dialogue.say_animated",
                       text="In the normal conversation, We will have conversation with 6 topics.")

    yield session.call("rie.dialogue.say_animated", text="This is the end of the test.")
    yield session.call("rom.optional.behavior.play", name="BlocklyCrouch")
    session.leave()


# Set up WAMP connection
wamp = Component(
    transports=[{
        "url": "ws://wamp.robotsindeklas.nl",
        "serializers": ["msgpack"]
    }],
    realm="rie.674ecb2501e236295c511afa"

)
wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])

