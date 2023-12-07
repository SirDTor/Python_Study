strokes = ["left", "rr", "bright aright", "ok", "enough", "stop", "jokes", "right"]
word_right = "right"
word_left = "left"
strokes_result = []
for stroke in strokes:
    strokes_temp = stroke.replace(word_right,word_left)
    strokes_result.append(strokes_temp)
print(strokes_result)
