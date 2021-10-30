Requirements: Install NEST-v3, python3.8, neo, sciunit and others.
### Install:
Install NEST,
pip install git+ssh://git@github.com/russelljjarvis/sciunit@dev
pip install git+ssh://git@github.com/russelljjarvis/BluePyOpt@neuronunit_reduced_cells


### Run
```python test_interface.py```
Code to make the NEST ADEXP single cell model optimizable via NeuronUnit and BluePyOpt.


![Output should look like this](https://github.com/russelljjarvis/NESTNeuronUnit/blob/master/NU_NEST.png)
```python
print(dir(model))
 '_backend', '_backend_run', '_class', '_id', '_properties', '_state', '_url', 'capabilities', 'check', 'check_params', 'check_run_params', 'curr_method', 'describe', 'description', 'dict_hash', 'extra_capability_checks', 'failed_extra_capabilities', 'get_backend', 'get_capabilities', 'get_membrane_potential', 'get_remote', 'get_remote_url', 'get_repo', 'get_spike_count', 'get_spike_train', 'get_version', 'hash', 'id', 'inject_square_current', 'is_match', 'json', 'model', 'name', 'nest', 'params', 'properties', 'raw_props', 'remote_url', 'reset_default_run_params', 'reset_run_params', 'run', 'run_args', 'set_attrs', 'set_backend', 'set_default_run_params', 'set_run_params', 'source_check', 'state', 'times', 'unimplemented', 'unpicklable', 'url', 'use_default_run_params', 'vM', 'verbose', 'version', 'voltmeter']

```

# DONE

- [x] Some basic NEST/NU interoperability
- [x] Inject current
- [x] set model parameters

## TODO
- [ ] Add appropriate sciunit model capabilities
- [ ] score a NU test.
- [ ] Run current search algorithm
