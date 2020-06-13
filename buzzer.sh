#!/bin/bash
# ラズパイ3でブザーを鳴らすサンプル
# 事前準備：GPIO12にブザーを接続すること

BUZZER_GPIO=12

# PWM周波数 ＝ 19.2MHz / CLOCK値 / RANGE値
# ドレミファソラシドっぽい音
PWM_CLOCK=100
PWM_RANGES=(734 654 583 550 490 437 389 367)

gpio -g mode ${BUZZER_GPIO} pwm
gpio pwm-ms
gpio pwmc ${PWM_CLOCK}
gpio -g pwm ${BUZZER_GPIO} 50

for range in "${PWM_RANGES[@]}"; do
  gpio pwmr ${range}
  sleep 1
done

gpio -g pwm ${BUZZER_GPIO} 0

