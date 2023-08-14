import json
import logging
import os

import openai
import tenacity

from llm_response import LLMResponse

logger = logging.getLogger(__name__)


class OpenAIProcessor:

    @tenacity.retry(
        stop=tenacity.stop_after_attempt(5),
        wait=tenacity.wait_random_exponential(max=30),
        retry=(tenacity.retry_if_exception_type(openai.error.OpenAIError)),
        reraise=True,
        before_sleep=tenacity.before_sleep_log(logger, logging.DEBUG)
    )
    async def agenerate_details(self, input_text, prompt, extraction_function):
        messages = [
            {"role": "system",
             "content": f'''{prompt}'''},

            {"role": "user",
             "content": "messages: " + json.dumps(input_text)},
        ]
        openai_api_key = os.getenv('OPENAI_API_KEY')
        response = await openai.ChatCompletion.acreate(
            model='gpt-3.5-turbo-16k',
            messages=messages,
            functions=extraction_function,
            function_call='auto',
            temperature=0.4,
            api_key=openai_api_key
        )
        response_message = response["choices"][0]["message"]
        if response_message.get("function_call"):
            response_text = response_message["function_call"].arguments
            print(f'FUNCTION CALL RESULT: {response_text}')
            return LLMResponse(text=response_text,
                               finish_reason=response["choices"][0]["finish_reason"],
                               total_tokens=response["usage"]["total_tokens"])
        else:
            return None
