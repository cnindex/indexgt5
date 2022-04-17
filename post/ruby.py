def main(name = ''):
	filename = name
	dic = {
		'愚蠢': 'Baloney',
		'所罗门的小钥匙': 'Lemegeton',
		'超量猎手': 'Overhunting',
		'警备员': 'Anti-Skill',
		'假想敌': 'Aggressor',
		'巡回派送': 'Delivery Go Round',
		'一方通行': 'Accelerator',
		'超能力': 'Level 5',
		'超能力者': 'Level 5',
		'特殊犯人': '天才',
		'红色小镇': 'Red Town',
		'橱窗购物': 'Window shopping',
		'共享办公室': 'Share Office',
		'风纪委员': 'Judgment',
		'越狱': 'Jailbreak',
		'妹妹们': 'Sisters',
		'空间移动': 'Teleport',
		'幻想杀手': 'Imagine Breaker',
		'无能力者': 'Level 0',
		'念动能力': 'Telekinesis',
		'高压切割': 'Highvoltage·Cutting',
		'改变身材': 'Character Making',
		'能力追迹': 'AIM Stalker',
		'现代魔法师': 'Advanced  Wizard',
		'永恒': 'Aeon',
		'王牌': 'Joker',
		'大能力者': 'Level 4',
		'舌祸拔取': 'Fishing Tongue',
		'把她搞定': '跟她谈判',
		'胁迫': '谈判',
		'幻想猛兽': 'AIM Burst',
		'主神之枪': 'Gungnir',
		'研究': '乐子',
		'纤维素纳米纤维': 'Cellulose Nanofiber',
		'物流黄蜂': 'Logistic Hornet',
		'仙境再现': 'Live adventures in wonderland',
		'滞空回线': 'Underline',
		'未知': '间隙',
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

namelist = ['0.5.md', '0.md', '1.md', '1.5.md', '2.md', '2.5.md', '3.md', '3.5.md', '4.md', '5.md', '6.md', '7.md']

for i in namelist:
	main('post/' + i)
	print(i, 'is finish!')
