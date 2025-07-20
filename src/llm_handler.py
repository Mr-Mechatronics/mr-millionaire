"""GenAI LLM model API handler."""

import json
import os

from litellm import completion
from pydantic import BaseModel

from src.lib_constant import LLMConst


class LLMHandler:

    """LLM API handler."""

    def __init__(self) -> None:
        """Constructor for LLMHandler."""
        self.model = os.getenv(LLMConst.llm_model)

    def request_llm(self, request_prompt: str, structure: BaseModel = None) -> str | dict:
        """Request LLM model through API.

        Args:
            request_prompt (str): prompt to be sent to LLM.
            structure (BaseModel): expected output structure. Defaults to None.

        Returns:
            Union[str, dict]: response from LLM.

        """
        response = completion(
            model=self.model,
            messages=[self._construct_msg(prompt=request_prompt)],
            response_format=structure,
        )
        content = response.choices[0].message.content

        if structure:
            return json.loads(content)
        return content

    @staticmethod
    def _construct_msg(prompt: str) -> dict:
        """Construct llm message dict with prompt.

        Args:
            prompt (str): prompt to be sent to LLM.

        Returns:
            dict: message dict.

        """
        return {
            "role": "user",
            "content": prompt,
        }
