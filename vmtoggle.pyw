import sys
import socket
import ctypes
user32 = ctypes.windll.user32

HOST = "192.168.56.1" # Host-only network host address
PORT = 8123 # TCP port

def wait_for_vm():
    """ Wait for a TCP connection and return when a connection is made """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    c, a = server.accept()
    c.close()

def run(title, hide_and_exit):
    vm = user32.FindWindow(NULL, title)
    # Hide the VM window and exit if so requested (useful for hiding the VM at 
    # startup)
    if hide_and_exit:
        user32.ShowWindow(0) # SW_HIDE
        sys.exit(0)
        
    user32.SetForegroundWindow(vm)
    user32.ShowWindow(window, 5) # SW_SHOW

    wait_for_vm()

    i = 0 
    while i < 32: # Just a limit to avoid an infinite loop
        last = user32.GetWindow(vm, 2) # GW_HWNDNEXT
        if user32.IsWindowVisible(last):
            break
        i += 1

    vm_thread = user32.GetWindowThreadProcessId(vm, 0x0) # NULL
    last_thread = user32.GetWindowThreadProcessId(last, 0x0) # NULL

    user32.AttachThreadInput(vm_thread, last_thread, True)
    user32.ShowWindow(vm, 0) # SW_HIDE
    user32.SetForegroundWindow(last)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1], False)
    elif len(sys.argv) == 3 and sys.argv[1] == "hide":
        run(sys.argv[2], True)
    else:
        sys.stderr.write("Invalid arguments")
        sys.exit(1)
