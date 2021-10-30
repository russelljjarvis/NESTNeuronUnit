from nest_nu_backend import *

model_params = {"V_peak": 20.0, "E_L": -60.0, "a": 80.0, "b": 80.5, "tau_w": 720.0}
model = NESTADEXP(nest=nest, attrs=model_params)
inject_param = {
    "start": 0 * qt.ms,
    "stop": 1000 * qt.ms,
    "delay": 100 * qt.ms,
    "amplitude": 900 * qt.pA,
    "duration": 1200 * qt.ms,
}
model.inject_square_current(inject_param)
vm = model.get_membrane_potential()
plt.plot(vm.times, vm)
plt.show()