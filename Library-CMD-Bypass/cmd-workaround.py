import os, sys, subprocess, io


print(f"Hello! {os.getlogin()}")
while True:
    user_input = input(f"{os.getcwd()} > ").strip().lower()

    if user_input in ['exit', 'quit']:  # Exit condition for the loop
        print("Exiting...")
        break

    handler = user_input.split()

    try:
        if not handler:
            continue
        elif handler[0] in ["clear", "cls"]:
            os.system('cls')
            continue
        elif handler[0] == "cd":
            os.chdir(os.path.expanduser(handler[1]))
            continue
        result = subprocess.Popen(['cmd', '/C'] + handler, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout_output, stderr_output = result.communicate()
        if stdout_output:
            print(stdout_output, end="")
        if stderr_output:
            print(stderr_output, file=sys.stderr)
    except FileNotFoundError:
        print(f"Command not found: {handler[0]}")
    except Exception as e:
        print(f"Error: {e}")
