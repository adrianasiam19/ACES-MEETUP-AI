from groq import Groq
import os
import streamlit as st
import dotenv
dotenv.load_dotenv()

key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
 
 #Set Up the Streamlit app
st.title("Chat with ME")
st.subheader("What's on your mind?")

#st.write("This is a simple chat app that uses the Groq API to generate completions.")

question = st.text_input("Ask a question:")
def request_answer(question):
    chat_completion = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": question,
        }
    ],

    # The language model which will generate the completion.
    model="llama-3.3-70b-versatile",

    #
    # Optional parameters
    #

    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=0.5,

    # The maximum number of tokens to generate. Requests can use up to
    # 32,768 tokens shared between prompt and completion.
    max_completion_tokens=1024,

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # likelihood-weighted options are considered.
    top_p=1,

    # A stop sequence is a predefined or user-specified text string that
    # signals an AI to stop generating content, ensuring its responses
    # remain focused and concise. Examples include punctuation marks and
    # markers like "[end]".
    stop=None,

    # If set, partial message deltas will be sent.
    stream=False,
)
    return chat_completion.choices[0].message.content
if question:
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking..."):
        answer = request_answer(question)
    with st.chat_message("assistant"):
        output = request_answer(question)
        st.write(output)
        #rint the completion returned by the LLM.
   