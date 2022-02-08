a, b = input('Количество_земных_дней, количество_часов\n').split()
a = a.strip(',')
kolich_zem_dney = float(a)
kolich_zem_chasov = float(b)
sec_v_sole: float = (24*60*60 + 39*60 + 35.244)
sec_zadano = kolich_zem_dney*24*60*60 + kolich_zem_chasov*60*60
kolich_sol = round(float(sec_zadano/sec_v_sole), 2)
print('число солов соответствующее введенным данным равно: ' + str(kolich_sol))
