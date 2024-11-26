from twisted.internet.defer import inlineCallbacks

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
            
        #WRONG
        elif action == "thumbs_up":
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
            
        #WRONG
        elif action == "point":
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
            
        elif action == "shrug":
            yield session.call("rom.optional.behavior.play", name="BlocklyShrug")
            
        #WRONG
        elif action == "clap":
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

        #WRONG
        elif action == "nod_clap":
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