visit=204595
detmin=92
detmax=95
pipetask run \
   -d "visit=${visit} AND detector<${detmax} AND detector>${detmin}" \
   -j 1 -b gen3-repo/butler.yaml \
   --output shared/test \
   --extend-run \
   --skip-existing \
   --instrument lsst.obs.lsst.LsstImSim \
   --register-dataset-types \
   --pipeline pipelines/ProcessCcd.yaml

#   -i "LSST-ImSim/raw/all,LSST-ImSim/calib,refcats,skymaps/imsim" \
