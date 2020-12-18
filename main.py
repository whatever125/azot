import subprocess
import datetime


def get_ips() -> list:
    """Возвращает имена компьютеров в AD их IP-адреса"""
    res = list(map(lambda x: x.split(':')[1].strip() if len(x.split(':')) == 2 else '', filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         'Get-ADComputer -Filter * -Properties Name, ipv4Address | Format-List -Property Name, ipv4*'],
        ).decode("CP866").split('\r\n'))))
    lis = []
    for i in range(0, len(res), 2):
        lis.append((res[i], res[i + 1]))
    return lis


def list_ips() -> list:
    """Возвращает список IP-адресов компьютеров в AD"""
    return list(filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         'Get-ADComputer -Filter * -Property ipv4Address | Select-Object -ExpandProperty ipv4*'],
        ).decode("CP866").split('\r\n')))


def free_space(computer: str) -> float:
    """Вычисление свободного пространства на HDD"""
    return sum(map(lambda space: float(space) / 1024 ** 3, filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_LogicalDisk -Computer {computer} -filter "DriveType=3" | Select-Object -ExpandProperty FreeSpace'],
        ).decode("CP866").split('\r\n'))))


def ram_capacity(computer: str) -> float:
    """Вычисление объема оперативной памяти"""
    return sum(map(lambda space: float(space) / 1024 ** 3, filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_PhysicalMemory -Computer {computer} | Select-Object -ExpandProperty Capacity'],
        ).decode("CP866").split('\r\n'))))


def processor_name(computer: str) -> list:
    """Возвращает название процессора"""
    return list(filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Processor -Computer {computer} | Select-Object -ExpandProperty Name'],
        ).decode("CP866").split('\r\n')))


def last_boot_up_time(computer: str) -> str:
    """Возвращает время последенего включения"""
    res = subprocess.check_output(
        ["powershell", "-Command",
         f'(Get-WmiObject Win32_OperatingSystem -Computer {computer}).LastBootUpTime'],
        ).decode("CP866")
    boot_up_time = datetime.datetime(year=int(res[:4]), month=int(res[4:6]), day=int(res[6:8]), hour=int(res[8:10]), minute=int(res[10:12]), second=int(res[12:14]))
    now_time = datetime.datetime.now()
    return str(now_time - boot_up_time).split('.')[0]


def logical_disk_info(computer: str) -> list:
    """Возвращает информацию о логических дисках"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_LogicalDisk -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def hdd_info(computer: str) -> list:
    """Возвращает информацию о жестких дисках"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_DiskDrive -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def os_info(computer: str) -> list:
    """Возвращает информацию об операционных системах"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_OperatingSystem -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def cpu_info(computer: str) -> list:
    """Возвращает информацию о процессорах"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Processor -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def vc_info(computer: str) -> list:
    """Возвращает информацию о видеокартах"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_VideoController -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def ram_info(computer: str) -> list:
    """Возвращает информацию об оперативной памяти"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_PhysicalMemory -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def net_info(computer: str) -> list:
    """Возвращает информацию о сетевых адаптерах"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Computer {computer} | Select-Object -Property *'],
        ).decode("CP866").split('\r\n')


def shutdown(computer: str):
    """Выключает компьютер"""
    subprocess.check_output(
        ["powershell", "-Command",
         f'Start-Process powershell -Verb runAs -WindowStyle Hidden -Wait "(Get-WmiObject -Class Win32_OperatingSystem -Computer {computer} -EnableAllPrivileges).Shutdown()"'],
         )


def reboot(computer: str):
    """Перезагружает компьютер"""
    subprocess.check_output(
        ["powershell", "-Command",
         f'Start-Process powershell -Verb runAs -WindowStyle Hidden -Wait "(Get-WmiObject -Class Win32_OperatingSystem -Computer {computer} -EnableAllPrivileges).Reboot()"'],
        )


def process_info(computer: str) -> list:
    """Возвращает информацию о запущенных процессах"""
    lis = list(map(lambda x: x.split(' : ')[1].strip(), filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Process -Computer {computer} | Format-List -Property Name, ProcessID'],
        ).decode("CP866").split('\r\n'))))
    out = []
    for i in range(0, len(lis), 2):
        out.append((lis[i], lis[i + 1]))
    return out


def terminate_process_by_id(process_id: int, computer: str):
    """Останавливает процесс по id"""
    subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Process -filter "ProcessID={process_id}" -Computer {computer}).Terminate()"""],
    )


def terminate_process_by_name(process_name: str, computer: str):
    """Останавливае процесс по имени"""
    subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Process -filter "Name='{process_name}'" -Computer {computer}).Terminate()"""],
        )


def service_info(computer: str) -> list:
    """Возвращает информацию о службах"""
    lis = list(map(lambda x: x.split(' : ')[1].strip(), filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Service -Computer {computer} | Format-List -Property Name, StartMode, State'],
        ).decode("CP866").split('\r\n'))))
    out = []
    for i in range(0, len(lis), 3):
        out.append((lis[i], lis[i + 1], lis[i + 2]))
    return out


def start_service(service_name: str, computer: str):
    """Запускает службу"""
    subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Computer {computer} -filter "Name='{service_name}'").StartService()"""],
        )


def stop_service(service_name: str, computer: str):
    """Останавливает службу"""
    subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Computer {computer} -filter "Name='{service_name}'").StopService()"""],
        )


def change_start_mode_service(service_name: str, start_mode: str, computer: str):
    """Изменяет режим запуска службы"""
    subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Service -Computer {computer} -filter "Name='{service_name}'").ChangeStartMode('{start_mode}')"""],
)


def run_register(computer: str):
    """Подключается к системному реестру"""
    subprocess.check_output(
        ["powershell", "-Command",
         f"""psexec -i -s \\\\{computer} regedit"""],
        )


def group_list(computer: str) -> list:
    """Возвращает список групп"""
    return list(filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f'Get-WmiObject -Class Win32_Group -Computer {computer} | Select-Object -ExpandProperty Name'],
        ).decode("CP866").split('\r\n')))


def list_group_users(computer: str, group_name: str) -> list:
    """Возвращает список пользователей группы"""
    return list(filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Group -Computer {computer} -Filter "Name='{group_name}'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Name"""],
        ).decode("CP866").split('\r\n')))


def list_administrators(computer: str) -> list:
    """Возвращает список администраторов"""
    return list(filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Group -Computer {computer} -Filter "Name='Администраторы'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Name"""],
        ).decode("CP866").split('\r\n')))


def list_remote_users(computer: str) -> list:
    """Возвращает список пользователей удаленного рабочего стола"""
    return list(filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         f"""(Get-WmiObject -Class Win32_Group -Computer {computer} -Filter "Name='Пользователи удаленного рабочего стола'").GetRelated('Win32_UserAccount') | Select-Object -ExpandProperty Name"""],
        ).decode("CP866").split('\r\n')))


def list_users() -> list:
    """Возвращает список пользователей AD"""
    return subprocess.check_output(
        ["powershell", "-Command",
         'Get-AdUser -Filter * | Select-Object SamAccountName'],
        ).decode("CP866").split('\r\n')


def list_user_information() -> list:
    """Возвращает информацию о пользователях AD для таблицы"""
    lis = list(map(lambda x: x.split(': ')[1].strip(), filter(lambda x: x != '', subprocess.check_output(
        ["powershell", "-Command",
         'Get-AdUser -Filter * -Property * | Format-List SamAccountName, SID, Name, EmployeeID, PasswordLastSet, Enabled'],
        ).decode("CP866").split('\r\n'))))
    out = []
    for i in range(0, len(lis), 6):
        out.append((lis[i], lis[i + 1], lis[i + 2], lis[i + 3], lis[i + 4], lis[i + 5]))
    return out


def disable_user(name: str):
    """Блокирует AD аккаунт пользователя"""
    subprocess.check_output(
        ["powershell", "-Command",
         f'Disable-ADAccount -Identity {name}'],
        )


def enable_user(name: str):
    """Разблокирeет AD аккаунт пользователя"""
    subprocess.check_output(
        ["powershell", "-Command",
         f'Enable-ADAccount -Identity {name}'],
        )


def remove_computer(name: str):
    """Выводит ПК из домена"""
    subprocess.check_output(
        ["powershell", "-Command",
         f'Start-Process powershell -Verb runAs -WindowStyle Hidden -Wait "Remove-Computer -ComputerName {name} -Restart -Force"'],
        )


def add_computer(domain_name: str):
    """Добавляет ПК в домен"""
    subprocess.check_output(
        ["powershell", "-Command",
         f'Start-Process powershell -Verb runAs -WindowStyle Hidden -Wait "Add-Computer -DomainName {domain_name} -Restart -Force"'],
        )


def user_info(name: str) -> list:
    """Возвращает информацию о пользователе"""
    return subprocess.check_output(
        ["powershell", "-Command",
         f'Get-AdUser -Identity {name} -Property *'],
        ).decode("CP866").split('\r\n')


def move_user(user: str, directory: str):
    subprocess.check_output(
        ["powershell", "-Command",
         f'Move-ADObject -Identity "{user}" -TargetPath "{directory}"'])


def who_blocked_user(name: str):
    controller = subprocess.check_output(
            ["powershell", "-Command",
             f'(Get-ADDomainController -filter *).HostName'],
            ).decode("CP866").split('\r\n')[0]
    data = subprocess.check_output(
        ["powershell", "-Command",
        f""" Get-WMIObject -Class Win32_NTLogEvent -Computer {controller} -filter "Logfile='Security' AND EventCode=4725" | select -First 10"""],
        ).decode("CP866").split('\r\n')
    lis = list(map(lambda x: x.split(':')[1].strip(), filter(lambda x: 'Имя учетной записи:' in x, data)))
    lis = lis[:(len(lis) // 2) * 2]
    for i in range(0, len(lis), 2):
        if lis[i + 1] == name:
            return lis[i]
    return 'Не удалось найти информацию'


def in_domain() -> bool:
    """Проверяет, находится ли компьютер в домене"""
    return subprocess.check_output(
            ["powershell", "-Command",
             '(Get-WmiObject win32_computersystem).PartOfDomain']).decode("CP866").split('\r\n')[0] == 'True'
