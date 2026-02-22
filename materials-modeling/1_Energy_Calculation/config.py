#
#  Adjust these variables for your QE run
#

# full path to your QE binaries (pw.x, pp.x etc)
qe_path="/opt/espresso/7.5"

# for OpenMP parallelization, OMP_NUM_THREADS envirovariable
omp_threads="2"

# command for parallel run
mpi_command="mpirun -np 2"
