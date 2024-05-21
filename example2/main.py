import machine
import utime

len_board= machine.Pin(25, machine.Pin.OUT)

while True:
  print("loop is runnin")
  # led is always on or off??
  len_board.toggle()
  utime.sleep(5)
