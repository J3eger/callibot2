input.onButtonPressed(Button.A, function () {
    while (!(grad == input.compassHeading())) {
        if (calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.hell)) {
            calliBot2.motor(C2Motor.links, C2Dir.vorwärts, 50)
            calliBot2.setLed(C2Motor.rechts, C2State.an)
            basic.pause(100)
            calliBot2.motorStop(C2Motor.links, C2Stop.Bremsen)
            calliBot2.setLed(C2Motor.rechts, C2State.aus)
        } else if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.hell)) {
            calliBot2.motor(C2Motor.rechts, C2Dir.vorwärts, 50)
            calliBot2.setLed(C2Motor.links, C2State.an)
            basic.pause(100)
            calliBot2.motorStop(C2Motor.rechts, C2Stop.Bremsen)
            calliBot2.setLed(C2Motor.links, C2State.aus)
        } else {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwärts, 70)
            basic.pause(100)
            calliBot2.motorStop(C2Motor.beide, C2Stop.Bremsen)
        }
    }
})
let grad = 0
input.calibrateCompass()
basic.pause(2000)
basic.showNumber(input.compassHeading())
grad = input.compassHeading() + 5
basic.pause(100)
basic.showNumber(grad)
basic.forever(function () {
	
})
