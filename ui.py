import customtkinter as ctk

class ChatbotUI:
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.root = ctk.CTk()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Chatbot")
        self.root.geometry("600x400")

        # Chat Window
        self.chat_window = ctk.CTkTextbox(self.root, state="disabled")
        self.chat_window.pack(fill="both", expand=True, padx=10, pady=10)

        # Input Field
        self.input_field = ctk.CTkEntry(self.root, placeholder_text="Type your message here...")
        self.input_field.pack(fill="x", padx=10, pady=5)

        # Send Button
        self.send_button = ctk.CTkButton(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self):
        prompt = self.input_field.get()
        if prompt:
            response = self.chatbot.respond(prompt)
            self.chat_window.configure(state="normal")
            self.chat_window.insert("end", f"You: {prompt}\nBot: {response}\n\n")
            self.chat_window.configure(state="disabled")
            self.input_field.delete(0, "end")

    def run(self):
        self.root.mainloop()
