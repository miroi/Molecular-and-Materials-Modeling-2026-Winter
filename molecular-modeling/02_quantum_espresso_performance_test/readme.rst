==================================
Quantum Espresso benchmark example
==================================

installation
------------
Ubuntu 24.04:  sudo apt-get install quantum-espresso c2x quantum-espresso-data quantum-espresso-data-sssp

broken native package 24.04 !!!, see https://gitlab.com/QEF/q-e/-/issues/684 !

Ubuntu 22.04:  sudo apt-get install quantum-espresso  quantum-espresso-data

external QE debian package 
~~~~~~~~~~~~~~~~~~~~~~~~~~
download deb-package:  https://github.com/pranabdas/espresso/releases

sudo apt install ./quantum-espresso_7.5-1_amd64.deb

export PATH=/opt/espresso/7.5:$PATH

check ldd /opt/espresso/7.5/pw.x

which pw.x
/opt/espresso/7.5/pw.x

provide pseudos: sudo apt-get install quantum-espresso-data

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
PWSCF v.6.7MaX (Ubuntu 22.04)

Nthr   WALL time
2       31.21s
4       16.25s    
8        9.30s


12th Gen Intel(R) Core(TM) i5-12450H
PWSCF v.7.5 (Ubuntu 24.04)
Nthr   Wall 
2      39.55s
6      3m34.84s      
