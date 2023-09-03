import matplotlib.pyplot as plt
import numpy as np
def narisi_histogram_tempov(tabela):
    tabela_tempov = []
    for l in tabela:
      tempo = round((l.cas / 60) / (l.razdalja/1000),3)
      tabela_tempov.append(tempo)
    return tabela_tempov  