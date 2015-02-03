from winsound import Beep
from time import sleep

# beep sound settings.
START_BEEP_FREQ, START_BEEP_LENG = 1000, 300
END_BEEP_FREQ, END_BEEP_LENG = 1570, 800

def sound_timer(sec):
  Beep(START_BEEP_FREQ,START_BEEP_LENG)
  while sec>0:
    m,s = divmod(sec,60)
    print('\r'+(str(m)+':' if m>0 else '')+'%02d'%s+'  ',end='')
    sleep(1)
    sec-=1
  Beep(END_BEEP_FREQ,END_BEEP_LENG)

if '__main__' == __name__:
  from sys import argv
  for arg in argv[1:]:
    if arg.isdecimal():
      sound_timer(int(arg))
    elif arg.startswith('s'):
      prob_num = int(arg[1])
      if arg.endswith('r'):
        sound_timer(50)
      else:
        list(map(sound_timer,[(15,45),(30,60),(20,60)][(prob_num-1)//2][-1 if arg.endswith('s') else 0:]))
    elif ':' in arg:
      min,sec = arg.split(':')
      sound_timer(int(min)*60+int(sec))
    elif arg.startswith('w'): #w1:independent w2:integrated
      if arg.endswith('r'):
        sound_timer(3*60)
      else:
        sound_timer((20 if arg.endswith('1') else 30) * 60)
