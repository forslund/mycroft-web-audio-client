from threading import Thread

from mycroft.stt import STTFactory
from mycroft.configuration import Configuration
from mycroft.util.log import LOG
from mycroft.messagebus.client import MessageBusClient
from mycroft.messagebus.message import Message
import speech_recognition as sr

authors = ["forslund", "jarbas"]

ws = None
config = Configuration.get()


def connect():
    ws.run_forever()


def read_wave_file(wave_file):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(wave_file) as source:
        audio = r.record(source)
    return audio


class FileConsumer:
    def __init__(self, emitter=None):
        super(FileConsumer, self).__init__()
        self.stt = None
        self.emitter = emitter
        LOG.info("Creating SST interface")
        self.stt = STTFactory.create()

    def handle_audio(self, audiofile):
        audio = read_wave_file(audiofile)
        text = self.stt.execute(audio).lower().strip()
        self.emitter.emit(
            Message("recognizer_loop:utterance",
                    {"utterances": [text]},
                    {"source": "wav_client"}))


ws = MessageBusClient()
config = Configuration.get()
Configuration.set_config_update_handlers(ws)
event_thread = Thread(target=connect)
event_thread.setDaemon(True)
event_thread.start()
file_consumer = FileConsumer(emitter=ws)
