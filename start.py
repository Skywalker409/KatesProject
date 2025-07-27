import subprocess
import os
import time

# Path to repo and script
repo_path = "/home/pi/KatesProject"
action_script = os.path.join(repo_path, "action.py")

def get_commit_hash(ref, cwd):
    result = subprocess.run(["git", "rev-parse", ref], cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip()

while True:
    print("==== Checking for updates ====")

    # Step 1: Fetch updates (doesn't modify local code)
    subprocess.run(["git", "fetch"], cwd=repo_path)

    # Step 2: Compare local HEAD to upstream
    local_commit = get_commit_hash("HEAD", cwd=repo_path)
    upstream_commit = get_commit_hash("@{u}", cwd=repo_path)

    if local_commit != upstream_commit:
        print("Update found! Pulling changes...")
        subprocess.run(["git", "pull"], cwd=repo_path)
    else:
        print("Already up to date.")

    # Step 3: Run the action script
    print("Running action.py...")
    subprocess.run(["python3", action_script])

    # Step 4: Wait 2 minutes
    print("Waiting 2 minutes before next check...\n")
    time.sleep(120)
