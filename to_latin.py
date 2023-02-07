import cyrtranslit

with open("test_eng.txt", "w", encoding='utf-8') as out:
	with open("test.txt", "r", encoding='utf-8') as f:
		for i in f.readlines():
			out.write(cyrtranslit.to_latin(i, lang_code="ru"))