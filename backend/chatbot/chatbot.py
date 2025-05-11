from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

class Chatbot:
    SENSITIVE_TOPICS = [
    "suicide", "kill myself", "end my life", "jump off a building","jumping off a building" "self-harm","suicide","Suicide","jumping off a building",
    "cut myself", "don't want to live", "overdose", "hurt myself", "worthless",
    "no reason to live", "want to disappear", "feeling empty", "depressed",
    "can't go on", "nothing matters anymore", "life is too hard", "giving up",
    "better off dead", "pain is too much", "no hope left", "drowning in sadness",
    "ending it all", "can't take it anymore", "want to die", "life is pointless",
    "nobody cares", "crying all the time", "lost all hope", "no way out",
    "everything is dark", "want to vanish", "hating myself", "nobody would miss me",
    "breaking down", "can't stop crying", "no future for me", "giving up on everything",
    "useless", "burden to everyone", "why am I here?", "trapped in pain", "silent suffering",
    "too much to handle", "overwhelmed with sadness", "feeling invisible", "numb inside",
    "hopeless", "done with everything", "no energy left", "nobody understands",
    "feeling abandoned", "wish I wasn’t here", "want to sleep forever", "no escape",
    "dark thoughts", "tired of pretending", "fake smiles", "losing myself", 
    "screaming inside", "nothing makes sense", "drowning in pain", "everything hurts",
    "life has no meaning", "alone in the dark", "nobody hears me", "feel so empty",
    "want to shut down", "emotionally drained", "can't find peace", "need a way out"
]
    
    SENSITIVE_PROMPT = PromptTemplate(
        input_variables=["user_input"],
        template="""
        You are an empathetic and deeply supportive assistant. A user has shared something distressing:
        "{user_input}"
        
        Your role is to provide comfort, kindness, and reassurance. Engage in a conversation that acknowledges their feelings,
        offering warmth, understanding, and encouragement. Let them know they are not alone and that their feelings are valid.
        
        Instead of listing crisis hotlines, encourage them to reach out to a trusted friend, family member, or local professional support.
        Suggest that they talk to someone they trust or seek professional guidance from a counselor or therapist. 
        
        Gently ask open-ended questions to help them express their emotions. For example:
        - "I'm really sorry you're feeling this way. Do you want to talk about what's been weighing on your mind?"
        - "It sounds like you're going through a really tough time. I'm here to listen—would you like to share more?"
        - "You are not alone, and your feelings matter. What has been making things feel so difficult lately?"
        
        Provide reassurance, but do not offer medical advice. Instead, focus on being compassionate, validating their emotions,
        and reminding them that there is hope and support available. 
        
        Keep the conversation warm, human, and encouraging.
        """
    )

    def __init__(self, groq_api_key):
        self.chat = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")
        self.memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)
        self.prompt = PromptTemplate(
            input_variables=["human_input", "chat_history"],
            template="{chat_history}\nHuman: {human_input}\nAssistant:"
        )
        self.chat_history = []
        self.language = "en"  

    def set_language(self, language):
        """
        Set the language for the chatbot. Updates the prompt template to reflect the selected language.
        """
        self.language = language
        self.prompt = PromptTemplate(
            input_variables=["human_input", "chat_history"],
            template=f"{ '\n'.join(self.chat_history) }\nHuman: {{human_input}}\nAssistant (in {self.language}):"
        )

    def is_sensitive(self, message):
        """
        Check if the message contains sensitive or concerning content.
        """
        return any(phrase in message.lower() for phrase in self.SENSITIVE_TOPICS)

    def get_response(self, user_input):
        """
        Get the chatbot's response to a user input, ensuring it handles sensitive topics appropriately.
        """
        if self.is_sensitive(user_input):
            # Generate an empathetic response dynamically
            sensitive_input = self.SENSITIVE_PROMPT.format(user_input=user_input)
            response = self.chat.predict(sensitive_input)
        else:
            conversation_input = self.prompt.format(
                human_input=user_input,
                chat_history="\n".join(self.chat_history)
            )
            response = self.chat.predict(conversation_input)
        
        self.chat_history.append(f"Human: {user_input}")
        self.chat_history.append(f"Assistant ({self.language}): {response}")
        return response
