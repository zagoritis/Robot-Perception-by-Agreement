from twisted.internet.defer import inlineCallbacks

@inlineCallbacks
def perform_non_verbal_cue(session, action):
    try:
        #AGREE:
        if action == "nod_agreement":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": 0.2}},
                {"time": 1000, "data": {"body.head.pitch": 0.0}}
            ])
            
        elif action == "double_nod_agreement":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 300, "data": {"body.head.pitch": 0.1}},
                {"time": 600, "data": {"body.head.pitch": 0.0}},
                {"time": 900, "data": {"body.head.pitch": 0.1}},
                {"time": 1200, "data": {"body.head.pitch": 0.0}}
            ])

        elif action == "nod_slightly":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": 0.05}},
                {"time": 1000, "data": {"body.head.pitch": 0.0}}
            ])
            
        elif action == "agree_eyes":
            yield session.call("rom.actuator.light.write", frames=[
                {"time": 100, "data": {"body.head.eyes": [0, 255, 0]}},
                {"time": 300, "data": {"body.head.eyes": [255, 255, 255]}},
                {"time": 700, "data": {"body.head.eyes": [0, 255, 0]}},
                {"time": 1000, "data": {"body.head.eyes": [255, 255, 255]}}
            ])
       
        # elif action == "thumbs_up":
        #     yield session.call("rom.optional.behavior.play", name="BlocklyArmsForward")
        #     yield session.call("rom.optional.behavior.play", name="BlocklyHappy")
        #     yield session.call("rom.optional.behavior.play", name="BlocklyStand")

        # elif action == "happy":
        #     yield session.call("rom.optional.behavior.play", name="BlocklyHappy")
        #     yield session.call("rom.optional.behavior.play", name="BlocklyStand")

        elif action == "clap":
            yield session.call("rom.optional.behavior.play", name="BlocklyApplause")
            yield session.call("rom.optional.behavior.play", name="BlocklyStand")
            
        #DISAGREE:
        elif action == "shake_head":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.yaw": -0.2}},
                {"time": 1000, "data": {"body.head.yaw": 0.2}},
                {"time": 1500, "data": {"body.head.yaw": 0.0}}
            ])
            
        elif action == "shake_head_fast":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 200, "data": {"body.head.yaw": -0.3}},
                {"time": 400, "data": {"body.head.yaw": 0.3}},
                {"time": 600, "data": {"body.head.yaw": -0.3}},
                {"time": 800, "data": {"body.head.yaw": 0.3}},
                {"time": 1000, "data": {"body.head.yaw": 0.0}}
            ])

        elif action == "shake_head_low":
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 500, "data": {"body.head.pitch": 0.2}},
            ])
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 800, "data": {"body.head.yaw": -0.1}},
                {"time": 1000, "data": {"body.head.yaw": 0.1}},
                {"time": 1200, "data": {"body.head.yaw": 0.0}}
            ])
            yield session.call("rom.actuator.motor.write", frames=[
                {"time": 1700, "data": {"body.head.pitch": 0.0}}
            ])
        
        elif action == "disagree_eyes":
            yield session.call("rom.actuator.light.write", frames=[
                {"time": 100, "data": {"body.head.eyes": [255, 0, 0]}},
                {"time": 1000, "data": {"body.head.eyes": [255, 255, 255]}}
            ])

        elif action == "point":
            yield session.call("rom.optional.behavior.play", name="BlocklyRightArmForward")
            yield session.call("rom.optional.behavior.play", name="BlocklyRightHandOpen")
            yield session.call("rom.optional.behavior.play", name="BlocklyStand")
            yield session.call("rom.optional.behavior.play", name="BlocklyStand")

        elif action == "shrug":
            yield session.call("rom.optional.behavior.play", name="BlocklyShrug")
            yield session.call("rom.optional.behavior.play", name="BlocklyStand")

        # elif action == "fear":
        #     yield session.call("rom.optional.behavior.play", name="BlocklyFearUp")
        #     yield session.call("rom.optional.behavior.play", name="BlocklyStand")
    
        else:
            print("No non-verbal action to perform.")
        
    except Exception as e:
        print(f"Error performing action '{action}': {e}")
        yield session.call("rie.dialogue.say", text="Oops, something went wrong with my gesture!")
