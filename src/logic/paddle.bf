>>>>>>            move to input
[-<+>]            copy input to temp
<                 back to temp

---- ---- ----    subtract ASCII for 'w'
[                 if == 'w'
  <<<< -          paddle_left_y--
]
++++ ++++ ++++    restore

---- ---- ---- ---- ---- ----    subtract ASCII for 's'
[
  <<<< +          paddle_left_y++
]
<<<<<<<<
