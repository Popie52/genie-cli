import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types

from prompts import system_prompt
from model import call_model
from schemas import (
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
)

from history import load_history, save_history


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("API key not found")

    client = genai.Client(api_key=api_key)

    # parser = argparse.ArgumentParser(description="Chatbot")
    # parser.add_argument("user_prompt", type=str, help="User prompt")
    # parser.add_argument("--verbose", action="store_true",
    #                     help="Verbose output")
    # args = parser.parse_args()
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    messages = load_history()


    # messages.append(
    #     types.Content(
    #         role="user",
    #         parts=[types.Part(text=system_prompt)],
    #     ))

    print(f"Chat assistant ready! Type 'exit' to quit.\n")

    while True:
        try:

            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            messages.append(types.Content(
                role="user",
                parts=[types.Part(text=user_input)]))


            response_text = call_model(
                system_prompt=system_prompt,
                messages=messages,
                available_functions=available_functions,
                client=client
            )

            if response_text and "API quota exceeded" not in response_text:
                save_history(messages)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"Error: {e}")
            save_history(messages)
            print("History saved. You can restart the chat anytime.\n")
    


if __name__ == "__main__":
    main()
