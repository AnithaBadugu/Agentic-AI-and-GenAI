#To-Do-List Example - MCP 


from fastmcp import FastMCP
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, Heading, Text

mcp = FastMCP("Todo App")

@mcp.tool(app=True)
def todo_list():
    """Display a simple to-do list."""

    with Column(gap=3) as view:
        Heading("My To-Do List")
        Text("1. Learn Python")
        Text("2. Practice DSA")
        Text("3. Learn MCP")
        Text("4. Build an AI Project")

    return PrefabApp(view=view)

if __name__ == "__main__":
    mcp.run()
