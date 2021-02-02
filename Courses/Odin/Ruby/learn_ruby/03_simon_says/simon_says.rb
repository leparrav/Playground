def echo(sFrase)
	return sFrase
end

def shout(sFrase)
	return sFrase.upcase
end

def repeat(sFrase, times = 2)
	temp = (sFrase+" ")*(times-1)
	return temp + sFrase
end

def start_of_word(sFrase,times)
	return sFrase[0,times]
end

def first_word(sFrase)
	sFrase.split(" ").first
end

def titleize(sFrase)
	all_words =  sFrase.split(" ")
	temp = ""
	for i in 0..all_words.length-2
		if not ["the","and","over"].include?(all_words[i]) or i == 0 then
			temp += all_words[i].capitalize + " "
		else 
			temp += all_words[i] + " "
		end 
	end
	temp += all_words[-1].capitalize
	return temp
end