import matplotlib as pyplot 

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels)
    plt.savefig('pie.png')
    plt.close()