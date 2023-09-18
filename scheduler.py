import schedule
import time
import subprocess

def run_updater():
    try:
        # Run your updater script
        subprocess.run(["python", "updater.py"], check=True)
        print("Updater.py has been executed successfully.")

        # Perform Git operations (add, commit, and push)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto commit from scheduler"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Git changes have been committed and pushed to the repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Schedule the updater to run at 3:00 AM every day
schedule.every().day.at("23:06").do(run_updater)

while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for 60 seconds to avoid high CPU usage
