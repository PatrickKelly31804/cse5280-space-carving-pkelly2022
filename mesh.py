import open3d as o3d
import numpy as np

def voxels_to_mesh(voxels):
    points = np.argwhere(voxels == 1)

    print("points in visual hull:", len(points))

    if len(points) == 0:
        print("No points to display.")
        return

    points = points.astype(float)
    points = points - points.mean(axis=0)
    points = points / points.max()

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    o3d.visualization.draw_geometries([pcd])
