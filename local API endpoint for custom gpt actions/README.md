# Setup and Configuration Guide for Test Actions API

### Step-by-Step Instructions

1. **Download the Required Files:**
   - Download the following files to a folder of your choosing:
     - `actions_server.py`
     - `action_schema.yaml`
     - `gpt_instructions.md`
     - `startserverandtunnel.bat`

2. **Install Python and Node.js (if not already installed):**
   - Python is needed to run the Flask server, and Node.js is needed to install LocalTunnel.
   - [Download and install Python](https://www.python.org/downloads/)
   - [Download and install Node.js](https://nodejs.org/)

3. **Start and Activate a Virtual Environment:**
   - A virtual environment helps manage dependencies and ensures they are isolated from other projects.
   - Open your command line or terminal.
   - Navigate to your project directory. If you don’t know how to navigate to your project directory, you can use the following methods:
     - **Windows:** Use `cd path\to\your\project`, where `path\to\your\project` is the path to your project folder. For example, `cd C:\Users\YourName\Projects\TestActions`.
     - **Mac/Linux:** Use `cd /path/to/your/project`, where `/path/to/your/project` is the path to your project folder. For example, `cd /Users/YourName/Projects/TestActions`.
   - Run the following commands to create and activate a virtual environment:
     - `python -m venv venv`
     - **Windows:** `venv\Scripts\activate`
     - **Mac/Linux:** `source venv/bin/activate`

4. **Install Flask:**
   - Flask is the web framework used to create the server.
   - Ensure your virtual environment is activated.
   - Run the following command to install Flask:
     - `pip install flask`

5. **Start the Server:**
   - Starting the server allows you to test if it is running correctly and ready to handle requests.
   - Ensure your virtual environment is activated.
   - Run the following command to start the Flask server:
     - `python actions_server.py`

6. **Edit Necessary Files:**
   - The .bat script and configuration files need to be updated with your unique URL string to ensure proper operation.
   - Open the following files in your text editor:
     - `startserverandtunnel.bat`
     - `action_schema.yaml`
     - `gpt_instructions.md`
   - Replace `changethistoyourcustomurl` with a random string of letters and numbers. Use `1a2b3c4d5e6f` as an example.

   **In `startserverandtunnel.bat`:**
   - Find the line: `start "LocalTunnel" cmd /k "lt --port 5000 --subdomain changethistoyourcustomurl"`
   - Replace it with: `start "LocalTunnel" cmd /k "lt --port 5000 --subdomain 1a2b3c4d5e6f"`

   **In `action_schema.yaml`:**
   - Find the line: `- url: https://changethistoyourcustomurl.loca.lt`
   - Replace it with: `- url: https://1a2b3c4d5e6f.loca.lt`

   **In `gpt_instructions.md`:**
   - Find the line: `- GPT sends POST to https://changethistoyourcustomurl.loca.lt/testactions.`
   - Replace it with: `- GPT sends POST to https://1a2b3c4d5e6f.loca.lt/testactions.`

7. **Save the Files:**
   - Saving the changes ensures the updates are applied and the scripts will use the correct URLs.

8. **Install LocalTunnel:**
   - LocalTunnel exposes your local server to the internet, making it accessible via a public URL.
   - Open a new tab in your command line or terminal.
   - Run the following command to install LocalTunnel globally:
     - `npm install -g localtunnel`

9. **Start LocalTunnel:**
   - Starting LocalTunnel makes your local server available on the internet through the specified subdomain.
   - Run the following command, replacing `1a2b3c4d5e6f` with your chosen string:
     - `lt --port 5000 --subdomain 1a2b3c4d5e6f`
   - **Note:** If your chosen subdomain is already in use, LocalTunnel will not work. You will need to choose a different, unique string.

10. **Test the Server:**
    - Testing ensures that the server and LocalTunnel are working correctly.
    - Open Command Prompt (cmd), not terminal.
    - Run the following CURL command, replacing `1a2b3c4d5e6f` with your chosen string:
      - `curl -X POST https://1a2b3c4d5e6f.loca.lt/testactions`
    - If the server responds with `{"message": "Test went successfully!"}`, the setup is correct.
    - If the server responds with `{"message": "Test unsuccessful! Is the server and localtunnel working?"}`, refer to the troubleshooting guide below.

11. **Configure Custom GPT:**
    - Configuring the GPT ensures it knows how to interact with your server.
    - Open the custom GPT configurator.
    - Copy the contents of `gpt_instructions.md` and `action_schema.yaml` into the respective sections of the configurator.
    - Add `/testactions` as a conversation starter.
    - **PLACEHOLDER IMAGE**: Add an image here showing how to copy and paste the contents into the configurator.

12. **Test GPT Actions:**
    - Testing ensures that the GPT can successfully interact with your server.
    - Ensure the server and LocalTunnel are running.
    - Use the conversation starter `/testactions` to test the actions.

### Troubleshooting Guide

If you receive a "Test unsuccessful! Is the server and localtunnel working?" message, follow these steps:

1. **Check the Server Status:**
   - Ensure the server is running. Verify this by checking the terminal or command prompt where the server started.
   - If the server is not running, navigate to the project directory and start the server using:
     - `python actions_server.py`

2. **Verify LocalTunnel Connection:**
   - Ensure LocalTunnel is connected and the tunnel URL is active. You should see a message indicating the tunnel URL (e.g., `https://1a2b3c4d5e6f.loca.lt`).
   - If LocalTunnel is not running, restart it using:
     - `lt --port 5000 --subdomain 1a2b3c4d5e6f`
   - Ensure the subdomain is unique and not already in use. If it is in use, choose a different string.

3. **Inspect Server Console Logs:**
   - Open the terminal or command prompt where the server is running.
   - Look for any error messages or logs indicating issues.
   - Common issues might include missing dependencies, incorrect configurations, or runtime errors.

4. **Check Dependencies:**
   - Ensure all required Python dependencies are installed. Run:
     - `pip list`
   - If any dependencies are missing, install them using:
     - `pip install -r requirements.txt`

5. **Verify Configuration Files:**
   - Double-check the `gpt_instructions.md`, `action_schema.yaml`, and `startserverandtunnel.bat` files to ensure they are correctly configured with the appropriate LocalTunnel URL and settings.
   - Ensure there are no typos or incorrect values. The lines should contain your unique string and not the example `1a2b3c4d5e6f` unless that is your chosen string.

6. **Provide Console Logs and Other Information to GPT for Troubleshooting:**
   - If you still cannot resolve the issue, provide the server console logs to the custom GPT for further assistance.
   - To copy the console logs, right-click on the terminal or command prompt window, select "Mark," highlight the text, and press Enter to copy it.
   - Paste the copied logs into the custom GPT along with any other relevant information to diagnose the issue.