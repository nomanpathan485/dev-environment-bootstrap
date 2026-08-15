from .diagnostic import run_diagnostics

def main():
    result = run_diagnostics()

    print("\nDeveloper Environment Diagnostics:")
    for tool, path in result["tools"].items():
        if path:
            print(f"[OK] {tool} found")
            print(f"    Path: {path}")
        else:
            print(f'[warning] {tool} not found')

    print("\nGit Identity:")
    git_identity = result["git_identity"]
    for key, value in git_identity.items():
        if value:
            print(f"[OK] {key}: {value}")
        else:
            print(f"[warning] {key} not set")

    print("\nSSH:")
    ssh_status = result["ssh_status"]
    if ssh_status["has_key"] == True:
        print(f"[Ok] SSH key found: {ssh_status['key_path']}")
    else:
        print(f"[WARN] SSH key not found")

if __name__ == "__main__":
    main()

