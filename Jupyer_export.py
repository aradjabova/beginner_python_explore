# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().system('pip install kaggle')


# %%
get_ipython().system('kaggle datasets download -d shivamb/netflix-shows')


# %%
get_ipython().system('unzip ')


# %%
import zipfile
with zipfile.ZipFile('netflix-shows.zip', 'r') as zip_ref:
    zip_ref.extractall('netflix-shows.zip')


# %%

None



# %%
