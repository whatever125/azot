import wmi
import datetime


class Wmi:
    """Класс для удобной работы с Windows Management Instrumentation"""
    def __init__(self, ip: str):
        """Инициализация экземпляра класса"""
        self.ip = ip
        self.conn = self.connect()
        self.register = self.connect_register()

    def connect(self) -> wmi.WMI:
        """Подключение к удаленному компьютеру"""
        return wmi.WMI(computer=self.ip, privileges=["RemoteShutdown"])

    def free_space(self) -> float:
        """Вычисление свободного пространства на HDD"""
        return sum(map(lambda disk: float(disk.FreeSpace) / 1024 ** 3,
                       self.conn.Win32_LogicalDisk(DriveType=3)))

    def logical_disk_info(self) -> list:
        """Возвращает информацию о логических дисках"""
        return self.conn.Win32_LogicalDisk(DriveType=3)

    def hdd_info(self) -> list:
        """Возвращает информацию о жестких дисках"""
        return self.conn.Win32_DiskDrive()

    def os_info(self) -> list:
        """Возвращает информацию об операционных системах"""
        return self.conn.Win32_OperatingSystem()

    def cpu_info(self) -> list:
        """Возвращает информацию о процессорах"""
        return self.conn.Win32_Processor()

    def vc_info(self) -> list:
        """Возвращает информацию о видеокартах"""
        return self.conn.Win32_VideoController()

    def ram_info(self) -> list:
        """Возвращает информацию об оперативной памяти"""
        return self.conn.Win32_ComputerSystem()

    def net_info(self) -> list:
        """Возвращает информацию о сетевых адаптерах"""
        return self.conn.Win32_NetworkAdapterConfiguration(IPEnabled=1)

    def time_info(self) -> str:
        """Возвращает время работы с последнего включения"""
        sdata = self.conn.Win32_PerfFormattedData_PerfOS_System()
        uptime = sdata[-1].SystemUpTime
        utime = datetime.timedelta(seconds=int(uptime))
        return str(utime)

    def shutdown(self):
        """Выключает компьютер"""
        self.conn.Win32_OperatingSystem(Primary=1)[0].Shutdown()

    def reboot(self):
        """Перезагружает компьютер"""
        self.conn.Win32_OperatingSystem(Primary=1)[0].Reboot()

    def process_info(self) -> list:
        """Возвращает информацию о запущенных процессах"""
        return self.conn.Win32_Process()

    def terminate_process_by_id(self, process_id: int):
        """Останавливает процесс по id"""
        for process in self.conn.Win32_Process(ProcessId=process_id):
            process.Terminate()

    def terminate_process_by_name(self, process_name: str):
        """Останавливае процесс по имени"""
        for process in self.conn.Win32_Process(Name=process_name):
            process.Terminate()

    def service_info(self) -> list:
        """Возвращает информацию о службах"""
        return self.conn.Win32_Service()

    def start_service(self, service_name: str):
        """Запускает службу"""
        for service in self.conn.Win32_Service(Name=service_name):
            service.StartService()

    def stop_service(self, service_name: str):
        """Останавливает службу"""
        for service in self.conn.Win32_Service(Name=service_name):
            service.StopService()

    def delete_service(self, service_name: str):
        """Удаляет службу"""
        for service in self.conn.Win32_Service(Name=service_name):
            service.Delete()

    def change_start_mode_service(self, service_name: str, start_mode: str):
        """Изменяет режим запуска службы"""
        print(self.conn.Win32_Service(Name=service_name))
        for service in self.conn.Win32_Service(Name=service_name):
            service.ChangeStartMode(StartMode=start_mode)

    def group_info(self) -> list:
        """Возвращает информацию о группах"""
        return self.conn.Win32_Group()

    def group_users(self, group_name) -> list:
        """Возвращает информацию о пользователях группы"""
        return self.conn.Win32_Group(Name=group_name)[0].associators(
            wmi_result_class="Win32_UserAccount")

    def connect_register(self) -> wmi.WMI:
        """Подключается к системному реестру"""
        return self.conn.StdRegProv

    def register_keys(self, hdefkey: str, ssubkey: str) -> tuple:
        """Возвращает подразделы указанного раздела"""
        return self.register.EnumKey(hdefkey, ssubkey)

    def register_values(self, hdefkey: str, ssubkey: str) -> tuple:
        """Возвращает параметры указанного раздела"""
        return self.register.EnumValues(hdefkey, ssubkey)

    def register_get_values(self, hdefkey: str, ssubkey: str) -> dict:
        """Возвращает значения параметров указанного раздела"""
        _, values, types = self.register.EnumValues(hdefkey, ssubkey)
        dic = {}
        for i in range(len(values)):
            if types[i] == 1:
                dic[values[i]] = self.register.GetStringValue(hdefkey, ssubkey, values[i])
            if types[i] == 2:
                dic[values[i]] = self.register.GetExpandedStringValue(hdefkey, ssubkey, values[i])
            if types[i] == 3:
                dic[values[i]] = self.register.GetBinaryValue(hdefkey, ssubkey, values[i])
            if types[i] == 4:
                dic[values[i]] = self.register.GetDWORDValue(hdefkey, ssubkey, values[i])
            if types[i] == 7:
                dic[values[i]] = self.register.GetMultiStringValue(hdefkey, ssubkey, values[i])
            if types[i] == 11:
                dic[values[i]] = self.register.GetQWORDValue(hdefkey, ssubkey, values[i])
        return dic
