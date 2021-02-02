def add(a,b)
	a+b
end

def subtract(a,b)
	a-b
end

def sum(a)
	a.inject(0) {|sum, i|  sum + i }
end

def multiply(a,b,c=1,d=1)
	a*b*c*d
end

def power(a,n)
	sum = 1
	for i in 1..n
		sum = sum*a
	end
	return sum
end

def factorial(n)
	if (n == 0) or (n == 1) then 
		return 1
	end
	return n*factorial(n-1)
end
