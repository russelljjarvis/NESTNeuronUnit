# About
Code to make the NEST ADEXP single cell model optimizable via NeuronUnit and BluePyOpt.

## Install:
### To test interopability
- Install NEST https://nest-simulator.readthedocs.io/en/stable/installation/linux_install.html
- Install sciunit
- Install Neo, quantities
```
pip install git+https://github.com/russelljjarvis/sciunit@dev
```

### Preliminary Run
```python test_interface.py```
```python spike_current_search.py```



![Output should look like this](https://github.com/russelljjarvis/NESTNeuronUnit/blob/master/NUNEST.png)

# DONE

- [x] Some basic NEST/NU interoperability
- [x] Inject current
- [x] set model parameters
- [x] RheobaseTest generate prediction, 
- [x] SpikeCurrentSearch Generate Prediction.

## TODO
- [ ] Find sensible NEST, Adexp parameter range.
- [ ] score a NU test against NEST model
- [ ] Run current search algorithm against NEST model
- [ ] Optimize a NEST model

### Future: to Do a BPO data driven optimization on the reduced model via NU model scoring
- Install BPO
- Install sciunit
- Install neuronunit
```
pip install git+https://github.com/russelljjarvis/sciunit@dev
pip install git+https://github.com/russelljjarvis/BluePyOpt@neuronunit_reduced_cells
pip install git+https://github.com/russelljjarvis/neuronunit
```
