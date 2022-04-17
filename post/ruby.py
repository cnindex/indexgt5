def main():
	filename = 'post/0.5.md'
	dic = {
		'愚蠢': 'Baloney',
	}

	out = ""

	with open(filename, 'r', encoding='UTF-8') as F:
		text = F.readlines()
		for i in text:
			new = i
			for word in dic:
				new = new.replace("%s(%s)"%(word, dic[word]), 
					"<ruby>%s<rp>(</rp><rt>%s</rt><rp>)</rp></ruby>"%(word, dic[word]))
			out = out + new


	with open(filename, 'w', encoding='UTF-8') as F:
		print(out, file = F)

main()