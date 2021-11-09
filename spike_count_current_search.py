import matplotlib
matplotlib.use("agg")
#from nest_nu_backend import *
from nest_nu_izhi_backend import *
import quantities as pq
from neuronunit.tests.target_spike_current import SpikeCountSearch
from neuronunit.tests.fi import RheobaseTest

blank_izhi_cont = nest.Create("izhikevich",n=1)

model_params = {"a":blank_izhi_cont.get("a")}
model_params.update({"b":blank_izhi_cont.get("b")})
model_params.update({"c":blank_izhi_cont.get("c")})
model_params.update({"d":blank_izhi_cont.get("d")})
model_params.update({"V_m":blank_izhi_cont.get("V_m")})
model_params.update({"U_m":blank_izhi_cont.get("U_m")})
model_params.update({"V_min":blank_izhi_cont.get("V_min")})
model_params.update({"V_th":blank_izhi_cont.get("V_th")})
print(model_params)
model = NESTIZHI(nest=nest, attrs=model_params)
inject_param = {
    "start": 0 * qt.ms,
    "delay": 100 * qt.ms,
    "amplitude": 900 * qt.pA,
    "duration": 1200 * qt.ms,
}


observation = {}
observation["value"] = 10
rt = RheobaseTest(observation={"value":10*pq.pA})

target_current = rt.generate_prediction(model)
print(target_current)
import pdb
pdb.set_trace()
scs = SpikeCountSearch(observation)
target_current = scs.generate_prediction(model)
print(target_current)
inject_param["amplitude"] = target_current
model.inject_square_current(inject_param)
vm = model.get_membrane_potential()
print(model.get_spike_count())
plt.plot(vm.times, vm)
plt.xlabel(pq.ms)
plt.ylabel(vm.dimensionality)
plt.title("$V_{M}$ PyNest Simulator run")
plt.show()
plt.savefig("NUNEST.png")

