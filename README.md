Here’s the **complete Markdown README** for the `Logoff Disconnected Users Service`, including all the instructions from the start:

```markdown
# Logoff Disconnected Users Service

## Overview
This Windows service logs off disconnected users of the `prospectbddev` session while ensuring one remains active for server operations. It runs automatically on system startup and periodically checks for disconnected users to log off.

---

## Features
- **Monitors disconnected users** (`prospectbddev`).
- **Keeps one user active** for server operations, logs off others.
- **Runs as a Windows Service** and starts automatically on boot.

---

## Prerequisites

### Required Software
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pywin32** library for Windows service support:
  ```bash
  pip install pywin32
  ```

---

## Installation Instructions

### 1. Download the Script
Save the following Python code as `logoff_disconnected_users_service.py`.

### 2. Modify Script Settings (Optional)
To customize the service name, display name, or description, edit the following lines in the script:

```python
_svc_name_ = "LogoffDisconnectedUsersService"
_svc_display_name_ = "Logoff Disconnected Users Service"
_svc_description_ = "Service that logs off disconnected 'prospectbddev' users except one."
```

### 3. Install the Service
Open **Command Prompt as Administrator**:
- Press **Win + X** and select **Command Prompt (Admin)** or **Windows PowerShell (Admin)**.
- Navigate to the directory containing the script.
- Run the following command to install the service:

```bash
python logoff_disconnected_users_service.py install
```

### 4. Configure the Service to Start Automatically
After installation, set the service to start automatically with the following command:

```bash
sc config LogoffDisconnectedUsersService start= auto
```

Note: Ensure there is a space after `start=`.

Alternatively, you can manually set the service to **Automatic** via **Services Manager**:
1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **LogoffDisconnectedUsersService** in the list.
3. Right-click the service → **Properties** → Set **Startup type** to **Automatic**.

---

## Managing the Service

### 1. Start the Service
To start the service after installation:

```bash
python logoff_disconnected_users_service.py start
```

### 2. Stop the Service
To stop the service:

```bash
python logoff_disconnected_users_service.py stop
```

### 3. Uninstall the Service
To uninstall the service, run:

```bash
python logoff_disconnected_users_service.py remove
```

---

## Logging and Output
The service logs the session IDs of users that are logged off. This is visible in the **Command Prompt** if running the service in the foreground.

For background service execution, you can check the **Windows Event Log** or add custom logging to the script for detailed logs.

---

## Troubleshooting

### Common Issues

- **Service Not Starting Automatically**:
  Ensure you've set the service to **Automatic** using `sc config` or through **Services Manager**.

- **Error: 'query user' Command Failed**:
  Ensure the service is run with **administrator privileges**.

- **Service Stops Unexpectedly**:
  Check the **Windows Event Log** for related error messages.

---

## Commands Summary

### Install the Service:

```bash
python logoff_disconnected_users_service.py install
```

### Set Startup to Automatic:

```bash
sc config LogoffDisconnectedUsersService start= auto
```

### Start the Service:

```bash
python logoff_disconnected_users_service.py start
```

### Stop the Service:

```bash
python logoff_disconnected_users_service.py stop
```

### Uninstall the Service:

```bash
python logoff_disconnected_users_service.py remove
```

---

## License
This script is provided under the **MIT License**. Feel free to modify and distribute it as you see fit.

```

This README provides all the necessary instructions for setting up, using, and managing the **Logoff Disconnected Users Service**, following best practices for clear and organized documentation.