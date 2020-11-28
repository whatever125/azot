import wmi
import datetime

ip = 'localhost'
username = ip + '\\' + 'username'
password = 'password'
# локальное подключение
conn = wmi.WMI()
# удаленное подключение
# conn = wmi.WMI(computer='', user=username, password=password, privileges=["RemoteShutdown"])

# свободное место на логических дисках
for disk in conn.Win32_LogicalDisk(DriveType=3):
    print(disk.Caption)
    print(float(disk.FreeSpace) / 1024 ** 3, 'GB free')
print()

# Информация о жестких дисках
for i in conn.Win32_DiskDrive():
    print(i.Model)
    print(float(i.Size) / 1024 ** 3, 'GB')
print()

# Операционная система, версия
for os in conn.Win32_OperatingSystem():
    print(os.Caption + ", version " + os.Version)
print()

# Название процессора
for pr in conn.Win32_Processor():
    print(pr.Name)
print()

# Название видеокарты, серийный номер
for vc in conn.Win32_VideoController():
    print(vc.Name)
    print(vc.PNPDeviceID)
print()

# объем оперативной памяти
for i in conn.Win32_ComputerSystem():
    print(float(i.TotalPhysicalMemory) / 1024 ** 3, "GB")
print()

# Модуль, ip, mac
for interface in conn.Win32_NetworkAdapterConfiguration(IPEnabled=1):
    print(interface.Description)
    print(interface.MACAddress)
    print(interface.IPAddress)
print()

# Время последнего включения
sdata = conn.Win32_PerfFormattedData_PerfOS_System()
uptime = sdata[-1].SystemUpTime
tnow = datetime.datetime.now()
utime = datetime.timedelta(seconds=int(uptime))
boot = tnow - utime
print(boot.day, boot.month, boot.year, boot.hour, boot.minute, boot.second)
print()

# Выключение
# os = conn.Win32_OperatingSystem(Primary=1)[0]
# os.Shutdown()
#
# Перезагрузка
# os = conn.Win32_OperatingSystem(Primary=1)[0]
# os.Reboot()

# Список процессов
for process in conn.Win32_Process():
    print(process.ProcessId, process.Name)
    # Пример завершения процесса
    if process.ProcessId == 10500:
        process.Terminate()
print()

# Сервисы
for service in conn.Win32_Service():
    print(service.Name, service.Description, service.ProcessId, service.StartMode, service.State)
    if service.Name == 'Name':
        service.StartService()  # Запуск сервиса
        service.StopService()  # Остановка сервиса
        service.Delete()  # Удаление сервиса
        service.ChangeStartMode(StartMode="")  # Изменение режима запуска: Boot, System, Manual, Automatic, Disabled
print()

# Группы и пользователи
for group in conn.Win32_Group():
    print(group.Caption, group.Description)
    for user in group.associators(wmi_result_class="Win32_UserAccount"):
        print("    ", user.Caption, user.FullName)
print()
