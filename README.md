VOICE ACTIVATED GIS
Overview
	Voice Activated GIS is a cutting-edge application designed to enhance the interaction between users and geographic information systems (GIS) through voice commands. Leveraging modern web technologies and machine learning algorithms, this project enables users to explore geographical data and perform actions on maps simply by speaking commands.

 Architecture
The project is divided into three main components:
1.	Backend Server (Python + Flask): Handles incoming voice commands, processes them, and communicates with the frontend to update the map accordingly.
2.	Frontend Application (HTML, CSS, JavaScript, Leaflet): Provides the user interface for interacting with the map, including displaying map layers, markers, and handling user inputs.
3.	Voice Command Processing (Python): Utilizes speech recognition libraries to convert spoken words into actionable commands for the GIS
 Components
 Backend (app.py)

 Routes: Defines endpoints for receiving voice commands and rendering the initial map page.
 Voice Command Handling: Integrates with the VoiceRecognition.py module to process voice commands and determine appropriate actions.

 Frontend (index.html)

 User Interface: Implements a simple UI with a map displayed using Leaflet and buttons for initiating voice commands.
 Interactivity: Uses JavaScript to fetch voice commands from the backend, interpret them, and update the map accordingly.

Voice Command Processing (VoiceRecognition.py)

 Command Classification: Parses spoken commands to identify actions such as zooming, navigating, or adding/removing markers.
 Coordinate Extraction: Extracts geographical coordinates from spoken commands to pinpoint locations on the map.

 Functionalities

 Voice Commands: Users can speak commands to interact with the map, such as "zoom in," "navigate to [location]," or "add a marker."
 Map Interaction: Supports various map views (e.g., street view, satellite view) and allows users to add/remove markers based on voice instructions.
 Realtime Updates: The map dynamically updates in response to voice commands, providing a seamless user experience.

Getting Started

1. Prerequisites: Ensure Python is installed on your system along with Flask and other dependencies listed in requirements.txt.
2. Setup: Navigate to the project directory and run python setup.py to install all necessary packages.
3. Running the Application: Start the Flask server by running python app.py. The default browser will open the application URL.
4. Usage: Use the "Tap to Speak" button on the webpage to initiate voice commands. Follow the onscreen instructions to interact with the map.

 Development

Contributions to the project are welcome. Developers should familiarize themselves with the project structure and contribute by improving existing features or adding new functionalities.
