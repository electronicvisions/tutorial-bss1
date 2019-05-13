#!/bin/bash

# drop all env
export -n PYTHONPATH
export -n PYTHONHOME
export -n MANPATH
export -n LIBRARY_PATH
export -n LD_LIBRARY_PATH
export -n TCLLIBPATH
export -n CPATH
export -n C_INCLUDE_PATH
export -n CPLUS_INCLUDE_PATH
export -n PKG_CONFIG_PATH
export -n CMAKE_PREFIX_PATH
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

#env

# module load slurm-singularity
export PATH=/wang/environment/cluster/slurm-skretch/bin:$PATH

# module load nmpm_software/current
#BASEDIR_NMPM_SOFTWARE=/wang/environment/software/container/meta-nmpm-software/current
BASEDIR_NMPM_SOFTWARE=/fasthome/sschmitt/projects/nmpm_software_oberthaler
#CONTAINER_IMAGE_NMPM_SOFTWARE=/containers/stable/2019-02-27_1.img
#CONTAINER_APP_NMPM_SOFTWARE=visionary-wafer

# load env
. /scif/apps/visionary-wafer/scif/env/90-environment.sh

export PATH=$BASEDIR_NMPM_SOFTWARE/bin:$PATH
export SINGULARITYENV_PREPEND_PATH=$BASEDIR_NMPM_SOFTWARE/bin:$PATH
export SINGULARITYENV_LD_LIBRARY_PATH=$BASEDIR_NMPM_SOFTWARE/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$BASEDIR_NMPM_SOFTWARE/lib

#env

# exec it
echo `which python`
exec python2 -m ipykernel $@
