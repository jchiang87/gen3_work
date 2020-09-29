import os
import subprocess
from lsst.daf.butler import DimensionUniverse
from lsst.pipe.base import QuantumGraph

visit = 204595
detmin = 92
detmax = 95

outfile = 'ProcessCcd.pickle'

if not os.path.isfile(outfile):
    command = f'''pipetask qgraph \\
    -d "visit={visit} AND {detmin}>detector AND detector<{detmax}" \\
    -b gen3-repo/butler.yaml \\
    --output shared/test \\
    --extend-run \\
    --skip-existing \\
    --instrument lsst.obs.lsst.LsstImSim \\
    --pipeline pipelines/ProcessCcd.yaml \\
    -q {outfile}'''
    print(command)
    subprocess.check_call(command, shell=True)
else:
    universe = DimensionUniverse()
    with open(outfile, 'rb') as fd:
        qgraph = QuantumGraph.load(fd, universe)

spacer = '  '
for nodes in qgraph:
    print(f'{nodes.taskDef.taskName}: {len(nodes.quanta)} quanta:')
    for value in nodes.initOutputs.values():
        print(value.run)
    for quantum in nodes.quanta:
        print(spacer, quantum.taskName)
        print(2*spacer, "inputs:")
        for input_key, inputs in quantum.predictedInputs.items():
            print(3*spacer, input_key.name, len(inputs))
        print(2*spacer, "outputs:")
        for output_key, outputs in quantum.outputs.items():
            print(3*spacer, output_key.name, len(outputs))
