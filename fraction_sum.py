def divide(lst):
	return round(lst[0]/lst[1])
def sum_fractions(ls):
                count=0
                for l in ls:
                    count = count+ divide(l)
                return  count

x=[30, 3]
y=[15, 7]
ls = [x,y]
print(sum_fractions(ls))
