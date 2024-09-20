from django.shortcuts import render
from .forms import InputForm
from .models import Conversation
from huggingface_hub import InferenceClient
import os
 
# Ensure dotenv is loaded
from dotenv import load_dotenv
load_dotenv()

# Fetch API token from environment variables
HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')

# Function to call Hugging Face API
def call_huggingface_api(user_input):
    # Initialize the client with the API token
    client = InferenceClient(token=HUGGINGFACE_API_TOKEN)
    
    # Prepare the input for the API
    input_json = {"inputs": user_input}
    
    # Make the request
    response = client.post(json=input_json, model="HuggingFaceH4/zephyr-7b-beta")
    
    # Decode the bytes response if needed
    response_str = response.decode('utf-8')
    
    # Process the response (assuming the format you're working with)
    processed_response = response_str[5:-4].split(sep=":")[1].strip()
    
    return processed_response

# Django view to handle form submission and save conversations
def index(request):
    user_input = None
    response = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            response = call_huggingface_api(user_input)
            
            # Save conversation to the database
            conversation = Conversation(user_input=user_input, model_response=response)
            conversation.save()

    else:
        form = InputForm()

    # Retrieve all conversations to display
    conversations = Conversation.objects.all().order_by('timestamp')

    return render(request, 'sde3.html', {'form': form, 'conversations': conversations})
