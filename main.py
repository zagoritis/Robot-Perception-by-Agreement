from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
import random

# Define topics, subtopics, and responses
TOPICS = [
    {
        "question": "Do you enjoy reading books to relax?",
        "subtopics": [
            {
                "question": "Do you think reading in the evening is better than in the morning?",
                "responses": {
                    "yes": "Yes, I completely agree! Reading in the evening can be a nice way to wind down. (Nods in agreement)",
                    "no": "Exactly, it is such a great way to start the day by reading a book! (Nods slightly)",
                    "neutral": "I see your point. I prefer reading in the evening. It helps me transition into relaxation.",
                    "disagree_yes": "That's surprising. I feel like evening can make reading feel less productive.",
                    "disagree_no": "Oh, I believe that evening reading feels more calming."
                }
            },
            {
                "question": "Do you think reading books is more entertaining than reading mangas?",
                "responses": {
                    "yes": "You are right! Books can make your imagination fly away!",
                    "no": "I couldn't have said it better, BOMBOCLAT!",
                    "neutral": "It depends on the mood. Books allow for deeper character development, while mangas are visually engaging.",
                    "disagree_yes": "That's not true. Mangas have a unique way of combining visuals and storytelling.",
                    "disagree_no": "You're wrong. Books let you dive into detailed worlds in your own way."
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
                    "yes": "Exactly! Fewer distractions can help you focus and get more done. (Nods approvingly)",
                    "no": "That's true! Productivity depends on habits, not just the amount of clutter. (Slight smile)",
                    "neutral": "Minimalism can improve productivity by creating a clean and organized environment. However, the effect depends on personal work styles.",
                    "disagree_yes": "I'm not convinced. Some people thrive in organized chaos. (Raises an eyebrow)",
                    "disagree_no": "I disagree! A minimalist workspace can make it easier to focus and stay on track. (Gestures thoughtfully)"
                }
            },
            {
                "question": "Do you think minimalism is sustainable in the long term?",
                "responses": {
                    "yes": "Totally! Once you embrace it, it can become a lifestyle choice. (Thumbs up)",
                    "no": "Exactly! It can be tough to maintain minimalism over time. (Nods slightly)",
                    "neutral": "Minimalism can be sustainable if integrated naturally into your lifestyle. However, it may feel restrictive for some, especially in certain phases of life.",
                    "disagree_yes": "I'm not so sure. Over time, maintaining minimalism might become exhausting. (Shrugs)",
                    "disagree_no": "I disagree! Once it becomes a habit, minimalism can be sustainable and fulfilling. (Smiles confidently)"
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
                    "yes": "Exactly! Educational games are a great way to learn while having fun. (Thumbs up)",
                    "no": "That's true! Entertainment games can also stimulate creativity and problem-solving. (Nods in agreement)",
                    "neutral": "Educational games have their merits, especially for learning new skills. But entertainment games can also be valuable for relaxation and social interaction.",
                    "disagree_yes": "I'm not sure. Entertainment games can also teach skills like teamwork and strategy. (Shrugs)",
                    "disagree_no": "I disagree! Educational games have more structured learning benefits. (Leans forward slightly)"
                }
            },
            {
                "question": "Do you think limiting game time can improve intelligence?",
                "responses": {
                    "yes": "Absolutely! Limiting game time leaves room for activities that enhance learning and creativity. (Nods approvingly)",
                    "no": "Exactly! It's about balance—playing games and pursuing other intellectual activities together. (Smiles understandingly)",
                    "neutral": "Limiting game time can help improve intelligence by encouraging diverse activities like reading or physical exercise. But games can still play a positive role when enjoyed in moderation.",
                    "disagree_yes": "I'm not sure. Even with more time, intelligence depends on how you use that extra time. (Shrugs)",
                    "disagree_no": "I disagree! Setting boundaries on gaming can boost focus and encourage more productive habits. (Leans forward slightly)"
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
                    "yes": "Absolutely! There's something special about preparing a meal yourself. (Thumbs up)",
                    "no": "True! Dining out is a treat and can be more relaxing. (Slight smile)",
                    "neutral": "Cooking at home can be rewarding and creative, but dining out offers a chance to explore new flavors and cuisines.",
                    "disagree_yes": "I'm not convinced. Dining out is often more enjoyable because of the ambiance and convenience. (Thoughtful look)",
                    "disagree_no": "I disagree! Cooking is a therapeutic process for many. (Nods confidently)"
                }
            },
            {
                "question": "Do you think cost is the biggest factor in choosing between the two?",
                "responses": {
                    "yes": "Exactly! Cooking at home saves a lot of money in the long run. (Nods)",
                    "no": "That's true! Factors like taste and convenience often matter more. (Agrees with a smile)",
                    "neutral": "Cost is an important factor, but so are convenience, health, and the overall experience of the meal.",
                    "disagree_yes": "I'm not so sure. People often prioritize convenience or taste over cost. (Skeptical tone)",
                    "disagree_no": "I disagree! For many, saving money by cooking at home is a top priority. (Smiles thoughtfully)"
                }
            }
        ]
    },
    {
        "question": "Do you think that sunny days are better for your mental health?",
        "subtopics": [
            {
                "question": "Do you think spending time outdoors is better on sunny days?",
                "responses": {
                    "yes": "Exactly! Sunshine and fresh air make for the perfect combination. (Thumbs up)",
                    "no": "Totally! Being outdoors is enjoyable no matter the weather. (Slight nod)",
                    "neutral": "Sunny days make outdoor activities more appealing for most people. However, rain or snow can also create unique experiences.",
                    "disagree_yes": "Not necessarily. Overcast or cool days can make outdoor activities feel more comfortable. (Thoughtful expression)",
                    "disagree_no": "I disagree! Sunny days encourage us to get outside and enjoy nature. (Smiles)"
                }
            },
            {
                "question": "Do you think weather significantly affects your productivity?",
                "responses": {
                    "yes": "I agree! Sunny days can energize you, while gloomy days might slow you down. (Nods in agreement)",
                    "no": "That's a great point! Productivity can depend more on your mindset than the weather. (Smiles)",
                    "neutral": "Weather can influence productivity, but it's not the only factor. Some people feel more driven on sunny days, while others focus better when it’s overcast.",
                    "disagree_yes": "I'm not sure about that. I think productivity is more about habit than weather. (Raises an eyebrow)",
                    "disagree_no": "I disagree! A sunny environment can really make you feel more motivated. (Gestures thoughtfully)"
                }
            }
        ]
    },
    {
        "question": "Do you think that traveling by plane is the best way to travel?",
        "subtopics": [
            {
                "question": "Do you think flying is more efficient than other forms of travel?",
                "responses": {
                    "yes": "Exactly! Flying saves so much time, especially for long distances. (Nods approvingly)",
                    "no": "That's true! Other forms of travel can be more enjoyable, but planes really win when it comes to efficiency. (Nods understandingly)",
                    "neutral": "Flying is often the most efficient way to travel for long distances. However, other methods like driving or taking the train might have their own advantages.",
                    "disagree_yes": "I'm not so sure. Flying can be stressful and sometimes less efficient when considering delays and security checks. (Shrugs slightly)",
                    "disagree_no": "I don't agree! Flying is hard to beat in terms of time-saving, especially for long-haul trips. (Smiles slightly)"
                }
            },
            {
                "question": "Do you think environmental impact should influence travel choices?",
                "responses": {
                    "yes": "Absolutely! Considering the carbon footprint of travel is so important. (Nods earnestly)",
                    "no": "I see your point. Not everyone has the flexibility to choose eco-friendly options. (Sympathetic nod)",
                    "neutral": "Environmental impact is an important factor in travel, but it often depends on individual priorities and alternatives.",
                    "disagree_yes": "I'm not sure. For many, convenience or cost might outweigh environmental concerns. (Shrugs)",
                    "disagree_no": "I don't agree! Reducing our travel footprint is crucial for the planet. (Gestures thoughtfully)"
                }
            }
        ]
    }
]

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
        yield session.call("rie.dialogue.say", text=topic["question"])

        # Listen for user's response
        user_response = yield session.call(
            "rie.dialogue.ask",
            question=topic["question"],
            answers={"yes": ["yes", "yeah"], "no": ["no", "nope"]}
        )

        # React to the response
        if user_response == "yes":
            yield session.call("rie.dialogue.say", text="That's great! Books can really help you relax.")
        elif user_response == "no":
            yield session.call("rie.dialogue.say", text="I understand! Reading isn't for everyone.")
        else:
            yield session.call("rie.dialogue.say", text="I'm sorry, I didn't quite catch that.")

        # Step 3: Discuss subtopics
        for subtopic in topic.get("subtopics", []):
            yield session.call("rie.dialogue.say", text=subtopic["question"])
            sub_response = yield session.call(
                "rie.dialogue.ask",
                question=subtopic["question"],
                answers={"yes": ["yes", "yeah"], "no": ["no", "nope"]}
            )

            if sub_response == "yes":
                yield session.call("rie.dialogue.say", text=subtopic["responses"]["yes"])
            elif sub_response == "no":
                yield session.call("rie.dialogue.say", text=subtopic["responses"]["no"])
            else:
                yield session.call("rie.dialogue.say", text=subtopic["responses"]["neutral"])

    # Step 4: Conclude the interaction
    yield session.call("rie.dialogue.say", text="Thank you for chatting with me! Goodbye!")
    yield session.call("rom.optional.behavior.play", name="BlocklyCrouch")
    session.leave()

# Set up WAMP connection
wamp = Component(
    transports=[{"url": "wss://wamp.robotsindeklas.nl", "serializers": ["msgpack"]}],
    realm="YOUR_REALM_HERE"
)
wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
