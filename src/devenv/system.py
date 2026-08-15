import shutil

def check_tool(tool_name):
    return shutil.which(tool_name)

# print(check_tool("git"))
   