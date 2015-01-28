from winsound import Beep#, PlaySound
from PyQt5.QtMultimedia import QAudio
from time import sleep

def sound_timer(sec):
  Beep(1300,300)
  while sec>0:
    m,s = divmod(sec,60)
    print('\r'+(str(m)+':' if m>0 else '')+'%02d'%s+'  ',end='')
    sleep(1)
    sec-=1
  Beep(1570,800)

if '__main__' == __name__:
  from sys import argv
  for arg in argv[1:]:
    if arg.isdecimal():
      sound_timer(int(arg))
    # elif arg.startswith('p'):
    elif arg.startswith('s'):
      prob_num = int(arg[1])
      if arg.endswith('r'):
        sound_timer(50)
      else:
        list(map(sound_timer,[(15,45),(30,60),(20,60)][(prob_num-1)//2][-1 if arg.endswith('p') else 0:]))
    #   QAudio()
    elif ':' in arg:
      min,sec = arg.split(':')
      sound_timer(int(min)*60+int(sec))
    elif arg.startswith('w'): #w1:independent w2:integrated
      if arg.endswith('r'):
        sound_timer(3*60)
      else:
        sound_timer((30 if arg.endswith('1') else 20) * 60)
