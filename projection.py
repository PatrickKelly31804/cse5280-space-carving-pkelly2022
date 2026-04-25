import numpy as np

def project_point(X, R, T, K):
    X_cam = R @ X + T.reshape(3,)
    
    if X_cam[2] <= 0:
        return None

    x = K @ X_cam
    x = x / x[2]

    return int(x[0]), int(x[1])
