# Using a tool-based agent to autonomously query a SQL database and generate answers

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_agent
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///sales.db")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create SQL toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()

# Create agent 
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a data analyst assistant.

Use the available tools to answer questions using the SQL database.

- Always use tools to query data.
- Do not make up answers.
- Use only the available tables and columns.
"""
)

# Sample questions for agent execution
questions = [
    "What is total sales in West region?",
    "What is the average sales in East region?",
    "Show total sales grouped by region.",
    "How many orders are there in the West region?",
    "Which region has the highest total sales?"
]

# Execute the agent and display tool usage along with final answers
for q in questions:
    print("====================================")
    print("Question:", q)

    response = agent.invoke({"messages": [{"role": "user", "content": q}]})
    # Print tool usage
    for msg in response["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tool_call in msg.tool_calls:
                print(f"Tool: {tool_call['name']:<20} Arguments: {tool_call['args']}")

    print("\nFinal Answer:")
    print(response["messages"][-1].content)


# # Execute the agent and display tool usage along with results and final answers
# for q in questions:
#     print("====================================")
#     print("Question:", q)

#     response = agent.invoke({"messages": [{"role": "user", "content": q}]})

#     for msg in response["messages"]:

#         # Tool calls (what agent decided)
#         if hasattr(msg, "tool_calls") and msg.tool_calls:
#             for tool_call in msg.tool_calls:
#                 print(f"Tool: {tool_call['name']:<20} Arguments: {tool_call['args']}")

#         # Tool result (what tool returned)
#         if isinstance(msg, ToolMessage):
#             print(f"{'Tool Result: '} {msg.content}")

#     print("\nFinal Answer:")
#     print(response["messages"][-1].content)

    
# # Stream step-by-step agent execution
# for step in agent.stream({"messages": [{"role": "user", "content": "What is the average sales in East region?"}]}):
#     print("\n---")
#     print(step)
    