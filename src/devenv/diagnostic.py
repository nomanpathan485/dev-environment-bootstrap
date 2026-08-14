from .system import check_tool
tools = ["git", "python", "code", "ssh"]

def run_diagnostics(tools=tools):
    result = {}

    for tool in tools:
        result[tool] = check_tool(tool)
    return result


if __name__ == "__main__":
    print(run_diagnostics())