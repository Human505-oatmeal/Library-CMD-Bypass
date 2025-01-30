import os, sys, subprocess

print(f"Hello! {os.getlogin()}")

while True:
    user_input = input(f"{os.getcwd()} > ")

    if user_input.strip().lower() in ['exit', 'quit']:  # Exit condition for the loop
        print("Exiting...")
        break

    handler = user_input.split()

    try:
        result = subprocess.run(['cmd', '/C'] + handler, capture_output=True, text=True)

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except FileNotFoundError:
        print(f"Command not found: {handler[0]}")
    except Exception as e:
        print(f"Error: {e}")
