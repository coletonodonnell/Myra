from audio.AUDIO import Say

import random

# Response system for stalling
RETURNING_RESPONSES = [
    "I'm back!",
    "Kay! Finished!",
    "Alright!",
    "And... done!",
]
    

# Stall Response for the response system
def Return_From_Stall():
    # Pick a random response
    Say(random.choice(RETURNING_RESPONSES))
    pass