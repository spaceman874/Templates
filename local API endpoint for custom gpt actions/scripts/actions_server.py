# actions_server.py
# Version: 1.0

from flask import Flask, request, jsonify  # Import necessary modules from Flask and logging
import logging

app = Flask(__name__)  # Initialize the Flask application

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set up logging to display debug messages

@app.route('/testactions', methods=['POST'])  # Define a route for the '/testactions' endpoint, allowing POST requests
def test_actions():
    try:
        logging.debug("Received test actions request.")  # Log that a test action request was received
        return jsonify({"message": "Test went successfully!"}), 200  # Return a success message with a 200 status code
    except Exception as e:
        logging.error(f"Error processing test actions: {e}")  # Log any errors that occur
        return jsonify({"message": "Test unsuccessful! Is the server and localtunnel working?"}), 500  # Return an error message with a 500 status code

if __name__ == '__main__':  # Ensure this block runs only if the script is executed directly
    app.run(host='0.0.0.0', port=5000, debug=True)  # Start the Flask app on all IP addresses on port 5000 with debug mode enabled