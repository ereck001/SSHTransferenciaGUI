#Programa de copia de arquivos na rede da PMP

import sys
from ui_login import Ui_Form
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget)
from ui_main import Ui_MainWindow

import paramiko
import socket

from scp import SCPClient




client = paramiko.SSHClient()

client.load_system_host_keys()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())







class Login(QWidget,Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.setFixedSize(600, 600)
        self.pushButton.clicked.connect(self.open_system)

    def open_system(self):
        if self.passwdInput.text() == "" and self.userInput.text().lower() == '':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('Senha inválida!\n')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Transferidor de arquivos PMP")
        self.setFixedSize(800, 800)
        self.setupUi(self)
        self.setWindowTitle("Main teste")
        self.radioButton.clicked.connect(self.checkTR)
        self.radioButton_3.clicked.connect(self.uncheckTR)
        self.radioButton_2.clicked.connect(self.uncheckTR)
        self.pushButton.clicked.connect(self.resposta)

    def checkTR(self):

        if self.radioButton.isChecked():
            self.inputIp.setVisible(False)
            self.inputLoja.setVisible(False)
    def uncheckTR(self):

        if not self.radioButton.isChecked():
            self.inputIp.setVisible(True)
            self.inputLoja.setVisible(True)



    def resposta(self):



        def transfCaixa( loja, caixa,pathFrom,pathTo):
            response = ''
            try:

                client.connect(hostname='192.168.{}.{}'.format(int(loja),int(caixa)),username='user', password='password',timeout=4)

                # Arquivos a serem copiados

                response = "copiando...\n Caixa {}\n".format(str(caixa))

                with SCPClient(client.get_transport()) as scp:

                    scp.put(pathFrom, pathTo)

                response +=' OK!'



            except paramiko.ssh_exception.NoValidConnectionsError as e:

                response = 'Host inacessível'

            except socket.timeout as e:

                response = 'Host inacessível'





                response ='Host inacessível'
            return response

        def transfBalcao( loja, caixa,pathFrom,pathTo):
            response = ''
            try:

                client.connect(hostname='192.168.{}.{}'.format(int(loja),int(caixa)),username='user', password='password',timeout=4)

                # Arquivos a serem copiados

                response = "copiando...\n Caixa {}\n".format(str(caixa))

                with SCPClient(client.get_transport()) as scp:

                    scp.put(pathFrom, pathTo)

                response +=' OK!'



            except paramiko.ssh_exception.NoValidConnectionsError as e:

                response = 'Host inacessível'

            except socket.timeout as e:

                response = 'Host inacessível'


            return response


        try:
            if self.radioButton_2.isChecked():
                if self.inputPathTo.text() != "" and self.inputPathFrom.text() != "":
                    pathTo = self.inputPathTo.text()
                    pathFrom = self.inputPathFrom.text()
                    res = transfCaixa(self.inputLoja.text(), self.inputIp.text(), pathFrom, pathTo)

                    self.terminal.setText(res)
                else:
                    self.terminal.setText("digite o caminho do arquivo")

            if self.radioButton_3.isChecked():

                if self.inputPathTo.text() != "" and self.inputPathFrom.text() != "":
                    pathTo = self.inputPathTo.text()
                    pathFrom = self.inputPathFrom.text()
                    res = transfBalcao(self.inputLoja.text(), self.inputIp.text(), pathFrom, pathTo)

                    self.terminal.setText(res)
                else:
                    self.terminal.setText("digite o caminho do arquivo")
        except FileNotFoundError:
            self.terminal.setText("Caminho errado ou arquivo inexistente")

        if self.radioButton.isChecked():

            pathTo = self.inputPathTo.text()
            pathFrom = self.inputPathFrom.text()

            for loja in range(1, 200):


                for caixa in range(1, 4):


                    try:

                        # res = "Loja {}\n".format(loja)
                        # self.terminal.setText(res)

                        print("Loja{}".format(loja))

                        client.connect(hostname='192.168.{}.{}'.format(loja, caixa + 20),username='user',password='password',timeout=4)

                        # Arquivos a serem copiados
                        print( "copiando...\n Caixa {}".format(caixa))
                        #res += "copiando...\n Caixa {}".format(caixa)
                        #self.terminal.setText(res)

                        with SCPClient(client.get_transport()) as scp:

                            scp.put(pathFrom, pathTo)

                        # res += ' OK!'
                        #self.terminal.setText(res)



                    except paramiko.ssh_exception.NoValidConnectionsError as e:

                        print('Host inacessível')
                        # res = 'Host inacessível'
                        # self.terminal.setText(res)
                    except socket.timeout as e:

                        print('Host inacessível')
                        # res = 'Host inacessível'
                        # self.terminal.setText(res)



                    except paramiko.ssh_exception.NoValidConnectionsError as e:

                        res = 'Host inacessível'
                        self.terminal.setText(res)

                    # for balcao in range(1, 6):

                    #     try:


                    #         res = "Loja {}".format(loja)
                    #         self.terminal.setText(res)

                    #         client.connect(hostname='192.168.{}.{}'.format(loja, balcao),username='user',password='password',timeout=4)

                    #         # Arquivos a serem copiados

                    #         self.terminal.setText("copiando...\n Balcão {}".format(caixa))

                    #         with SCPClient(client.get_transport()) as scp:

                    #             scp.put('c:/logo_pmp.ico', '/home/caixa/Downloads/logo_pmp.ico')

                    #         self.terminal.append(' OK!')



                    #     except paramiko.ssh_exception.NoValidConnectionsError as e:

                    #         self.terminal.append('Host inacessível')

                    #     except socket.timeout as e:

                    #         self.terminal.append('Host inacessível')



                    #     except paramiko.ssh_exception.NoValidConnectionsError as e:

                    #         self.terminal.append('Host inacessível')







if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()