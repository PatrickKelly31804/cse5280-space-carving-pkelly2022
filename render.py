import torch
import numpy as np
from pytorch3d.io import load_objs_as_meshes
from pytorch3d.renderer import (
    FoVPerspectiveCameras, RasterizationSettings,
    MeshRenderer, MeshRasterizer, SoftSilhouetteShader
)
import matplotlib.pyplot as plt

def render_views(obj_path, num_views=20):
    device = torch.device("cpu")

    mesh = load_objs_as_meshes([obj_path], device=device)

    images = []
    masks = []
    cameras_data = []

    for i in range(num_views):
        angle = 2 * np.pi * i / num_views

        R = torch.tensor([[
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ]], dtype=torch.float32)

        T = torch.tensor([[0, 0, 3]], dtype=torch.float32)

        cameras = FoVPerspectiveCameras(R=R, T=T)

        raster_settings = RasterizationSettings(image_size=256)

        renderer = MeshRenderer(
            rasterizer=MeshRasterizer(
                cameras=cameras,
                raster_settings=raster_settings
            ),
            shader=SoftSilhouetteShader()
        )

        silhouette = renderer(mesh)[0, ..., 3].cpu().numpy()

        images.append(silhouette)
        masks.append((silhouette > 0.5).astype(int))

        cameras_data.append((R.numpy(), T.numpy()))

    return images, masks, cameras_data
