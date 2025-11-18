#!/bin/bash
#SBATCH --job-name=refl1dTest    # job name
#SBATCH --nodes=4                # node count

#SBATCH --time=00:10:00          # total run time limit (HH:MM:SS)
#SBATCH --output refl1dTest-%j.out

#SBATCH --ntasks-per-node=4

module purge

singularity exec --bind /home/vol07/scarf1137/jounaidr/ada:/test /home/vol07/scarf1137/jounaidr/ada/mpi4py-mpich-refl1d.sif refl1d /test/Ni58_basic_model.py --fit=dream --export=test --burn=1000 --samples=10000 --init=lhs --mpi --session=/test/test.h5 --batch
