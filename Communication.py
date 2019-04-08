import numpy as np
import socket
import time


class Gaveta(object):

    def __init__(self, gvt):
        self.gvt = gvt

    def connect(self):
        #ip = '10.128.45.' + str(self.gvt + 1)
        #Vitor
        ip = '10.0.6.' + str(self.gvt + 61)
        #Vitor
        time.sleep(0.03)
        try:
            self.socket = socket.create_connection((ip, 5000), timeout=3)
            return True
        except Exception:
            return False

    def disconnect(self):
        time.sleep(0.03)
        try:
            self.socket.close()
            return True
        except Exception:
            return False

    def read(self, msg):
        self.socket.send(('R' + msg).encode('utf-8'))
        resp = self.socket.recv(1024).decode('utf-8')
        time.sleep(0.030)
        if resp == 'NONE':
            return resp
        else:
            leitura = np.array(resp.split(';'), float)
            return leitura

    def read_channels(self, msg):
        self.socket.send(('R' + msg).encode('utf-8'))
        resp = self.socket.recv(1024).decode('utf-8')
        time.sleep(0.030)
        if resp == 'NONE':
            return resp
        else:
            leitura = np.array(resp.split(';'), int)
            return list(leitura)

    def reset_run_control(self):
        self.socket.send('WFR1'.encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def run_control(self):
        self.socket.send('WFS1'.encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
        return True

    def set_active_channels(self, chns):
        self.socket.send(('WH' + ';'.join(map(str, chns))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def set_enabled_channels(self, chns):
        if chns == []:
            self.socket.send(('WENONE').encode('utf-8'))
        else:
            self.socket.send(('WE' + ';'.join(map(str, chns))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def set_PT100(self, chns):
        if chns == []:
            self.socket.send(('WhNONE').encode('utf-8'))
        else:
            self.socket.send(('Wh' + ';'.join(map(str, chns))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def end_curves(self):
        self.socket.send(('WGR').encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
        self.socket.send(('WFR1').encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def interpolation_points(self, chn, points):
        self.socket.send(('WV' + str(chn) + ';' + ';'.join(points)).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def hold(self, chns):
        if chns == []:
            self.socket.send(('WLNONE').encode('utf-8'))
        else:
            self.socket.send(('WL' + ';'.join(map(str, chns))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def test(self, gvts, setpoint):
        string = [setpoint] * 8
        for gvt in gvts:
            self.socket.send(('WS' + ';'.join(map(str, string))).encode('utf-8'))
            self.socket.recv(1024).decode('utf-8')

    def turn_on(self):
        self.socket.send('WGS'.encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
        return True

    def get_initial_parameters(self, chn):
        self.socket.send(('Gr' + str(chn)).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
        self.socket.send(('GO' + str(chn)).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def set_parameters(self, r, t, a):
        self.socket.send(('Wr' + ';'.join(map(str, r))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
        self.socket.send(('WO' + ';'.join(map(str, t))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
        self.socket.send(('WA' + ';'.join(map(str, a))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')

    def set_t0(self, t):
        self.socket.send(('WO' + ';'.join(map(str, t))).encode('utf-8'))
        self.socket.recv(1024).decode('utf-8')
