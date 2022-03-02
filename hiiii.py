import glob
import matplotlib.pyplot as plt



listex, listey = [], []
for i in glob.glob("Lab5/*.csv"):
    file = open(i, 'r')
    results = list(file)
    file.close()
    x1, y1 = [], []
    results = results[3:]
    for i in results:
        result = i.replace('\n', '').split(',')
        x1.append(float(result[0]))
        y1.append(float(result[1]))
    listex.append(x1)
    listey.append(y1)
print(len(listex), len(listey))

#fig1, fig2, fig3, fig4, fig5, fig6 = plt.figure(6)
for i in range(6):
    plt.figure()
    plt.plot(listex[i], listey[i])
    plt.savefig(f"Graph{i}.pdf")
plt.show()