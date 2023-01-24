from client import Client

c = Client("test", "test")

c.setAudioConnected(True)

c.send_audio()
