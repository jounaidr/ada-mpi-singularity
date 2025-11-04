#!/bin/bash
#SBATCH --job-name=refl1dTest   # create a name for your job
#SBATCH --nodes=2                # node count

#SBATCH --time=00:10:00          # total run time limit (HH:MM:SS)
#SBATCH --output refl1dTest-%j.out

#SBATCH --ntasks-per-node=4

module purge
#module load MPICH
#module load mpi4py/1.3
module load contrib/dls-ap/intel/mpi/latest

mpirun -np 8 singularity exec --bind /home/vol07/scarf1137/jounaidr/ada:/test /home/vol07/scarf1137/jounaidr/ada/mpi4py-mpich-refl1d.sif python3.11 /test/align_magnetic_test.py
