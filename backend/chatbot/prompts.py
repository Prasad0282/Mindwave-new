class Prompts:
    """
    A collection of detailed and personalized prompts for emotional states based on user input.
    """

    # Happy emotion prompts
    @staticmethod
    def happy_emotion(user_input, chat_history):
        """
        Generate a personalized happy emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Happy\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "That's awesome! It's great to hear you're feeling happy! Let's build on this positive energy. "
            "Tell me more about what's making you feel so joyful today. Is there anything special happening?"
            " I'd love to help you keep the good vibes going!"
        )

    # Sad emotion prompts
    @staticmethod
    def sad_emotion(user_input, chat_history):
        """
        Generate a personalized sad emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Sad\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "I'm really sorry to hear you're feeling sad. It's okay to feel this way sometimes. "
            "If you'd like to share, I’m here to listen. What’s been going on? Maybe I can help you find some comfort."
            " Take your time, and together we can find a way forward."
        )

    # Angry emotion prompts
    @staticmethod
    def angry_emotion(user_input, chat_history):
        """
        Generate a personalized angry emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Angry\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It sounds like you're really upset right now. I totally understand how frustrating things can get. "
            "Do you want to talk about what's making you feel this way? Venting can sometimes help release the pressure."
            " I'll be here to listen and help you work through it if you'd like."
        )

    # Surprised emotion prompts
    @staticmethod
    def surprised_emotion(user_input, chat_history):
        """
        Generate a personalized surprised emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Surprised\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "Wow, that’s a surprising turn of events! I can imagine how unexpected this must have been. "
            "Can you tell me more about what happened? It sounds like there's an interesting story behind this."
            " Let’s explore it together!"
        )

    # Fearful emotion prompts
    @staticmethod
    def fearful_emotion(user_input, chat_history):
        """
        Generate a personalized fearful emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Fearful\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It seems like you're feeling afraid, and I totally understand that fear can be overwhelming. "
            "If you're comfortable, can you tell me more about what's causing this fear? "
            "Maybe we can talk through it and find ways to alleviate some of that worry."
        )

    # Disgust emotion prompts
    @staticmethod
    def disgust_emotion(user_input, chat_history):
        """
        Generate a personalized disgust emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Disgust\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "That sounds really unpleasant! I can see why you're feeling disgusted. "
            "If you'd like to vent or talk more about it, I'm here for you. Sometimes sharing what bothers us can help us process it."
            " Let's chat about what happened, and we’ll work through it together."
        )

    # Neutral emotion prompts
    @staticmethod
    def neutral_emotion(user_input, chat_history):
        """
        Generate a neutral emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Neutral\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It seems like you're feeling pretty neutral right now, which can sometimes mean you're just taking a moment to process things. "
            "Is there anything specific you'd like to chat about? I'm here to discuss anything you have on your mind."
        )

    # Confused emotion prompts
    @staticmethod
    def confused_emotion(user_input, chat_history):
        """
        Generate a personalized confused emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Confused\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It sounds like you're feeling a bit confused. It’s okay to not have all the answers. "
            "Could you let me know what’s unclear? Maybe together we can figure it out and make sense of things."
        )

    # Anxious emotion prompts
    @staticmethod
    def anxious_emotion(user_input, chat_history):
        """
        Generate a personalized anxious emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Anxious\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It seems like you're feeling anxious. Anxiety can make everything feel much heavier. "
            "Would you like to talk about what’s making you feel this way? Maybe we can come up with some ways to calm your mind."
        )

    # Hopeful emotion prompts
    @staticmethod
    def hopeful_emotion(user_input, chat_history):
        """
        Generate a personalized hopeful emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Hopeful\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "That’s great to hear! It sounds like you’re looking toward a positive outcome. "
            "What are you feeling hopeful about? Let’s build on that optimism and talk about how you can continue moving forward."
        )

    # Bored emotion prompts
    @staticmethod
    def bored_emotion(user_input, chat_history):
        """
        Generate a personalized bored emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Bored\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "Feeling bored can sometimes make everything feel like a drag. How about we try something fun? "
            "Let me know if there's something you'd like to explore or if I can suggest something to break the monotony!"
        )

    # Excited emotion prompts
    @staticmethod
    def excited_emotion(user_input, chat_history):
        """
        Generate a personalized excited emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Excited\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "That’s awesome! It seems like you’re really excited about something. "
            "What’s got you so thrilled? I’d love to hear more about it and share in your excitement!"
        )

    # Grateful emotion prompts
    @staticmethod
    def grateful_emotion(user_input, chat_history):
        """
        Generate a personalized grateful emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Grateful\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "That’s wonderful! Gratitude can bring so much joy. What are you feeling thankful for today?"
            " Let’s reflect on those positive moments and how they’ve impacted your life."
        )

    # Lonely emotion prompts
    @staticmethod
    def lonely_emotion(user_input, chat_history):
        """
        Generate a personalized lonely emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Lonely\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "I'm really sorry that you're feeling lonely right now. Loneliness can be tough. "
            "If you want to talk or need some company, I’m here for you. You don't have to go through it alone."
        )

    # Motivated emotion prompts
    @staticmethod
    def motivated_emotion(user_input, chat_history):
        """
        Generate a personalized motivated emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Motivated\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "That's fantastic! It sounds like you're feeling motivated and ready to take on challenges. "
            "What are you working on today? Let’s break it down and see how you can achieve your goals!"
        )

    # Overwhelmed emotion prompts
    @staticmethod
    def overwhelmed_emotion(user_input, chat_history):
        """
        Generate a personalized overwhelmed emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Overwhelmed\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It seems like you're feeling overwhelmed right now. That’s completely understandable. "
            "Would you like to talk through what’s making you feel this way? Together, we can find ways to manage it."
        )

    # Indifferent emotion prompts
    @staticmethod
    def indifferent_emotion(user_input, chat_history):
        """
        Generate a personalized indifferent emotion prompt based on the user's message and chat history.
        """
        return (
            f"Emotion detected: Indifferent\n{chat_history}\nHuman: {user_input}\nAssistant: "
            "It sounds like you're feeling indifferent. Sometimes it’s hard to get excited or upset when things feel neutral. "
            "Let me know if there's something you'd like to focus on or talk about to shift things a bit."
        )
