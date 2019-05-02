from collections import defaultdict
import time

from PyQt4.QtCore import QTimer, QTime

import Communication
import numpy as np
import pyqtgraph as pg


class Lib(object):

    def __init__(self):
        self.App = None
        self.control = self.Control_Variables()
        self.measurements = self.Measurements().dict_measurements
        self.config = self.Configuration()
        self.vars = self.Variables()
        self.graph = self.Graph_plots()
        
        # 11 gavetas podem ser conectadas
        self.fitaaque1 = Communication.Gaveta(0)
        self.fitaaque2 = Communication.Gaveta(1)
        self.fitaaque3 = Communication.Gaveta(2)
        self.fitaaque4 = Communication.Gaveta(3)
        self.fitaaque5 = Communication.Gaveta(4)
        self.fitaaque6 = Communication.Gaveta(5)
        self.fitaaque7 = Communication.Gaveta(6)
        self.fitaaque8 = Communication.Gaveta(7)
        self.fitaaque9 = Communication.Gaveta(8)
        self.fitaaque10 = Communication.Gaveta(9)
        self.fitaaque11 = Communication.Gaveta(10)

    def reading_th(self, g):
        while(self.control.run_control_on[g]):
            time.sleep(self.control.meas_time)
            try:
                self.vars.temperatures[g] = getattr(self, 'fitaaque' + str(g + 1)).read('p')
                self.vars.temp_res[g] = getattr(self, 'fitaaque' + str(g + 1)).read('t')
                self.vars.temp_pt100[g] = getattr(self, 'fitaaque' + str(g + 1)).read('T')
                self.vars.currents[g] = getattr(self, 'fitaaque' + str(g + 1)).read('I')
                self.vars.voltages[g] = getattr(self, 'fitaaque' + str(g + 1)).read('U')
                self.vars.powers[g] = getattr(self, 'fitaaque' + str(g + 1)).read('W')
                
                for chn in self.control.channels_on[g]:
                    index = self.vars.channels[g].index(chn)
                    self.vars.time_now[g][chn] = round(time.time() - self.vars.start_time[g][chn])
                    self.measurements['Temperatura'][g][chn] = np.append(self.measurements['Temperatura'][g][chn], float(self.vars.temperatures[g][index]))
                    self.measurements['Tensão'][g][chn] = np.append(self.measurements['Tensão'][g][chn], float(self.vars.voltages[g][index]))
                    self.measurements['Potência'][g][chn] = np.append(self.measurements['Potência'][g][chn], float(self.vars.powers[g][index]))
                    self.measurements['Corrente'][g][chn] = np.append(self.measurements['Corrente'][g][chn], float(self.vars.currents[g][index]))
                    self.measurements['Tempo'][g][chn] = np.append(self.measurements['Tempo'][g][chn], self.vars.time_now[g][chn])
                    
                tmp = time.localtime()
                datetime = time.strftime('%d/%m/%Y %H:%M:%S', tmp)
                
                _temps = [' '] * 8
                _temps_res = [' '] * 8
                _temps_pt = [' '] * 8
                _crnts = [' '] * 8
                _volts = [' '] * 8
                _pwrs = [' '] * 8
                
                for chn in range(8):
                    if chn in self.control.channels_on[g]:
                        index = self.vars.channels[g].index(chn)
                        _temps[chn] = self.vars.temperatures[g][index]
                        _temps_res[chn] = self.vars.temp_res[g][index]
                        _temps_pt[chn] = self.vars.temp_pt100[g][index]
                        _crnts[chn] = self.vars.currents[g][index]
                        _volts[chn] = self.vars.voltages[g][index]
                        _pwrs[chn] = self.vars.powers[g][index]
                        
                _temps = '\t'.join(map(str, _temps))
                _temps_res = '\t'.join(map(str, _temps_res))
                _temps_pt = '\t'.join(map(str, _temps_pt))
                _crnts = '\t'.join(map(str, _crnts))
                _volts = '\t'.join(map(str, _volts))
                _pwrs = '\t'.join(map(str, _pwrs))
                         
                self.vars.file[g].write(datetime + '\t' + _temps + '\t' + _temps_res + '\t' + _temps_pt + '\t' + _crnts + '\t' + _volts + '\t' + _pwrs)
                self.vars.file[g].write('\n')
                self.vars.file[g].flush()
            except:
                pass
            
    class Control_Variables(object):

        def __init__(self):
            self.GAVETAS = []
            self.GAVETAS_ON = []
            self.group = defaultdict(list)
            self.channels_on = defaultdict(list)
            self.channels_off = defaultdict(list)
            self.PT100_channels = defaultdict(list)
            self.holded_channels = defaultdict(list)
            self.plot_group_grps = defaultdict(list)
            self.plot_group_gvts = defaultdict(list)
            
            for i in range(3):
                self.group[i] = defaultdict(list)
            
            for i in range(11):
                self.plot_group_gvts[i] = [False] * 3
            for i in range(4):
                self.plot_group_grps[i] = [False] * 4
            
            self.curves_on = [False] * 11
            self.run_control_on = [False] * 11
            self.measurements_ON = False
            self.meas_time = None

    class Measurements(object):

        def __init__(self):
            temperature = []
            voltage = []
            power = []
            current = []
            time_on = []
            
            for i in range(11):
                temperature.append([])
                voltage.append([])
                power.append([])
                current.append([])
                time_on.append([])
                for j in range(8):
                    temperature[i].append(np.array([]))
                    voltage[i].append(np.array([]))
                    power[i].append(np.array([]))
                    current[i].append(np.array([]))
                    time_on[i].append(np.array([]))
            
            self.dict_measurements = {'Temperatura': temperature, 'Potência': power, 'Corrente': current, 'Tensão': voltage, 'Tempo': time_on}

    class Configuration(object):

        def __init__(self):
            self.temp = []
            self.times = []
            self.taxa = dict()
            self.patamar = dict()
            self.temp_est = dict()
            self.n_est_aq = [1] * 3
            self.n_aq_temp = [1] * 3
            self.n_aq_taxa = [1] * 3
            self.n_aq_patamar = [1] * 3
                   
            for i in range(11):
                self.temp.append(defaultdict(list))
                self.times.append(defaultdict(list)) 
            
            for i in range(3):
                self.taxa[i] = []
                self.patamar[i] = []
                self.temp_est[i] = []

    class Variables(object):

        def __init__(self):
            self.temperatures = []
            self.temp_res = []
            self.temp_pt100 = []
            self.currents = []
            self.voltages = []
            self.powers = []
            self.times = []
            
            self.channels = dict()
            
            for i in range(11):
                self.channels[i] = []
                self.temperatures.append(np.array([]))
                self.temp_res.append(np.array([]))
                self.temp_pt100.append(np.array([]))
                self.currents.append(np.array([]))
                self.voltages.append(np.array([]))
                self.powers.append(np.array([]))
                self.times.append(np.array([]))

            self.file = [None] * 11
            self.hours = [0] * 3
            self.mins = [0] * 3
            self.secs = [0] * 3
            
            self.interpolation_points = []
            self.start_time = []
            self.hold_start = []
            self.time_now = []
            self.total_time = []
            self.name = []
            self.r0 = []
            self.t0 = []
            self.a = []
                
            for i in range(11):
                self.interpolation_points.append(defaultdict(list))
                self.start_time.append(defaultdict(list))
                self.hold_start.append(defaultdict(list))
                self.time_now.append(defaultdict(list))
                self.total_time.append(defaultdict(list))
                self.name.append(defaultdict(list))
                self.r0.append([])
                self.t0.append([])
                self.a.append([])
                for j in range(8):
                    self.name[i][j] = 'G' + str(i + 1) + 'S' + str(j + 1) + 'ab'
            
    class Graph_plots(object):
        
        def __init__(self):
            self.exp_gvt = defaultdict(list)
            self.exp_grp = defaultdict(list)
            self.curves_grp = defaultdict(list)
            self.curves_gvt = defaultdict(list)
            
            for i in range(11):
                self.exp_gvt[i] = [None] * 3
                
            for i in range(4):
                self.exp_grp[i] = [None] * 3
                
            self.unit = {'Temperatura': '°C', 'Potência': 'Watts', 'Corrente': 'Amp', 'Tensão': 'Volts'}
            self.pen = ['r', (0, 147, 108), 'b', 'm', (170, 0, 0), (132, 112, 255), 'k', (255, 165, 0), (0, 96, 144), (170, 0, 127), (100, 100, 0)]
            self.pen_esp = ['c', 'g', 'y']
