#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

Nmajors = np.array([61,65,91],'f')
years = np.array([2013,2014,2015],'f')

plt.figure()
plt.plot(years,Nmajors,'gs',markersize=20)
plt.xlabel('Year',fontsize=22)
plt.ylabel('Number of Physics Majors',fontsize=22)
plt.xticks(years,['2013','2014','2015'])
plt.axis([2012.8,2015.3,55,100])
plt.savefig('Nmajors_year.png')

total_sch = np.array([1627+187,2210+138,2099+177],'f')
fte = np.array([8.67,10.08,10.75],'f')
plt.figure()
plt.plot(years,total_sch/fte,'gs',markersize=20)
plt.ylabel('SCH/FTE',fontsize=22)
plt.xticks(years,['2013','2014','2015'])
#plt.axis([2012.8,2015.3,55,100])
plt.savefig('sch_fte_year.png')
'''
2015
faculty = Vernizzi,Moustakas,, Coohill, Finn, McColgan, Rosenberry, Medsker

Bellis
Coohill
Finn
McColgan
Medsker
Moustakas
Rosenberry    
Vernizzi

'''
