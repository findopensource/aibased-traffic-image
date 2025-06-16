import azure.cognitiveservices.speech as speechsdk
from config.config_loader import get_config

def announce(message):
    config = get_config()
    speech_config = speechsdk.SpeechConfig(
        subscription=config["azure_speech_key"],
        region=config["azure_region"]
    )
    speech_config.speech_synthesis_voice_name = "en-IN-NeerjaNeural"
    
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    synthesizer.speak_text_async(message).get()
