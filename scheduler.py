import schedule
import time
import subprocess
from datetime import datetime
def run_updater():
    log_data = []
    try:
        # Run your updater script
        subprocess.run(["python", "updater.py"], check=True)
        print("Updater.py has been executed successfully.")

        # Perform Git operations (add, commit, and push)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto commit from scheduler"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Git changes have been committed and pushed to the repository.")
        
        now = datetime.now()
        log_data.append({"timestamp": now.strftime("%Y-%m-%d %H:%M:%S")})
        print("Updated: ", log_data)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Schedule the updater to run at 3:00 AM every day
schedule.every().day.at("12:11").do(run_updater)

while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for 60 seconds to avoid high CPU usage
