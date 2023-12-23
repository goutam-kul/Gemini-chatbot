import streamlit as st

def main():
    st.title("ChatGPT Style UI")

    # Create a sidebar for user input
    user_input = st.text_area("You:", height=100)

    # Display chat history in the main section
    st.markdown("---")
    st.header("Chat History")

    # Example bot response
    bot_response = get_bot_response(user_input)

    # Update chat history
    update_chat_history(user_input, bot_response)

def get_bot_response(user_input):
    # Replace this function with your actual chat bot logic
    # For simplicity, it just echoes the user's message
    return f"Bot: You said '{user_input}'"

def update_chat_history(user_input, bot_response):
    # Display user's message
    st.markdown(f"**You:** {user_input}")

    # Display bot's response
    st.markdown(f"**Bot:** {bot_response}")

if __name__ == "__main__":
    main()
