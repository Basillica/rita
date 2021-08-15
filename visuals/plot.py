from html.parser import HTMLParser
from io import StringIO
import mpld3
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('WebAgg')

tr_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tr_data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def plot():
    fig1 = plt.figure()
    plt.xlabel('RelativeTime (ms)')
    plt.ylabel('AbsoluteTime (ms)')
    plt.title('R-A Combinations')
    plt.plot(tr_data[:], tr_data2[:], 'bx')
    # plt.plot(tr_data[outliers,0],tr_data[outliers,1],'ro')
    value = mpld3.fig_to_html(fig1, d3_url=None, mpld3_url=None, no_extras=False,
                              template_type='general', figid=None, use_http=False)

    html = '<HTML><HEAD><TITLE>Python Matplotlib Graph</TITLE></HEAD>' + '\n' + \
        '<BODY>' + '\n' + \
        '<CENTER>' + '\n' + \
        '<br><br>' + '\n' + \
        '<H3>Graph</H3>' + '\n' + \
        value + '\n' + \
        '<br>' + '\n' + \
        '</CENTER>' + '\n' + \
        '</BODY>' + '\n' + \
        '</html>' + '\n'
    return html
