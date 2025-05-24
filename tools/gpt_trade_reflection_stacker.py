# Phase 127 – GPT Trade Reflection Stacker

def stack_reflections(reflections, new_entry):
    reflections.append(new_entry)
    return reflections[-7:]  # keep last 7 reflections