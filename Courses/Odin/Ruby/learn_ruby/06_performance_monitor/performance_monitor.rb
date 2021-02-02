def measure(times = 1)
  start = Time.now
  if block_given?
    1.upto(times) do
      yield
    end
  end
  elapsed_time = Time.now - start
  elapsed_time / times
end