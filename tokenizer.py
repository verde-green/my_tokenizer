import MeCab
from pyknp import Juman

class MeCabTokenizer:
    def __init__(self, output_format="", dict_path=None):
        if output_format is None:
            # segmentation fault 回避
            raise ValueError("Argument 'output_format' is None. This value should not be None.")

        self.opt = f"{output_format} -d {dict_path}" if dict_path else output_format
        
        self.tagger = MeCab.Tagger(self.opt)
        self.tagger.parse("")

    def parse(self, sentence: str, out=None) -> list:
        if "wakati" in self.opt:
            return self.tagger.parse(sentence).rstrip().split()
        
        elif "Chasen" in self.opt:
            if out:
                # EOSはスライスして除外
                return [s.split("\t")[0] for s in self.tagger.parse(sentence).split("\n")[:-2] 
                        if s.split("\t")[3].split("-")[0] not in out]
            else:
                return [s.split("\t")[0] for s in self.tagger.parse(sentence).split("\n")[:-2]]
        
        else:
            if out:
                # EOSはスライスして除外
                return [s.split("\t")[0] for s in self.tagger.parse(sentence).split("\n")[:-2] 
                        if s.split("\t")[1].split(",")[0] not in out]
            else:
                return [s.split("\t")[0] for s in self.tagger.parse(sentence).split("\n")[:-2]]


class JumanTokenizer:
    def __init__(self):
        self.juman = Juman()

    def parse(self, sentence: str, out=[]) -> list:
        out_list = out

        # Juman では句読点等は"特殊"に分類されている
        if "記号" in out:
            out_list.append("特殊")

        return [m.midasi for m in self.juman.analysis(sentence).mrph_list() 
                if m.hinsi not in out_list]

