import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QScrollBar, QTreeWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal, QObject
import PyQt5.QtGui as QtGui
import xlsxwriter
import time
import threading
import main

class Signal(QObject):
    signal = pyqtSignal()
    user_signal = pyqtSignal()


class SAMThread(QThread):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def run(self):
        if type(self.widget) == InfWidget:
            self.get_pc_info()
        elif type(self.widget) == UserInfWidget:
            self.get_user_info()
        elif type(self.widget) == MyWidget:
            if self.widget.clicked_button == 0:
                self.request()
            else:
                self.load_users()
        elif type(self.widget) == ManWidget:
            self.pc_management()
        elif type(self.widget) == UserManWidget:
            self.user_management()

    def get_pc_info(self):
        ip = self.widget.ip
        self.widget.tabWidget.setEnabled(False)

        self.widget.error.setText('Загрузка информации о дисках...')
        hdd = self.widget.format_information(main.hdd_info(ip))
        self.widget.textEdit.clear()
        for i in hdd:
            self.widget.textEdit.append(i)

        self.widget.error.setText('Загрузка информации о разделах...')
        disks = self.widget.format_information(main.logical_disk_info(ip))
        self.widget.textEdit_7.clear()
        for i in disks:
            self.widget.textEdit_7.append(i)
        self.widget.textEdit_7.moveCursor(QtGui.QTextCursor.Start)

        self.widget.error.setText('Загрузка информации об операционной системе...')
        os = self.widget.format_information(main.os_info(ip))
        self.widget.textEdit_2.clear()
        for i in os:
            self.widget.textEdit_2.append(i)

        self.widget.error.setText('Загрузка информации о процессорах...')
        cpu = self.widget.format_information(main.cpu_info(ip))
        self.widget.textEdit_3.clear()
        for i in cpu:
            self.widget.textEdit_3.append(i)

        self.widget.error.setText('Загрузка информации об оперативной памяти...')
        ram = self.widget.format_information(main.ram_info(ip))
        self.widget.textEdit_5.clear()
        for i in ram:
            self.widget.textEdit_5.append(i)

        self.widget.error.setText('Загрузка информации о видеокартах...')
        vc = self.widget.format_information(main.vc_info(ip))
        self.widget.textEdit_4.clear()
        for i in vc:
            self.widget.textEdit_4.append(i)

        self.widget.error.setText('Загрузка информации о сетевых адаптерах...')
        net = self.widget.format_information(main.net_info(ip))
        self.widget.textEdit_6.clear()
        for line in net:
            self.widget.textEdit_6.append(line)

        # self.widget.error.setText('Загрузка информации о пользователях...')
        # groups = main.group_list(ip)
        # for i, group in enumerate(groups):
        #     item = QTreeWidgetItem()
        #     item.setText(0, group)
        #     for j in main.list_group_users(ip, group):
        #         child = QTreeWidgetItem(item)
        #         child.setText(0, j)
        #     self.widget.treeWidget.insertTopLevelItem(i, item)

        self.widget.textEdit.moveCursor(QtGui.QTextCursor.Start)
        self.widget.textEdit_2.moveCursor(QtGui.QTextCursor.Start)
        self.widget.textEdit_3.moveCursor(QtGui.QTextCursor.Start)
        self.widget.textEdit_4.moveCursor(QtGui.QTextCursor.Start)
        self.widget.textEdit_5.moveCursor(QtGui.QTextCursor.Start)
        self.widget.textEdit_6.moveCursor(QtGui.QTextCursor.Start)
        self.widget.textEdit_7.moveCursor(QtGui.QTextCursor.Start)

        self.widget.error.setText('')
        self.widget.tabWidget.setEnabled(True)

    def get_user_info(self):
        self.widget.textEdit.clear()
        self.widget.error.setText('Загрузка информации о пользователе...')
        for line in main.user_info(self.widget.name):
            self.widget.textEdit.append(line)
        self.widget.error.setText('')

    def request(self):
        self.widget.error.setText('Загрузка информации о компьютерах...')
        # ips = main.get_ips()
        ips = [('netbook-19', 'localhost'), ('netbook-4', '192.168.137.48'), ('netbook',  '192.168.137.123')]
        pc_data = []
        for i, j in enumerate(ips):
            pc_data.append((j[0],
                            j[1],
                            ', ',
                            ', ',
                            f'{round(main.free_space(j[1]), 2)} GB',
                            f'{round(main.ram_capacity(j[1]), 2)} GB',
                            ', '.join(main.processor_name(j[1])),
                            main.last_boot_up_time(j[1])))
        self.widget.s.signal.emit()
        self.widget.pc_info = pc_data
        self.widget.error.setText('')

    def load_users(self):
        self.widget.error.setText('Загрузка информации о пользователях...')
        users_data = main.list_user_information()
        self.widget.users_info = users_data
        self.widget.s.user_signal.emit()
        self.widget.error.setText('')

    def pc_management(self):
        self.widget.error.setText('Загрузка информации о процессах...')
        self.widget.tabWidget.setEnabled(False)
        process = main.process_info(self.widget.ip)
        self.widget.tableWidget.setRowCount(len(process))
        self.widget.tableWidget.clearContents()
        self.widget.tableWidget.horizontalHeader().setSectionResizeMode(1)
        for i, j in enumerate(process):
            self.widget.tableWidget.setItem(i, 0, QTableWidgetItem(j[0]))
            self.widget.tableWidget.setItem(i, 1, QTableWidgetItem(j[1]))
        self.widget.error.setText('Загрузка информации о службах...')
        serv = main.service_info(self.widget.ip)
        self.widget.tableWidget_2.setRowCount(len(serv))
        self.widget.tableWidget_2.clearContents()
        self.widget.tableWidget_2.horizontalHeader().setSectionResizeMode(1)
        for i, j in enumerate(serv):
            self.widget.tableWidget_2.setItem(i, 0, QTableWidgetItem(j[0]))
            self.widget.tableWidget_2.setItem(i, 1, QTableWidgetItem(j[1]))
            self.widget.tableWidget_2.setItem(i, 2, QTableWidgetItem(j[2]))
        self.widget.tabWidget.setEnabled(True)
        self.widget.error.setText('')

    def user_management(self):
        pass


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clicked_button = 0
        self.s = Signal()
        self.s.signal.connect(self.load_table)
        self.s.user_signal.connect(self.load_user_table)
        uic.loadUi('azot.ui', self)
        self.pc_info = []
        self.users_info = []
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.export)
        self.pushButton_3.clicked.connect(self.pc_information)
        self.pushButton_4.clicked.connect(self.pc_management)
        self.pushButton_5.clicked.connect(self.request)
        self.pushButton_8.clicked.connect(self.user_management)
        self.pushButton_9.clicked.connect(self.load_users)
        self.pushButton_10.clicked.connect(self.user_information)

        self.tableWidget.horizontalHeader().setSectionResizeMode(1)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1)

        # self.start_thread()

    def start_thread(self):
        self.thread = threading.Thread(target=self.threading_func, daemon=True)
        self.thread.start()

    def threading_func(self):
        while True:
            sleep = self.spinBox.value() * 60
            self.request()
            for i in range(sleep):
                time.sleep(1)
                if self.spinBox.value() * 60 != sleep:
                    continue

    def export(self):
        fname = QFileDialog.getSaveFileName(self, 'Cохранить файл',
                                            'computers.xlsx', "Excel(*.xlsx)")[0]
        if fname[-5:] != '.xlsx':
            fname += '.xlsx'
        export = []
        for i in range(self.tableWidget.rowCount()):
            export.append(list())
            for j in range(self.tableWidget.columnCount()):
                if self.tableWidget.item(i, j):
                    export[-1].append(self.tableWidget.item(i, j).text())
                else:
                    export[-1].append('')
        workbook = xlsxwriter.Workbook(fname)
        worksheet = workbook.add_worksheet()
        for i in range(self.tableWidget.columnCount()):
            worksheet.write(0, i, self.tableWidget.horizontalHeaderItem(i).text())
        for i in range(len(export)):
            for j in range(len(export[i])):
                worksheet.write(i + 1, j, export[i][j])
        workbook.close()

    def pc_information(self):
        try:
            self.setEnabled(False)
            self.error.setText('')
            self.inf = InfWidget(self.tableWidget.selectedItems()[1].text(), self)
        except IndexError:
            self.setEnabled(True)
            self.error.setText('Выберите компьютер')

    def user_information(self):
        self.inf2 = UserInfWidget(self.tableWidget_2.selectedItems()[0].text(), self)

    def pc_management(self):
        self.man = ManWidget(self.tableWidget.selectedItems()[1].text(), self)
        self.man.show()

    def user_management(self):
        self.man2 = UserManWidget(self.tableWidget_2.selectedItems()[0].text(), self)
        self.man2.show()

    def search(self):
        self.tableWidget.clearContents()
        table3 = list(filter(lambda x: self.lineEdit.text() in x[0], self.table2))
        self.tableWidget.setRowCount(len(table3))
        for i in range(len(table3)):
            for j in range(len(table3[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(table3[i][j]))

    def request(self):
        self.clicked_button = 0
        self.thread = SAMThread(self)
        self.thread.start()

    def load_table(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(len(self.pc_info))
        self.tableWidget.clearContents()
        for i, j in enumerate(self.pc_info):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(j[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(j[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(j[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(j[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(j[4]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(j[5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(j[6]))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(j[7]))
        self.tableWidget.setSortingEnabled(True)
        self.table2 = []
        for i in range(self.tableWidget.rowCount()):
            self.table2.append(list())
            for j in range(self.tableWidget.columnCount()):
                if self.tableWidget.item(i, j):
                    self.table2[-1].append(self.tableWidget.item(i, j).text())
                else:
                    self.table2[-1].append('')

    def load_user_table(self):
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setRowCount(len(self.users_info))
        self.tableWidget_2.clearContents()
        for i, j in enumerate(self.users_info):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(j[0]))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(j[1]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(j[2]))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(j[3]))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(j[4]))
            self.tableWidget_2.setItem(i, 5, QTableWidgetItem(j[5]))
        self.tableWidget_2.setSortingEnabled(True)

    def load_users(self):
        self.clicked_button = 1
        self.thread = SAMThread(self)
        self.thread.start()


class InfWidget(QWidget):
    def __init__(self, ip, parent):
        super().__init__()
        self.ip = ip
        self.parent = parent

        uic.loadUi('information_pc.ui', self)
        self.show()
        self.treeWidget.header().setSectionResizeMode(5)
        self.thread = SAMThread(self)
        self.thread.start()

    def format_information(self, inf):
        while inf[0] == '':
            inf = inf[1:]
        while inf[-1] == '':
            inf = inf[:-1]
        return list(map(lambda x: '\n' * 2 + '-' * 80 + '\n' * 2 if x == '' else x, inf))

    def closeEvent(self, event):
        self.parent.setEnabled(True)


class UserInfWidget(QWidget):
    def __init__(self, name, parent):
        super().__init__()
        self.parent = parent
        self.name = name

        uic.loadUi('information_user.ui', self)
        self.show()
        self.thread = SAMThread(self)
        self.thread.start()


class ManWidget(QWidget):
    def __init__(self, ip, parent):
        super().__init__()
        self.ip = ip
        self.parent = parent
        uic.loadUi('management_pc.ui', self)
        self.show()
        self.thread = SAMThread(self)
        self.thread.start()
        self.pushButton.clicked.connect(self.threading_run_register)
        self.pushButton_2.clicked.connect(self.threading_shutdown)
        self.pushButton_3.clicked.connect(self.threading_reboot)
        self.pushButton_4.clicked.connect(self.threading_terminate_process)
        self.pushButton_5.clicked.connect(self.threading_start_service)
        self.pushButton_6.clicked.connect(self.threading_stop_service)

    def threading_shutdown(self):
        self.thread = threading.Thread(target=self.terminate_process)
        self.thread.start()

    def shutdown(self):
        self.error.setText('Выключаю компьютер...')
        main.shutdown(self.ip)
        self.error.setText('Готово')

    def threading_reboot(self):
        self.thread = threading.Thread(target=self.terminate_process)
        self.thread.start()

    def reboot(self):
        self.error.setText('Перезагружаю компьютер...')
        main.reboot(self.ip)
        self.error.setText('Готово')

    def threading_terminate_process(self):
        self.thread = threading.Thread(target=self.terminate_process)
        self.thread.start()

    def terminate_process(self):
        self.error.setText('Останавливаю процесс...')
        main.terminate_process_by_id(self.tableWidget.selectedItems()[1].text(), self.ip)
        self.tableWidget.removeRow(self.tableWidget.selectedItems()[1].row())
        self.error.setText('Готово')

    def threading_start_service(self):
        self.thread = threading.Thread(target=self.stop_service)
        self.thread.start()

    def start_service(self):
        self.error.setText('Запускаю службу...')
        main.start_service(self.tableWidget_2.selectedItems()[0].text(), self.ip)
        self.tableWidget_2.selectedItems()[2].setText('Running')
        self.error.setText('Готово')

    def threading_stop_service(self):
        self.thread = threading.Thread(target=self.stop_service)
        self.thread.start()

    def stop_service(self):
        self.error.setText('Останавливаю службу...')
        main.stop_service(self.tableWidget_2.selectedItems()[0].text(), self.ip)
        self.tableWidget_2.selectedItems()[2].setText('Stopped')
        self.error.setText('Готово')

    def threading_run_register(self):
        self.thread = threading.Thread(target=self.run_register)
        self.thread.start()

    def run_register(self):
        self.error.setText('Запускаю редактор реестра...')
        main.run_register(self.ip)
        self.error.setText('Готово')


class UserManWidget(QWidget):
    def __init__(self, name, parent):
        super().__init__()
        self.parent = parent
        self.name = name
        uic.loadUi('management_user.ui', self)
        self.pushButton.clicked.connect(self.start_block_user)
        self.pushButton_2.clicked.connect(self.start_unblock_user)

    def start_block_user(self):
        self.thread = threading.Thread(target=self.block_user, daemon=True)
        self.thread.start()

    def start_unblock_user(self):
        self.thread = threading.Thread(target=self.unblock_user, daemon=True)
        self.thread.start()

    def block_user(self):
        self.error.setText('Блокирую пользователя...')
        main.disable_user(self.name)
        self.error.setText('Готово')

    def unblock_user(self):
        self.error.setText('Разблокирую пользователя...')
        main.enable_user(self.name)
        self.error.setText('Готово')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
