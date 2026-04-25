import numpy as np

def render_views(obj_path, num_views=20):
    images = []
    masks = []
    cameras_data = []

    for i in range(num_views):
        angle = 2 * np.pi * i / num_views

        R = np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])

        T = np.array([0, 0, 3])

        # fake silhouette (circle)
        img_size = 256
        mask = np.zeros((img_size, img_size))

        cx, cy = img_size // 2, img_size // 2
        radius = 55

        for x in range(img_size):
            for y in range(img_size):
                if (x - cx)**2 + (y - cy)**2 < radius**2:
                    mask[y, x] = 1

        images.append(mask)
        masks.append(mask)
        cameras_data.append((R, T))

    return images, masks, cameras_data
