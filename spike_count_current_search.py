import matplotlib
matplotlib.use("agg")
from nest_nu_backend import *
import quantities as pq
from neuronunit.tests.target_spike_current import SpikeCountSearch
from neuronunit.tests.fi import RheobaseTest

#julia> extremum_param
#10-element Array{Float64,1}:
#  2.547209933643486
#   7.036149590585986
# 700.0
# -64.33254842113216
#  13.383250387337624
# 300.0
# -45.0
#   3.390090501433403
# -61.185712499250116
#  20.0
# ranges_adexp[:"a"] = (2.0, 10)
#    ranges_adexp[:"b"] = (5.0, 10)
#    ranges_adexp[:"cm"] = (700.0, 983.5)
#    ranges_adexp[:"v0"] = (-70, -55)
#    ranges_adexp[:"τ_m"] = (10.0, 42.78345)
#    ranges_adexp[:"τ_w"] = (300.0, 454.0)  # Tau_w 0, means very low adaption
#   ranges_adexp[:"θ"] = (-45.0,-10)
#    ranges_adexp[:"delta_T"] = (1.0, 5.0)
#    ranges_adexp[:"v_reset"] = (-70.0, -15.0)
#   ranges_adexp[:"spike_delta"] = (1.25, 20.0)

model_params = {"V_peak": 10.0, "E_L": -40.0, "a": 2.54, "b": 7.03, "tau_w": 30.0}
model = NESTADEXP(nest=nest, attrs=model_params)
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

