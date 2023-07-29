import subprocess
import os
import sys

def push_to_github(ssh, folder):
    # navigate to project folder
    os.chdir(folder)

    # Initialize git
    subprocess.check_output('git init', shell=True)

    # Add all files to the staging area
    subprocess.check_output('git add .', shell=True)

    # Commit the changes
    subprocess.check_output('git commit -m "Initial commit"', shell=True)

    # Add the remote origin
    try:
        subprocess.check_output(f'git remote add origin {ssh}', shell=True)
    except subprocess.CalledProcessError:
        # If the remote origin already exists, set a new URL
        subprocess.check_output(f'git remote set-url origin {ssh}', shell=True)

    # Push the changes
    subprocess.check_output('git push -u origin main', shell=True)

if __name__ == "__main__":
    args = sys.argv
    push_to_github(args[1], args[2])


