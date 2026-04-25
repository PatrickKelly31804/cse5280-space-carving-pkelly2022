import open3d as o3d
import numpy as np

def voxels_to_mesh(voxels):
    points = np.argwhere(voxels == 1)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    pcd.estimate_normals()

    mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd)

    o3d.visualization.draw_geometries([mesh])
