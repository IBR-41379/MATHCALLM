#!pip install --upgrade langchain
#!pip install openai
#!pip install -q --upgrade google-generativeai langchain-google-genai chromadb pypdf


import os
import json
from typing import Dict, List
import chainlit as cl
import autogen
from autogen.agentchat.contrib.math_user_proxy_agent import MathUserProxyAgent

config_list = [
    {
        "model": "gpt-3.5-turbo-16k",
        "api_key": "your_api_key_here"
    }
]

llm_config = {
    "timeout": 600,
    "seed": 42,
    "config_list": config_list,
}

MATH_SYSTEM_MESSAGE = """You are a helpful AI math assistant.
Solve mathematical tasks using your math and coding skills.
Solve the task step by step. Explain your plan first, then execute it step by step. Be clear which step uses code (if any), and which step uses your mathematical skill.
When using code, you must indicate the script type in the code block. Use Python for calculations when necessary.
When you find an answer, verify the answer carefully. Include your reasoning and calculations in your response.
Always provide a final, numerical answer to the problem.
Reply "TERMINATE" at the end when the math problem is completely solved with a final answer."""

assistant = autogen.AssistantAgent(
    name="math_assistant",
    system_message=MATH_SYSTEM_MESSAGE,
    llm_config=llm_config,
)

class MathUserProxyAgentWithMemory(MathUserProxyAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_history: List[Dict] = []

    def initiate_chat(self, recipient, problem: str, silent: bool = False):
        message = {
            "content": problem,
            "role": "user",
        }
        self.chat_history.append(message)
        
        full_response = ""
        while "TERMINATE" not in full_response:
            # Start or continue the conversation
            response = recipient.generate_reply(sender=self, messages=self.chat_history)

            print("-------------------\n", response, "\n-------------------")
            
            if response is not None:
                self.chat_history.append({"content": response, "role": "assistant"})
                full_response += response + "\n"
            else:
                response = "I apologize, but I couldn't generate a response. Could you please rephrase your question?"
                break
            
            # If the response doesn't end with TERMINATE, prompt for continuation
            if "TERMINATE" not in response:
                continuation_prompt = "Please continue solving the problem. If you've reached a final answer, end with TERMINATE."
                self.chat_history.append({"content": continuation_prompt, "role": "user"})
        
        return full_response

mathproxyagent = MathUserProxyAgentWithMemory(
    name="mathproxyagent",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False},
    llm_config=llm_config,
)

@cl.on_chat_start
async def math_chatbot():
    welcome_message = """
    **Welcome to MathCallm, our Math Problem Solver!** 🧮
    I am a math assistant. I can help you solve various math problems step-by-step.
    Please provide a math problem, and I'll do my best to solve it for you!
    """
    await cl.Message(content=welcome_message).send()

@cl.on_message
async def main(message: cl.Message):
    problem = message.content
    
    response = mathproxyagent.initiate_chat(assistant, problem=problem)
    
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()