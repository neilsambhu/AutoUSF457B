# AutoUSF457B
Automatically transfer University of South Florida 457B assets from Nationwide to Charles Schwab

1. Create environment.yml file via conda
with your conda environment activated, run the following command to generate dependency yaml file:
	conda env export > environment_droplet.yml
2. Commit the yml file, git clone the repo onto the target OS, and create a conda environment from it as follows:
	conda env create -f environment.yml