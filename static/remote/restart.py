import static.router.scripts as s
import static.router.infomation as i
import subprocess


def restart_all_vm(room):
    try:
        list_pathvm = i.get_pathvm_by_room(room)
        for path in list_pathvm:
            command = s.SCRIPT_CONNECT_TO_SERVER + s.PATH_VMRUN + "reset " + path
            subprocess.run(command, shell=True, stdout=subprocess.PIPE)
            print("Restarting VM: " + path)
    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))


def restart_vm_by_id(id):
    try:
        path_vm = i.get_all_vmpath()
        for path in path_vm:
            if path.id == id:
                command = s.SCRIPT_CONNECT_TO_SERVER + s.PATH_VMRUN + "reset " + path
                subprocess.run(command, shell=True, stdout=subprocess.PIPE)
            return "Restarting VM: " + path
    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))
