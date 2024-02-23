from channels.generic.websocket import WebsocketConsumer
from mimetypes import guess_extension



class FileExtensionConsumer(WebsocketConsumer):
    def connect(self):
        """
        Called when a WebSocket connection is established.
        """
        # Accept the WebSocket connection
        self.accept()

    def disconnect(self, close_code):
        """
        Called when a WebSocket connection is closed.
        """
        # No action needed when the connection is closed
        pass

    def receive(self, text_data):
        """
        Called when a message is received from the WebSocket.
        Extracts file extension from the received text data and sends it back.
        """
        # Extract file extension from the received text data
        file_extension = text_data.split(';')[0].split(':')[-1]

        # Send the extracted file extension back to the client
        self.send(text_data=f"{guess_extension(file_extension)}.")
