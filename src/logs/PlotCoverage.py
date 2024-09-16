from pandas import read_csv
from pathlib import Path
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
import os

coverage_path = (Path(__file__).parent / "../../Log/Coverage").resolve()

def makePlot(years: np.ndarray, labels: np.ndarray, table_data: np.ndarray, brand: str) -> None:
    data = np.pad(table_data, ((0,0),(1,1)))
    diff_arr = np.diff(data)

    plus_idxs = np.where(diff_arr==1)
    minus_idxs = np.where(diff_arr==-1)
    plus = list(zip(plus_idxs[0],plus_idxs[1]))
    minus = list(zip(minus_idxs[0],minus_idxs[1]))
    assert(len(plus) == len(minus))

    data = []
    for _, (start, stop) in enumerate(zip(plus, minus)):
        assert(start[0] == stop[0])
        data.append((int(years[start[1]]), int(years[stop[1]-1]), labels[start[0]]))

    verts = []
    colors = []
    for d in data:
        start = d[0]
        stop = d[1]
        label = d[2]
        v = [(start, np.where(labels == label)[0][0]-.4),
             (start, np.where(labels == label)[0][0]+.4),
             (stop+1,  np.where(labels == label)[0][0]+.4),
             (stop+1,  np.where(labels == label)[0][0]-.4),
             (start, np.where(labels == label)[0][0]-.4)]
        verts.append(v)
        colors.append(f"C{np.where(labels==label)[0][0]}")

    bars = PolyCollection(verts, facecolors=colors)

    fig, ax = plt.subplots()
    plt.title(f"{brand}")
    plt.ylabel("Models")
    plt.xlabel("Years")
    
    ax.add_collection(bars)
    ax.autoscale()

    ax.set_yticks(np.arange(labels.shape[0]), labels)
    ax.set_xticks(list(range(int(years[0]),int(years[-1])+1)))
    ax.set_xticklabels(years, rotation=-45)

    plt.tight_layout()
    os.makedirs(coverage_path / "plots", exist_ok=True)
    plt.savefig(coverage_path / f"plots/{brand}.png")
    # plt.show()

####################################################################################################

brands = list(map(lambda x: x[:-4], filter(lambda x: ".csv" in x, os.listdir(coverage_path))))
for b in brands:
    table = read_csv(coverage_path / f"{b}.csv").fillna("")
    years = table.columns.values[1:]
    labels = table.to_numpy()[:,0]
    data = 1 * (table.to_numpy()[:,1:] == 'x')
    makePlot(years, labels, data, b)