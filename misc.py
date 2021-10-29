import scipy

def svd(theta, compute_uv=True, full_matrices=True):
    """SVD with gesvd backup"""
    try:
        return scipy.linalg.svd(theta,
                                compute_uv=compute_uv,
                                full_matrices=full_matrices)
    except:
        print("*gesvd*")
        return scipy.linalg.svd(theta,
                                compute_uv=compute_uv,
                                full_matrices=full_matrices,
                                lapack_driver='gesvd')

