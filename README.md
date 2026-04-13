---
license: apache-2.0
language:
- bn
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
- bn
- speech
model-index:
- name: Vosk Small Bengali Model Streaming version
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Banspeech
      type: other
    metrics:
    - name: Test WER
      type: wer
      value: 32.9
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice
      type: common_voice
      args: bn
    metrics:
    - name: Test WER
      type: wer
      value: 17.9
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Fleurs
      type: fleurs
      args: bn
    metrics:
    - name: Test WER
      type: wer
      value: 20.6
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: IndicTTS
      type: other
    metrics:
    - name: Test WER
      type: wer
      value: 30.9
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Kathbath
      type: ai4bharat/Kathbath
    metrics:
    - name: Test WER
      type: wer
      value: 19.3
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Kathbath Noisy
      type: ai4bharat/Kathbath
    metrics:
    - name: Test WER
      type: wer
      value: 22.5
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Respin 2023
      type: other
    metrics:
    - name: Test WER
      type: wer
      value: 20.9
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Respin 2025
      type: other
    metrics:
    - name: Test WER
      type: wer
      value: 16.6
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Subakko
      type: SUST-CSE-Speech/SUBAK.KO
    metrics:
    - name: Test WER
      type: wer
      value: 24.6

Version 0.60
