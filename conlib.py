from pylab import *

pl = 0.4
pc = 0.4
pn = 0.2
c = 0.2
def initialize():
	global pl, pc, pn, libresult, conresult, neuresult, t, timesteps
	libresult = [pl]
	conresult = [pc]
	neuresult = [pn]
	t = 0
	timesteps = [t]

def observe():
	global pl, pc, pn, libresult, conresult, neuresult, t, timesteps
	libresult.append(pl)
	conresult.append(pc)
	neuresult.append(pn)
	timesteps.append(t)

def update():
	global pl, pc, pn, libresult, conresult, neuresult, t, timesteps
	delta_cl = pc - pl
	delta_cn = pc - pn
	delta_ln = pl - pn
	

	if delta_cl > 0:
		pc += c * delta_cl
		pl -= c * delta_cl
	elif delta_cl < 0:
		pl += c * delta_cl
		pc -= c * delta_cl
	
	if delta_cn > 0:
		pc += c * delta_cn
		pn -= c * delta_cn
	elif delta_cn < 0:
		pn += c * delta_cn
		pc -= c * delta_cn
	
	if delta_ln > 0:
		pn += c * delta_ln
		pl -= c * delta_ln
	elif delta_ln < 0:
		pl += c * delta_ln
		pn -= c * delta_ln

	t = t + 0.1


initialize()
while t < 1.:
	update()
	observe()

print libresult
print conresult
plot(timesteps, libresult)
plot(timesteps, conresult)
plot(timesteps, neuresult)
show()
