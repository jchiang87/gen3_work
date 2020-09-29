visit=204595
detmin=92
detmax=95
pipetask run \
   -d "visit=${visit} AND detector<${detmax} AND detector>${detmin}" \
   -j 1 -b gen3-repo/butler.yaml \
   -i "LSST-ImSim/raw/all,LSST-ImSim/calib,refcats,skymaps/imsim" \
   --output shared/isr_test \
   --skip-existing \
   --instrument lsst.obs.lsst.LsstImSim \
   --register-dataset-types \
   --task lsst.ip.isr.IsrTask:isr

#   --extend-run \
