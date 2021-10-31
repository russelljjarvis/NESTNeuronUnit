import matplotlib
matplotlib.use("agg")
from nest_nu_backend import *
import quantities as pq
from neuronunit.tests.target_spike_current import SpikeCountSearch
model_params = {"V_peak": 20.0, "E_L": -60.0, "a": 80.0, "b": 80.5, "tau_w": 720.0}
model = NESTADEXP(nest=nest, attrs=model_params)
inject_param = {
    "start": 0 * qt.ms,
    "delay": 100 * qt.ms,
    "amplitude": 900 * qt.pA,
    "duration": 1200 * qt.ms,
}
model.inject_square_current(inject_param)
vm = model.get_membrane_potential()
print(model.get_spike_count())
plt.plot(vm.times, vm)
plt.xlabel(pq.ms)
plt.ylabel(vm.dimensionality)
plt.title("$V_{M}$ PyNest Simulator run")
plt.show()
plt.savefig("NUNEST.png")



observation = {}
observation["value"] = 10
scs = SpikeCountSearch(observation)
target_current = scs.generate_prediction(model)
print(target_current)

