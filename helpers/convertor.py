

from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

async def video_to_audio(video_file, audio_file):
    try:
        clip = VideoFileClip(video_file)
        clip.audio.write_audiofile(audio_file)
        print(f"Audio file saved as: {audio_file}")
    except Exception as e:
        print(f"Error converting video to audio: {e}")


async def audio_to_text(audio_file):
    AudioSegment.converter = os.path.abspath("./driver/ffmpeg.exe")
    recognizer = sr.Recognizer()
    wav_file = audio_file.replace('.mp3', '.wav')  # Ensure you're not overwriting the original

    try:
        audio = AudioSegment.from_file(audio_file)
        audio.export(wav_file, format='wav', parameters=["-ac", "1", "-ar", "16000"])

        if not os.path.exists(wav_file) or os.path.getsize(wav_file) == 0:
            raise ValueError("Exported WAV file is empty or not found.")

        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print("Transcription successful.")
            return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
    except Exception as e:
        print(f"Error processing audio file: {e}")
        if wav_file and os.path.exists(wav_file):
            os.remove(wav_file)


async def convertor(data):
    try:
        video_file = data.get('file')
        audio_file = os.path.join(os.path.dirname("./files/audio/"), 'audio.wav')
        if not os.path.exists(os.path.dirname(audio_file)):
            os.makedirs(os.path.dirname(audio_file))
        await video_to_audio(video_file, audio_file)
        text = await audio_to_text(audio_file)
        return { 'success': True, 'text': text }
    except Exception as e:
        print(f"Exception occurred (convertor): {e}")
        return { 'success': False }