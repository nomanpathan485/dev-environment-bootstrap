import subprocess

def git_config(key):
    result = subprocess.run(["git", "config", key],
    capture_output=True,
    text=True,
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return None
# print(git_config("user.name"))
# print(git_config("user.email"))

def get_git_identity():
    identity = {}
    identity["user.name"] = git_config("user.name")
    identity["user.email"] = git_config("user.email")
    return identity 
print(get_git_identity())