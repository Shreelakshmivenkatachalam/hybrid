from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_TREFLE_API_KEY' with your actual Trefle API key
TREFLE_API_KEY = 'NNbitpMTANdUQ1Sq8cFYawkBScxufPPCxyu0kHBg74M'
TREFLE_API_BASE_URL = 'https://trefle.io/api/v1/plants'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get the user's search query from the form
    query = request.form.get('query')

    # Make a request to the Trefle API to search for plants based on the query
    response = requests.get(f'{TREFLE_API_BASE_URL}/search', params={'q': query, 'token': TREFLE_API_KEY})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract relevant information about the plants
        plants = data.get('data', [])

        # Render the search results in a template
        return render_template('search_results.html', plants=plants)
    else:
        # If the request was not successful, display an error message
        return f'Error fetching data from Trefle API: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)
