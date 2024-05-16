PATH_VMRUN = 'cd "C:\Program Files (x86)\VMware\VMware Workstation & vmrun -T ws" '

SCRIPT_CONNECT_TO_SERVER = 'sshpass -p Phap123 ssh Administrator@192.168.38.100 '

SCRIPT_RESTART = SCRIPT_CONNECT_TO_SERVER + PATH_VMRUN +"reset "

SCRIPT_STOP = SCRIPT_CONNECT_TO_SERVER + PATH_VMRUN +"stop "

SCRIPT_SHOW_IP = SCRIPT_CONNECT_TO_SERVER + PATH_VMRUN +"getGuestIPAddress "

SCRIPT_SHOW_CONFIG = SCRIPT_CONNECT_TO_SERVER + " type "

SCRIPT_UPDATE = SCRIPT_CONNECT_TO_SERVER + PATH_VMRUN + " upgradevm "

def get_script_restart_vm(vm_name):
    return SCRIPT_RESTART + vm_name

def get_script_stop_vm(vm_name):
    return SCRIPT_STOP + vm_name

def get_script_show_ip(vm_name):
    return SCRIPT_SHOW_IP + vm_name

def get_script_show_config(vm_name):
    return SCRIPT_SHOW_CONFIG + vm_name

def get_script_update_vm(vm_name):
    return SCRIPT_UPDATE + vm_name


