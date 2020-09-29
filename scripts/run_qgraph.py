import os
import pickle
import subprocess
from lsst.daf.butler import DimensionUniverse
from lsst.pipe.base import QuantumGraph, QuantumGraphTaskNodes

def write_qgnode(qgnode, outfile):
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    qgraph = QuantumGraph()
    qgraph.append(qgnode)
    with open(outfile, 'wb') as fd:
        pickle.dump(qgraph, fd)

visit = 204595
detmin = 92
detmax = 95

butlerConfig = 'gen3-repo/butler.yaml'
inCollection = 'LSST-ImSim/raw/all,LSST-ImSim/calib,refcats,skymaps/imsim'
outCollection = 'shared/qgraph_test'
qgraph_file = 'ProcessCcd.pickle'

# Initialize the run.
run_init = f'''pipetask run -b {butlerConfig} \\
    -i {inCollection} \\
    --output-run {outCollection} --init-only --skip-existing \\
    --register-dataset-types --qgraph {qgraph_file} --no-versions'''
print(run_init)
subprocess.check_call(run_init, shell=True)

# Load the quantum graph.
with open(qgraph_file, 'rb') as fd:
    qgraph = QuantumGraph.load(fd, DimensionUniverse())

# Loop over quanta in the nodes and run each quantum in turn.
i = 0
for nodes in qgraph:
    task_def = nodes.taskDef
    for quantum in nodes.quanta:
        my_nodes = QuantumGraphTaskNodes(task_def, [quantum],
                                         quantum.initInputs, {})
        quantum_file = f'quantum_dir/quantum_{i:03d}.pickle'
        i += 1
        write_qgnode(my_nodes, quantum_file)
        print()
        run_quantum = f'''pipetask run -b {butlerConfig} \\
           -i {inCollection} \\
           --output-run {outCollection} --extend-run --skip-init-writes \\
           --qgraph {quantum_file} --no-versions --skip-existing'''
        print(run_quantum)
        subprocess.check_call(run_quantum, shell=True)
