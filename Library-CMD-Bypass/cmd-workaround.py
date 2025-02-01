import os, sys, subprocess, io

print(f"Hello! {os.getlogin()}")
#  TODO
#  Encode output with UTF-8
#  directly communicate via the .communicate() method.
#  Handle weird stdout errors..

while True:
    user_input = input(f"{os.getcwd()} > ").lower()

    if user_input.strip().lower() in ['exit', 'quit']:  # Exit condition for the loop
        print("Exiting...")
        break

    handler = user_input.split()

    try:
        if handler[0] in ["clear", "cls"]:
            os.system('cls')
        if handler[0] == "cd":
            os.chdir(os.path.expanduser(handler[1]))
            continue
        result = subprocess.Popen(['cmd', '/C'] + handler, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_output, stderr_output = result.communicate()
        if result.stdout:
            print(stdout_output.decode())
        if result.stderr:
            print(stderr_output.decode(), file=sys.stderr)
    except FileNotFoundError:
        print(f"Command not found: {handler[0]}")
    except Exception as e:
        print(f"Error: {e}")
