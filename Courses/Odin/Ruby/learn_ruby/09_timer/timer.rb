class Timer
	attr_accessor :seconds

	def initialize(seconds=0)
		@seconds = seconds
	end

	def time_string
		min = ( @seconds / 60 ) % 60
		hour = ( @seconds / 60 ) / 60
		sec = @seconds % 60
		"%02d:%02d:%02d" % [hour, min, sec]
	end
end