# LinPurge
Automatically clean up traces left behind on a Linux system after penetration testing or post-exploitation activities.

# Core Features:
• Shell History Cleaning: Deletes or wipes the shell history files (.bash_history, .zsh_history, etc.), which might contain commands run during the engagement.

• Log File Cleaning: Clears logs from common system logs like /var/log/auth.log, /var/log/syslog, /var/log/secure, etc.

• Temporary File Removal: Removes temporary files created by various tools during the penetration test, which might be stored in directories like /tmp, /var/tmp, or ~/.cache.

• History and Command Remnants: Scrubs history files of specific commands and data remnants, such as wget, curl, or command-based payloads.

• Clears Process Information: Tries to remove information that might have been left in the process table during exploitation, like any custom processes created during the engagement.

• File Modification Timestamps: Resets file modification timestamps for files that were altered during the test (to avoid file timestamp anomalies).

• Clearing User and Group Modifications: Cleans up traces of user or group modifications, such as created or modified users, sudo permissions, and group memberships.

# USAGE: 
```
python3 LinPurge.py
```

# Additional Information
```

The script should be run with root privileges to clean certain files like /var/log or /etc/passwd
```
```

Ensure the system is not actively being used by others while the cleanup process is running, as it can interfere with ongoing processes.
```

 # DISCLAIMER
 The tool is for Educational Purposes Only. 
 I am not responsible for any illegal/harmful activities done by those who use it.

 # :beer: Support :beer:
 If you'd want to support me in what I do, you can do that here: https://buymeacoffee.com/0x0bfixious
 
