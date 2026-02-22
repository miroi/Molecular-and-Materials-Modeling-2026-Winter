TASK 1: Calculate Total Energy  (QE and ASE)
============================================

Exercise
--------

Step 1.1
~~~~~~~~~
Run the SCF Calculation directly in QE
/path/to/qe/bin/pw.x < Si.in > Si.out
(if using a parallel version, invoke it by mpirun -np N /path/to/qe/bin/pw.x < Si.in > Si.out)

Verify if the calculation converged successfully:
grep "JOB DONE." Si.out
grep "convergence has been achieved" Si.out
To get the final total energy (in Ry):
grep ! Si.out

Step 1.2
~~~~~~~~
Run the SCF Calculation in QE by ASE. Only one modification is required in the ASE script: Replace the QE executable path with your local pw.x location.
python3 si_ase.py > si_ase.out
Inspect ASE generated QE input files and repeat all the previous steps.


Challenge
---------
...
