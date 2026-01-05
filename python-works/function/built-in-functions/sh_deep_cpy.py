"""here we have shallow copy and deepcopy
shallow copy only copies the outer list(with loctaion for inner list) 
while deep copy copies the inner list(contains all list and values) as well"""
from copy import copy
from copy import deepcopy

vrindha_color=["black","blue","green"]
shiva_color=copy(vrindha_color)
shiva_color.append("purple")
print("vrindha",vrindha_color)
print("shiva",shiva_color)


arun_food=[["dose","tea"],
           ["meals","lime juice"],
           ["chapathy","lime tea"]]

resin_food=deepcopy(arun_food)
resin_food[0][0]="idly"
print("arun",arun_food)
print("resin",resin_food)
