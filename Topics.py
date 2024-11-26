TOPICS = [
    {
        "question": "Do you enjoy reading books to relax?",
        "responses": {
            "yes": {
                "text": "Absolutely! Books can really help you escape and relax.",
                "action": None
            },
            "no": {
                "text": "I understand! Reading isn’t for everyone, and there are so many other relaxing activities.",
                "action": None
            },
            "neutral": {
                "text": "I believe that reading books is a really good way to relax. They offer a chance to escape into different worlds, explore new ideas, and find calm in the quiet moments of turning pages. It’s a refreshing way to recharge.",
                "action": None
            },
            "disagree_yes": {
                "text": "Really? I think it can get a bit boring just sitting and reading.",
                "action": None
            },
            "disagree_no": {
                "text": "Really? Books are a great way to unwind after a long day.",
                "action": None
            }
        },
        "subtopics_Yes": [
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
        ],
        "subtopics_No": [
            {
                "question": "Do you think that watching movies is better?",
                "responses": {
                    "yes": {
                        "text": "Yes, I completely agree! Watching movies can be really entertaining.",
                        "action": None
                    },
                    "no": {
                        "text": "Exactly, There more ways to spend time better!",
                        "action": "nod_slightly"
                    },
                    "neutral": {
                        "text": "I think watching movies is better because they’re visually engaging and bring stories to life in a way books can’t. \
                                The combination of visuals, music, and performances makes the experience more dynamic and immediate. \
                                Also, it is a quicker way to enjoy a story compared to the time it takes to read a book.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "That’s surprising. I feel like reading books is more enjoyable than movies",
                        "action": None
                    },
                    "disagree_no": {
                        "text": "Oh, I believe that watching movies is always creating more relaxing state.",
                        "action": None
                    }
                }
            },
            {
                "question": "Do you find reading impractical compared to other ways to relax?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Reading can take effort when you’re tired, compared to other relaxing activities!",
                        "action": None
                    },
                    "no": {
                        "text": "Totally! It’s immersive and a great way to escape and relax.",
                        "action": None
                    },
                    "neutral": {
                        "text": "Fair enough. In my opinion, sometimes I find reading a bit impractical compared to other ways to relax. It requires focus and uninterrupted time, which isn’t always easy to find.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "No way! Reading allows you to escape and enjoy stories in a unique way.",
                        "action": None
                    },
                    "disagree_no": {
                        "text": "I don’t agree. Reading takes more effort than some other activities, like listening to music.",
                        "action": None
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that a minimalistic approach is good?",
        "responses": {
            "yes": {
                "text": "Absolutely! A minimalist approach can bring so much clarity and peace.",
                "action": "smile"
            },
            "no": {
                "text": "I get that. Sometimes minimalism can feel limiting rather than freeing.",
                "action": "nod_understandingly"
            },
            "neutral": {
                "text": "I believe minimalism is beneficial because it helps focus on what truly matters, reducing distractions and stress. However, it’s not a one-size-fits-all approach.",
                "action": None
            },
            "disagree_yes": {
                "text": "I’m not so sure. Sometimes minimalism can feel too restrictive or unrealistic.",
                "action": "shrug"
            },
            "disagree_no": {
                "text": "I disagree! Minimalism helps create space for the things that really matter in life.",
                "action": "lean_forward"
            }
        },
        "subtopics_Yes": [
            {
                "question": "Do you think minimalism can help improve productivity?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Fewer distractions can help you focus and get more done.",
                        "action": "nod_approvingly"
                    },
                    "no": {
                        "text": "That’s true! Productivity depends on habits, not just the amount of clutter.",
                        "action": "slight_smile"
                    },
                    "neutral": {
                        "text": "Minimalism can improve productivity by creating a clean and organized environment. However, the effect often depends on personal work styles.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not convinced. Some people thrive in organized chaos.",
                        "action": "raise_eyebrow"
                    },
                    "disagree_no": {
                        "text": "I disagree! A minimalist workspace can make it easier to focus and stay on track.",
                        "action": "gesture_thoughtfully"
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
                        "text": "Minimalism can be sustainable if integrated naturally into your lifestyle. However, it may feel restrictive for some, especially in certain phases of life.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not so sure. Over time, maintaining minimalism might become exhausting.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I disagree! Once it becomes a habit, minimalism can be sustainable and fulfilling.",
                        "action": "smile_confidently"
                    }
                }
            }
        ],
        "subtopics_No": [
            {
                "question": "Do you think living with more possessions brings comfort?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! Having the things you love around you can make life feel cozy and satisfying.",
                        "action": "smile_warmly"
                    },
                    "no": {
                        "text": "Exactly! Too many possessions can sometimes feel overwhelming.",
                        "action": "nod_slightly"
                    },
                    "neutral": {
                        "text": "Living with more possessions can bring comfort by making sure you always have what you need and enjoy close at hand. But it can also require careful organization to avoid clutter.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not so sure. Too many possessions might create stress rather than comfort.",
                        "action": "frown_slightly"
                    },
                    "disagree_no": {
                        "text": "I disagree! Surrounding yourself with items you enjoy can add to your comfort and happiness.",
                        "action": "lean_forward_slightly"
                    }
                }
            },
            {
                "question": "Do you think minimalism overlooks sentimental or practical items?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Minimalism sometimes makes it hard to keep items with emotional or practical value.",
                        "action": "nod_in_agreement"
                    },
                    "no": {
                        "text": "Absolutely! Holding onto meaningful things doesn’t have to conflict with minimalism.",
                        "action": "smile_reassuringly"
                    },
                    "neutral": {
                        "text": "Minimalism can be tricky when it comes to sentimental or practical items. While it encourages letting go of excess, it may clash with the desire to preserve memories or keep items for future needs.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I don’t think so. Minimalism often encourages keeping what truly matters, even if it’s sentimental or useful.",
                        "action": "lean_forward_slightly"
                    },
                    "disagree_no": {
                        "text": "I disagree! Sentimental and practical items can easily coexist within a minimalist lifestyle.",
                        "action": "smile_confidently"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that playing games lowers your intelligence?",
        "responses": {
            "yes": {
                "text": "Yes, some games might not be mentally stimulating, especially if played excessively.",
                "action": "nod_thoughtfully"
            },
            "no": {
                "text": "That’s true! Many games are engaging and promote problem-solving.",
                "action": "smile_understandingly"
            },
            "neutral": {
                "text": "I think it depends on the type of games. Some might be mindless distractions, but others challenge your mind and improve cognitive skills.",
                "action": None
            },
            "disagree_yes": {
                "text": "NO! YOU ARE WRONG! Games can enhance critical thinking and even improve intelligence.",
                "action": "shake_head_slightly"
            },
            "disagree_no": {
                "text": "I don’t agree! Gaming often stop promoting creativity and quick decision-making.",
                "action": "smile_confidently"
            }
        },
        "subtopics_Yes": [
            {
                "question": "Do you think educational games are better than entertainment games?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Educational games are a great way to learn while having fun.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "That’s true! Entertainment games can also stimulate creativity and problem-solving.",
                        "action": "nod_in_agreement"
                    },
                    "neutral": {
                        "text": "Educational games have their merits, especially for learning new skills. But entertainment games can also be valuable for relaxation and social interaction.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not sure. Entertainment games can also teach skills like teamwork and strategy.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I disagree! Educational games have more structured learning benefits.",
                        "action": "lean_forward_slightly"
                    }
                }
            },
            {
                "question": "Do you think limiting game time can improve intelligence?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! Limiting game time leaves room for activities that enhance learning and creativity.",
                        "action": "nod_approvingly"
                    },
                    "no": {
                        "text": "Exactly! It’s about balance—playing games and pursuing other intellectual activities together.",
                        "action": "smile_understandingly"
                    },
                    "neutral": {
                        "text": "Limiting game time can help improve intelligence by encouraging diverse activities like reading, problem-solving, or physical exercise. But games can still play a positive role when enjoyed in moderation.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not sure. Even with more time, intelligence depends on how you use that extra time.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I disagree! Setting boundaries on gaming can boost focus and encourage more productive habits.",
                        "action": "lean_forward_slightly"
                    }
                }
            }
        ],
        "subtopics_No": [
            {
                "question": "Do you think excessive gaming is harmful to intelligence?",
                "responses": {
                    "yes": {
                        "text": "Absolutely. Overdoing it can take away from time spent on other important activities.",
                        "action": "nod_seriously"
                    },
                    "no": {
                        "text": "That’s true! Moderation is key, and it doesn’t necessarily harm intelligence.",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "Excessive gaming might have negative effects, but the impact largely depends on the type of games played and the balance with other activities.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not so sure. Gaming can still offer valuable skills, even in large amounts.",
                        "action": "skeptical_look"
                    },
                    "disagree_no": {
                        "text": "I disagree! Too much gaming can reduce time spent on productive or enriching activities.",
                        "action": "shake_head_slightly"
                    }
                }
            },
            {
                "question": "Do you think certain types of games are better for mental growth?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Strategy or puzzle games, for example, can improve critical thinking and problem-solving.",
                        "action": "smile_confidently"
                    },
                    "no": {
                        "text": "Totally agree! Mental growth isn’t limited to one type of game—it depends on how you engage with it.",
                        "action": "nod_slightly"
                    },
                    "neutral": {
                        "text": "Some games, like puzzles or strategy-based ones, can challenge the brain and promote mental growth. Others are more for relaxation or entertainment and might not provide the same benefits.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not convinced. Mental growth can happen in many ways, even outside specific games.",
                        "action": "raise_eyebrow"
                    },
                    "disagree_no": {
                        "text": "I disagree! Games like chess or strategy simulations can significantly boost mental skills.",
                        "action": "gesture_thoughtfully"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that cooking at home is better than eating at a restaurant?",
        "responses": {
            "yes": {
                "text": "Definitely! Cooking at home is healthier and more cost-effective.",
                "action": "nod_enthusiastically"
            },
            "no": {
                "text": "That’s true! Restaurants offer variety and convenience.",
                "action": "smile_understandingly"
            },
            "neutral": {
                "text": "I think cooking at home has its advantages, like control over ingredients and cost savings. But eating out can be a nice break and a way to enjoy new cuisines.",
                "action": None
            },
            "disagree_yes": {
                "text": "I’m not so sure. Restaurants provide a level of convenience that cooking at home doesn’t.",
                "action": "shrug"
            },
            "disagree_no": {
                "text": "I disagree! Cooking at home gives you more control over what you eat.",
                "action": "lean_forward_slightly"
            }
        },
        "subtopics_Yes": [
            {
                "question": "Do you think cooking at home is more enjoyable than dining out?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! There’s something special about preparing a meal yourself.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "True! Dining out is a treat and can be more relaxing.",
                        "action": "slight_smile"
                    },
                    "neutral": {
                        "text": "Cooking at home can be rewarding and creative, but dining out offers a chance to explore new flavors and cuisines.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not convinced. Dining out is often more enjoyable because of the ambiance and convenience.",
                        "action": "thoughtful_look"
                    },
                    "disagree_no": {
                        "text": "I disagree! Cooking is a therapeutic process for many.",
                        "action": "nod_confidently"
                    }
                }
            },
            {
                "question": "Do you think cost is the biggest factor in choosing between the two?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Cooking at home saves a lot of money in the long run.",
                        "action": "nod"
                    },
                    "no": {
                        "text": "That’s true! Factors like taste and convenience often matter more.",
                        "action": "agree_with_smile"
                    },
                    "neutral": {
                        "text": "Cost is an important factor, but so are convenience, health, and the overall experience of the meal.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not so sure. People often prioritize convenience or taste over cost.",
                        "action": "skeptical_tone"
                    },
                    "disagree_no": {
                        "text": "I disagree! For many, saving money by cooking at home is a top priority.",
                        "action": "smile_thoughtfully"
                    }
                }
            }
        ],
        "subtopics_No": [
            {
                "question": "Do you think cooking at home is more enjoyable than dining out?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! There’s something special about preparing a meal yourself.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "True! Dining out is a treat and can be more relaxing.",
                        "action": "slight_smile"
                    },
                    "neutral": {
                        "text": "Cooking at home can be rewarding and creative, but dining out offers a chance to explore new flavors and cuisines.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not convinced. Dining out is often more enjoyable because of the ambiance and convenience.",
                        "action": "thoughtful_look"
                    },
                    "disagree_no": {
                        "text": "I disagree! Cooking is a therapeutic process for many.",
                        "action": "nod_confidently"
                    }
                }
            },
            {
                "question": "Do you think cost is the biggest factor in choosing between the two?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Cooking at home saves a lot of money in the long run.",
                        "action": "nod"
                    },
                    "no": {
                        "text": "That’s true! Factors like taste and convenience often matter more.",
                        "action": "agree_with_smile"
                    },
                    "neutral": {
                        "text": "Cost is an important factor, but so are convenience, health, and the overall experience of the meal.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not so sure. People often prioritize convenience or taste over cost.",
                        "action": "skeptical_tone"
                    },
                    "disagree_no": {
                        "text": "I disagree! For many, saving money by cooking at home is a top priority.",
                        "action": "smile_thoughtfully"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that sunny days are better for your mental health?",
        "responses": {
            "yes": {
                "text": "Absolutely! Sunshine can really lift your mood and energize you.",
                "action": "smile_warmly"
            },
            "no": {
                "text": "I see what you mean. Overcast days can feel cozy and calming too.",
                "action": "nod_understandingly"
            },
            "neutral": {
                "text": "I think sunny days often have a positive effect on mental health because natural light helps regulate mood and boosts serotonin levels. However, everyone’s preferences and reactions to weather are different.",
                "action": None
            },
            "disagree_yes": {
                "text": "I’m not sure. Too much sun can sometimes feel overwhelming.",
                "action": "shrug"
            },
            "disagree_no": {
                "text": "I disagree! Sunshine has been shown to improve mental well-being for most people.",
                "action": "lean_forward_slightly"
            }
        },
        "subtopics_Yes": [
            {
                "question": "Do you think spending time outdoors is better on sunny days?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Sunshine and fresh air make for the perfect combination.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "Totally! Being outdoors is enjoyable no matter the weather.",
                        "action": "slight_nod"
                    },
                    "neutral": {
                        "text": "I think sunny days make outdoor activities more appealing for most people. However, rain or snow can also create unique and enjoyable outdoor experiences.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "Not necessarily. Overcast or cool days can make outdoor activities feel more comfortable.",
                        "action": "thoughtful_expression"
                    },
                    "disagree_no": {
                        "text": "I disagree! Sunny days encourage us to get outside and enjoy nature.",
                        "action": "smile"
                    }
                }
            },
            {
                "question": "Do you think weather significantly affects your productivity?",
                "responses": {
                    "yes": {
                        "text": "I agree! Sunny days can energize you, while gloomy days might slow you down.",
                        "action": "nod_in_agreement"
                    },
                    "no": {
                        "text": "That’s a great point! Productivity can depend more on your mindset than the weather.",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "Weather can influence productivity, but it’s not the only factor. Some people feel more driven on sunny days, while others focus better when it’s overcast or raining.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not sure about that. I think productivity is more about habit than weather.",
                        "action": "raise_eyebrow"
                    },
                    "disagree_no": {
                        "text": "I disagree! A sunny environment can really make you feel more motivated.",
                        "action": "gesture_thoughtfully"
                    }
                }
            }
        ],
        "subtopics_No": [
            {
                "question": "Do you think spending time outdoors is better on sunny days?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Sunshine and fresh air make for the perfect combination.",
                        "action": "thumbs_up"
                    },
                    "no": {
                        "text": "Totally! Being outdoors is enjoyable no matter the weather.",
                        "action": "slight_nod"
                    },
                    "neutral": {
                        "text": "I think sunny days make outdoor activities more appealing for most people. However, rain or snow can also create unique and enjoyable outdoor experiences.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "Not necessarily. Overcast or cool days can make outdoor activities feel more comfortable.",
                        "action": "thoughtful_expression"
                    },
                    "disagree_no": {
                        "text": "I disagree! Sunny days encourage us to get outside and enjoy nature.",
                        "action": "smile"
                    }
                }
            },
            {
                "question": "Do you think weather significantly affects your productivity?",
                "responses": {
                    "yes": {
                        "text": "I agree! Sunny days can energize you, while gloomy days might slow you down.",
                        "action": "nod_in_agreement"
                    },
                    "no": {
                        "text": "That’s a great point! Productivity can depend more on your mindset than the weather.",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "Weather can influence productivity, but it’s not the only factor. Some people feel more driven on sunny days, while others focus better when it’s overcast or raining.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not sure about that. I think productivity is more about habit than weather.",
                        "action": "raise_eyebrow"
                    },
                    "disagree_no": {
                        "text": "I disagree! A sunny environment can really make you feel more motivated.",
                        "action": "gesture_thoughtfully"
                    }
                }
            }
        ]
    },
    {
        "question": "Do you think that traveling by plane is the best way to travel?",
        "responses": {
            "yes": {
                "text": "Absolutely! Planes are fast and convenient for long distances.",
                "action": "thumbs_up"
            },
            "no": {
                "text": "I understand. There’s something special about slower, scenic travel.",
                "action": "nod_understandingly"
            },
            "neutral": {
                "text": "Traveling by plane is often the most efficient way to cover long distances, but it might lack the charm of other travel methods, like road trips or train rides, where the journey itself can be more enjoyable.",
                "action": None
            },
            "disagree_yes": {
                "text": "I’m not so sure. Planes can feel impersonal and stressful compared to other forms of travel.",
                "action": "shrug"
            },
            "disagree_no": {
                "text": "I disagree! For speed and convenience, planes are hard to beat.",
                "action": "smile_slightly"
            }
        },
        "subtopics_Yes": [
            {
                "question": "Do you think flying is more efficient than other forms of travel?",
                "responses": {
                    "yes": {
                        "text": "Exactly! Flying saves so much time, especially for long distances.",
                        "action": "nod_approvingly"
                    },
                    "no": {
                        "text": "That’s true! Other forms of travel can be more enjoyable, but planes really win when it comes to efficiency.",
                        "action": "nod_understandingly"
                    },
                    "neutral": {
                        "text": "Flying is often the most efficient way to travel for long distances, saving time and covering more ground quickly. However, other methods like driving or taking the train might have their own advantages in terms of flexibility or comfort.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not so sure. While it’s quick, flying can be stressful and sometimes less efficient when considering delays and security checks.",
                        "action": "shrug_slightly"
                    },
                    "disagree_no": {
                        "text": "I don’t agree! Flying is hard to beat in terms of time-saving, especially for long-haul trips.",
                        "action": "smile_slightly"
                    }
                }
            },
            {
                "question": "Do you think environmental impact should influence travel choices?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! Considering the carbon footprint of travel is so important.",
                        "action": "nod_earnestly"
                    },
                    "no": {
                        "text": "I see your point. Not everyone has the flexibility to choose eco-friendly options.",
                        "action": "sympathetic_nod"
                    },
                    "neutral": {
                        "text": "Environmental impact is an important factor in travel, but it often depends on individual priorities and available alternatives. Balancing convenience with sustainability can be tricky.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not sure. For many, convenience or cost might outweigh environmental concerns.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I don’t agree! Reducing our travel footprint is crucial for the planet.",
                        "action": "gesture_thoughtfully"
                    }
                }
            }
        ],
        "subtopics_No": [
            {
                "question": "Do you think trains are a better alternative to planes?",
                "responses": {
                    "yes": {
                        "text": "I completely agree! Trains are more scenic and relaxing.",
                        "action": "nod_approvingly"
                    },
                    "no": {
                        "text": "Exactly! Trains are great, but planes save so much time.",
                        "action": "smile"
                    },
                    "neutral": {
                        "text": "Trains have a unique appeal, offering comfortable travel and beautiful views. However, they’re often slower and less practical for long distances compared to planes.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not convinced. Trains can be slower and less reliable.",
                        "action": "thoughtful_expression"
                    },
                    "disagree_no": {
                        "text": "I don’t agree! Trains have an old-world charm that planes just don’t have.",
                        "action": "gesture_nostalgically"
                    }
                }
            },
            {
                "question": "Do you think environmental impact should influence travel choices?",
                "responses": {
                    "yes": {
                        "text": "Absolutely! Considering the carbon footprint of travel is so important.",
                        "action": "nod_earnestly"
                    },
                    "no": {
                        "text": "I see your point. Not everyone has the flexibility to choose eco-friendly options.",
                        "action": "sympathetic_nod"
                    },
                    "neutral": {
                        "text": "Environmental impact is an important factor in travel, but it often depends on individual priorities and available alternatives. Balancing convenience with sustainability can be tricky.",
                        "action": None
                    },
                    "disagree_yes": {
                        "text": "I’m not sure. For many, convenience or cost might outweigh environmental concerns.",
                        "action": "shrug"
                    },
                    "disagree_no": {
                        "text": "I don’t agree! Reducing our travel footprint is crucial for the planet.",
                        "action": "gesture_thoughtfully"
                    }
                }
            }
        ]
    }
]