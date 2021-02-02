class Book
	attr_accessor :title

	def title= (name)
		little_words = ['and', 'the', 'of', 'over', 'in', 'a', 'an']
		@title = name.capitalize.split.map{ |str| little_words.include?(str) ? str : str.capitalize }.join(' ')
	end



end