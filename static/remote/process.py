import static.router.user as u
import static.router.scripts as s
import subprocess

list_process = []

def exce_list_process_in_1vm(path_vm,id):
    try:
        # Get username and password
        VM_USERNAME, VM_PASSWORD = u.getuser_by_id_room(id)
        command = s.SCRIPT_CONNECT_TO_SERVER + " " + s.PATH_VMRUN + " -gu " + VM_USERNAME + " -gp " + VM_PASSWORD + " listProcessesInGuest " + path_vm + " -interactive"
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        listt = process.stdout.splitlines()
        for i in listt:
            list_process.append(i.decode('utf-8'))
        print("Processes running in the guest:")

    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))


def exce_list_process():
    try:
       for i in list_process:
              pass
    except:
        return None


def get_list_process():
    return list_process

