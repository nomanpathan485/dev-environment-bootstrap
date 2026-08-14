from  .diagnostic import run_diagnostics

def main():
    results = run_diagnostics()
    for tool, path in results.items():
        if path is not None:
            print(tool, "found at:", path)
        else:
            print(tool, "not found")

if __name__ == "__main__":
    main()