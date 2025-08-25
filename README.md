# Generation of sample data

## 1. build the apptainer container

Many HPC administrators want apptainer containers to be built on their host so that they can audit the recipes.
```shell
$ apptainer build mef90rockylinux9mpich.sif mef90rockylinux9mpich.def
```

The provided recipe uses mpich, so it will work on any cluster with intel mpich or any flavour of mvapich installed.
If the host cluster uses openmpi, the recipe will need modifications.

## 2. Generate meshes
```shell
$ apptainer run <apptainer container> python3 src/heteroCirc.py -n <n> --prefix <prefix>
```
This will generate `n` meshes `meshes/<prefix>-<num>.msh`. Each mesh corresponds to a given microstructure rotated by an angle $2\pi/n$. The density and average radius of the inclusion can be controlled respectively with `--d` and `--R`.

## 3. Run computations
For each generated mesh:
```shell
$ srun -n <num cores> apptainer run <apptainer container> vDef -geometry meshes/<prefix>.msh -result result/<prefix>.exo -options_file packedInclusions.yaml
```
A good guideline is to pick num_cores of the order of number of vertices / 5000. The number of vertices in the mesh is printed during mesh generation

## 4. Generate pictures and movies
For *each* computation: 
```shell
$ apptainer run <apptainer container> visit -cli -nowin -s src/plotFrames.py --BB -2.5  2.5  -2.5 2.5  results/<prefix>.exo 
```
This will generate `<prefix>.mp4` and `<prefix>.png` as well as snapshots of the fracture evolution in the folder `<prefix>-Frames`
The value 2.5 corresponds to the parameter

## 5. Compute and plot the $J$-integral
For *each* computation
```shell
$ apptainer run <apptainer container> visit -cli -nowin -s src/Jint.py --bb -3 -3 3 3 -i results/<prefix>.exo
```
This step can take a while and is not parallelized and will generate the file `results/<prefix>_Jint.txt`
```shell
$ apptainer run <apptainer container> python3 plotJint.py -o results/<prefix>_Jint.pdf results/<prefix>_Jint.txt
```
This will generate the file will generate the file `results/<prefix>_Jint.pdf`