import matplotlib.pyplot as plt

SILENT = True
import warnings

from neuronunit.plotting.plot_utils import check_bin_vm_soma
from neuronunit.allenapi.allen_data_driven import opt_setup
from sciunit.scores import RelativeDifferenceScore
import pandas as pd
import pickle
import quantities as pq

specimen_id = 325479788
model_type = "ADEXP"

##
# call opt_setup
##
"""
from nb_utils import optimize_job

fitnesses,scores,obs_preds,opt,target,hall_of_fame,cell_evaluator = optimize_job(specimen_id,
                                             model_type,
                                             score_type=RelativeDifferenceScore,
                                             efel_filter_iterable=efel_filter_iterable)
 

    
plt.plot(suite.traces["vm_soma"].times,suite.traces["vm_soma"])
plt.xlabel(pq.s)
plt.ylabel(suite.traces["vm_soma"].dimensionality)
plt.title("$V_{M}$ Allen Specimen id 325479788, sweep number 64")
plt.show()
"""
