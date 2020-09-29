visit=204595
detmin=92
detmax=95
pipetask qgraph \
   -d "visit=${visit} AND detector<${detmax} AND detector>${detmin}" \
   -i "LSST-ImSim/raw/all,LSST-ImSim/calib,refcats,skymaps/imsim" \
   -b gen3-repo/butler.yaml \
   --skip-existing \
   --instrument lsst.obs.lsst.LsstImSim \
   --pipeline pipelines/ProcessCcd.yaml \
   --save-qgraph ProcessCcd.pickle

#
#   --output shared/test \
#   --extend-run \
