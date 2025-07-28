import subprocess
import os
import time

# Set correct paths for user 'luke'
repo_path = "/home/luke/Desktop/KatesProject"
action_script = os.path.join(repo_path, "action.py")

def get_commit_hash(ref, cwd):
    result = subprocess.run(
        ["git", "rev-parse", ref], cwd=cwd, capture_output=True, text=True
    )
    return result.stdout.strip()

def repo_exists(path):
    return os.path.exists(os.path.join(path, ".git"))

def clone_repo():
    print("Cloning repository...")
    subprocess.run([
        "git", "clone",
        "https://github.com/Skywalker409/KatesProject.git",
        repo_path
    ])

# Ensure repo is cloned
if not repo_exists(repo_path):
    clone_repo()

# Loop to fetch + compare commits + run script
while True:
    print("==== Checking for updates ====")

    # Fetch updates from remote
    subprocess.run(["git", "fetch"], cwd=repo_path)

    try:
        # Get commit hashes
        local_commit = get_commit_hash("HEAD", cwd=repo_path)
        upstream_commit = get_commit_hash("origin/main", cwd=repo_path)
    except Exception as e:
        print("Error comparing commits:", e)
        time.sleep(120)
        continue

    if local_commit != upstream_commit:
        print("Update found! Pulling changes...")
        subprocess.run(["git", "pull"], cwd=repo_path)
    else:
        print("Already up to date.")

    # Run the script
    print("Running action.py...\n")
    subprocess.run(["python", action_script])

    # Wait before next check
    time.sleep(5)
