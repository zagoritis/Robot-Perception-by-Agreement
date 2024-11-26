from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
import random

# Define topics, subtopics, and responses with non-verbal actions
TOPICS = [
    {
        "question": "Do you enjoy reading books to relax?",
        "subtopics": [
            {
                "question": "Do you think reading in the evening is better than in the morning?",
                "responses": {
                    "yes": {
                        "text": "Yes, I completely agree! Reading in the evening can be a nice way to wind down.",
                        "action": "nod_agreement"
                    },
                    "no": {
                        "text": "Exactly, it is such a great way to start the day by reading a book!",
                        "action": "nod_slightly"
                    },
                    "neutral": {
                        "text": "I see your point. I prefer reading in the evening. It helps me transition into relaxation.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "That's surprising. I feel like evening can make reading feel less productive.",
                        "action": "shake_head"
                    },
                    "disagree_no": {
                        "text": "Oh, I believe that evening reading feels more calming.",
                        "action": "tilt_forward"
                    }
                }
            },
            {
                "question": "Do you think reading books is more entertaining than reading mangas?",
                "responses": {
                    "yes": {
                        "text": "You are right! Books can make your imagination fly away!",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "I couldn't have said it better, BOMBOCLAT!",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "It depends on the mood. Books allow for deeper character development, while mangas are visually engaging.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "That's not true. Mangas have a unique way of combining visuals and storytelling.",
                        "action": "shake_head"
                    },
                    "disagree_no": {
                        "text": "You're wrong. Books let you dive into detailed worlds in your own way.",
                        "action": "tilt_forward"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that a minimalistic approach is good?",
        "subtopics": [
            {
                "question": "Do you think minimalism can help improve productivity?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Fewer distractions can help you focus and get more done.",
                        "action": "nod_agreement"
                    },
                    "no": {
                        "text": "That's true! Productivity depends on habits, not just the amount of clutter.",
                        "action": "slight_smile"
                    },
                    "neutral": {
                        "text": "Minimalism can improve productivity by creating a clean and organized environment.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I'm not convinced. Some people thrive in organized chaos.",
                        "action": "raise_eyebrow"
                    },
                    "disagree_no": {
                        "text": "I disagree! A minimalist workspace can make it easier to focus and stay on track.",
                        "action": "tilt_forward"
                    }
                }
            },
            {
                "question": "Do you think minimalism is sustainable in the long term?",
                "responses": {
                    "yes": {
                        "text": "Totally! Once you embrace it, it can become a lifestyle choice.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "Exactly! It can be tough to maintain minimalism over time.",
                        "action": "nod_slightly"
                    },
                    "neutral": {
                        "text": "Minimalism can be sustainable if integrated naturally into your lifestyle.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I'm not so sure. Over time, maintaining minimalism might become exhausting.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I disagree! Once it becomes a habit, minimalism can be sustainable and fulfilling.",
                        "action": "smile"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that playing games lowers your intelligence?",
        "subtopics": [
            {
                "question": "Do you think educational games are better than entertainment games?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Educational games are a great way to learn while having fun.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "That's true! Entertainment games can also stimulate creativity.",
                        "action": "nod_slightly"
                    },
                    "neutral": {
                        "text": "Educational games have their merits, especially for learning new skills.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I'm not sure. Entertainment games can also teach teamwork and strategy.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I disagree! Educational games have more structured learning benefits.",
                        "action": "tilt_forward"
                    }
                }
            },
            {
                "question": "Do you think limiting game time can improve intelligence?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! Limiting game time leaves room for other activities.",
                        "action": "nod_agreement"
                    },
                    "no": {
                        "text": "Exactly! It's about balance—games and intellectual activities together.",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "Limiting game time encourages diverse activities while keeping games positive.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I'm not sure. Intelligence depends on how you use that extra time.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I disagree! Setting boundaries on gaming can boost focus.",
                        "action": "tilt_forward"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that cooking at home is better than eating at a restaurant?",
        "subtopics": [
            {
                "question": "Do you think cooking at home is more enjoyable than dining out?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! There's something special about preparing a meal yourself.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "True! Dining out is a treat and can be more relaxing.",
                        "action": "slight_smile"
                    },
                    "neutral": {
                        "text": "Cooking at home can be rewarding, but dining out offers exploration.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I'm not convinced. Dining out is often more enjoyable.",
                        "action": "thoughtful"
                    },
                    "disagree_no": {
                        "text": "I disagree! Cooking is a therapeutic process for many.",
                        "action": "smile"
                    }
                }
            },
            {
                "question": "Do you think cost is the biggest factor in choosing between the two?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Cooking at home saves a lot of money in the long run.",
                        "action": "nod_agreement"
                    },
                    "no": {
                        "text": "That's true! Factors like taste and convenience matter more.",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "Cost is important, but so are convenience, health, and experience.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I'm not so sure. People often prioritize convenience or taste.",
                        "action": "skeptical"
                    },
                    "disagree_no": {
                        "text": "I disagree! Many prioritize cost savings by cooking at home.",
                        "action": "smile"
                    }
                }
            }
        ]
    }
]


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
            yield session.call("rom.optional.behavior.play", name="BlocklyRightArmUp")
        elif action == "smile":
            # Simulate a smile with an eye light pattern
            yield session.call("rom.actuator.light.write", frames=[
                {"time": 1000, "data": {"body.head.eyes": [0, 255, 0]}}  # Green light in the eyes
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


# Main interaction function
@inlineCallbacks
def main(session, details):
    print("Starting interaction...")
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")

    # Step 1: Detect user face
    print("Looking for a face...")
    yield session.call("rie.vision.face.find")
    yield session.call("rie.dialogue.say", text="Hello! Nice to meet you!")
    yield session.call("rom.optional.behavior.play", name="BlocklyWaveRightArm")

    # Step 2: Select and discuss 3 topics
    chosen_topics = random.sample(TOPICS, 3)
    for topic in chosen_topics:
        
        # Listen for user's response
        raw_response = yield session.call(
            "rie.dialogue.ask",
            question=topic["question"],
            answers={"yes": ["yes", "yeah"], "no": ["no", "nope"]}
        )

        # Categorize response dynamically
        user_response = interpret_response(raw_response)

        if user_response == "yes":
            yield session.call("rie.dialogue.say", text=topic["question"])#["yes"])
        elif user_response == "no":
            yield session.call("rie.dialogue.say", text=topic["question"])#["no"])
        else:
            ask_with_clarification() # Fix this

        # Step 3: React to response and handle subtopics
        for subtopic in topic.get("subtopics", []):
            yield session.call("rie.dialogue.say", text=subtopic["question"])
            
            sub_raw_response = yield session.call(
                "rie.dialogue.ask",
                question=topic["question"],
                answers={"yes": ["yes", "yeah"], "no": ["no", "nope"]}
            )

            # Categorize response dynamically
            sub_user_response = interpret_response(sub_raw_response)

            if sub_user_response == "yes":
                yield session.call("rie.dialogue.say", text=topic["question"]["yes"])
            elif sub_user_response == "no":
                yield session.call("rie.dialogue.say", text=topic["question"]["no"])
            else:
                ask_with_clarification() # Fix this

            response_data = subtopic["responses"].get(sub_user_response, subtopic["responses"]["neutral"])
            yield session.call("rie.dialogue.say", text=response_data["text"])
            if response_data["action"]:
                yield perform_non_verbal_cue(session, response_data["action"])

    # Step 4: Conclude the interaction
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
