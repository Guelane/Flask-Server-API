# imports
from flask import Flask, request, jsonify

# Create an instance of Flask and assign it to a variable
app = Flask(__name__)


# Sample data to work with to test the functionality of our API
user_data = [
    {
        'user_id': 1,
        'user_name': 'User1',
        'prompt': 'Please provide feedback on our new product design.'
    },
    {
        'user_id': 2,
        'user_name': 'User2',
        'prompt': 'Describe your favorite travel destination.'
    },
    {
        'user_id': 3,
        'user_name': 'User3',
        'prompt': 'Share your thoughts on the latest technology trends.'
    },
    {
        'user_id': 4,
        'user_name': 'User4',
        'prompt': 'Write a short story about a detective solving a mystery.'
    },
    {
        'user_id': 5,
        'user_name': 'User5',
        'prompt': 'Discuss the impact of climate change on global ecosystems.'
    }
]


# Implement Logic for the base URL http://localhost:5000/v1/
@app.route("/v1/", methods=["GET", "POST"])
def index():
    """
    Handle GET and POST requests for the '/v1/' endpoint.

    - GET: Retrieves a list of user data in JSON format.
    - POST: Adds a new user to the user data list.

    Returns:
        - If GET: Returns a JSON list of user data with a 200 status code if users exist.
          Returns a 404 status code with a message if no users are found.
        - If POST: Adds a new user to the user data list and returns the updated user data
          in JSON format with a 201 status code if the request data is valid.
          Returns a 404 status code with an error message if the 'user' or 'prompt' fields
          in the form data are not strings.
    """
        
    # Handle GET requests
    if request.method == "GET":
        # Check if there are users in the user_data list
        if len(user_data) > 0:
            # If there are users, return them as JSON
            return jsonify(user_data), 200
        else:
            # If there are no users, return a message with a 404 status code
            return "There's no users, for now!", 404

    # Handle POST requests
    if request.method == "POST":
        # Check if the 'user' and 'prompt' fields in the form data are strings
        if isinstance(request.form['user'], str) and isinstance(request.form['prompt'], str):
            # Extract 'user' and 'prompt' from the form data
            new_user = request.form['user']
            new_prompt = request.form['prompt']
            
            # Generate a new user_id by incrementing the last user's user_id
            new_user_id = user_data[-1]['user_id'] + 1
            
            # Create a new dictionary with user information
            new_object = {
                'user_id': new_user_id,
                'user_name': new_user,
                'prompt': new_prompt
            }
            
            # Append the new user to the user_data list
            user_data.append(new_object)
            
            # Return the updated user_data as JSON
            return jsonify(user_data), 201
        else:
            # If 'user' or 'prompt' is not a string, return an error message with a 404 status code
            return "Please provide a string for User or Prompt", 404


# Entry point of the application
if __name__ == '__main__':
    # Start the Flask application in debug mode
    app.run(debug=True)

