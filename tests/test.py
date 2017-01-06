# coding=utf-8
import utf8proc as m

assert m.__version__ == '0.0.1'
assert m.normalize("Test") == "test"
assert m.normalize("Écoute") == "ecoute"
assert m.naturalSmallerThan("a", "b")
assert m.naturalSmallerThan("é", "f")

print m.naturalSorted(["c", "b", "f", "a", "é"]) 
assert m.naturalSorted(["c", "b", "f", "a", "é"]) == [u"a", u"b", u"c", u"é", u"f"]
assert m.sort(["c", "b", "f", "a", "é"]) == [3, 1, 0, 4, 2]