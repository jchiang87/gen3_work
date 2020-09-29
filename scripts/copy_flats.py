import os
import glob
import shutil

src_dir = '/home/Run2.1i/CALIB/flat/i/2022-08-06'
dest_dir = '/home/Gen3/work/gen2-repo/CALIB/flat/i_sim_1.4/2022-08-06'
src_files = glob.glob(os.path.join(src_dir, 'flat*.fits'))
for src in src_files:
    dest_basename = os.path.basename(src).replace('i-', 'i_sim_1.4-')
    dest = os.path.join(dest_dir, dest_basename)
    shutil.copy(src, dest)
