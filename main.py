import subprocess
import datetime
import win32evtlog


def get_ips() -> list:
    """Возвращает имена компьютеров в AD их IP-адреса"""
    res = list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         'Get-ADComputer -Filter * -Properties Name, ipv4Address | Select-Object Name, ipv4*'],
        capture_output=True, shell=False).stdout.decode("CP866").split()[4:]))
    lis = []
    for i in range(0, len(res), 2):
        lis.append((res[i], res[i + 1]))
    return lis


def list_ips() -> list:
    """Возвращает список IP-адресов компьютеров в AD"""
    return list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         'Get-ADComputer -Filter * -Property ipv4Address | Select-Object -ExpandProperty ipv4*'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def free_space(computer: str) -> float:
    """Вычисление свободного пространства на HDD"""
    return sum(map(lambda space: float(space) / 1024 ** 3, filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_LogicalDisk -Computer {computer} -filter "DriveType=3" | Select-Object -ExpandProperty FreeSpace'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n'))))


def ram_capacity(computer: str) -> float:
    """Вычисление объема оперативной памяти"""
    return sum(map(lambda space: float(space) / 1024 ** 3, filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_PhysicalMemory -Computer {computer} | Select-Object -ExpandProperty Capacity'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n'))))


def processor_name(computer: str) -> list:
    """Возвращает название процессора"""
    return list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Processor -Computer {computer} | Select-Object -ExpandProperty Name'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def last_boot_up_time(computer: str) -> str:
    """Возвращает время последенего включения"""
    res = subprocess.run(
        ["powershell", "-Command",
         f'(Get-WmiObject Win32_OperatingSystem -Computer {computer}).LastBootUpTime'],
        capture_output=True, shell=False).stdout.decode("CP866")
    boot_up_time = datetime.datetime(year=int(res[:4]), month=int(res[4:6]), day=int(res[6:8]), hour=int(res[8:10]), minute=int(res[10:12]), second=int(res[12:14]))
    now_time = datetime.datetime.now()
    return str(now_time - boot_up_time).split('.')[0]


def logical_disk_info(computer: str) -> list:
    """Возвращает информацию о логических дисках"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_LogicalDisk -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def hdd_info(computer: str) -> list:
    """Возвращает информацию о жестких дисках"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_DiskDrive -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def os_info(computer: str) -> list:
    """Возвращает информацию об операционных системах"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_OperatingSystem -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def cpu_info(computer: str) -> list:
    """Возвращает информацию о процессорах"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Processor -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def vc_info(computer: str) -> list:
    """Возвращает информацию о видеокартах"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_VideoController -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def ram_info(computer: str) -> list:
    """Возвращает информацию об оперативной памяти"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_PhysicalMemory -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def net_info(computer: str) -> list:
    """Возвращает информацию о сетевых адаптерах"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Computer {computer} | Select-Object -Property *'],
        capture_output=True).stdout.decode("CP866").split('\r\n')


def shutdown(computer: str):
    """Выключает компьютер"""
    subprocess.run(
        ["powershell", "-Command",
         f'(Get-WmiObject -Class Win32_OperatingSystem -Computer {computer} -EnableAllPrivileges).Shutdown()'])


def reboot(computer: str):
    """Перезагружает компьютер"""
    subprocess.run(
        ["powershell", "-Command",
         f'(Get-WmiObject -Class Win32_OperatingSystem -Computer {computer} -EnableAllPrivileges).Reboot()'])


def process_info(computer: str) -> list:
    """Возвращает информацию о запущенных процессах"""
    lis = list(map(lambda x: x.split(' : ')[1].strip(), filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Process -Computer {computer} | Format-List -Property Name, ProcessID'],
        capture_output=True).stdout.decode("CP866").split('\r\n'))))
    out = []
    for i in range(0, len(lis), 2):
        out.append((lis[i], lis[i + 1]))
    return out


def terminate_process_by_id(process_id: int, computer: str):
    """Останавливает процесс по id"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Process -filter "ProcessID={process_id}" -Computer {computer}).Terminate()"""])


def terminate_process_by_name(process_name: str, computer: str):
    """Останавливае процесс по имени"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Process -filter "Name='{process_name}'" -Computer {computer}).Terminate()"""])


def service_info(computer: str) -> list:
    """Возвращает информацию о службах"""
    lis = list(map(lambda x: x.split(' : ')[1].strip(), filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Service -Computer {computer} | Format-List -Property Name, StartMode, State'],
        capture_output=True).stdout.decode("CP866").split('\r\n'))))
    out = []
    for i in range(0, len(lis), 3):
        out.append((lis[i], lis[i + 1], lis[i + 2]))
    return out


def start_service(service_name: str, computer: str):
    """Запускает службу"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Computer {computer} -filter "Name='{service_name}'").StartService()"""])


def stop_service(service_name: str, computer: str):
    """Останавливает службу"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Computer {computer} -filter "Name='{service_name}'").StopService()"""])


def change_start_mode_service(service_name: str, start_mode: str, computer: str):
    """Изменяет режим запуска службы"""
    subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Computer {computer} -filter "Name='{service_name}'").ChangeStartMode({start_mode})"""])


def run_register(computer: str):
    """Подключается к системному реестру"""
    subprocess.run(
        ["powershell", "-Command",
         f"""psexec -i -s \\\\{computer} regedit"""])


def group_list(computer) -> list:
    """Возвращает список групп"""
    return list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Group -Computer {computer} | Select-Object -ExpandProperty Name'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def list_group_users(computer: str, group_name: str) -> list:
    """Возвращает список пользователей группы"""
    return list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Group -Computer {computer} -Filter "Name='{group_name}'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Name"""],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def list_administrators(computer) -> list:
    """Возвращает список администраторов"""
    return list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Group -Computer {computer} -Filter "Name='Администраторы'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Name"""],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def list_remote_users(computer) -> list:
    """Возвращает список пользователей удаленного рабочего стола"""
    return list(filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Group -Computer {computer} -Filter "Name='Пользователи удаленного рабочего стола'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Name"""],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')))


def list_users() -> list:
    """Возвращает список пользователей AD"""
    return subprocess.run(
        ["powershell", "-Command",
         'Get-AdUser -Filter * | Select-Object SamAccountName'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')


def list_user_information() -> list:
    """Возвращает информацию о пользователях AD для таблицы"""
    lis = list(map(lambda x: x.split(': ')[1].strip(), filter(lambda x: x != '', subprocess.run(
        ["powershell", "-Command",
         'Get-AdUser -Filter * -Property * | Format-List SamAccountName, Name, PasswordLastSet, EmployeeID, SID, Enabled'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n'))))
    out = []
    for i in range(0, len(lis), 6):
        out.append((lis[i], lis[i + 1], lis[i + 2], lis[i + 3], lis[i + 4], lis[i + 5]))
    return out


def disable_user(name: str):
    """Блокирует AD аккаунт пользователя"""
    subprocess.run(
        ["powershell", "-Command",
         f'Disable-ADAccount -Identity {name}'],
        capture_output=True, shell=False)


def enable_user(name: str):
    """Разблокирeет AD аккаунт пользователя"""
    subprocess.run(
        ["powershell", "-Command",
         f'Enable-ADAccount -Identity {name}'],
        capture_output=True, shell=False)


def remove_computer(name: str):
    """Выводит ПК из домена"""
    subprocess.run(
        ["powershell", "-Command",
         f'Remove-ADComputer -Identity {name}'],
        capture_output=True, shell=False)


def add_computer(domain_name: str):
    """Добавляет ПК в домен"""
    subprocess.run(
        ["powershell", "-Command",
         f'Add-Computer -DomainName {domain_name} -Restart -Force'],
        capture_output=True, shell=False)


def user_info(name: str) -> list:
    """Возвращает информацию о пользователе"""
    return subprocess.run(
        ["powershell", "-Command",
         f'Get-AdUser -Identity {name} -Property *'],
        capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')


def who_blocked_user(name: str):
    controllers = subprocess.run(
            ["powershell", "-Command",
             f'(Get-ADDomainController -filter *).HostName'],
            capture_output=True, shell=False).stdout.decode("CP866").split('\r\n')
    return_events = []
    for controller in controllers:
        hand = win32evtlog.OpenEventLog(controller, 'Security')
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        return_events += [event for event in events if int(event.EventID) == 4725]
    return return_events


# hand = win32evtlog.OpenEventLog('192.168.137.29', 'Security')
# flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
# events = win32evtlog.ReadEventLog(hand, flags, 0)
