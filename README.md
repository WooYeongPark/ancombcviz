## ANCOMBCviz
ANCOMBCviz is a Python package for analyzing differential abundance of group by microbiome composition and visualizing the resulting ANCOM-BC as a plot.

## Method
In ANCOM-BC, program of analysis to diffrential abundance. This tool use compositional  microbiome relative abundance data analysis. and This method also use ANCOM-BC, LefSe2, ALDEx2 usually.
In ANCOMBCviz, this ANCOM-BC results file make image file. plot type is `barplot`, `heatmap`.
This package also need `numpy >= 2.0`, `pandas`, `matplotlib >= 0.7.1`, `seaborn`, `skbio.stats.composition.ancom`.



## Installation
### Installation using conda
```
conda env create -f environment.yml
```
If finished installation of conda env. activate conda and installation by pip.
```
cd ancombc_viz ## Before do this code, you clonning this repository by your directory.
```
```
pip install -e .
```


### From PyPI
```
pip install ancombcviz
```

### From source
1. `git clone git@github.com:WooYeongPark/ancombcviz.git` 
2. `cd ancombc_viz`
3. `pip install -e .`

## Usage
### Python API
```
from ancombc_viz.simple_name import extract_p_g_or_f
from ancombc_viz.plotting import plot_group_bar
```

## License
This project is licensed under the MIT License. see the LICESNSE file for details.