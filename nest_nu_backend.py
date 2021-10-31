import nest
nest.set_verbosity(40)
#print(nest.version())
import nest.voltage_trace
from sciunit.models import RunnableModel
import matplotlib.pyplot as plt
from neo import AnalogSignal
import quantities as qt
from quantities import mV, ms, s
import numpy as np
try:
    import asciiplotlib as apl
except:
    pass
class NESTADEXP(RunnableModel):
    def set_attrs(self, attrs):
        self.model.set(
            V_peak=attrs["V_peak"],
            E_L=attrs["E_L"],
            a=attrs["a"],
            b=attrs["b"],
            tau_w=attrs["tau_w"],
        )
        self.attrs=attrs

    def __init__(self, nest=nest, attrs={}):

        self.model = nest.Create("aeif_cond_exp",n=1)
        backend = "NEST"
        
        self.vM = None
        self.times = None
        self.set_attrs(attrs)
        self.nest = nest
        self.voltmeter = None
        self.initiated = False
        self.ampl=0
        self.backend="NEST"
        self.lookup={}

    def inject_square_current(self, c={},amplitude=0*qt.pA,duration=0*qt.ms,delay=0*qt.ms,padding=0*qt.ms):
        #self.model = nest.Create("aeif_cond_exp",n=1)
        #self.set_attrs(self.attrs)
        #print(self.model.get())
        if len(c):
            duration = float(c["duration"])
            start = float(c["delay"])
            amplitude = float(c["amplitude"])
            simduration = float(c["delay"]) + float(c["duration"])
        else:
            start=float(delay)
            simduration = float(delay) + float(duration)#+float(padding)
            amplitude=float(amplitude)
            duration= float(duration)
        if not hasattr(self,"dc"):
              
            self.voltmeter = self.nest.Create("voltmeter", params={"interval": 0.1})            
          
            dc = nest.Create("dc_generator")
            self.dc = dc
            spike_rec = nest.Create('spike_recorder')
            self.spike_rec = spike_rec
            self.nest.Connect(self.dc, self.model, "all_to_all")
            self.nest.Connect(self.voltmeter, self.model)
            self.nest.Connect(self.model,self.spike_rec)

        
        self.dc.set(amplitude=amplitude, start=start, stop=duration)

        self.nest.Simulate(simduration)
        spikes = self.spike_rec.get('events', 'times')
        self.spikes=spikes
        vM = self.voltmeter.get()["events"]["V_m"]
        vm = AnalogSignal(vM, units=mV, sampling_period=self.nest.resolution * ms)
        self.vM = vm
        try:
            fig = apl.figure()
            fig.plot([float(t) for t in vm.times],[float(v) for v in vm], label="data", width=50, height=15)
            fig.show()
        except:
            pass
        return self.vM
        
    def get_spike_count(self):
        return len(self.spikes)

    def get_spike_train(self):
        return self.spikes

    def get_membrane_potential(self):
        return self.vM

    def _backend_run(self):
        results = {}
        results["vm"] = self.vM
        results["t"] = self.vM.times
        results["run_number"] = results.get("run_number", 0) + 1
        return results
