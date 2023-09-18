import subprocess

# Define the file paths for the scripts you want to run
sleeper_script = "sleeper.py"
contracts_script = "contracts.py"

try:
    # Run sleeper.py
    subprocess.run(["python", sleeper_script], check=True)

    # Run contracts.py
    subprocess.run(["python", contracts_script], check=True)

    print("Both scripts have been executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")