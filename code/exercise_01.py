import numpy as np

import pyhmf as pynn
from pymarocco import PyMarocco
import Coordinate as C
from pysthal.command_line_util import init_logger

init_logger("ERROR", [('sthal', 'INFO')])

marocco = PyMarocco()
marocco.default_wafer = C.Wafer(30)
marocco.calib_path = "/wang/data/calibration/brainscales/wip"
marocco.defects.path = marocco.calib_path
marocco.backend = PyMarocco.Hardware
marocco.persist = "exercise_01.xml.gz"
marocco.checkl1locking = PyMarocco.CheckButIgnore
marocco.verification = PyMarocco.Skip
pynn.setup(marocco=marocco)
           
neuron_parameters = {
    'cm':        0.2, # nF
    'v_reset':   -30, # mV
    'v_rest':    -20, # mV
    'v_thresh':  -16, # mV
    'e_rev_I':   -40, # mV
    'e_rev_E':     0, # mV
    'tau_m':      10, # ms
    'tau_refrac':  1, # ms
    'tau_syn_E':   5, # ms
    'tau_syn_I':   5, # ms
}

population = pynn.Population(2, pynn.IF_cond_exp, neuron_parameters)
population.record()

neuron0 = pynn.PopulationView(population, [0])
neuron0.record_v()
neuron1 = pynn.PopulationView(population, [1])
neuron1.record_v()

stimulus_0 = pynn.Population(1, pynn.SpikeSourceArray, {"spike_times" : [10,50,55,60,65,105,110,115,120,125]}) # in ms
stimulus_1 = pynn.Population(1, pynn.SpikeSourceArray, {"spike_times" : [300,310,320,325,330,335,340,345]}) # in ms

marocco.manual_placement.on_hicann(stimulus_1, C.HICANNOnWafer(C.Enum(98)))

pynn.Projection(stimulus_0, neuron0, pynn.AllToAllConnector(weights=0.005), target="excitatory") # weight in uS
pynn.Projection(stimulus_0, neuron1, pynn.AllToAllConnector(weights=0.005), target="excitatory") # weight in uS

pynn.Projection(stimulus_1, neuron0, pynn.AllToAllConnector(weights=0.1), target="excitatory") # weight in uS
pynn.Projection(stimulus_1, neuron1, pynn.AllToAllConnector(weights=0.1), target="excitatory") # weight in uS

print "starting experiment"
pynn.run(500) # in ms
pynn.end()

print "storing results"
np.savetxt("spikes_nrn0.txt", neuron0.getSpikes())
np.savetxt("membrane_nrn0.txt", neuron0.get_v())

np.savetxt("spikes_nrn1.txt", neuron1.getSpikes())
np.savetxt("membrane_nrn1.txt", neuron1.get_v())

print "done"