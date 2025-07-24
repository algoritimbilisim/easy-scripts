# docker-kill (Docker Reset)

## Description
This script forcefully stops and resets Docker services on macOS. It terminates Docker processes, removes service binaries, and reinstalls them from the Docker application. Useful for fixing Docker connectivity issues or corrupted installations.

## Requirements
- Bash
- macOS
- Docker Desktop installed in `/Applications/Docker.app`
- sudo privileges

## Usage
```bash
bash docker-kill.sh
```

## What it does
1. **Stop Docker Processes**: Kills all Docker-related processes using pkill
2. **Stop Services**: Removes Docker vmnetd and socket services from launchctl
3. **Remove Binaries**: Deletes existing Docker helper binaries from system directories
4. **Reinstall Binaries**: Copies fresh binaries from Docker.app installation

## Services Affected
- `com.docker.vmnetd` - Docker virtual network daemon
- `com.docker.socket` - Docker socket service

## Files Modified
- `/Library/PrivilegedHelperTools/com.docker.vmnetd`
- `/Library/PrivilegedHelperTools/com.docker.socket`

## When to Use
- Docker won't start or connect
- Network connectivity issues with containers
- After Docker updates that fail to complete properly
- When Docker services become unresponsive

## Warning
This script requires sudo privileges and will forcefully terminate Docker processes. Make sure to save any work in running containers before executing.