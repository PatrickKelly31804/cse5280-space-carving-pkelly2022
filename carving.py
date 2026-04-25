import numpy as np
from projection import project_point

def space_carve(masks, cameras, grid_size=32):
    voxels = np.ones((grid_size, grid_size, grid_size))

    K = np.eye(3)

    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):

                X = np.array([x/grid_size, y/grid_size, z/grid_size])

                for mask, (R, T) in zip(masks, cameras):
                    proj = project_point(X, R[0], T[0], K)

                    if proj is None:
                        voxels[x,y,z] = 0
                        break

                    px, py = proj

                    if px < 0 or py < 0 or px >= mask.shape[1] or py >= mask.shape[0]:
                        voxels[x,y,z] = 0
                        break

                    if mask[py, px] == 0:
                        voxels[x,y,z] = 0
                        break

    return voxels
