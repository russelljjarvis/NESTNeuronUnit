import matplotlib.pyplot as plt
from neo import AnalogSignal
import quantities as qt
from quantities import mV, ms, s

import nest
nest.ResetKernel()
nest.resolution = 0.1

import nest.voltage_trace
from sciunit.models import RunnableModel
class NESTADEXP(RunnableModel):
    def set_attrs(self,attrs):
        self.model.set(V_peak=attrs["V_peak"], E_L=attrs["E_L"],
        a=attrs["a"], b=attrs["b"], tau_w=attrs["tau_w"])


    def __init__(self,nest=nest, attrs = {}):

        self.model = nest.Create("aeif_cond_exp")
        backend = 'NEST'
        self.vM = None
        self.times = None
        self.set_attrs(attrs)
        self.nest = nest
        self.voltmeter = None
    def inject_square_current(self,c):
        simduration = float(c['delay'])+float(c['duration'])
        duration = float(c['duration'])
        start = float(c['delay'])
        amplitude = float(c['amplitude'])
        dc = nest.Create("dc_generator")
        dc.set(amplitude=amplitude, start=start, stop=duration)

        self.nest.Connect(dc, self.model, 'all_to_all')
        voltmeter = self.nest.Create("voltmeter", params={'interval': 0.1})
        self.nest.Connect(voltmeter, self.model)
        self.nest.Simulate(simduration)
        vM = voltmeter.get()["events"]["V_m"]
        vm = AnalogSignal(vM,
                     units = mV,
                     sampling_period = self.nest.resolution * ms)
        self.vM = vm
        self.voltmeter = voltmeter
    #def get_spike_count(self):
    #    spkcnt = len(self.voltmeter.get()["events"]["times"])
    #    print(self.voltmeter.get()["events"]["times"])
    #    return spkcnt
    def get_spike_train(self):
        train = self.voltmeter.get()["events"]["times"]
        return train


    def get_membrane_potential(self):
        return self.vM

    def _backend_run(self):
        results = {}
        results['vm'] = self.vM
        results['t'] = self.vM.times
        results['run_number'] = results.get('run_number',0) + 1
        return results
model_params={'V_peak':20., 'E_L':-60.0, 'a':80.0, 'b':80.5, 'tau_w':720.0}
model = NESTADEXP(nest=nest,attrs=model_params)
inject_param={'start':0*qt.ms,'stop':1000*qt.ms,'delay':100*qt.ms,'amplitude':900*qt.pA,'duration':1200*qt.ms}
model.inject_square_current(inject_param)
vm = model.get_membrane_potential()
plt.plot(vm.times,vm)
plt.show()
print(model.get_spike_count())
