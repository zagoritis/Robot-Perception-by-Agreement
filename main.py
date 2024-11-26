from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
import random
from Topics import TOPICS

# Function to handle non-verbal cues
@inlineCallbacks
def perform_non_verbal_cue(session, action):
    try:
        if action == "nod_agreement":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": 0.1}},
                {"time": 1000, "data": {"body.head.pitch": 0.0}}
            ])
            
        elif action == "nod_slightly":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": 0.05}},
                {"time": 1000, "data": {"body.head.pitch": 0.0}}
            ])
            
        elif action == "shake_head":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.yaw": -0.2}},
                {"time": 1000, "data": {"body.head.yaw": 0.2}},
                {"time": 1500, "data": {"body.head.yaw": 0.0}}
            ])
            
        elif action == "tilt_forward":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": -0.1}},
                {"time": 1000, "data": {"body.head.pitch": 0.0}}
            ])
            
        elif action == "thumbs_up":
            #wokring?
            yield session.call("rom.actuator.motor.write", frames=[
            {"time": 500, "data": {
                "body.arm.right.shoulderPitch": -1.0,  # Arm parallel to ground
                "body.arm.right.shoulderRoll": 0.0,   # Arm straight out
                "body.hand.right.thumb": 0.0,         # Extend thumb
                "body.hand.right.index": 1.0,         # Close index finger
                "body.hand.right.middle": 1.0,        # Close middle finger
                "body.hand.right.ring": 1.0,          # Close ring finger
                "body.hand.right.little": 1.0}}       # Close little finger
            ])
            
        elif action == "smile":
            # Simulate a smile with an eye light pattern
            yield session.call("rom.actuator.light.write", frames=[
                {"time": 1000, "data": {"body.head.eyes": [0, 255, 0]}}
            ])
            
        elif action == "point":
            #working?
            yield session.call("rom.actuator.motor.write", frames=[
            {"time": 500, "data": {
                "body.arm.right.shoulderPitch": -1.0, # Arm parallel to ground
                "body.arm.right.shoulderRoll": 0.0,   # Arm straight out
                "body.hand.right.index": 0.0,         # Extend index finger
                "body.hand.right.thumb": 1.0,         # Close thumb
                "body.hand.right.middle": 1.0,        # Close middle finger
                "body.hand.right.ring": 1.0,          # Close ring finger
                "body.hand.right.little": 1.0}}       # Close little finger
            ])

        elif action == "look_around":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.yaw": 0.2}},
                {"time": 1000, "data": {"body.head.yaw": -0.2}},
                {"time": 1500, "data": {"body.head.yaw": 0.0}}
            ])
            
        elif action == "shrug":
            yield session.call("rom.optional.behavior.play", name="BlocklyShrug")
            
        elif action == "clap":
            #not working
            yield session.call("rom.actuator.motor.write", frames=[
            {"time": 500, "data": {
                "body.arm.right.shoulderPitch": 1.0,  # Bring hands together
                "body.arm.left.shoulderPitch": 1.0,
                "body.arm.right.shoulderRoll": 0.2,
                "body.arm.left.shoulderRoll": -0.2}},
            {"time": 800, "data": {
                "body.arm.right.shoulderPitch": 1.2,  # Pull hands slightly apart
                "body.arm.left.shoulderPitch": 1.2}},
            {"time": 1100, "data": {
                "body.arm.right.shoulderPitch": 1.0,  # Clap again
                "body.arm.left.shoulderPitch": 1.0}}
            ])

        elif action == "nod_clap":
            #working?
               yield session.call("rom.actuator.motor.write", frames=[
            {"time": 500, "data": {
                "body.head.pitch": 0.2,  # Nod down
                "body.arm.right.shoulderPitch": 1.0,  # Hands together
                "body.arm.left.shoulderPitch": 1.0}},
            {"time": 1000, "data": {
                "body.head.pitch": -0.2,  # Nod up
                "body.arm.right.shoulderPitch": 1.2,  # Hands apart
                "body.arm.left.shoulderPitch": 1.2}},
            {"time": 1500, "data": {
                "body.head.pitch": 0.0,  # Reset head
                "body.arm.right.shoulderPitch": 1.0,  # Clap again
                "body.arm.left.shoulderPitch": 1.0}}
            ])

        elif action == "look_around":
            #not working
            yield session.call("rom.actuator.motor.write", frames=[
            {"time": 1000, "data": {"body.head.yaw": 0.5}},  # Look left
            {"time": 2000, "data": {"body.head.yaw": -0.5}},  # Look right
            {"time": 3000, "data": {"body.head.yaw": 0.0}}   # Reset to center
            ])

        else:
            print("No non-verbal action to perform.")
            
    except Exception as e:
        print(f"Error performing action '{action}': {e}")
        yield session.call("rie.dialogue.say", text="Oops, something went wrong with my gesture!")


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
