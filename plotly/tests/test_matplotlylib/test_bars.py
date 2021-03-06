import matplotlib.pyplot as plt

from . nose_tools import compare_dict, run_fig
from . data.bars import *


def test_vertical_bar():
    fig, ax = plt.subplots()
    ax.bar(left=D['left'], height=D['height'])
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict,
                                       VERTICAL_BAR['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   VERTICAL_BAR['layout'])
    assert equivalent, msg


def test_horizontal_bar():
    fig, ax = plt.subplots()
    ax.barh(bottom=D['bottom'], width=D['width'])
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict,
                                       HORIZONTAL_BAR['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   HORIZONTAL_BAR['layout'])
    assert equivalent, msg


def test_h_and_v_bars():
    fig, ax = plt.subplots()
    ax.bar(left=D['multi_left'], height=D['multi_height'],
           width=10, color='green', alpha=.5)
    ax.barh(bottom=D['multi_bottom'], width=D['multi_width'],
            height=10, color='red', alpha=.5)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict,
                                       H_AND_V_BARS['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   H_AND_V_BARS['layout'])
    assert equivalent, msg