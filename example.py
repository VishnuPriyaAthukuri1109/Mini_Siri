import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get the list of voices
voices = engine.getProperty('voices')

# Set the voice to a female voice (change index if needed)
engine.setProperty('voice', voices[1].id)  # Adjust index for the preferred voice

# Set the rate (speed) of speech
engine.setProperty('rate', 160)  # Lower value for slower speech, higher for faster

# Set the volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)  # Maximum volume

# Make the engine speak
engine.say("Hello! How can I assist you today?")

# Wait until the speech is finished
engine.runAndWait()
