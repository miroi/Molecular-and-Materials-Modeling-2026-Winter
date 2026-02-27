==================================
Quantum Espresso benchmark example
==================================

installation
------------

Ubuntu 24.04
~~~~~~~~~~~~

broken native package 24.04, see https://gitlab.com/QEF/q-e/-/issues/684 !

download deb-package from  https://github.com/pranabdas/espresso/releases

sudo apt install ./quantum-espresso_7.5-1_amd64.deb

export PATH=/opt/espresso/7.5:$PATH

check: ldd /opt/espresso/7.5/pw.x

which pw.x
/opt/espresso/7.5/pw.x

also provide: 
sudo apt-get install c2x quantum-espresso-data quantum-espresso-data-sssp

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

displays input, output files

performance test
----------------
We have simple example of 2 molecules, adapted for QE package default pseudos

12th Gen Intel(R) Core(TM) i7-12700K
PWSCF v.6.7MaX (Ubuntu 22.04)

Nproc   WALL time
2       31.21s
4       16.25s    
8        9.30s


12th Gen Intel(R) Core(TM) i5-12450H
PWSCF v.7.5 (Ubuntu 24.04)

export OMP_NUM_THREADS=1

Nproc   Wall 
1      1m 9.57s
2      35.68s
6      18.18s

challenge
~~~~~~~~~
increase the cutoffs and run performance tests 

