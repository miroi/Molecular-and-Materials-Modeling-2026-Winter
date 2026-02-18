==================================
Quantum Espresso benchmark example
==================================

installation
------------
Ubuntu 24.04:  sudo apt-get install quantum-espresso c2x quantum-espresso-data quantum-espresso-data-sssp

Ubuntu 22.04:  sudo apt-get install quantum-espresso  quantum-espresso-data

check installed QE
~~~~~~~~~~~~~~~~~~

summary: 
dpkg -s quantum-espresso

list files: dpkg -L  quantum-espresso  quantum-espresso-data

installed pseudos: 
ls -l /usr/share/espresso/pseudo/

find QE version
~~~~~~~~~~~~~~~
apt show quantum-espresso

dpkg -l quantum-espresso


QE visualizer
~~~~~~~~~~~~~
sudo apt install xcrysden


performance test
----------------
We have simple example of 2 molecules, adapted for QE package default pseudos


12th Gen Intel(R) Core(TM) i7-12700K
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PWSCF v.6.7MaX (Ubuntu 22.04)

Nthr   WALL time
2       31.21s
4       16.25s    
8        9.30s


