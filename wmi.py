import wmi
import datetime


class Wmi:
    def __init__(self, ip: str):
        self.ip = ip
        self.conn = self.connect()

    def connect(self) -> wmi.WMI:
        return wmi.WMI(computer=self.ip, privileges=["RemoteShutdown"])

    def free_space(self) -> float:
        return sum(map(lambda disk: float(disk.FreeSpace) / 1024 ** 3,
                       self.conn.Win32_LogicalDisk(DriveType=3)))

    def logical_disk_info(self) -> list:
        return self.conn.Win32_LogicalDisk(DriveType=3)

    def hdd_info(self) -> list:
        return self.conn.Win32_DiskDrive()

    def os_info(self) -> list:
        return self.conn.Win32_OperatingSystem()

    def cpu_info(self) -> list:
        return self.conn.Win32_Processor()

    def vc_info(self) -> list:
        return self.conn.Win32_VideoController()

    def ram_info(self) -> list:
        return self.conn.Win32_ComputerSystem()

    def net_info(self) -> list:
        return self.conn.Win32_NetworkAdapterConfiguration(IPEnabled=1)

    def time_info(self) -> datetime.timedelta:
        sdata = self.conn.Win32_PerfFormattedData_PerfOS_System()
        uptime = sdata[-1].SystemUpTime
        utime = datetime.timedelta(seconds=int(uptime))
        return utime

    def shutdown(self) -> list:
        self.conn.Win32_OperatingSystem(Primary=1)[0].Shutdown()

    def reboot(self) -> list:
        self.conn.Win32_OperatingSystem(Primary=1)[0].Reboot()

    def process_info(self) -> list:
        return self.conn.Win32_Process()

    def terminate_process_by_id(self, process_id: int):
        for process in self.conn.Win32_Process(ProcessId=process_id):
            process.Terminate()

    def terminate_process_by_name(self, process_name: str):
        for process in self.conn.Win32_Process(Name=process_name):
            process.Terminate()

    def service_info(self) -> list:
        return self.conn.Win32_Service()

    def start_service(self, service_name: str):
        for service in self.conn.Win32_Service(Name=service_name):
            service.StartService()

    def stop_service(self, service_name: str):
        for service in self.conn.Win32_Service(Name=service_name):
            service.StopService()

    def delete_service(self, service_name: str):
        for service in self.conn.Win32_Service(Name=service_name):
            service.Delete()

    def change_start_mode_service(self, service_name: str, start_mode: str):
        print(self.conn.Win32_Service(Name=service_name))
        for service in self.conn.Win32_Service(Name=service_name):
            service.ChangeStartMode(StartMode=start_mode)

    def group_info(self) -> list:
        return self.conn.Win32_Group()

    def group_users(self, group_name) -> list:
        return self.conn.Win32_Group(Name=group_name)[0].associators(wmi_result_class="Win32_UserAccount")
