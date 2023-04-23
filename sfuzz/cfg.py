import inspect

from pycfg.pycfg import PyCFG, CFGNode


class CFG:

    def __init__(self, fn):
        self.fn = fn
        self.__pycfg = PyCFG()
        self.graph = None
        self.gen_graph()

    def gen_graph(self):
        self.__pycfg.gen_cfg(inspect.getsource(self.fn))
        self.graph = CFGNode.to_graph(arcs=[])

    def get_graph(self) -> PyCFG:
        return self.__pycfg

    def draw_graph(self):
        self.graph.draw("graph.png", prog="dot")

    def get_annotations(self):
        signature = inspect.signature(self.fn)
        annotations = []
        for param in signature.parameters.values():
            annotations.append((param.name, param.annotation))
        return annotations, signature.return_annotation
