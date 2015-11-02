import numpy as np
from scipy.spatial import cKDTree

# ------------------ SphericalNearestNeighbour ---------------------------


class SphericalNearestNeighbour():
    """
    Spherical nearest neighbour queries using scipy's fast kd-tree
    implementation.
    """
    def __init__(self, lat, lon, el_dp, eradius=6371009):
        cart_data = self.spherical2cartesian(lat, lon, el_dp, eradius)
        self.kd_tree = cKDTree(data=cart_data, leafsize=10)
        self.eradius = eradius

    def query(self, lat, lon, el_dp, k=1):
        points = self.spherical2cartesian(lat, lon, el_dp, self.eradius)
        d, i = self.kd_tree.query(points, k=k)
        return d, i

    def query_pairs(self, maximum_distance):
        return self.kd_tree.query_pairs(maximum_distance)

    def spherical2cartesian(self, lat, lon, el_dp, eradius):
        """
        Converts a list of :class:`~obspy.fdsn.download_status.Station`
        objects to an array of shape(len(list), 3) containing x/y/z in meters.
        """
        shape = len(lat)
        r = eradius + el_dp
        # Convert data from lat/lng to x/y/z.
        colat = 90.0 - lat
        cart_data = np.empty((shape, 3), dtype=np.float64)
        cart_data[:, 0] = r * np.sin(np.deg2rad(colat)) * \
        np.cos(np.deg2rad(lon))
        cart_data[:, 1] = r * np.sin(np.deg2rad(colat)) * \
        np.sin(np.deg2rad(lon))
        cart_data[:, 2] = r * np.cos(np.deg2rad(colat))
        return cart_data
