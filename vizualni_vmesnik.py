def narisi_histogram_tempov(tabela):
    tabela_tempov = []
    for l in tabela:
      tempo = round((int(l.cas) / 60) / (int(l.razdalja)/1000),3)
      tabela_tempov.append(tempo)
    return tabela_tempov  