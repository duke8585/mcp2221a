def set_env():
    import os
    os.environ['BLINKA_MCP2221'] = '1'
    # print(os.environ["BLINKA_MCP2221"])
    global board
    import board
    global digitalio
    import digitalio
    global sleep
    from time import sleep
    global math
    import math

def blink():
    """blink LED, see https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221?view=all#gpio"""
    led = digitalio.DigitalInOut(board.G0)
    led.direction = digitalio.Direction.OUTPUT

    while True:
        led.value = True
        sleep(0.5)
        led.value = False
        sleep(0.5)

def button():
    """digital input, see https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221?view=all#gpio"""
    button = digitalio.DigitalInOut(board.G0)
    button.direction = digitalio.Direction.INPUT

    while True:
        print(button.value)
        sleep(0.1)

def bpm():
    """see button"""
    button = digitalio.DigitalInOut(board.G0)
    button.direction = digitalio.Direction.INPUT
    from time import time
    length = 20
    l = [1] + [0 for _ in range(length-1)]

    while True:
        if button.value:
            ts = time()
            sleep(0.3)
            l.pop(0)
            l.append(ts)

        # print(l)
        diffs = [l[i] - l[i + 1] for i in range(length-1)]
        avg = (sum(diffs) / float(length-1))
        bpm = round(-60/avg,3)
        print(f'{bpm}')

def sensor():
    """
    see https://notenoughtech.com/raspberry-pi/light-sensor-lm393-ky018/
    resistance falls with light intensity
    https://upload.wikimedia.org/wikipedia/commons/1/1a/LDR.png
    """
    button = digitalio.DigitalInOut(board.G0)
    button.direction = digitalio.Direction.INPUT

    while True:
        print(button.value)
        sleep(0.1)

def main():
    sensor()


if __name__ == '__main__':
    set_env()
    main()