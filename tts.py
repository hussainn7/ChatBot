import time
import sounddevice as sd
import torch

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000  # 48000
speaker = 'aidar'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu

# Load the TTS model
model, _ = torch.hub.load(
    repo_or_dir='snakers4/silero-models',
    model='silero_tts',
    language=language,
    speaker=model_id
)
model.to(device)


# Function to perform TTS and play the audio
def va_speak(what: str):
    audio = model.apply_tts(
        text=what + "..",
        speaker=speaker,
        sample_rate=sample_rate,
        put_accent=put_accent,
        put_yo=put_yo
    )

    # Adjust the volume factor as needed
    volume_factor = 1.0
    sd.play(volume_factor * audio, sample_rate * 1.05)

    # Wait for the audio to finish playing
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

# Example usage:
# va_speak("Хауди Хо, друзья!!!")