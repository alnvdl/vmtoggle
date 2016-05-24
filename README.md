# VM toggler

A simple script for Windows that:
1. Places a VM window in foreground
2. Waits for a signal from the VM
3. Finds the window that had focus before the VM
4. Hides the VM window
5. Switches to the window found in step 3

This is most useful for fullscreen VMs, but it will work with pretty much any 
regular window.

Typically, the user should configure this script to be run in the host via a 
shortcut in the taskbar, or via a keyboard shortcut.

On the VM side, the guest OS should have an easy way to connect via TCP as a 
signal for toggling back to the host OS when requested.
