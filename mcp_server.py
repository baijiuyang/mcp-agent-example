from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("UserManager")


@mcp.tool()
def create_user(name: str, email: str) -> dict:
    """
    Create a new user with a unique ID.
    """
    response = httpx.post(
        "http://localhost:8000/users", json={"name": name, "email": email}
    )
    return response.json()


@mcp.tool()
def list_users() -> list:
    """
    List all users.
    """
    response = httpx.get("http://localhost:8000/users")
    return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")
