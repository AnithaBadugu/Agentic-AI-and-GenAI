#MCP - Simple calculator + Question Answering

from fastmcp import FastMCP
from google import genai

mcp= FastMCP("Gemini Calc")
client=genai.Client(api_key="")
@mcp.tool()
def ask_gemini(questions:str):
    response=client.models.generate_content(
        model="gemini-3.5-flash",
        contents=questions
    )
    return response.text
       
@mcp.tool()
def cal(a:float, b:float, operation:str):
    if operation=="add":
        return a+b 
    if operation=="sub":
        return a-b 

if __name__=="__main__":
    mcp.run()
