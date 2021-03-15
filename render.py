import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from data import get_filtered_dataset

import consts


def get_column_from_dataset(dataset, column_name):
    return dataset[column_name].to_numpy()


def set_labels(axis):
    axis.set_xlabel('{X}'.format(X=consts.CRITERIA_1))
    axis.set_ylabel('{Y}'.format(Y=consts.CRITERIA_2))
    axis.set_zlabel('{Z}'.format(Z=consts.CRITERIA_3))


def set_limits(axis):
    axis.set_xlim([0, 50])
    axis.set_ylim([0, 90])
    axis.set_zlim([0, 100])


def render_single_3d_scatter(axis, criteria_1, criteria_2, criteria_3, colors):
    axis.scatter(criteria_1, criteria_2, criteria_3,
                 c=colors, cmap='viridis')
    set_labels(axis)
    set_limits(axis)


def render_3d_scatter(axis, dataset, colors):
    column_E = get_column_from_dataset(dataset, consts.CRITERIA_1)
    column_J = get_column_from_dataset(dataset, consts.CRITERIA_2)
    column_D = get_column_from_dataset(dataset, consts.CRITERIA_3)

    return render_single_3d_scatter(axis, column_E, column_J, column_D, colors)


# def render_centroids(axis, )


def render_3d_scatter_from_dataset(dataset, cluster_prediction):
    fig, ((cluster_axis, class_1_axis), (class_2_axis, class_3_axis)) = plt.subplots(
        2, 2, subplot_kw=dict(projection='3d'))

    class_1_dataset = get_filtered_dataset(
        consts.DATASET_PATH, consts.QUERY_CLASS_1, consts.COLUMNS)
    class_2_dataset = get_filtered_dataset(
        consts.DATASET_PATH, consts.QUERY_CLASS_2, consts.COLUMNS)
    class_3_dataset = get_filtered_dataset(
        consts.DATASET_PATH, consts.QUERY_CLASS_3, consts.COLUMNS)

    render_3d_scatter(cluster_axis, dataset, cluster_prediction)
    render_3d_scatter(class_1_axis, class_1_dataset, '#1f77b4')
    render_3d_scatter(class_2_axis, class_2_dataset, '#ff7f0e')
    render_3d_scatter(class_3_axis, class_3_dataset, '#2ca02c')

    return plt.show()
