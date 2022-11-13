#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pm4py
import graphviz

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery

# viz
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.process_tree import visualizer as pt_visualizer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.dfg import visualizer as dfg_visualization


# In[2]:


permitLog = pm4py.read_xes('data/original/PermitLog.xes_')
internationalDeclarations = pm4py.read_xes('data/original/InternationalDeclarations.xes_')
domesticDeclarations = pm4py.read_xes('data/original/DomesticDeclarations.xes_')
prepaidTravelCost = pm4py.read_xes('data/original/PrepaidTravelCost.xes_')
requestForPayment = pm4py.read_xes('data/original/RequestForPayment.xes_')


# In[13]:


heuristic_net = pm4py.discover_heuristics_net(permitLog, dependency_threshold=0.99)
pm4py.view_heuristics_net(heuristic_net)


# In[14]:


heuristic_net = pm4py.discover_heuristics_net(prepaidTravelCost, dependency_threshold=0.99)
pm4py.view_heuristics_net(heuristic_net)


# In[15]:


heuristic_net = pm4py.discover_heuristics_net(domesticDeclarations, dependency_threshold=0.99)
pm4py.view_heuristics_net(heuristic_net)


# In[16]:


heuristic_net = pm4py.discover_heuristics_net(internationalDeclarations, dependency_threshold=0.99)
pm4py.view_heuristics_net(heuristic_net)


# In[17]:


log = requestForPayment
log[0][0]


# In[18]:


heuristic_net = pm4py.discover_heuristics_net(requestForPayment, dependency_threshold=0.99)
pm4py.view_heuristics_net(heuristic_net)


# In[19]:


net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(requestForPayment)
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)


# In[20]:


process_tree = pm4py.discover_process_tree_inductive(requestForPayment)
bpmn_model = pm4py.convert_to_bpmn(process_tree)
pm4py.view_bpmn(bpmn_model)


# In[21]:


pm4py.view_process_tree(process_tree)


# In[22]:


# len(domesticDeclarationsDF)


# In[12]:


#len(internationalDeclarationsDF)


# In[ ]:


#len(requestForPaymentDF)


# In[ ]:




