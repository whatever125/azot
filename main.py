import subprocess


def get_ips() -> dict:
    """Возвращает имена компьютеров в AD их IP-адреса"""
    res = list(filter(lambda x: x != 'Name' and x != ':' and x != 'IPv4Address', subprocess.run(
        ["powershell", "-Command",
         'Get-ADComputer -Filter * -Properties Name, ipv4Address | Format-List Name, ipv4*'],
        capture_output=True, shell=False).stdout.decode("CP866").split()))
    dic = {}
    for i in range(0, len(res), 2):
        dic[res[i]] = res[i + 1]
    return dic


def list_ips() -> list:
    """Возвращает список IP-адресов компьютеров в AD"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-ADComputer -Filter * -Property ipv4Address | Select-Object -ExpandProperty ipv4*'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')


def free_space() -> float:
    """Вычисление свободного пространства на HDD"""
    return sum(map(lambda space: float(space) / 1024 ** 3, subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_LogicalDisk -filter "DriveType=3" | Select-Object -ExpandProperty FreeSpace'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def logical_disk_info() -> list:
    """Возвращает информацию о логических дисках"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_LogicalDisk | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def hdd_info() -> list:
    """Возвращает информацию о жестких дисках"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_DiskDrive | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def os_info() -> list:
    """Возвращает информацию об операционных системах"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_OperatingSystem | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def cpu_info() -> list:
    """Возвращает информацию о процессорах"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_Processor | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def vc_info() -> list:
    """Возвращает информацию о видеокартах"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_VideoController | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def ram_info() -> list:
    """Возвращает информацию об оперативной памяти"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get -WmiObject -Class Win32_PhysicalMemory | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def net_info() -> list:
    """Возвращает информацию о сетевых адаптерах"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_NetworkAdapterConfiguration | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def shutdown():
    """Выключает компьютер"""
    subprocess.run(
        ["powershell", "-Command",
         '(Get-WmiObject -Class Win32_OperatingSystem -EnableAllPrivileges).Shutdown()'])


def reboot():
    """Перезагружает компьютер"""
    subprocess.run(
        ["powershell", "-Command",
         '(Get-WmiObject -Class Win32_OperatingSystem -EnableAllPrivileges).Reboot()'])


def process_info() -> list:
    """Возвращает информацию о запущенных процессах"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_Process | Select-Object -Property Name, ProcessID'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def terminate_process_by_id(process_id: int):
    """Останавливает процесс по id"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Process -Property * -filter "ProcessID={process_id}").Terminate()"""])


def terminate_process_by_name(process_name: str):
    """Останавливае процесс по имени"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Process -Property * -filter "Name='{process_name}'").Terminate()"""])


def service_info() -> list:
    """Возвращает информацию о службах"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_Service | Select-Object -Property Name, StartMode, DelayedAutoStart, Description, DisplayName, State'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def start_service(service_name: str):
    """Запускает службу"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Property * -filter "Name='{service_name}'").StartService()"""])


def stop_service(service_name: str):
    """Останавливает службу"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Property * -filter "Name='{service_name}'").StopService()"""])


def change_start_mode_service(service_name: str, start_mode: str):
    """Изменяет режим запуска службы"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Property * -filter "Name='{service_name}'").ChangeStartMode({start_mode})"""])


def run_register():
    """Подключается к системному реестру"""
    subprocess.run(
        ["powershell", "-Command",
         f"""Invoke-WmiMethod -Class Win32_Process -Name create -ArgumentList 'regedit'"""])


def group_list() -> list:
    """Возвращает список групп"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-WmiObject -Class Win32_Group | Select-Object -ExpandProperty Name'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')


def list_administrators():
    """Возвращает список администраторов"""
    return subprocess.run(
        ["powershell", "-Command",
         """(Get-WmiObject -Class Win32_Group -Filter "Name='Администраторы'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Caption"""],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')


def list_remote_users():
    """Возвращает список удаленных пользователей"""
    return subprocess.run(
        ["powershell", "-Command",
         """(Get-WmiObject -Class Win32_Group -Filter "Name='Пользователи удаленного управления'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Caption"""],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')


# Get-WmiObject Win32_OperatingSystem -ComputerName ((Get-ADComputer -filter * -SearchBase "OU=Member Servers,DC=Company,DC=Com").Name)