# cse5280-space-carving-pkelly2022
3-D object modeling: space carving
# CSE5280 Space Carving

This project implements a basic visual hull reconstruction pipeline using space carving.

The program creates multiple silhouette views, projects 3D voxel points into each view using a pinhole camera model, removes voxels that fall outside the silhouettes, and converts the remaining voxels into a point cloud/mesh using Open3D.

## Main steps

1. Generate multiple camera views and silhouettes
2. Project 3D voxel points into 2D image coordinates
3. Carve away inconsistent voxels
4. Visualize the remaining visual hull
5. Reconstruct a mesh with Open3D

## How to run

Install dependencies:

pip3 install numpy open3d matplotlib

Run:

python3 main.py

## Files

main.py - runs the full pipeline  
render.py - creates views, silhouettes, and camera parameters  
projection.py - implements pinhole projection  
carving.py - performs space carving  
mesh.py - converts voxels to an Open3D mesh  
utils.py - helper file
