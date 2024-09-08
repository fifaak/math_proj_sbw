import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

def radar_chart(values, labels, title, font_properties):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='#76D7C4', alpha=0.25)
    ax.plot(angles, values, color='#76D7C4', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontproperties=font_properties)
    ax.set_title(title, fontproperties=font_properties)
    ax.yaxis.set_tick_params(labelsize=10)

    return fig

def plot_grade_comparison(grades, questions, labels, font_properties):
    fig, ax = plt.subplots()
    ax.barh(labels, grades, color='#5DADE2', label='Grade (40%)', align='center')
    ax.barh(labels, questions, left=grades, color='#F1948A', label='Question (60%)', align='center')
    ax.set_xlabel('คะแนนรวม (เต็ม 100)', fontproperties=font_properties)
    ax.set_title('เปรียบเทียบคะแนนจากเกรดและคำถาม', fontproperties=font_properties)
    ax.legend(prop=font_properties)

    for label in ax.get_xticklabels():
        label.set_fontproperties(font_properties)
    for label in ax.get_yticklabels():
        label.set_fontproperties(font_properties)

    return fig
