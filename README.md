Requirements: Install NEST-v3, python3.8, neo, sciunit and others.
## Install:
### To test interopability
- [] Install NEST
- [] Install sciunit
```
pip install git+https://github.com/russelljjarvis/sciunit@dev
```
### To Do a BPO data driven optimization on the reduced model via NU model scoring
- [] Install BPO
- [] Install sciunit
- [] Install neuronunit
```
pip install git+https://github.com/russelljjarvis/sciunit@dev
pip install git+https://github.com/russelljjarvis/BluePyOpt@neuronunit_reduced_cells
pip install git+https://github.com/russelljjarvis/neuronunit
```

### Run
```python test_interface.py```
Code to make the NEST ADEXP single cell model optimizable via NeuronUnit and BluePyOpt.


![Output should look like this](https://github.com/russelljjarvis/NESTNeuronUnit/blob/master/NU_NEST.png)

# DONE

- [x] Some basic NEST/NU interoperability
- [x] Inject current
- [x] set model parameters

## TODO
- [ ] score a NU test against NEST model
- [ ] Run current search algorithm against NEST model
- [ ] Optimize a NEST model
