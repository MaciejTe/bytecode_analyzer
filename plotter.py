import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

import config as cfg

# import pygal


class Plotter(object):
    def __init__(self):
        pass

    @staticmethod
    def generate_bar_chart():
        plt.bar(range(len(cfg.PERFORMANCE_DICT)),
                cfg.PERFORMANCE_DICT.values(),
                align='center')
        plt.xticks(range(len(cfg.PERFORMANCE_DICT)),
                   cfg.PERFORMANCE_DICT.keys())

        plt.ylabel('Time [s]')
        plt.title('Interpreter performance')

        plt.savefig(cfg.IMAGES_PATH + '/performance', bbox_inches='tight')

    # def generate_bar_chart(self):
    #     line_chart = pygal.HorizontalBar()
    #     line_chart.title = 'Interpreter performance [s]'
    #
    #     performance = [cfg.PERFORMANCE_DICT[key] for key, val in
    #                    cfg.PERFORMANCE_DICT.iteritems()]
    #     print performance, len(performance), '*****'
    #
    #     for interpreter, perf in cfg.PERFORMANCE_DICT.iteritems():
    #         line_chart.add(interpreter, float(perf))
    #
    #     # line_chart.render()
    #     line_chart.render_to_png(filename=cfg.IMAGES_PATH + '/performance.png')


if __name__ == '__main__':
    plotter_obj = Plotter()
    # plotter_obj.generate_bar_chart()
    plotter_obj.gal_chart()
