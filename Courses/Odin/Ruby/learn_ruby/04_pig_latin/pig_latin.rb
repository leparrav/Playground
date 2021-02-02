def translate(phrase)
	temp = ""
	list_words = phrase.split(" ")
	for word in list_words
		if ["a","e","i","o","u"].include?(word[0].downcase) then
			# if there is not a puntuaction at the end REGEXP not working...
			if not ['!','.',',',':'].include?(word[-1]) then
				# No need to capitalize vowels becase they don't move
				temp += word + "ay" + ' '
			else
				temp += word[0..-2] + "ay" + word[-1] + ' '
			end
		else 
			# How many consonants there at the start?
			count, last_letter = 0,''
			for i in (0..word.length) 
				if ["a","e","i","o","u"].include?(word[i]) and last_letter.downcase != 'q' then
					count = i
					break;
				end
				last_letter = word[i]
			end

			# If first letter is capitalized
			if word[0] == word[0].capitalize then
				if  not ['!','.',',',':'].include?(word[-1]) then 
					temp += word[count..-1].capitalize + word[0..count-1].downcase + "ay" + ' '
				else
					temp += word[count..-2].capitalize + word[0..count-1].downcase + "ay" + word[-1]  + ' '
				end
			else
				if  not ['!','.',',',':'].include?(word[-1]) then 
					temp += word[count..-1] + word[0..count-1].downcase + "ay" + ' '
				else
					temp += word[count..-2] + word[0..count-1].downcase + "ay" + word[-1]  + ' '
				end
			end
		end
	end
	return temp[0..-2]
end