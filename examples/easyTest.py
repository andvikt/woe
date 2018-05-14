#%%
%load_ext autoreload
%autoreload 1
#%aimport woe2.ease
from woe import ease as e


#%%

fd = vs.process('UCI_Credit_Card')

#%%
stats = (fd.groupby('var_name').agg({'iv': max})
            .sort_values(['iv'], ascending=False)
        )
stats