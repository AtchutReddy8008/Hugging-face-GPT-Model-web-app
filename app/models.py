from django.db import models

class Conversation(models.Model):
    user_input = models.TextField()  # Stores the user's input
    model_response = models.TextField()  # Stores the AI response
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-generated timestamp

    def __str__(self):
        return f"Conversation at {self.timestamp}"
