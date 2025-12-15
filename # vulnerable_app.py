# vulnerable_app.py
# Example of unsafe code (for demo only!) and a safer alternative.

import subprocess


def ping_host_vulnerable():
    """
    VULNERABLE EXAMPLE (for demo):
    Takes user input and passes it directly to the system shell.

    A security tool like Snyk Code should flag this as high severity,
    because an attacker could inject extra commands.
    """
    host = input("Enter a host to ping: ")

    # ❌ VULNERABLE: User input is concatenated into a shell command.
    # An attacker could enter something like:
    #   8.8.8.8 && rm -rf /
    # so the shell would execute both ping and the malicious command.
    command = f"ping -c 1 {host}"

    # shell=True + untrusted input = command injection risk
    subprocess.run(command, shell=True, check=False)


def ping_host_safe():
    """
    SAFER EXAMPLE:
    Uses a list of arguments and does NOT invoke the shell directly.
    User input is passed as a separate argument, limiting injection risk.
    """
    host = input("Enter a host to ping safely: ")

    # ✅ SAFER: No shell=True, arguments passed as a list.
    # The command is not interpreted by a shell, so injection is harder.
    subprocess.run(["ping", "-c", "1", host], check=False)


def main():
    print("1) Run vulnerable ping")
    print("2) Run safer ping")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        ping_host_vulnerable()
    elif choice == "2":
        ping_host_safe()
    else:
        print("Unknown option.")


if __name__ == "__main__":
    main()
