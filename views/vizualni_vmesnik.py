import matplotlib.pyplot as plt
import numpy as np
def narisi_histogram_tempov(tabela):
    tabela_tempov = []
    for l in tabela:
      tempo = l.razdalja / l.cas
      tabela_tempov.append(tempo)
    values = np.array(tabela_tempov) 
    return plt.hist(values)     