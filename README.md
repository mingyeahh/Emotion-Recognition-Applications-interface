# HAIID-part2
## About the Project
This is a coursework for Durham University Level 3 module of Human-AI Interaction Design. This project will install and utilise the API for emotion recognition application provided by IBM Watson® Natural Language Understanding and Google Vision AI.


## Getting Started
Here is how you could utilise the code.

### Prerequisites

* Python3 (including pip)
* Images files for analysis via Google Cloud Vision API


### Installation

1. Get API keys
* Get an API key and URL for IBM Watson® Natural Language Understanding. Please follow [Get Started Tutorial](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-getting-started) by IBM Watson® Natural Language Understanding.
* Get credentials for Google Cloud Vision AI. Please follow [Quickstarts Tutorial](https://cloud.google.com/vision/docs/quickstarts) by Google Vision API. This will result in a JSON file containing your credentials being downloaded.

2. Install ibm-watson
    ```sh
    pip install ibm-watson
    ```
3. Install google cloud vision
    ```sh
    pip install google-cloud
    ```
4. Install python-dotenv
    ```sh
    pip install python-dotenv
    ```

5. Clone the repo in the terminal
   ```sh
   git clone git@github.com:mingyeahh/HAIID-part2.git
   ```

6. Open a new file called `.env` in the directory `HAIID-part2`. Remember that this should be a private file that will store all the credentials.

7. Add your API keys to the `.env` file
   ```py
   IBM='ENTER YOUR IBM API KEY'
   IBMURL='ENTER YOUR IBM URL'
   GOOGLE_APPLICATION_CREDENTIALS='path/to/credentials_file.json'
   ```

<!-- USAGE EXAMPLES -->
## Usage
* To use the IBM Watson® Natural Language Understanding, go to the terminal and type:
    ```py
    python3 ibm.py
    ```
    and follow the instructions.

* To use Google Cloud Vision API, go to the terminal and type:
    ```py
    python3 googlevision.py path/to/imagefile.jpeg
    ```


