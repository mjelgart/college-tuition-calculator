
r=.06
start = 50000



def calculate(target, years):
  current_total = start*(1+r)**years
  
  for yearly_savings in range(50000):
    
    for year in range(years):
      current_total += (yearly_savings)*(1+r)**(years - year)
    if current_total > target:
      print('You can save ${0} per year to save ${1}.'.format(yearly_savings,target))
      return yearly_savings
    else:
      current_total = start*(1+r)**years
  
  
print('Total is ${0}.'.format(calculate(830000,27)+calculate(898272,29)+calculate(971462,31)))
