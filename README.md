# Agentic-AI-Agent4
cover topic basic of handoffs 

from agent import handoff 
math_teacher=Agent(name="" , instructoions="",handoff_description="spacialization of this agent is math teacher"),
physic_teacher=Agent(name="" , instructoions="",handoff_description="spacialization of this agent is physic teacher"),
science_teacher=Agent(name="" , instructoions="", handoff_description="spacialization of this agent is science teacher"),
triage_agent=Agent(
   name="triage_agent",
   instructions=" "You are a triage teacher. Your job is to choose the correct subject expert for the student.\n\n"
        "Handoff rules:\n"
        "- math_teacher: if the question is about mathematics, numbers, equations, or formulas.\n"
        "- physic_teacher: if the question is about physics, motion, forces, or energy.\n"
        "- chemistry_teacher: if the question is about chemistry, elements, compounds, or reactions.\n"
        "- science_teacher: if the question is about general science, biology, nature, or space.\n\n"
        "If the topic matches one of these, hand off the conversation to that agent by name." ,
     model=model,
    
    handoffs=[math_teacher, physic_teacher, chemistery_teacher, science_teacher]
)
