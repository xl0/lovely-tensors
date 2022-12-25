#/usr/bin/env python
# %%

from matplotlib import pyplot as plt
import torch
from lovely_tensors import monkey_patch, set_config, get_config

monkey_patch()

# %%

# |hide
numbers = torch.load("../nbs/mysteryman.pt")
in_stats = ( (0.485, 0.456, 0.406),     # mean
             (0.229, 0.224, 0.225) )    # std

mean = torch.tensor(in_stats[0])[:,None,None]
std = torch.tensor(in_stats[1])[None,:,None,None]
numbers = (numbers*std + mean).clip(0,1)

# %%

print("make figure, provide axes, plt.show()")

fig = plt.figure(figsize=(8,3))
fig.set_constrained_layout(True)
gs = fig.add_gridspec(2,2)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1,1:])

ax2.set_axis_off()
ax3.set_axis_off()

numbers.plt(ax=ax1)
numbers.rgb(ax=ax2)
numbers.chans(ax=ax3)

plt.show()


# %%

print("numers.plt(), plt.show() - nothing should happen")

numbers.plt();
plt.show()

# %%

print("fig_close=False, numers.plt(), plt.show()")
set_config(fig_close=False)
numbers.plt();
plt.show()

# %%

print("fig_show=True, numers.plt() - should still show")
set_config(fig_close=True, fig_show=True)
numbers.plt();

