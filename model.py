from google.genai import types
from call_function import call_function
from google.genai.errors import ClientError
from quota import is_quota_blocked, save_quota_block


def call_model(
    system_prompt,
    messages,
    available_functions,
    client,
    verbose=False,
    max_iter=5,
):
    blocked, blocked_until = is_quota_blocked()

    if blocked:
        msg = f"🚨 API quota exceeded. Try again after {blocked_until.strftime('%Y-%m-%d %H:%M:%S')}"
        print(msg)
        return msg

    try:
        while True:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt,
                ),
            )

            if not response.candidates:
                raise RuntimeError("🚨 No response from model")

            # add model responses to conversation
            # Here we are updating the message itself
            for candidate in response.candidates:
                messages.append(candidate.content)

            # handle tool calls
            if response.function_calls:
                for function_call in response.function_calls:
                    function_call_result = call_function(
                        function_call, verbose=verbose
                    )

                    if not function_call_result.parts:
                        continue
                        # raise RuntimeError("Function call returned no parts")

                    function_response = function_call_result.parts[0].function_response

                    # if function_response is None or function_response.response is None:
                    #     raise RuntimeError("Function response missing")

                    if verbose and function_response:
                        print(f"-> {function_response.response}")

                    # function_parts.append(function_call_result.parts[0])

                    messages.append(
                        types.Content(
                            role="user",
                            parts=[function_call_result.parts[0]]
                        )
                    )

            else:
                print(f"Prompt Results:")
                print(response.text)
                print()
                return response.text
                
    except ClientError as e:
        if "RESOURCE_EXHAUSTED" in str(e):
            save_quota_block()  
            msg = "🚨 API quota exceeded. Please try again after 24 hours."
            print(msg)
            return msg
        else:
            raise