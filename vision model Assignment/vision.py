from groq import Groq
import os
import streamlit as st
import dotenv
dotenv.load_dotenv()

key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# Set Up the Streamlit app
st.title("Welcome to the Vision Model App")
#for the image url
image_url = st.text_input("Enter the image URL:")
#Display the image


def describe_image(image_url):
    """
    Function to describe the image using the Groq API.
    """
    # Create a chat completion request to describe the image
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe this image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content
if image_url:
    st.image(image_url, caption='Image')
    # Call the describe_image function and display the result
    description = describe_image(image_url)
    st.write("Description of the image:")
    st.write(description)