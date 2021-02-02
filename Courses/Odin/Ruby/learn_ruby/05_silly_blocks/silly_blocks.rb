def reverser(&block)
  block.call.split.map {|word| word.reverse}.join(' ').rstrip
end
def adder(num = 1, &block)
  block.call + num
end
def repeater(times = 1, &block)
  0.upto(times-1) do
    block.call
  end
end