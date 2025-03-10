import subprocess
import re
import time
import win32serviceutil
import win32service
import win32event
import win32api
import servicemanager

class LogoffDisconnectedUsersService(win32serviceutil.ServiceFramework):
    _svc_name_ = "LogoffDisconnectedUsersService"  # Service name
    _svc_display_name_ = "Logoff Disconnected Users Service"
    _svc_description_ = "A service that logs off disconnected 'prospectbddev' users except one."

    def __init__(self, args):
        super(LogoffDisconnectedUsersService, self).__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        """Stop the service."""
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        """Main function that runs the service."""
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)

        while True:
            # Check the disconnected users and log them off periodically
            self.logout_disconnected_users()
            time.sleep(60)  # Check every 60 seconds

    def logout_disconnected_users(self):
        """Logs off disconnected 'prospectbddev' users, keeping only one logged in."""
        result = subprocess.run(['query', 'user'], capture_output=True, text=True, errors='ignore')
        if result.returncode not in [0, 1]:
            print("Error: query user command failed.")
            return
        
        disconnected_users = []  # List to store disconnected users' session IDs
        for line in result.stdout.split('\n')[1:]:  # Skip header
            parts = re.split(r'\s{2,}', line.strip())  # Split by 2+ spaces
            if len(parts) >= 4 and parts[2] == "Disc" and "prospectbddev" in parts[0]:  # Check if user is 'prospectbddev' and state is Disconnected
                session_id = parts[1]  # Extract session ID
                disconnected_users.append(session_id)
        
        if len(disconnected_users) > 1:
            # Log off all but one disconnected 'prospectbddev' user
            for session_id in disconnected_users[1:]:  # Skip the first one (keep it logged in)
                print(f"Logging off session {session_id}")
                subprocess.run(['logoff', session_id])
        else:
            print("Only one or no disconnected prospectbddev user found, no action taken.")

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(LogoffDisconnectedUsersService)
