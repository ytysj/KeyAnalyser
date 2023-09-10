from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts import options as opts
import logging
import database


def render_key_num(data_list):
    key_num_dict = {}
    for item in data_list:
        key = item[2]
        if key in key_num_dict:
            key_num_dict[key] += 1
        else:
            key_num_dict[key] = 1
    
    return key_num_dict

def render_bar(data_dict):
    # 提取键和值，并排序
    keys = sorted(list(data_dict.keys()), key=lambda x: data_dict[x], reverse=False)
    values = [data_dict[k] for k in keys]

    bar = (
        Bar()
        .add_xaxis(keys)
        .add_yaxis('Number', values, category_gap = "50%")
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar Chart"),
            xaxis_opts=opts.AxisOpts(name="Keys"),
            yaxis_opts=opts.AxisOpts(name="Counts"),
        )
    )
    bar.width = '80%'
    bar.render("analysis.html")

def render_pie(data_dict):
    data_list = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    pie_chart = Pie()
    pie_chart.add("", data_list)
    pie_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="Pie Chart", pos_top='200%', pos_left='center')
    )
    pie_chart.width = '90%'
    pie_chart.height = '650px'
    pie_chart.render("analysis.html")

if __name__ == "__main__":
    print("ananlysis module test start")
    database.init_db()
    data_list = database.query_all_item()
    key_num_dict = render_key_num(data_list)
    print(key_num_dict)

    render_pie(key_num_dict)
    render_bar(key_num_dict)