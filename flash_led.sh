#!bin/bash
# ラズパイ3でLEDを点滅させるサンプル
# 事前準備：GPIO17にLED赤、GPIO18にLED緑を接続すること

LED_RED_GPIO=17
LED_GREEN_GPIO=18

for v in $(seq 10); do
    gpio -g write ${LED_RED_GPIO} 0
    gpio -g write ${LED_GREEN_GPIO} 1
    sleep 1
    gpio -g write ${LED_RED_GPIO} 1
    gpio -g write ${LED_GREEN_GPIO} 0
    sleep 1
done

gpio -g write ${LED_RED_GPIO} 0
gpio -g write ${LED_GREEN_GPIO} 0
