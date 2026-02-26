=======================================================
TASK 4: Electronic properties: Si (Charge and DOS, ASE)
=======================================================

In this task, we'll calculate a few key electronic properties :

 (1) 3D charge density (using post-processing tool pp.x)
 (2) Löwdin partial charges (using projwfc.x)
 (3) total DOS (using dos.x)
 (4) projected DOS (using projwfc.x) — through a streamlined ASE workflow combining SCF and NSCF calculations.

The SCF calculation generates the charge density and Löwdin charges, while a subsequent NSCF calculation (with calculation='nscf' in the CONTROL namelist and matching outdir/prefix to read the SCF charge density) produces the DOS data using a denser k-grid.

Each post-processing tool requires its specific input format (detailed in accompanying notes), but ASE automates the execution sequence.

First, copy your relaxed atomic structure into the provided ASE script (electronic_a_si.py) and update the Quantum ESPRESSO executable path to your local pw.x location.

Challenge
---------
Modify the Electronic Properties: Si script and test the effects of different values of Gaussian broadening (degauss)

