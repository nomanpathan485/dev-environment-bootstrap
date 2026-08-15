from .system import check_tool
from .git_check import get_git_identity
from .ssh_check import get_ssh_status
Tools = ["git", "python", "code", "ssh"]

def run_diagnostics(tools=None):
    if tools is None:
        tools = Tools
    tool_result = {}

    for tool in tools:
        tool_result[tool] = check_tool(tool)
    return {
        "tools": tool_result,
        "git_identity": get_git_identity(),
        "ssh_status": get_ssh_status()
    }

if __name__ == "__main__":
    print(run_diagnostics())