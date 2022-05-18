# Show Landslide erosion and deposition draped over the shaded topographic relief
import copy
# Libraries for scientific computing (ndarrays) and plotting
import numpy as np
import matplotlib as mpl; import matplotlib.pyplot as plt

# Landlab libraries
from landlab import RasterModelGrid, imshowhs_grid, imshow_grid # Component to manage the grid and methods for display

def my_landslide_plot(grid):
    cmap1 = copy.copy(mpl.cm.get_cmap("Blues"))
    thres_drape1=0.01
    thres_drape2=0.01
    alpha  = .8
    alpha2 = .8
    drape1 = np.sqrt(grid.at_node["landslide__erosion"])
    drape2 = np.sqrt(grid.at_node["landslide__deposition"])
    cmap1 = copy.copy(mpl.cm.get_cmap("hot_r"))
    cmap2 = copy.copy(mpl.cm.get_cmap("winter_r"))
    plt.figure(figsize=(10,10))
    imshowhs_grid(grid, "topographic__elevation",
                  plot_type='Drape2',         
                  drape1 = drape1,
                  cmap=cmap1,
                  thres_drape1=thres_drape1,
                  alpha=alpha,
                  drape2 = drape2,
                  cmap2=cmap2,
                  thres_drape2=thres_drape2,
                  alpha2=alpha2,
                  add_double_colorbar=True, 
                  cbar_tick_size =8,
                  cbar_label_color='red',
                  cbar_label_fontweight = 'normal',
                  add_label_bbox = True, )
    plt.show()