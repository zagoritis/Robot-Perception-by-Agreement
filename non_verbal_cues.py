from twisted.internet.defer import inlineCallbacks

@inlineCallbacks
def perform_non_verbal_cue(session, action):
    try:
        if action == "nod_agreement":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": 0.2}},
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
        
        elif action == "agree_eyes":
            yield session.call("rom.actuator.light.write", frames=[
                {"time": 1000, "data": {"body.head.eyes": [0, 255, 0]}},
                {"time": 1000, "data": {"body.head.eyes": [255, 255, 255]}}
            ])
        
        elif action == "disagree_eyes":
            yield session.call("rom.actuator.light.write", frames=[
                {"time": 1000, "data": {"body.head.eyes": [255, 0, 0]}},
                {"time": 1000, "data": {"body.head.eyes": [255, 255, 255]}}
            ])

        elif action == "thumbs_up":
            yield session.call("rom.optional.behavior.play", name="BlocklyArmsForward")
        
        elif action == "point":
            yield session.call("rom.optional.behavior.play", name="BlocklyRightArmForward")
        
        elif action == "shrug":
            yield session.call("rom.optional.behavior.play", name="BlocklyShrug")
            
        elif action == "clap":
            yield session.call("rom.optional.behavior.play", name="BlocklyApplause")
        
        elif action == "look_around":
            yield session.call("rom.optional.motor.write", frames=[
                {"time": 1000, "data": {"body.head.yaw": 0.8}},
                {"time": 500, "data": {"body.head.pitch": -0.1}},
                {"time": 500, "data": {"body.head.pitch": 0.0}},
                {"time": 4000, "data": {"body.head.yaw": -0.8}},
                {"time": 500, "data": {"body.head.pitch": 0.1}},
                {"time": 500, "data": {"body.head.pitch": 0.0}},
                {"time": 7000, "data": {"body.head.yaw": 0.0}}
            ])

        else:
            print("No non-verbal action to perform.")
            
    except Exception as e:
        print(f"Error performing action '{action}': {e}")
        yield session.call("rie.dialogue.say", text="Oops, something went wrong with my gesture!")
