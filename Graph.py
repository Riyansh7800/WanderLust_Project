import pymnet
import matplotlib.pyplot as plt
import pandas as pd

node = pd.read_csv('D:/Project/Monuments_node.csv')
redge = pd.read_csv('D:/Project/RBMN_edges.csv')
medge = pd.read_csv('C:/Users/ayush/Desktop/new/MBMN_edges.csv')

# Create a multilayer network
net = pymnet.MultiplexNetwork(couplings='categorical',directed=False)

# Add nodes and layers
net.add_layer('RBMN',1)
net.add_layer('MBMN',1)

for _,data in node.iterrows():
    net.add_node(data['id'],1)
    net.add_node(data['id'],2)

for _, data in redge.iterrows():
    net[data['Source'],data['Target'],'RBMN','RBMN']=data['Weight']

for _, data in medge.iterrows():
    net[data['source'],data['target'],'MBMN','MBMN']=data['weight']


# Create the visualization
fig = plt.figure(figsize=(100, 60))
pymnet.visuals.draw(net, layout='circular', show=False, layergap=2, layerPadding=0.01, figsize=(20,20), autoscale=True)
plt.title("Multilayer Visualization")
plt.savefig('C:/Users/ayush/Desktop/b.png')

