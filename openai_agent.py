import asyncio
import os

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerStdio

async def ask(agent: Agent, message: str):
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)


async def run(mcp_server: MCPServer):
    agent = Agent(
        name="User Management Agent",
        instructions="You are a user management agent. You can create and list users.",
        mcp_servers=[mcp_server],
    )

    await ask(agent, "List the current users")
    await ask(agent, "Add a user with name new_user and email new_user@example.com")
    await ask(agent, "What users do we have?")


async def main():
    async with MCPServerStdio(
        name="User management MCP Server",
        params={
            "command": "python",
            "args": ["mcp_server.py"],
        },
    ) as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="MCP Filesystem Example", trace_id=trace_id):
            print(
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n"
            )
            await run(server)


if __name__ == "__main__":
    asyncio.run(main())
