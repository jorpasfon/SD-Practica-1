# SD-Practica-1
Pràctica 1 SD - Map-reduce

## Prerequisites
Have pyactor installed (_pip install pyactor_)

## Local execution
1. Define a mapper and reducer function in both **Server** and **Host** files (You have _mapper2_, _mapper3_, _merge_ and _reduce_count_ as examples)
2. In the **Server** file, replace _mapper2_ and _merge_ for your mapper and reducer functions
3. Edit _path_fitxer_ variable with the path to the file you want to map-reduce
4. In the **Reducer** class, you can set the output result file in the _set_dict_ function changing the "nouDiccF4.txt" string

## Distributed execution
In addition to local execution steps:
1. In the **Registry** file, replace the _create_host_ IP with your machine's one (Ex. **192.168.1.1**)
2. In the **Server** file, replace the _create_host_ IP with your machine's one (Ex. **192.168.1.2**) and the _lookup_url_ with the **Registry**'s one (In this example **192.168.1.1**)
3. In each **Host** file, replace the _create_host_ IP with your machine's one (Ex. **192.168.1.3**) and the _lookup_url_ with the **Registry**'s one (In this example **192.168.1.1**)

If you have multiple hosts in the same machine, make sure the port they are using is not the same. For example **192.168.1.3:1278**, and **192.168.1.3:1280**

Also, make sure you have the same path to the file you want to map-reduce in the Host machines
