strokes = ["left", "rr", "bright aright", "ok", "enough", "stop", "jokes", "right"]
check_word = "right"
left_word = "left"
result_strokes = []
for stroke in strokes:
    temp_strokes = stroke.replace("right","left")
    result_strokes.append(temp_strokes)
print(result_strokes)
