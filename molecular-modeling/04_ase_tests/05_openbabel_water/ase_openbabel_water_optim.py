
#
# with Google AI help
#

from openbabel import openbabel as ob
from openbabel import pybel

from ase import Atoms
from ase.visualize import view

# List available force fields
print("\nList of openbabel FFs :",pybel.forcefields,"\n")

#mol = pybel.readstring("smi", "O")
#mol.addh()
#mol.make3D()
#mol.write("xyz", "water.xyz", overwrite=True)

mol = next(pybel.readfile("xyz", "water_uglygeom.xyz"))
print(f"Molecular Formula: {mol.formula}")

thisff="mmff94"
print(" Selected FF :", thisff)

ff = pybel._forcefields[thisff]
success = ff.Setup(mol.OBMol)
if success:
    print(f"Energy before optimization: {ff.Energy()} kJ/mol")

# Redirect Open Babel internal logs to a file
#ob.obErrorLog.SetOutputStream("optimization_log.txt")
ob.obErrorLog.SetOutputLevel(5) # Adjust level as needed

mol.localopt(forcefield=thisff, steps=500)

# Stop redirection if necessary
ob.obErrorLog.StopLogging()

success = ff.Setup(mol.OBMol)
if success:
    print(f"Energy after optimization: {ff.Energy()} kJ/mol")

#mol = pybel.readstring("smi", "C1=NC2=C(N1)C(=NC=N2)N") # Adenine
#mol.draw(show=True, filename=None)

def pybel_to_ase(mol):
    # 1. Get atomic numbers
    numbers = [a.atomicnum for a in mol.atoms]
    # 2. Get 3D coordinates
    coords = [a.coords for a in mol.atoms]
    # 3. Create ASE Atoms object
    return Atoms(numbers=numbers, positions=coords)

# Convert
ase_mol = pybel_to_ase(mol)

# This opens a separate GUI window (ase-gui)
#view(ase_mol)

mol.write("xyz", "water_opt.xyz", overwrite=True)

