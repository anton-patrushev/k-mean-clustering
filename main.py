from data import get_filtered_dataset
from clustering import fit_cluster

import consts

from render import render_3d_scatter_from_dataset


def main():
    dataset = get_filtered_dataset(
        consts.DATASET_PATH, consts.SEARCH_QUERY, consts.COLUMNS)

    points = dataset.to_numpy()

    cluster = fit_cluster(3, points)

    render_3d_scatter_from_dataset(
        dataset, cluster.predict(points), cluster.cluster_centers_)


main()
