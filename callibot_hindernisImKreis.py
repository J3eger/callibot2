def on_button_pressed_a():
    while True:
        while calliBot2.entfernung(C2Einheit.CM) >= 7:
            if calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.HELL):
                calliBot2.motor(C2Motor.LINKS, C2Dir.VORWÄRTS, 100)
                calliBot2.set_led(C2Motor.RECHTS, C2State.AN)
                basic.pause(1)
                calliBot2.motor_stop(C2Motor.LINKS, C2Stop.BREMSEN)
                calliBot2.set_led(C2Motor.RECHTS, C2State.AUS)
            elif calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.HELL):
                calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWÄRTS, 100)
                calliBot2.set_led(C2Motor.LINKS, C2State.AN)
                basic.pause(1)
                calliBot2.motor_stop(C2Motor.RECHTS, C2Stop.BREMSEN)
                calliBot2.set_led(C2Motor.LINKS, C2State.AUS)
            else:
                calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWÄRTS, 100)
                basic.pause(1)
                calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
        if calliBot2.entfernung(C2Einheit.CM) < 7:
            calliBot2.motor(C2Motor.LINKS, C2Dir.RÜCKWÄRTS, 30)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWÄRTS, 30)
            basic.pause(700)
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWÄRTS, 50)
            basic.pause(800)
            calliBot2.motor(C2Motor.LINKS, C2Dir.VORWÄRTS, 30)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.RÜCKWÄRTS, 30)
            basic.pause(650)
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWÄRTS, 50)
            basic.pause(800)
            calliBot2.motor(C2Motor.LINKS, C2Dir.VORWÄRTS, 30)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.RÜCKWÄRTS, 30)
            basic.pause(650)
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWÄRTS, 50)
            basic.pause(700)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWÄRTS, 30)
            calliBot2.motor(C2Motor.LINKS, C2Dir.RÜCKWÄRTS, 30)
            basic.pause(700)
            
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    calliBot2.motor(C2Motor.LINKS, C2Dir.RÜCKWÄRTS, 30)
    calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWÄRTS, 30)
    basic.pause(700)
    calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
    basic.show_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)