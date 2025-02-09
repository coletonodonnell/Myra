from audio.AUDIO import Say

import random

# Response system for stalling
STALLING_RESPONSES = [
    "Working on it...",
    "Just a moment...",
    "Processing...",
    "Give me a second...",
]
    

# Stall Response for the response system
def Stall():
    # Pick a random response
    Say(random.choice(STALLING_RESPONSES))
    pass