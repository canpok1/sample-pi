# ラズパイ3でLEDを点滅させるサンプル
# 事前準備：GPIO17(PIN11)にLED赤、GPIO18(PIN12)にLED緑を接続すること

import RPi.GPIO as GPIO
import time

LED_RED_PIN = 11
LED_GREEN_PIN = 12
COUNT = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)

for _ in range(COUNT):
    GPIO.output(LED_RED_PIN,True)
    GPIO.output(LED_GREEN_PIN,False)
    time.sleep(1.0)
    GPIO.output(LED_RED_PIN,False)
    GPIO.output(LED_GREEN_PIN,True)
    time.sleep(1.0)

GPIO.output(LED_RED_PIN,False)
GPIO.output(LED_GREEN_PIN,False)

GPIO.cleanup()
