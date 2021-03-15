import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import consts


def get_column_from_dataset(dataset, column_name):
    return dataset[column_name].to_numpy()


def set_labels(axis):
    axis.set_xlabel('Criteria 1 Label - {X}'.format(X=consts.CRITERIA_1))
    axis.set_ylabel('Criteria 2 Label - {Y}'.format(Y=consts.CRITERIA_2))
    axis.set_zlabel('Criteria 3 Label - {Z}'.format(Z=consts.CRITERIA_3))


def render_3d_scatter(criteria_1, criteria_2, criteria_3, cluster_prediction):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
        2, 2, subplot_kw=dict(projection='3d'))

    ax1.scatter(criteria_1, criteria_2, criteria_3,
                c=cluster_prediction, cmap='viridis')
    set_labels(ax1)

    # ax2.scatter(criteria_1, criteria_2, criteria_3,
    #             c=cluster_prediction, cmap='viridis')
    # set_labels(ax2)

    # ax3.scatter(criteria_1, criteria_2, criteria_3,
    #             c=cluster_prediction, cmap='viridis')
    # set_labels(ax3)

    # ax4.scatter(criteria_1, criteria_2, criteria_3,
    #             c=cluster_prediction, cmap='viridis')
    # set_labels(ax4)

    plt.show()


def render_3d_scatter_from_dataset(dataset, cluster_prediction):
    column_E = get_column_from_dataset(dataset, consts.CRITERIA_1)
    column_J = get_column_from_dataset(dataset, consts.CRITERIA_2)
    column_D = get_column_from_dataset(dataset, consts.CRITERIA_3)

    return render_3d_scatter(column_E, column_J, column_D,  cluster_prediction)
