import matplotlib.pyplot as plt
import numpy as np

import config as cfg


class Plotter(object):
    def __init__(self):
        pass

    @staticmethod
    def generate_bar_chart():
        y_pos = np.arange(len(cfg.PLOT_OBJECTS))
        performance = [cfg.PERFORMANCE_DICT[key] for key, val in
                       cfg.PERFORMANCE_DICT.iteritems()]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, cfg.PLOT_OBJECTS)
        plt.ylabel('Time [s]')
        plt.title('Interpreter performance')

        plt.savefig(cfg.IMAGES_PATH + '/performance', bbox_inches='tight')


if __name__ == '__main__':
    plotter_obj = Plotter()
    plotter_obj.generate_bar_chart()
