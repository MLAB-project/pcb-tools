%load_ext autoreload
%autoreload 2

import gerber

pcb = gerber.PCB
pl = pcb.from_directory('/home/roman/repos/Modules/sensors/LIGHTNING01A'+'/hw/cam_profi/',
            board_name = 'LIGHTNING01A', verbose = True)
pl2 = pcb.from_directory('/home/roman/repos/Modules/sensors/RPS01A'+'/hw/cam_profi/',
            board_name = 'RPS01A', verbose = True)
pl3 = pcb.from_directory('/home/roman/repos/Modules/sensors/SHT31V01A'+'/hw/cam_profi/',
            board_name = 'SHT31V01A', verbose = True)
pn = gerber.PCB

for layer in pl2.layers:
    print(layer.layer_class)

pl2.layer_by_type('topsilk')

pl2.addLayer(layer = '/home/roman/repos/Modules/sensors/LIGHTNING01A/hw/cam_profi/LIGHTNING01A-B.Cu.gbr')

pn.layers

panel = gerber.panel()
panel.addPCB(pl)
panel.addPCB(pl2)
#panel.addPCB(pl3)

panel.join(placement = {'LIGHTNING01A': {
                                'offset': (10.16*3, 0),
                                'rotate':False
                        },
                        #'SHT31V01A': {
                        #        'offset': (10.16*3, 10.16*3),
                        #        'rotate':False
                        #},
                        'RPS01A':{'offset': (0, 0)}})
panel.write('/home/roman/repos/Modules/sensors/LIGHTNING01A/hw/aaa')

l = pl2.layers[2]
l.cam_source.statements
help(l.cam_source.primitives[0])
l.cam_source.primitives[0]
help(l.cam_source)

e = gerber.PCB()
e = gerber.PCB(['topsilk', 'bottomsilk', 'bottompaste'], 'new')

e = gerber.PCB
help(e)

p = pl2

#pl.offset(-pl.board_bounds[0][0], -pl.board_bounds[1][0])
p.set_orgin()
#p.offset(50, 50)
help(p.layers[3])
p.layers[3].__dict__
p.layers[3].cam_source.settings.__dict__

p.write(subfolder = '/home/roman/repos/Modules/sensors/LIGHTNING01A/hw/aaa')

pl.layers[3].filename
for lay in pl.layers:
    print(lay, lay.bounds)

lay.filename
lay.cam_source.primitives
lay.cam_source.statements

pl.board_bounds
pl.board_size
pl.offset(10, 23)


pl.layer_count
pl.layers
help(pl.drill_layers[0])

pl.copper_layers
print(pl.copper_layers[1].primitives)

pl.board_bounds
help(pl.copper_layers[0])

gre = pl.copper_layers[0].cam_source
gre.filename
gre.size

help(pl.top_layers)

help(pcb.drill_layers)

for x in pcb.board_bounds:
    print(x)

help(gerber)

import os
os.path.basename('/oo/ee/eue.qu')

file = gerber.read('/home/roman/repos/Modules/sensors/LIGHTNING01A/hw/cam_profi/LIGHTNING01A-B.Cu.gbr')
file = gerber.read('/home/roman/repos/Modules/sensors/LIGHTNING01A/hw/cam_profi/LIGHTNING01A.drl')

file.offset(10,10)
file.write('/home/roman/repos/Modules/sensors/LIGHTNING01A/hw/cam_profi/aaa/a.drl')

file.bounding_box
file.bounds

help(file)

help(file)
file.statements[40].y


file.bounding_box
file.bounds
file.units
file.notation
