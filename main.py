from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
import random

@inlineCallbacks
def main(session, details):
    # Step 1: Greet and detect face
    print("Starting interaction...")
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")
    print("Looking for a face...")
    yield session.call("rie.vision.face.find")
    yield session.call("rie.dialogue.say", text="Hello! Nice to meet you!")
    yield session.call("rom.optional.behavior.play", name="BlocklyWaveRightArm")
    
    # Step 2: Introduce discussion topics
    topics = ["climate change", "artificial intelligence", "space exploration"]
    for _ in range(3):  # Discuss 3 topics
        topic = random.choice(topics)
        yield session.call("rie.dialogue.say", text=f"Let's talk about {topic}. What do you think?")
        
        # Step 3: Get user response
        answers = {"yes": ["yes", "yeah", "yep"], "no": ["no", "nope"]}
        user_response = yield session.call("rie.dialogue.ask", question=f"Do you like {topic}?", answers=answers)
        
        # Step 4: Respond based on input
        if user_response == "yes":
            yield session.call("rie.dialogue.say", text="That's great! I like it too.")
            yield session.call("rom.actuator.motor.write", frames=[{"time": 1000, "data": {"body.head.pitch": 0.1}}])
        elif user_response == "no":
            yield session.call("rie.dialogue.say", text="I see, that's an interesting perspective.")
            yield session.call("rom.actuator.motor.write", frames=[{"time": 1000, "data": {"body.head.pitch": -0.1}}])
        else:
            yield session.call("rie.dialogue.say", text="I'm sorry, I didn't quite understand.")
    
    # Step 5: End the interaction
    yield session.call("rie.dialogue.say", text="Thank you for chatting with me! Goodbye!")
    yield session.call("rom.optional.behavior.play", name="BlocklyCrouch")
    session.leave()

# Create wamp connection
wamp = Component(
    transports=[{"url": "wss://wamp.robotsindeklas.nl", "serializers": ["msgpack"]}],
    realm="YOUR_REALM_HERE"
)
wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])