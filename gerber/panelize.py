import os

from .pcb import PCB

class panel(object):
    """panel basic class"""
    def __init__(self, space = 0.1, units = 'inches', name = 'panel'):
        self.boards = {}
        self.layers = set() #nazvy typu vrstev
        self.name = name
        self.units = units
        self.space = space
        self.newPCB = None

    def addPCB(self, pcb):
        self.boards[pcb.name] = pcb

    def validate(self):
        pass

    def join(self, placement):
        """
            Join boards from config JSON
        """
        for boardName in self.boards:
            board = self.boards[boardName]
            for layer in board.layers:
                self.layers.add(layer.layer_class)
        print("[PANEL]: required layers:", self.layers)

        for boardName in placement:
            offval = placement[boardName].get('offset', (0,0))
            board = self.boards[boardName]
            board.set_orgin()                                                   # move module to (0,0)
            board.offset(offval[0], offval[1])                                  # make offset for panel placement

            if not self.newPCB:
                self.newPCB = board
            else:
                for layName in self.layers:
                    layer = board.layer_by_type(layName)
                    if layer and self.newPCB.layer_by_type(layName):
                        try:
                            self.newPCB.layer_by_type(layName).cam_source.statements += layer.cam_source.statements
                            #self.newPCB.layer_by_type(layName).primitives += layer.primitives
                        except Exception as e:
                            print(e)
                        print(len(self.newPCB.layer_by_type(layName).cam_source.statements))
                    else:
                        print("Skip", layName)
        try:
            board.reannotate()
        except Exception as e:
            pass

    def write(self, subfolder):
        self.newPCB.write(subfolder = subfolder)
