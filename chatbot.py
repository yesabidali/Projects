from google import genai

# Initialize the client with your API key
client = genai.Client(api_key="AIzaSyAz9UPz_Mk0buASgtUXnsq5uvn6qqy7otQ")

print("Welcome to the AI Chat! Type 'exit' to quit.")

while True:
    # Prompt the user for input
    user_input = input("You: ").strip()
    
    # If the user types 'exit', break out of the loop
    if user_input.lower() == "exit":
        print("Exiting chat. Goodbye!")
        break

    try:
        # Call the API with the user's input
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input
        )
        # Print the response from the API
        print("AI:", response.text)
    except Exception as e:
        # Print any error that occurs during the API call
        print("An error occurred:", e)