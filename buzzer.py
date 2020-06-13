#!/bin/bash
# ラズパイ3でブザーを鳴らすサンプル
# 事前準備：GPIO12(PIN32)にブザーを接続すること

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 32
COUNT = 10
# ドレミファソラシドっぽい音
# https://tomari.org/main/java/oto.html
FREQS = [523, 587, 659, 698, 783, 880, 987, 1046]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

for freq in FREQS:
    buzzer = GPIO.PWM(BUZZER_PIN, freq)
    buzzer.start(50)
    time.sleep(0.5)

    buzzer.stop()
    time.sleep(0.5)

GPIO.cleanup()

