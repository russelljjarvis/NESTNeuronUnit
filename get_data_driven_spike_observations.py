from neo import AnalogSignal
from neuronunit.allenapi import make_allen_tests_from_id
specimen_id = (
    325479788,
    324257146,
    476053392,
    623893177,
    623960880,
    482493761,
    471819401
)
specimen_id = specimen_id[1]
target_num_spikes=7
sweep_numbers, data_set, sweeps = make_allen_tests_from_id.allen_id_to_sweeps(specimen_id)
(vmm,stimulus,sn,spike_times) = make_allen_tests_from_id.get_model_parts_sweep_from_spk_cnt(
    target_num_spikes, data_set, sweep_numbers, specimen_id
)


