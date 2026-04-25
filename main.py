from render import render_views
from carving import space_carve
from mesh import voxels_to_mesh

def main():
    obj_path = "model.obj"  # put your OBJ file here

    images, masks, cameras = render_views(obj_path)

    voxels = space_carve(masks, cameras)

    voxels_to_mesh(voxels)

if __name__ == "__main__":
    main()
