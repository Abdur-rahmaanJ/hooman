

def check_scatter_chart(option, value):
    if option == 'hist_color':
        if value not in ['r', 'g', 'b']:
            raise Exception('"hist_color" takes only values r or g or b')


def check(function, option, value):
    if function == 'scatterchart':
        check_scatter_chart(option, value)