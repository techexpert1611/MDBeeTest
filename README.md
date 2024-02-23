# File Extension Service

This project provides WebSocket service using Django, facilitating the secure transmission of files from clients to the server. The server will analyze the received files, identify their extensions, and promptly communicate this information back to the client.

## Prerequisites

Before getting started, ensure that you have Python and pip installed on your system. You can download and install Python from [the official Python website](https://www.python.org/downloads/), which typically includes pip.

## Installation

1. **Clone the repository:** 
2. **Navigate to the root directory** of the cloned repository where the `requirements.txt` file is located.
3. **Create a virtual environment:** 
   ```bash
   python -m venv myenv  # Replace 'myenv' with your preferred name for the virtual environment
4. **Activate the virtual environment:**
   1. *On Windows:* `myenv\Scripts\activate`
   2. *On macOS and Linux:* `source myenv/bin/activate`
5. **Install dependencies:** `pip install -r requirements.txt`

The WebSocket service will be available at `ws://127.0.0.1:8000/ws/file_extension/`.

## Usage

- **To run the development server:** Navigate to the root directory of the project and run `python manage.py runserver`.


## Configuration

- `file_extension.routing`: Contains WebSocket URL patterns for routing WebSocket connections to the appropriate consumers.
- `FileExtensionConsumer`: Consumer class responsible for handling WebSocket connections and extracting file extensions.

## ASGI Configuration

The ASGI configuration file (`asgi.py`) routes WebSocket connections to the appropriate consumer using the `ProtocolTypeRouter` and `URLRouter`.

## Interaction with the WebSocket Service
The WebSocket service accepts connections from clients and provides the following functionality:
1. Accepts file input from clients. 
2. Converts the file input data into a base64 string and passes it to the WebSocket. 
3. Extracts file extensions from the received base64 string. 
4. Sends the extracted file extension back to the client.


## Security Measures
**Below can be the security concerns while doing the interaction with websocket:**
   - Use wss:// instead of ws:// for encrypted data transmission.

   - Implement strong authentication for authorized user connections.

   - Configure CORS to restrict connections to trusted domains.

   - Check file types/extensions to prevent malicious uploads.

   - Enforce file size limits to prevent resource exhaustion. .

## Assumptions

- Currently we are not using secure websocket connection as we have implemented this for local environment but in production by using wss://.
- As i mentioned on the security mesures we can use the authentication part to protect the websocket routes but as this was an brief requirement so currently i have not used it but for production environment we can implement it.