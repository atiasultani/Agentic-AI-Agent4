
import os
from openai import AsyncOpenAI 
from agents import Agent, OpenAIChatCompletionsModel
from agents.tracing import set_tracing_disabled
from dotenv import load_dotenv
from agents.run import Runner
import asyncio

load_dotenv()

MODEL_NAME="gemini-2.0-flash"
API_KEY=os.getenv("GEMINI_API_KEY")

External_client=AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=External_client
            )

set_tracing_disabled(True)

#Agents for different subjects
math_teacher= Agent(
    name="math_teacher",
    instructions="you are helping a student with math problems.",
    model = model
    )

physic_teacher= Agent(
    name="physic_teacher",
    instructions="you are helping a student with Physic problems.",
    model = model
    )

chemistery_teacher= Agent(
    name="chemistry_teacher",
    instructions="you are a Chemistery Teacher help a student.",
    model = model
    )

science_teacher= Agent(
    name="science_teacher",
    instructions="your name is {shushi} you are Teacher of a student in science subject.",
    model = model,
    )

#Main Agent that triages the student requests
#and hands off to the appropriate subject teacher

triage_agent=Agent(
        name="triage_agent",
        instructions= "You are a triage teacher. Decide which of the following agents should answer:\n"
        "- math_teacher: for mathematics or numbers\n"
        "- physic_teacher: for physics, motion, forces\n"
        "- chemistry_teacher: for chemistry, elements, reactions\n"
        "- science_teacher: for general science and biology\n"
        "If a question clearly belongs to one category, hand off to that agent by name.",
        model=model,
        handoffs=[math_teacher,physic_teacher,chemistery_teacher,science_teacher])
#Main function to run the triage agent
async def main():

    print("Hello from agentic-ai-agent4!")
    user_prompt=input("Enter your prompt: ")
    result= await Runner.run( 
        starting_agent=triage_agent,
        input=user_prompt,
          max_turns=10  )
    print(result.final_output) 
if __name__ == "__main__":
    asyncio.run(main())
