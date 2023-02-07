import cyrtranslit
from textgenrnn import textgenrnn

def to_cirilic(s: str) -> str:
	return cyrtranslit.to_cyrillic(s, "ru")

textgen = textgenrnn("textgenrnn_weights.hdf5")
#textgen.train_from_file("test_eng.txt", num_epochs=10)

result = textgen.generate(10, True, temperature=0.45)
for i in result:
 	print(to_cirilic(i))