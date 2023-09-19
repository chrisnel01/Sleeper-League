import schedule
import time
import subprocess
import json
from datetime import datetime

def run_updater():
    try:
        with open("log.json", "r") as log_file:
                log_data = json.load(log_file)

        # Append the current date and time to the log
        now = datetime.now()
        log_data.append({"timestamp": now.strftime("%Y-%m-%d %H:%M:%S")})
        print("Updated: ", log_data)

        # Save the updated log data to log.json
        with open("log.json", "w") as log_file:
            json.dump(log_data, log_file, indent=4)
            
        # Run your updater script
        subprocess.run(["python", "updater.py"], check=True)
        print("Updater.py has been executed successfully.")

        # Perform Git operations (add, commit, and push)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto commit from scheduler"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Git changes have been committed and pushed to the repository.")

        print("Updated: ", log_data)

        # Save the updated log data to log.json
        with open("log.json", "w") as log_file:
            json.dump(log_data, log_file, indent=4)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Schedule the updater to run at 3:00 AM every day
schedule.every().day.at("00:05").do(run_updater)

while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for 60 seconds to avoid high CPU usage
