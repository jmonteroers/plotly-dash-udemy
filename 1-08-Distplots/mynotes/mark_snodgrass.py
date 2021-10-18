import plotly.offline as pyo
import plotly.figure_factory as ff

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]
data = [snodgrass, twain]
group_labels = ["Snodgrass' Writings", "Mark Twain's Writings"]
fig = ff.create_distplot(data, group_labels, bin_size=2*[0.05])
pyo.plot(fig, filename="mark_snodgrass.html")
