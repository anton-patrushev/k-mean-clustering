from data import get_filtered_dataset
from clustering import fit_cluster

import consts


def main():
    dataset = get_filtered_dataset(
        consts.DATASET_PATH, consts.SEARCH_QUERY, consts.COLUMNS)

    cluster = fit_cluster(3, dataset.to_numpy())


main()
